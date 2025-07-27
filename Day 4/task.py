import random

random_integer =  random.randint(1,10)     #Random integers  anything between 1 to 10
print(random_integer)
random1 = random.random()*100
print(random1)                             #Random Floating Numbers   (start from 0)

random2 = random.uniform(3,5)             # With Range for float
print(random2)

r1 = random.randrange(0,9)                  # r1 is from 0 to 10
print(r1)              #  for integers


# randrange(a, b+1). == randint(a,b)   no can be a or b hence dor randrange a or b+1

r1 = random.randint(1,10)
r2 = random.randrange(1,9,5)     # step means the difference between numbers
print(r1 , r2 )                       # do research on both specially for randrange



# Heads or Tails
no = random.randint(1,2)
if no == 1:
    print("Heads")
else:
    print("Tails")
