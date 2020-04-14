#### Reasoning

---

we use a mechanical theorem prover to solve problems by reasoning or finding models. The theorem prover is Z3. The official release is here:

https://github.com/Z3Prover/z3

If you use unix, you can install it using pip:

https://pypi.org/project/z3-solver/#description

Here is a good description of how to install it by Bob Moore of UT Austin:

http://www.cs.utexas.edu/users/moore/acl2/manuals/current/manual/index-seo.php/SMT____Z3-INSTALLATION

Two problem are described as the following:

- Lady or Tiger

There are three rooms. Each contains either a lady or a tiger but not both. Furthermore, one room contained a lady and the other two contained tigers. Each of the rooms has a sign, and at most one of the three signs was true. The three signs are:

1. Room I: A TIGER IS IN THIS ROOM.
2. Room II: A LADY IS IN THIS ROOM.
3. Room III: A TIGER IS IN ROOM II.

Which room contains the lady?



- Ranking problem

1. Lisa is not next to Bob in the ranking
2. Jim is ranked immediately ahead of a biology major
3. Bob is ranked immediately ahead of Jim
4. One of the women (Lisa and Mary) is a biology major
5. One of the women is ranked first

What are possible rankings for the four people?

