import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import the data
csv_data = pd.read_csv('./GP/gp-training-set.csv')
csv_data.loc[csv_data['Label']==0,'Label']=-1    # change 0 to -1 for simplifing computing
X = csv_data.iloc[:,:-1]   #input tuples
L = csv_data.loc[:,'Label'] #labels

# parameter
random_seed = 24
initialization_size = 40
iteration_size = 500
best_size = 10
acc_rate = 0.95

# initialize the weights
def initialize_w():
    np.random.seed(random_seed)
    W = np.random.uniform(-1,1,(initialization_size,10)) # threshold = -w_0
    return W

# fitness function1: accuracy
def compute_fitness(W):
    mout = np.dot(X,W.T)        #linear combination
    lout = np.ones(mout.shape)  #label_output
    fitness_w = np.zeros(initialization_size) #fitness of each vector_w
    for i in range(mout.shape[1]):
        lout[mout[:,i]<0,i] = -1
        fitness_w[i] = sum(lout[:,i]==L)/L.shape[0]
    return fitness_w

# F1-score calculation
def F1_score(y,l):
    TP,TN,FP,FN = 0,0,0,0
    for i in range(l.shape[0]):
        if y[i] == 1 and l[i] == 1:
            TP = TP+1
        elif y[i] == 1 and l[i] == -1:
            FP = FP+1
        elif y[i] == -1 and l[i] == 1:
            FN = FN+1
        elif y[i] == -1 and l[i] == -1:
            TN = TN+1
    pre = 0 if (TP+FP)==0 else TP/(TP+FP)
    recall = 0 if (TP+FN)==0 else TP/(TP+FN)
    F1 = 0 if (pre+recall)==0 else (2*pre*recall)/(pre+recall)
    return F1

# fitness function2: F1-score
def compute_fitness_F1(W):
    mout = np.dot(X, W.T)  # linear combination
    lout = np.ones(mout.shape)  # label_output
    fitness_w = np.zeros(initialization_size)  # fitness of each vector_w
    for i in range(mout.shape[1]):
        lout[mout[:, i] < 0, i] = -1
        fitness_w[i] = F1_score(lout[:,i],L)
    return fitness_w

# copy operator
def copy(W,F):
    return W[np.argsort(-F)[:best_size], :]  #save some best W (descending order)

# corss process
def cross(f,m):
    cut = np.random.randint(1,10) #from 1 to 9: no null vector
    return np.concatenate((f[:cut],m[cut:]))

# crossover operator
def crossover(W,F):
    parents = np.random.choice(range(initialization_size),size=(initialization_size-best_size)*2,p=F/sum(F))  #choose parents via fitness probablity
    crossW = np.zeros([initialization_size-best_size,10])
    for i in range(int(parents.shape[0]/2)):
        father = W[parents[2*i],:]
        mother = W[parents[2*i+1],:]
        crossW[i,:] = cross(father,mother)
    return crossW

# mutation operator
def mutate(W):
    m_w = np.random.randint(0, initialization_size)
    m_feature = np.random.randint(0,10)
    W[m_w,m_feature] = np.random.uniform(-1,1)
    return W

# generation
def generate_w(W,F):
    W1 = copy(W,F)
    W2 = crossover(W,F)
    newW = np.concatenate((W1, W2), axis=0)
    return mutate(newW)

# termination
def termination_condition(F):
    if F.mean()>acc_rate:
        return True
    else:
        return False

plot_F = np.zeros(iteration_size) # plot
# Genetic Programing
def Genetic_Programing():
    W = initialize_w()
    for itr in range(iteration_size):
        F = compute_fitness(W)  #ACC
        # F = compute_fitness_F1(W) #F1-score
        plot_F[itr] = F.mean() # plot
        if termination_condition(F):
            break
        W = generate_w(W,F)
    F = compute_fitness(W)
    print(F.max()) #largest ACC
    return W[F.argmax(),:]

# Visualization
def visual_fitness():
    plt.plot(plot_F) # plot
    plt.show()       # plot

output_w = Genetic_Programing()
visual_fitness()