import random

def gen_random(count, nmin, nmax):
    for i in range(count):
        yield random.randint(nmin, nmax)

'''print("5 random numbers from 1 to 10:")
for n in gen_random(5, 1, 10):
    print(n, end =" ")
print()'''