####Genetic Programming

Design and implement a genetic programming system to evolve some perceptrons that match well with a given training set. A training set is a collection of tuples of the form (x1, ..., xn, l), where xi’s are real numbers and l is either 1 (positive example) or 0 (negative example). So for your genetic programming system, a “program” is just a tuple (w1,...,wn,θ) of numbers (weights and the threshold). Answer the following questions:

1. What’s your fitness function?
2. What’s your crossover operator?
3. What’s your copy operator?
4. What’s your mutation operator, if you use any?
5. What’s the size of the initial generation, and how are programs generated?
6. When do you stop the evolution? Evolve it up to a fixed iteration, when it satisfies a condition on the fitness function, or a combination of the two?

---

1. Fitness Function:

   I try two fitness functions: accuracy & F1-score.

2. Crossover operator

   Choose two w vectors on the basis of their fitness probability. And then randomly choose a position to cut these two w vectors, take each piece of them and concatenate two piece into one new w vector.

3. Copy operator

   For the best w vectors, I just save them into next generation. In experiment, I save best 10 out of 40.

4. Mutation operator

   In each generating process, I randomly choose one w vector and randomly choose one weight in this vector into one random real number which satisfies [-1,1].

5. My initial generation size is 40, and each generation size is the same. The generating process is that I do the copy operator firstly to save best 10 w vectors out of 40. And then do the crossover operator to generate the other 30 w vectors. Finally, I do the mutation operator to randomly change one w vector among those 40 new w vectors.

6. The combination of fixed iteration and termination conditions. When the average fitness is bigger than 0.9(a parameter), the evolution stops because the rate is high enough for me. Otherwise, the program would stop after 500 iterations.