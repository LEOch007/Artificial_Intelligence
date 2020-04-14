# Using a powerful mathematical theorem solver Z3
from z3 import *

# symbols
B1 = Bool('Bob ranks 1')
B2 = Bool('Bob ranks 2')
B3 = Bool('Bob ranks 3')
B4 = Bool('Bob ranks 4')

L1 = Bool('Lisa ranks 1')
L2 = Bool('Lisa ranks 2')
L3 = Bool('Lisa ranks 3')
L4 = Bool('Lisa ranks 4')

J1 = Bool('Jim ranks 1')
J2 = Bool('Jim ranks 2')
J3 = Bool('Jim ranks 3')
J4 = Bool('Jim ranks 4')

M1 = Bool('Mary ranks 1')
M2 = Bool('Mary ranks 2')
M3 = Bool('Mary ranks 3')
M4 = Bool('Mary ranks 4')

BM1 = Bool('biology major ranks 1')
BM2 = Bool('biology major ranks 2')
BM3 = Bool('biology major ranks 3')
BM4 = Bool('biology major ranks 4')

# logics
s = Solver()
# one person takes only one position
s.add(Or( And(B1,Not(B2),Not(B3),Not(B4)), And(B2,Not(B1),Not(B3),Not(B4)), And(B3,Not(B2),Not(B1),Not(B4)), And(B4,Not(B2),Not(B3),Not(B1)) ))
s.add(Or( And(L1,Not(L2),Not(L3),Not(L4)), And(L2,Not(L1),Not(L3),Not(L4)), And(L3,Not(L2),Not(L1),Not(L4)), And(L4,Not(L2),Not(L3),Not(L1)) ))
s.add(Or( And(J1,Not(J2),Not(J3),Not(J4)), And(J2,Not(J1),Not(J3),Not(J4)), And(J3,Not(J2),Not(J1),Not(J4)), And(J4,Not(J2),Not(J3),Not(J1)) ))
s.add(Or( And(M1,Not(M2),Not(M3),Not(M4)), And(M2,Not(M1),Not(M3),Not(M4)), And(M3,Not(M2),Not(M1),Not(M4)), And(M4,Not(M2),Not(M3),Not(M1)) ))
s.add(Or( And(BM1,Not(BM2),Not(BM3),Not(BM4)), And(BM2,Not(BM1),Not(BM3),Not(BM4)), And(BM3,Not(BM2),Not(BM1),Not(BM4)), And(BM4,Not(BM2),Not(BM3),Not(BM1)) ))

# one position needs only one person
s.add(Or( And(B1,Not(L1),Not(J1),Not(M1)),And(L1,Not(B1),Not(J1),Not(M1)),And(J1,Not(B1),Not(L1),Not(M1)),And(M1,Not(B1),Not(J1),Not(L1)) ))
s.add(Or( And(B2,Not(L2),Not(J2),Not(M2)),And(L2,Not(B2),Not(J2),Not(M2)),And(J2,Not(B2),Not(L2),Not(M2)),And(M2,Not(B2),Not(J2),Not(L2)) ))
s.add(Or( And(B3,Not(L3),Not(J3),Not(M3)),And(L3,Not(B3),Not(J3),Not(M3)),And(J3,Not(B3),Not(L3),Not(M3)),And(M3,Not(B3),Not(J3),Not(L3)) ))
s.add(Or( And(B4,Not(L4),Not(J4),Not(M4)),And(L4,Not(B4),Not(J4),Not(M4)),And(J4,Not(B4),Not(L4),Not(M4)),And(M4,Not(B4),Not(J4),Not(L4)) ))

# 5 rules
s.add(Or( And(B1,Not(L2)),And(B2,Not(L1),Not(L3)),And(B3,Not(L2),Not(L4)),And(B4,Not(L3)) ))
s.add(Or( And(J1,BM2),And(J2,BM3),And(J3,BM4) ))
s.add(Or( And(B1,J2),And(B2,J3),And(B3,J4) ))
s.add(Or( And(BM1==L1,BM2==L2,BM3==L3,BM4==L4),And(BM1==M1,BM2==M2,BM3==M3,BM4==M4) ))
s.add(Or( And(L1,Not(M1)),And(Not(L1),M1) ))

print(s.check())
print(s.model())

print('\n The ranking list is: '+'Mary Bob Jim Lisa')