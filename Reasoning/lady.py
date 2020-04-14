# Using a powerful mathematical theorem solver Z3
from z3 import *

# symbols
L1 = Bool('Lady in Room 1')
L2 = Bool('Lady in Room 2')
L3 = Bool('Lady in Room 3')
T1 = Bool('Tiger in Room 1')
T2 = Bool('Tiger in Room 2')
T3 = Bool('Tiger in Room 3')
S1 = Bool('Sign 1 is true')
S2 = Bool('Sign 2 is true')
S3 = Bool('Sign 3 is true')

# logics
s = Solver()
s.add(Or(L1,T1))
s.add(Or(L2,T2))
s.add(Or(L3,T3))
s.add(Not(And(L1,T1)))
s.add(Not(And(L2,T2)))
s.add(Not(And(L3,T3)))

s.add(Or( And(L1,T2,T3), And(L2,T1,T3), And(L3,T1,T2) ))
s.add(Or( And(S1,Not(S2),Not(S3)), And(S2,Not(S1),Not(S3)), And(S3,Not(S1),Not(S2)), And(Not(S1),Not(S2),Not(S3)) ))

s.add(S1==T1)
s.add(S2==L2)
s.add(S3==T2)

if str(s.check()) == 'sat':
    print('satisfiability or not: ' + str(s.check()))
    print(s.model())
else:
    print('satisfiability or not: ' + str(s.check()))

# The answer is: Lady in the room 1
# check the answer
print('\nthe model is satisfied before')
print('now adding Not(L1)')
s.add(Not(L1))
print('The satisfiability of the model is: ' + str(s.check()))
print('Therefore, the answer is L1: Lady in the room 1')