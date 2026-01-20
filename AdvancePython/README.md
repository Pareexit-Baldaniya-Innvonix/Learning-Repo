# AdvancePython Learning

## Day 1

Task 1:
- Class: Blueprint of the object
- Objest: Actual instance(interface) of the class

## Day 2

Task 1: simple constructure
- method namely `__init__` used to set up the initial state of the object

Task 3:
1. Instance method:
    - used to access or change data belonging to a specific object
    - always take self as a first argument
    - use for describing action to specific item

2. Class Method:
    - belongs to class itself
    - used to see and change the things which affect every object created from that class
    - using `@classmethod` decorator
    - take cls as first argument

3. Static Method:
    - related to class
    - they don't need to know anything about class and object
    - used as a general tool
    - use `@staticmethod`

4. Accessors:
    - used to access a piece of data without changing it
    - `@property` decorator used for it
    - take self as a first argument

5. Mutators:
    - used to change a piece of data
    - useful because allow to add "rules" before change
    - take self, value as a first arguments

## Day 3

Task 1:
Nested(Inner) class means a class inside a class

Task 2:
1. Instance method:
    - using self as a parameter for pointing instance of the class
    - they access and modify instance state through self and class state through `self.__class__`
    - common methods in python classes

2. Class method:
    - using cls parameter for pointing to the class itself
    - they modify class level state through cls, but they can't modify individual instance state

3. Static method:
    - don't take self and cls as a parameters
    - they can't modify instance or class state directly
    - mainly use for organizational purposes and namespacing

Task 3:
1. Inheritance:
    - that allows to inherite instance or methods from another class

2. Constructors:
    - generally used for instantiating an object
    - task to assign values to the data members of the class when an object of the class is created
    - `__init__` method is called the constructor

`super()`:
    - allows us to access the temporary object of the class
    - not use the base class name explictly
    - helps in working with multiple inheritances

3. Method overloading:
    - methods or functions have same name but different signature
    - example of compiletime polymorphism
    - no need of more than one class
    - ingeritance may or may not be required

4. Method Overriding:
    - methods and functions have same name and same signature
    - example of runtime polymorphism
    - need of atleast two classes
    - inheritance always required

## Day 4

Task 1: Modules
- modules are like a code library
- to create a module file just save it with .py extension
- a file contains a set of functions which we want to include in the application

Task 2: Package
- it is like a container which contains various functions to perform specific task 
- package is a folder which contains multiple module files in it
- also a '`__init__.py`' file may empty but contain the package list

Task 3: Decorators
- Decorators lets add extra behaviour to a function, without changing the function code
- it is a function that takes another function as input, and returns a function

## Day 5

Task 1:
1. Process:
    - it is a instance of the program
    - they do not share the memory
    - they are independent from each other

2. Thread:
    - it's an entity in the process that can be schedule for execution
    - a process can spawn multiple threds
    - all threads within the process can share a same memory

## Day 6

Task 1: Types of exception
- an unexpected event that occurs during program execution
- errors that are occured at run time that called exception or logical error

1. Built-in Exceptions:
    - SyntaxError: when syntax error is encountered  --> missing colon after a if statement

    - ZeroDivisionError: attempt to divide a number by zero  --> 10 / 0

    - TypeError: operation applied to an object of incorrect type  --> '5' + 2

    - ValueError: a function gets an argument of the right type but inappropriate Value  --> int("abc")

    - IndexError: trying to access an index which is out of the range in a list  --> my_list[10]

    - KeyError: searching for a dictionary key that doesn't exist  --> my_dict['age']

    - FileNotFoundError: attempting to open a file that does not exist  --> open("ghost_file.txt")

    - AttributeError: trying to call a method that does not exist for for that object  --> .append() on a string instead of list

2. Exception Hierarchy:
    - All exceptions in python are organized in a 'family tree'
    - top is BaseException, and most common errors belongs to the Exception class

    BaseException:  --> root of all exceptions

    KeyboardInterrupt:  --> when user hits ctrl + c

    SystemExit:  --> program is told to close

    Exception:  --> for all regular errors

3. User-Defined Exceptions:
    - create own custom exceptions by creating a new class that inherits from the Exception class

Task 2: Logging
- built-in way to track events that happens when code runs
- we can categorize message by importance and save them to a file for a later review

-> 5 levels:
1. Debug: 10  --> detailed info, when diagnosing problem
2. Info: 20  --> confermation that things are working as expected
3. Warning: 30  --> an indication that something unexpected happened
4. Error: 40  --> due to more serious problem, software has not been able to perform a function
5. Critical: 50  --> a serious problem, indicate that program itself may be unable to continue running

