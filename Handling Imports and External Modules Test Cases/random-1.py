#Import defined functions from the module random

import random
def test_random_basic():
 x: float = random.random()
 y: int = random.randint(1, 10)
 z: int = int(x * y) + 1 
 print(x)
 print(y)
 print(z)
test_random_basic()