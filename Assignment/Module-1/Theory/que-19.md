##### Understanding iterators and creating custom iterators.

An iterator in Python is an object that holds a sequence of values and provide sequential traversal through a collection of items such as lists, tuples and dictionaries. 

The Python iterators object is initialized using the iter() method. It uses the next() method for iteration.

1.__iter__(): __iter__() method initializes and returns the iterator object itself.
2.__next__(): the __next__() method retrieves the next available item, throwing a StopIteration exception when no more items are available.

##### Creating an iterator
Creating a custom iterator in Python involves defining a class that implements the __iter__() and __next__() methods according to the Python iterator protocol.

**Define the Class:** Start by defining a class that will act as the iterator.

**Initialize Attributes:** In the __init__() method of the class, initialize any required attributes that will be used throughout the iteration process.

**Implement __iter__():** This method should return the iterator object itself. This is usually as simple as returning self.

**Implement __next__():** This method should provide the next item in the sequence each time it’s called.