import inspect
from inspect import *
import sys


def test_function(things
                  , *args
                  , kw1
                  , kw2=1312
                  , kw3=666
                  , **kwargs: "provide **kwargs here"):
    assignTest = "something I assigned to assignTest"
    return "thirty four thousand " + things


# example of adding a property to a func below:
test_function.example_property = "this is a property that does not do anything bro"

print(f"[This is an example of the self added property:] {test_function.example_property}")
print(f"[Example of .__doc__ :] {str(test_function.__doc__)}")
print(f"[This is the original:] {test_function('sure', kw1=1)}")
print(f"[This is a example of the use of Dir:] {dir(test_function('sure', kw1=1))}")
print(f"[This is the introspection signature:] {inspect.signature(test_function)}")
print(f"[This is the introspection signature ran through dir:] {dir(inspect.signature(test_function))}")
print(f"[This is an example of seeing the code through introspection:] \n\t {test_function.__code__}")
# Note that you can use these later to do some cool shit
print(f"[isfunction:] {isfunction(test_function)}")
print(f"[ismethod:] {ismethod(test_function)}")
print(f"[isrouting:] {isroutine(test_function)}")
print(f"[getmodule:] {inspect.getmodule((test_function))}")
print()

