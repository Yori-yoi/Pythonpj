import numpy as np
rng=np.random.default_rng(seed=1) #for a particular seed it will keep repeating useful if we need to use same numbers
print(rng.integers(1,7))
print(rng.integers(low=1,high=101,size=(3,2)))


np.random.seed(seed=1)
print(np.random.uniform(low=-1,high=1,size=(3,4))) # for decimal numbers


array=np.array([1,2,3,4,5])
rng.shuffle(array)
number=rng.choice(array)
num_arr=rng.choice(array,size=(3,4))


print(array)
print(number)
print(num_arr)