Task 3: Event
- it is an action that happens in the system
- computer listen these signals and triggers specific code when they occur

common events:
1. Mouse Events:  --> clicking a button, moving the cursor, or scrolling
2. Keyboard Events:  --> pressing a key, releasing a key
3. Window Events:  --> resizing a window, closing the app
4. System Events:  --> a timer finishing, a file finishing a download

Event Patterns:
1. `<Button-1>`: left mouse click  --> event.x, event.y (coordinates)
2. `<Double-1>`: Doulbe click  --> event.num (button number)
3. `<Return>`: Enter key pressed  --> event.widget (the focused element)
4. `<FocusIn>`: Widget gets focus  --> event.type (type of event)
5. `<Motion>`: Mouse moving  --> event.x_root, event.y_root

Task 4: 'with' statement in file handling
- it is a context manager, used to safely and automatically close file even if error occur
- replace long try-catch-finally block
- imporove readability by reducing unnecessary code
- safe file handling

-> working on two special methods
1. `__enter__()`  --> opens the file
2. `__exit__()`  --> ensures file colses automatically

## Day 7

Task 1: Decorators
- decorators are function that takes function and return it with some additional functionalities
- it is a wrapper funtion that modifies the behaviour
- use '`@`' symbol for assigning a decorator to the function

Task 2:
- it is like a blueprint for other classes
- define common interface for all subclasses
- provide shared functionality

`@abstractmethod`:
- it is a decorator
- used inside a ABC(Abstract Base Class) to define a required behavior without providing a actual code for it
- in logic only contains pass
- it catches design error before code is running

Task 4: built-in decorators are like a 'tags' that python provides

1. `@property`:
    - used to make a methods look and act like a variable
    - use with parentheses '()'

2. `@staticmethod`:
    - methods in a class need to know about the object they belong to
    - uses self as a first argument

3. `@classmethod`:
    - it looks at the entire class
    - uses cls as first argument, not self
    - creating a new object from a different data type

4. `@functools.lru_cache`:
    - build-in decorator from the functools library
    - speeding up complex problems

## Day 8

Task 1: Pickling
- this is the process of converting a object into byte stream
- using that it can be saved to a file or transmitted over a network

Task 2: Exceptions and handling

Exceptions:
1. ZeroDivisionError -> divide by zero (5 / 0)
2. ValueError -> correct data type but inappropriate value int("hello")
5. IndexError -> trying to access an list index which is not exist 
6. TypeError -> operation applied to wrong datatype
7. KeyError -> trying to access a dictionary key that hasn't been defined
8. FileNotFoundError -> trying to access the file which is not exist

Exception Handling:

```
try:
    code
except SomeException:
    code
except SomeException:
    code
else:
    code
finally:
    code
```

## Day 9

Task 1: 
- database is a collection of data which is stored electronically
- managed by DBMS allows user to do CRUD operations
- two types:

1. Relational databases(RDBMS):
    - MySQL, PostgreSQL, SQLite
    - stores data in tables as row and column
    - all data connected through keys, enables JOIN operations
    - slower
    - prioritize ACID(Atomicity, Consistency, Isolation, Durability) for accuracy 
    - store in binary file format

2. Non-Relational databases(NoSQL):
    - MongoDB, Cassandra
    - stores data in documents, key-value pairs, wide column and graphs
    - dynamic, each record has different structure
    - no database JOINs are there
    - faster
    - prioritize BASE(Basically Available, Soft state, Eventual consistency) for speed and availability
    - store in json file format

- `mysql -u root -p` --> for connecting to the MySQL  ## here pass is only pressing 'enter' key
- `show databases;` --> for checking all available databases
- `show tables;` --> for checking all available tables in database
- `status;` --> for full info of database
- `use database_name` --> for switch to that database
- `select * from database_name;` --> for getting all tables

different ways to delete database:
1. manual:
    - `DROP DATABASE DATABASE_NAME;`  --> quick terminal work
    - `DROP DATABASE IF EXISTS DATABASE_NAME`
    - directly delete through the terminal

2. programmatic:
    - `cursor.execute("DROP DATABASE IF EXISTS DATABASE_NAME")`  --> automation
    - uses a connector library to delete database through script
    - automatically delete the database

3. shell utility:
    - `mysqladmin -u root -p drop database_name`  --> quick deletion usind linux cmd
    - also delete database through terminal but ask before proceeding
    - delete database without entering into mysql