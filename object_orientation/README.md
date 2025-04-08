
# Object Oriented Programming with Python

## Python vs. Java classes

============================ =====================
Java                         Python
============================ =====================
strict encapsulation         no real encapsulation
interfaces                   multiple inheritance
public / private classes     everything is public
defined attributes / methods flexible
============================ =====================


## Class definitions

In `space_game/` you find examples of class definitions.
Here are some common features used there:

* defining a class with type hints (in `game.py`)
* simple inheritance in `game.py`
* calling the method of a superclass with `super()` in `game.py`
* properties (`game.py`)
* staticmethods (in `galaxy.py`)

The example uses the **pydantic** library.
**Dataclasses** and **pydantic classes** are very similar. Dataclasses have the advantage that they are built into Python, pydantic performs additional type checks at the time of object creation.

## Abstract Base Classes

The **abc** module allows to declare abstract classes and methods. 
You find an example in `descriptors.py`.
Create both valid and invalid instances of the defined class.

The example uses the **descriptor protocol**, a mechanism to control the getting and setting of attributes using object composition. 

## Operator Overloading

Python has a long list of special **double-underscore methods** ("dunder methods").
They all have in common that they should never be called directly. 
Practically, every Python operator can be overloaded by a method.

Common use cases are:

* making objects printable with `__repr__()`  and `__str__()`
* checking equality with `__eq__()`
* making objects sortable with `__lt__()` (less than) or `__gt__()`

You find an application example in `sortable_objects.py`

I would advise using operator overloading sparingly. Most of the time, a regular method is easier to read.


## Dynamic Attributes

The special methods `__getattr__` and `__setattr__` allow you to intercept the process of attribute access. They work like a more generic **property**. You can use them to retrieve attributes from elsewhere or to generate them on-the-fly. However, since methods use the same mechanism you will always want to call the inherited method.

Execute the example in `getattr_setattr.py`

## Multiple Inheritance

Python allows multiple inheritance, often found under the term **mixins**.
It is tricky, because the namespaces potentially collide.
I advise to avoid multiple inheritance whenever possible.

A livesaver is checking the **method resolution order**, see `multiple_inheritance.py`

## Metaclasses

**Metaclasses** control how Python creates objects. This helps to understand the language better.
There are not too many reasons to use metaclasses in a project.

Execute the example in `metaclasses.py` and see what it does.

## Slots

The `__slots__` attribute is a mechanism to define the available attributes more strictly.
This mechanism is used by **dataclasses** and **pydantic** with a more comfortable interface.

Run the example in `slots.py`. Remove the comment and run the code again.

## Links

- [Introduction to OOP with Python](https://python-basics-tutorial.readthedocs.io/en/latest/oop/index.html)
- [Abstract Base Classes](https://www.academis.eu/advanced_python/classes/abc.html)
- [Pydantic](https://docs.pydantic.dev/)
- [Operator Overloading](https://www.academis.eu/advanced_python/classes/operator_overloading.html)
- [Descriptor Protocol](https://docs.python.org/3/howto/descriptor.html)
- [Metaclasses](https://www.academis.eu/advanced_python/classes/metaclasses.html)
- [Using Slots](https://wiki.python.org/moin/UsingSlots)
- [Video: Pythonic objects](https://www.youtube.com/watch?v=k55d3ZUF3ZQ)
- [Video: Descriptors and Metaclasses](https://www.youtube.com/watch?v=7PzeZQGVPKc)
