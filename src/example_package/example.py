import sys

from example_package.module1.module1 import my_sum
from example_package.module2 import module2_function

module2_function()
args = sys.argv[1:]
print(my_sum(*args))