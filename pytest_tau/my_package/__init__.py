# In python, any folder with dunder __init__.py - Is called Package
from my_package.acume import Accumulator

accum = Accumulator()
print(accum.count)

# accum.count = 10
# As it is getter-read-only method, if we are trying to assign the value.
# It throws AttributeError: property 'count' of 'Accumulator' object has no setter.

accum.add()
print(accum.count)

accum.add(3)
print(accum.count)