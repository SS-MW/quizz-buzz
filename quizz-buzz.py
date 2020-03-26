import os
import select
import platform
import traceback


QUESTION_SET = [
    "JAVA",
    "SPRING",
    "AOP",
    "SPRING SECURITY",
    "DATABASES",
    "HTML",
    "CSS",
    "JAVASCRIPT",
    "NODEJS",
    "REACTJS",
    "MAVEN",
    "LINUX",
    "AWS",
    "DOCKER",
    "SYSTEM DESIGN/DEVOPS",
]

java = {

    1:  {
        "Q": '\n\n1.  What is object oriented programming and why is it used?',
        "A": """

- Programs organized around objects.
- Ideal for large and complex programs that need to be actively updated/mainted
- Benefits include:
  - modularity for easier troubleshooting
  - code reuse through inheritance and composition
  - flexibility through polymorphism
  - logical/natural problem solving """

    },

    2: {
        "Q": '\n\n2.  Describe inheritance vs composition',
        "A": """

- Two ways of establishing relationships between classes or objects
- Inheritance is an 'is-a' relationship, composition is a 'has-a' relationship.
- Inheritance is tightly coupled. Changing a parent class affects all child classes.
- Composition is loosely coupled
- Inheritance should be used to create a specialized version of a super class
- Composition should be used to account for ever-changing set of behaviors """

    },

    3: {
        "Q": '\n\n3.  What is aggregation?',
        "A": """

- Similiar to composition, reflects a 'has-a' relationship with other objects
- The aggregate object does not own/instantiate other objects
- When an aggregate object is destroyed, remaining aggregated objects are not. """

    },

    4: {
        "Q": '\n\n4.  What is delegation?',
        "A": """

- OOP concept of passing off the duty/functionality of a class to another class
- Done by creating an instance of the delegate class then calling the methods of that class in the delegating class """

    },

    5:  {
        "Q": '\n\n5.  What are the four pillars of OOP?',
        "A": """
    - Abstraction: Methodology of hiding implementation details from the user and only providing functionality
    - Encapsulation: Mechanism of wrapping up the data and code together as a single unit
    - Inheritance: Process where one class acquires properties of another
    - Polymorphism: Ability of a variable, function, or object to take many forms"""

    },

    6:  {
        "Q": '\n\n6.  What are the two types of polymorphism that Java supports?',
        "A": """

    - Runtime polymorphism: Overriding since the compiler checks at run time what kind of object has to be referenced with which method call
    - Compile-time polymorphism: Overloading since the compiler knows when the program is compiled what method is referenced due to the unique method signature """

    },

    7: {
        "Q": '\n\n7.  What is the diamond problem?',
        "A": """

    An issue with multiple inheritance where class B and C inherit from class A and class D inherits from class B and C, leading to ambiguity about what methods to run when a call to class D is made. """

    },

    8:  {
        "Q": '\n\n8.  What are the differences between JDK, JRE, and JVM?',
        "A": """

    JDK: Java Development Kit, tool used to compile, document, and package Java programs; containes the JRE
    JRE: Java Runtime Environment, implementation of JVM, a physical runtime environment that containes the Java class libraries, class loader and virtual machine, in which Java bytecode can be executed
    JVM: Java Virtual Machine, abstract machine that allows computers to run Java code and manages the programs resources during execution """

    },

    9:  {
        "Q": '\n\n9.  What is classpath in Java?',
        "A": """

    Parameter that the JVM requires to locate the user-defined classes and packages """

    },

    10: {
        "Q": '\n\n10. What is an access modifer?',
        "A": """

    Specify who can access a class, method, or variable. Can be expanded by subclasses, but not narrowed.

        - Private: Only accessible within the class
        - Default: Only accessible within same package
        - Protected: Accessible outside the package but via inheritance only
        - Public: Accessible from anywhwere"""
    },

    11: {
        "Q": '\n\n11. What is a constructor and what are the two types in Java?',
        "A": """

    A constructor is a block of code that is used to initialize an object, must have the same name as that class and no return type, automatically called.

        - Default: Does not take any parameters, instance properties initialized with default values
        - Parameterized: Initializes instance properties with provided parameter values"""

    },

    12: {
        "Q": '\n\n12. What is a method in Java?',
        "A": """

    Function used to represent behavior of an object, must have a return type, invoked explicitly, no default provided"""

    },

    13: {
        "Q": '\n\n13. What is the difference between overloading and overriding?',
        "A": """

    - Overloading: Methods in the same class sharing the same name, but with a different number or type of parameters
    - Overriding: Subclass sharing the same method as parent class, but changed behavior; must have same name, number, and type of parameters and return type; private and static methods cannot be overriden"""

    },

    14: {
        "Q": '\n\n14. What is an abstract class in Java?',
        "A": """

    A class that provides the complete default, code, and/or details that must be overridden; a class can only extend a single abstract class. Methods can be public or protected."""

    },

    15: {
        "Q": '\n\n15. What is an interface in Java?',
        "A": """

    Blueprint of a class that is naturally stateless, contains only method signatures and static constants with no body code; a class can implement several interfaces. Variables are implicitly "public static final" and methods are implicitly "public abstract"."""

    },

    16: {
        "Q": '\n\n16. How do interfaces achieve polymorphism in Java?',
        "A": """

    Interfaces help provide polymorphism through a compositional relationship. Since interfaces do not provide method functionality, the methods can take on different forms when it's implemented in classes. A good example is the runnable interface."""

    },

    17: {
        "Q": '\n\n17. What are the differences between interfaces and abstract classes?',
        "A": """

    Abstract classes are important for code reusability and default functionality, whereas interfaces achieve loose coupling of classes and dynamic method resolution at run time. Therefore, interfaces are better used when objects share a method signature allowing for a polymorphic hierarchy of value types, while abstract classes should be used when objects share a common behavior. Additionally sub-classes can implement multiple interfaces, but only a single abstract class."""

    },

    18: {
        "Q": '\n\n18. What are marker interfaces in Java?',
        "A": """

    Interface with no fields or methods that serve to tag a class. Examples are serializable and cloneable."""

    },

    19: {
        "Q": '\n\n19. What is a singleton in Java?',
        "A": """

    A class which can only have one instance exist at a time per JVM. A class is made singleton by making its constructor private and creating a static method that returns an object of the singleton class contained within the class.

        Eager vs Lazy Singleton:

        - Eager:

            public class Singleton {
            	private static Singleton instance = new Singleton();
            	private Singleton() {}
            	public static Singleton getInstance() { return instance; }
            }

        - Lazy:

            public class Singleton {
            	private static Singleton instance = null;
            	private Singleton() {}
            	public static Singleton getInstance() {
            		if (instance == null) instance = new Singleton();
            		return instance;
            	}
            }
    """
    },

    20: {
        "Q": '\n\n20. How do you make a singleton thread-safe in Java?',
        "A": """

    For a lazily instaniated singleton, make the object field "private static volatile" and use a double checked synchronized block for the getInstance method. For an eager instantiated singleton, simply use the final keyword with the instance."""

    },

    21: {
        "Q": '\n\n21. What does the volatile keyword do?',
        "A":  """

    The volatile keyword is used to mark a java variable as being stored in main memory. More precisely, that means that every read of a volatile variable will be read from the computers main memory, and not from the CPU cache, and every write to a volatile variable will be written to main memory, and not just to the CPU cache."""

    },

    22: {
        "Q": '\n\n22. What is a package in Java?',
        "A": """

    A collection of related classes and interfaces bundled together.

        - Used to modularize code and optimize reuse.
        - Avoids name-clashes
        - Provides easier access control
        - Can contain hidden classes
        - Creates hierarchial structure for location related classes"""

    },

    23: {
        "Q": '\n\n23. What is the JIT compiler in Java?',
        "A": """

    Component of the JRE, the Just In Time compiler converts Java byte code into instructions sent to the computer processor as machine code just in time for execution."""

    },

    24: {
        "Q": '\n\n24. What is a generic in Java?',
        "A": """

    Allows methods or classes to accept a set of related types, providing compile time safety, catching invalid types at compile time and flexibility.

        - Generic methods: methods written with a single method declaration and can be called with arguments of different types. Use a <> enclosing of the type before return type declaration. Can have multiple type parameters, i.e. <T extends Number & Comparable> or <T>

        - Generic classes: classes with names followed by a type parameter section indicating the parameters it accepts, i.e. public class Box<T>"""

    },

    25: {
        "Q": '\n\n25. What is a wrapper class in Java?',
        "A": """

    Class whose object wraps a primitive data type, allows primitive to use java.util packages, and supports synchronization in multi-threading

    - Auto-boxing: automatic conversion of primitive types to the corresponding wrapper class
    - Auto-unboxing: automatic conversion of wrapper class to primitive type"""

    },

    26: {
        "Q": '\n\n26. Why is it important to override equals and hashcode for objects?',
        "A": """

    If not overridden, equals will perform a comparison on object memory address, that is unique for each instance. Hashcode is necessary so that packages such as HashSet, HashMap, HashTable can hash equal objects correctly, where two object instances that are equal should have the same integer hash code value, though they can also have the same hash code if they are not equal, however not ideal."""

    },

    27: {
        "Q": '\n\n27. What are the two types of exceptions in Java?',
        "A": """

    - Checked exception: Exceptions checked at compile time, if a method throws a checked exception, then the method must either handle it or throw it again. Compiler will know because the check exception is thrown and must be handled before compilation is completed.
    - Unchecked exception: Exceptions not checked at compile time, i.e division by zero"""

    },

    28: {
        "Q": '\n\n28. How do you create a thread in Java?',
        "A": """

    - The Runnable interface in java that is to be implemented by a class whose instances are intended to be executed by a thread, in which case run() method of Runnable must be overridden.
    - Thread class which can be extended to create a class that can be executed by a thread. run() method must be overridden"""

    },

    29: {
        "Q": '\n\n29. Which method of creating a thread is better?',
        "A": """

    Implementing runnable is almost always better due to it being an interface, allowing for extension of another abstract class. If you want to override the thread start() method, extending thread is the better option."""

    },

    30: {
        "Q": '\n\n30. What are the different states a thread can be in?',
        "A": """

    - New: When created
    - Runnable: Ready to run, could also be running
    - Blocked: About to enter a synchronized block
    - Waiting: Waiting for a signal from another thread
    - Timed Waiting: Timed out
    - Terminated: Finished execution or errored out"""

    },

    31: {
        "Q": '\n\n31. What is multi-threading?',
        "A": """

    Feature that allows concurrent execution of two or more parts of a program for maximum utilization of CPU. Each part is a thread, a light-weight process."""

    },

    32: {
        "Q": '\n\n32. What are the wait() and notify() methods for?',
        "A": """

    Wait and notify are how Java avoids polling between threads and resources. Wait() tells the calling thread to give up a lock and go to sleep unil another thread calls the notify() method, allowing it to continue operation after the current thread release the lock."""

    },

    33: {
        "Q": '\n\n33. What does the synchronization keyword in Java do?',
        "A": """

    Multi-threaded programs may come to a situation where multiple threads try to access and change the same resources, known as race conditions. Synchronized blocks in java are synchronized on some object meaning that it can only have one thread executing inside them at a time. All other threads attepmting to enter the synchronized block are blocked until the thread inside the synchronized block exits."""

    },

    34: {
        "Q": '\n\n34. What is a deadlock?',
        "A": """

    Occurs when two threads are waiting on each other to release the locks, creating a race condition around who will release the lock first creating a deadlock."""

    },

    35: {
        "Q": '\n\n35. What is the producer/consumer problem?',
        "A": """

    With a producer thread, consumer thread, and shared fixed-size buffer, the producer should not try to add data into the buffer if it's full and the consumer cannot remove data from an empty buffer."""

    },

    36: {
        "Q": '\n\n36. What is a stream?',
        "A": """

    Sequence of objects that supports methods such as filter, map, collect, and reduce that can be piped to produce the desired result."""

    },

    37: {
        "Q": '\n\n37. What are some methods for streams?',
        "A": """

    - map
    - filter
    - sorted
    - forEach
    - collect
    - reduce
    """

    },

    38: {
        "Q": '\n\n38. What is garbage collection and how does it work in java?',
        "A": """

    Automatic process implmented by the JVM in which unreferenced objects in the heap memory are identified and marked as ready for gabage collection, marked objects are deleted based on a generational strategy that categorizes objects by age. All other processes pause during garbage collection. Different areas of heap space:

        - Young gen: Newly created objects
        - Old gen: Objects that are long-lived eventually are moved into old gen
        - Metaspace: static methods and variables and important metadata, constant pools, etc"""

    },

    39: {
        "Q": '\n\n39. What are the two types of variables in Java?',
        "A": """

    - Local variable: Used inside a method, constructor, or block, has a local scope
    - Instance variable: Variable bound to the object itself, that can only be used by the instance of that object"""

    },

    40: {
        "Q": '\n\n40. What does the static keyword do?',
        "A": """

    Method belonging directly to a class that can be called without creating an instance of the class, can only access other static instance variables and methods, unless a reference is passed in, cannot be overridden."""

    },

    41: {
        "Q": '\n\n41. What does the final keyword do?',
        "A": """

    - Final variable: Variable whos value cannot be changed after assignment
    - Final method: Method that canno be overridden by the inheriting class
    - Final class: Class cannot be extended by any subclass, but can extend another class"""

    },

    42: {
        "Q": '\n\n42. Describe Final vs Finally vs Finalize',
        "A": """

    - Final is a keyword used to apply restrictions on class, method, and variable. Final class can't be inherited, final method can't be overridden and final variable value cant be changed.
    - Finally is a block keyword used to place important code that will be executed whether exception is handled or not
    - Finalize is a garbage collection method used to perform clean up processing just before an object is garbage collected"""

    },

    43: {
        "Q": '\n\n43. What does break and continue do in Java?',
        "A": """

    - Break: Used in switches or loops that cause the innermost loop or switch to terminate when executed
    - Continue: Used in loops to jump to the next iteration of the innermost loop"""

    },

    44: {
        "Q": '\n\n44. What does this() and super() represent in Java?',
        "A": """

    - this(): represents the current instances of a class, used to call default constructors, access methods, pointing to the current instance
    - super(): represents the current instance of a parent/base class, used to call default construtors of parent/base class, access methods of base class, pointing to superclass."""

    },

    45: {
        "Q": '\n\n45. What is a linked list in java?',
        "A": """

    Linked List are linear data structures where the elements are not stored in contiguous locations and every element is a separate object with a data part and address part. The elements are linked using pointers and addresses."""

    },

    46: {
        "Q": '\n\n46. What is the difference between queue and deque?',
        "A": """

    Deque or double-ended queue supports addition and removal of elements from either end of the data structure (FIFO) and (LIFO) whereas queues only support addition to the end and removal from the front (FIFO). """

    },

    47: {
        "Q": '\n\n47. What is a PriorityQueue in Java?',
        "A": """

    PriorityQueue is a queue that follows the FIFO algorithm but allows from processing of element by a comparable priority parameter, essentially a priority heap. Default is lowest value to highest, think ranking. """

    },

    48: {
        "Q": '\n\n48. How do you make a collection class thread-safe?',
        "A": """

    In the case of HashMap and ArrayList, HashTable/ConcurrentHashMap and Vector provides thread-safe alternatives. Otherwise, the collection can be wrapped using a Collections.synchronized wrapper corresponding to the interface class. I.e. Collections.synchronizedSet(new TreeSet<>()); In the case of HashMap, ConcurrentHashMap is best for concurrent performance due to a map being divided into synchronized segments, allowing multiple threads to access at once unlike HashTable where the entire map is synchronized."""
    },

    49: {
        "Q": '\n\n49. How does the collection hierarchy look in Java?',
        "A": """

    - Map: Interface of Util package that maps unique keys to values, cannot contain duplicate keys and is a one-to-one relationship
    - Collection: Interface of Util package that is parent of List, Queue, and Set, also interfaces
    - List: Parent of ArrayList, Vector (Parent of Stack), and LinkedList
    - Queue: Parent of LinkedList, Deque, and PriorityQueue
    - Set: HashSet, SortedSet (Parent of TreeSet)"""

    },

    50: {
        "Q": '\n\n50. What does JDBC do and what steps are taken to use it?',
        "A": """

    Software component that enables java applications to interact with databases
        - Steps: Register driver class, create connection, create statement, execute query, close connection
        - Returns are stored as a ResultSet, representing a row of a table
        - Statement: General purpose access to database
        - Prepared Statement: Uses input parameters to create query during execution"""

    },

    51: {
        "Q": '\n\n51. What is an object pool?',
        "A": """

    Used for expensive objects, a container that contains some number of objects so that when an object is taken from the pool, it is not available in the pool until it is returned """

    },

    52: {
        "Q": '\n\n52. What does the Javac compiler do?',
        "A": """

    Converts the Java programs into a class file, containing byte code, that can be executed on any computer """

    },

    53: {
        "Q": '\n\n53. Explain public static void main(String args[]) in Java?',
        "A": """

    - Public is an access modifier, used to specify who can access this method
    - Static is a keyword, in this case meaning that a method can be accessed without creating an instance of a class,
    - Void is a return type, defines that the method will not return a value
    - String args[] is a parameter passed to the main method"""

    },

    54: {
        "Q": '\n\n54. Why is Java not 100% Object-oriented?',
        "A": """

    It uses 8 primitive data types"""

    },

    55: {
        "Q": '\n\n55. What are the differences between ArrayList vs Linked List vs Vector?',
        "A": """

    ArrayList is not synchronized, not thread-safe, does not define increment size, uses Iterator for traversal, and faster, vector is synchronized, thread-safe, defines increment size, uses Enumeration and Iterator for traversal, and slower; LinkedList is implemented with queues and list."""

    },

    56: {
        "Q": '\n\n56. What is the difference between Equals() vs ==?',
        "A": """

    Equals() is used for checking content equality of two objects defined by business logic, == is used for primitives and reference comparison for objects"""

    },

    57: {
        "Q": '\n\n57. What is the difference between stack and heap memory?',
        "A": """

    Stack memory is used by a single threads of execution, can’t be accessed by other threads, LIFO methods to free memory, exists until end of execution of thread, only contains local primitives and references to objects in heap space. Heap memory is used by all parts of the application, objects stored in heap are globally accessible, memory management based on generation of object, lives from start to finish of app execution, all objects are stored in heap space."""

    },

    58: {
        "Q": '\n\n58. Why are pointers not used in Java?',
        "A": """

    Pointers are unsafe and increases the complexity of the program. Also the JVM uses implicit memory allocation so pointers are not necessary."""

    },

    59: {
        "Q": '\n\n59. Why are Java Strings immutable?',
        "A": """

    Strings are cached in the String pool, maintained in the Java heap, and shared between multiple clients, so actions from one client might affect the rest if it was mutable, enhancing security, caching, and synchronization."""

    },

    60: {
        "Q": '\n\n60. What is the difference between creating String with “” vs new String(“”)?',
        "A": """

    When quotations are used, Java first searches for an existing string that matches in the String pool. However, when new String is used, Java creates a new String object in the heap space every time."""

    },

    61: {
        "Q": '\n\n61. How do you make a class immutable?',
        "A": """

    Make all fields private and final. Don’t provide and setters. Return clones of the fields in the getter methods to return a copy of the field rather than the actual reference."""

    },

    62: {
        "Q": '\n\n62. Describe HashMap vs HashTable',
        "A": """

    HashTables are synchronized and thread-safe, HashMap are not. HashTable does not allow null keys or values, HashMap allows a single null key and any number of null values. """

    },

    63: {
        "Q": '\n\n63. Shallow vs Deep Clone',
        "A": """

    The shallow copy of an object will have exact copies of all the fields of the original object. If the original object has any references to other objects as fields, then only references of those objects are copied into clone objects, copies of those objects are not created. Deep copy of an object will have exact copies of all the fields of original object just like a shallow copy. But in addition, if the original object has any references to other objects as fields, then copies of those objects are also created by calling clone() method on them, creating two completely dis-joint objects."""

    },

    64: {
        "Q": '\n\n64. What is the serializable interface used for?',
        "A": """

    Serialization is a mechanism that allows objects to be represented as a sequence or stream of bytes including the object’s data, type, and types of data stored in the object in order to be passed around, including between platforms. In Java, the serializable interface must be implemented and all fields in the class must also be serializable. """

    },

    65: {
        "Q": '\n\n65. What does the transient keyword do?',
        "A": """

    The transient keyword is used in serializable classes to indicate a field that should not be passed during serialization, especially useful for sensitive information (credit card number, SSN, etc.)"""

    },

    66: {
        "Q": '\n\n66. What is variable and method hiding?',
        "A": """ Overriding except for static variables and methods and it occurs at compile-time."""
    },

    67: {
        "Q": '\n\n67. New Features in Java 8?',
        "A": """

    forEach() method in Iterable interface, default and static methods in Interfaces, Lambda expressions, Java Stream API (Works well with improved Iterable interface), improved Java Time API (Time Zones!), and various Collection and Concurrency API improvements. \n\n\n\n"""

    }
}

spring = {

    1: {
        "Q": '\n\n1. Tight Coupling vs Loose Coupling',
        "A": """
Tight Coupling: When a class is dependent on another class’s object; one class knows a lot about the other’s implementation
Loose Coupling: Removes the dependency by only allowing a class to know what the other has exposed through its interface"""

    },

    2: {
        "Q": '\n\n2. What is dependency injection?',
        "A": """

An aspect of Inversion of Control stating that objects do not need to be created manually, just described how they should be created and an IoC container will instantiate required classes when needed."""

    },

    3: {
        "Q": '\n\n3. What are the three types of dependency injection?',
        "A": """

- Constructor Injection: No partial injection, doesn’t override setter methods, creates new instance if any modification occurs, better for large number of properties
- Setter Injection: Partial injection, overrides the constructor property, doesn’t create new instances when a property value is changes, better for smaller number of properties
- Interface Injection: Implemented interface that uses the interface method to inject the object in the main class, useful for loggers """

    },

    4: {
        "Q": '\n\n4. What is Inversion of Control?',
        "A": """

A design pattern that provides loose coupled programs by removing dependencies from your code, in Spring the IoC container creates instances of objects, configures the instance, and assembles the dependencies. """

    },

    5: {
        "Q": '\n\n5. What are the two Inversion of Control containers in Spring?',
        "A": """

Two IoC containers in Spring:
    - BeanFactory: A basic container that provides and manages bean instances by finding beans, identifying and wiring dependencies, and managing the lifecycle
    - ApplicationContext: Interface representing an advanced container that holds all information, metadata, and beans in the application. Can be defined using XML or the @Configuration annotation. """

    },

    6: {
        "Q": '\n\n6. What are beans in Spring?',
        "A": """

Java objects that are initialized by the Spring IoC container. """

    },

    7: {
        "Q": '\n\n7. What are the different scopes of beans in Spring?',
        "A": """

- Singleton: Default. Bean instance will only be instantiated once and the same instance is returned by the IoC container.
- Prototype: Bean instance is created each time it’s requested
- Request: Bean instance is created per HTTP request
- Session: Bean instance is created per HTTP session
- Global-session: Bean instance is created per HTTP global session """

    },

    8: {
        "Q": '\n\n8. What is the lifecycle of a bean?',
        "A": """

1. Bean Definitions Loaded
2. Post Process Bean Definitions
3. For each bean: Instantiate Bean
4. For each bean: Setters Called
5. Beans Initialized
6. Beans Ready for Use """

    },

    9: {
        "Q": '\n\n9. What is autowiring in Spring?',
        "A": """

Enables implicit automatic injection of beans so the IoC container knows to inject a bean. Modes: no, byName, byType, constructor, autodetect. No autowiring is default unless @Autowired annotation is used, then byType is the default. """

    },

    10: {
        "Q": '\n\n10. What is component scan in Spring?',
        "A": """

Component Scan: Method of asking Spring to detect Spring-managed components, can be done using the @Configuration or @ComponentScan annotation or XML. In Spring Boot, @SpringBootApplication performs the scan. """

    },

    11: {
        "Q": '\n\n11. What is the Spring Boot Actuator?',
        "A": """

Actuator: spring-boot-actuator module that provides all of Spring Boot’s production ready features that allow developers to monitor and interact with the application through a number of built-in endpoints """

    },

    12: {
        "Q": '\n\n12. What is JAX-RS?',
        "A": """

Java API for RESTful Web Services is a Java API that provides support in creating web services according to the REST architectural pattern using annotations to simplify Java development of a REST API. (@Produces, @Consumes, @Get, @Put, etc.) """

    },

    13: {
        "Q": '\n\n13. What is an E-Tag?',
        "A": """

A HTTP response header containing a hash code used to determine changes in content at a given URL. First request contains etag and the second request for the same resource will send a 304 redirect status code to indicate for the browser to check previously cached data. Reduces bandwidth and network traffic. """

    },

    14: {
        "Q": '\n\n14. What is SOAP?',
        "A": """

A XML based messaging protocol for exchanging information in computer networks. """

    },

    15: {
        "Q": '\n\n15. What is REST?',
        "A": """

 A software architectural style that defines a set of constraints for creating web services including being a client server, stateless, cacheable, layered, and having a uniform interface """

    },

    16: {
        "Q": '\n\n16. What is Eureka?',
        "A": """

A REST service discovery service developed by Netflix for locating services for load balancing and failovers """

    },

    17: {
        "Q": '\n\n17. Describe REST vs SOAP',
        "A": """

SOAP is a protocol, REST is an architectural style; SOAP uses service interfaces to expose functionality, REST uses URI’s; SOAP is XML only, REST permits HTML, plain text, XMl, JSON, etc. SOAP requires more bandwidth """

    },

    18: {
        "Q": '\n\n18. What is Spring?',
        "A": """

A lightweight, loosely coupled, integrated framework for the development of Java EE applications """

    },

    19: {
        "Q": '\n\n19. What are the benefits of using Spring?',
        "A": """

It’s lightweight, with little overhead of using the framework in development. Inversion of control, which takes care of wiring dependencies of various objects instead of creating or looking for dependent objects. Aspect oriented programming, which allows separation of business logic from system services. MVC framework, which is used to create web applications or RESTful web services. Fast development, reducing the amount of boiler-plate code in JDBC operations, file uploading, etc. """

    },

    20: {
        "Q": '\n\n20. Name some sub-projects of Spring',
        "A": """

Core, Web, JDBC, ORM integration (JPA, JDO, Hibernate) """

    },

    21: {
        "Q": '\n\n21. How are beans created?',
        "A": """

They can be created using a setter injection, a constructor injection, or field injection through annotations (@Bean) or XML files. Constructor arguments are best for mandatory dependencies, since they allow for injecting values into immutable fields, and setters are best for optional dependencies. """

    },

    22: {
        "Q": '\n\n22. What is an Embedded Server in Spring Boot?',
        "A": """

In Spring Boot, a server is available as part of the application in the jar, making deployment easy and independent. """

    },

    23: {
        "Q": '\n\n23. What is Spring MVC used for?',
        "A": """

Provides a decoupled approach to developing web apps through the use of DispatchServlet, ModelAndView, and ViewResolver. """

    },

    24: {
        "Q": '\n\n24. What is the front controller class of Spring MVC?',
        "A": """

DispatchServlet works as the front controller. The first request from a client will go to the DispatchServlet and dispatch to the appropriate controllers """

    },

    25: {
        "Q": '\n\n25. How does Spring MVC work?',
        "A": """

When the client sends a request to a specific URL, the request first hits the web container which looks into its web.xml file and finds the servlet that is mapped to that URL. The servlet is then delegated to process that request. In Spring MVC, this is the DispatchServlet, which listens for a URL pattern to match and pass the request to the correct controller based on the URL requested based on the RequestMapping annotation or MVC configuration file. """

    },

    26: {
        "Q": '\n\n26. Spring MVC vs Spring REST',
        "A": """

Spring MVC requires binding the controller and views tightly so that Spring MVC can manage the view data. Spring REST separates the controller from the view and manages the controller exclusively for exposing data through REST API’s.  """

    },

    27: {
        "Q": '\n\n27. What is JPA?',
        "A": """

Java Persistence API (JPA): Defines the mapping from Java object to a record in a database table. JPA provides useful annotations which can help define the relationship between classes and tables """

    },

    28: {
        "Q": '\n\n28. What is Hibernate?',
        "A": """

Hibernate helps create queries under the hood to interact with databases using the JPA mappings """

    },

    29: {
        "Q": '\n\n29. What are the advantages of using JdbcTemplate?',
        "A": """

JdbcTemplate takes care of creating the connection, creating the statement, starting the transaction, committing the transaction, and closing the connection. """

    },

    30: {
        "Q": '\n\n30. Difference between JDBC and Spring JDBC?',
        "A": """
In JDBC, checked exceptions need to be written, in Spring JDBC, those exceptions are made into runtime exceptions, requiring manual exception handling. """

    },

    31: {
        "Q": '\n\n31. What are the 3 object states in Hibernate?',
        "A": """
Transient: Object not associated with Hibernate, Persistent: Object is representing a record in a table, Detached: Object is just removed from Hibernate\n\n\n\n """

    }

}

aop = {

    1: {
        "Q": '\n\n1. What is AOP?',
        "A": """

Aspect Oriented Programming (AOP): Methodology that divides the program logic into pieces or concerns to improve modularization. This separation of concerns (SoC) makes software easier to maintain by grouping features and behaviors into parts with a specific purpose. """

    },

    2: {
        "Q": '\n\n2. What is a cross-cutting concern in AOP?',
        "A": """

Concern that affects the entire application, but should be centralized in one location in code. i.e. transaction management, authentication, logging, security, etc. """

    },

    3: {
        "Q": '\n\n3. What is a join point AOP?',
        "A": """

Any point in the program. i.e. method execution, exception handling, field access, etc. """

    },

    4: {
        "Q": '\n\n4. What is an advice in AOP and what are the different types?',
        "A": """

Action taken by an aspect at a particular join point. Types: Before Advice, After Returning Advice, After Throwing Advice, After (finally) Advice, Around Advice """

    },

    5: {
        "Q": '\n\n5. What is a pointcut in AOP?',
        "A": """

Expression Language of AOP"""

    },

    6: {
        "Q": '\n\n6. What is an aspect in AOP?',
        "A": """

A class that contains advices and join points """

    },

    7: {
        "Q": '\n\n7. What is an interceptor in AOP?',
        "A": """

A class that contains a single advice """

    },

    8: {
        "Q": '\n\n8. What is a target object in AOP?',
        "A": """

A proxy object that is advised by one or more aspects """

    },

    9: {
        "Q": '\n\n9. What is weaving in AOP?',
        "A": """

Process of linking aspects with target application, occurs at runtime """

    }
}

spring_security = {

    1: {
        "Q": '\n\n1. Authentication vs Authorization?',
        "A": """

Authentication: User is who they say they are
Authorization: User can access what they want to access """

    },

    2: {
        "Q": '\n\n2. Granted Authorities vs Roles?',
        "A": """

Granted Authorities: Individual privilege that restricts access in a fine-grained manner
Role: Coarse-grained access restriction that is essentially a container for granted authorities/privileges """

    },

    3: {
        "Q": '\n\n3. How does basic authentication work in Spring Security?',
        "A": """

Done via a basic HTTP header with the user and password encoded in base64 in the format “user:password”. Does not require cookies, session identifiers, or login pages, making it the simplest form of authentication. However, it is vulnerable to man in the middle attacks so everything should be done over a SSL connection. """

    },

    4: {
        "Q": '\n\n4. How does form-based authentication work in Spring?',
        "A": """

Forms Based Authentication: Upon login of the user, Spring authenticates and creates a JSESSIONID as a cookie that is returned as a response. For further communication, that JSESSIONID cookie is used for the client to communicate back and forth with the server with the server checking the session each time. """

    },

    5: {
        "Q": '\n\n5. How does JWT Authentication work in Spring?',
        "A": """

JWT Authentication: Upon login of the user, Spring security server creates and returns an access token for the authenticated user. For every request to the resource server, a resource server must validate the access token, checking for proper authorization and authentication before the request is handled """

    },

    6: {
        "Q": '\n\n6. How is a JWT Token formatted?',
        "A": """

(Header(Hashing algorithm + Type). Payload(Data). Signature(Secret)) """

    },

    7: {
        "Q": '\n\n7. How is Spring Security implemented?',
        "A": """

Spring Security is implemented using Servlet Filters under the hood to pre-process and post-process web requests """

    },

    8: {
        "Q": '\n\n8. What is OAuth2?',
        "A": """

An authentication framework where the application requiring authentication delegates user authentication to a separate service that hosts the user account such as Google or Facebook. """

    },

    10: {
        "Q": '\n\n10. What is SSL? TLS?',
        "A": """

- Secure Sockets Layer (SSL): Standardized technology protocol for keepings internet connections secure by requiring encryption algorithms to ensure data passed remains private. When a website is encrypted with SSL the browser first makes sure that the website has a valid SSL certificate before accessing its information.
- Transfer Layer Security (TLS): Is successor of SSL which is more rigid in its standards for security such as requiring stronger cipher suites """

    }
}

databases = {

    1: {
        "Q": '\n\n1. What is a database?',
        "A": """

Organized collection of data, stored and retrieved digitally from a remote or local computer """

    },

    2: {
        "Q": '\n\n2. What is the Difference between DBMS and RDBMS?',
        "A": """

DBMS: Database Management System, system software responsible for creation, retrieval, updating, and management of a database.
RDBMS: Relational DBMS, stores data in the form of a collection of tables and relations defined between the common fields of the tables """

    },

    3: {
        "Q": '\n\n3. What is SQL?',
        "A": """

Standard language for relational database management systems """

    },

    4: {
        "Q": '\n\n4. DDL vs DML vs DCL',
        "A": """

- DDL: Data Definition Language, allows various operations on the database such as CREATE, ALTER, and DELETE
- DML: Data Manipulation Language, allows access and manipulation on data such as INSERT, UPDATE, DELETE, and, SELECT
- DCL: Data Control Language, allows control of access to the database, i.e. granting and revoking access permissions """

    },

    5: {
        "Q": '\n\n5. How are SQL databases organized?',
        "A": """

- Table: Organized collection of data stored in the form of rows and columns
- Fields: The columns of a table
- Records: The rows of a table """

    },

    6: {
        "Q": '\n\n6. What are SQL constraints?',
        "A": """

Used to specify the rules concerning data in the table during creation or after the creation of the table

- NOT NULL: Restricts null values
- CHECK: Verifies that all values satisfy a condition
- DEFAULT: Assigns a default value if no value is specified
- UNIQUE: Ensures unique values to be inserted into the field; there can be multiple unique constraints per table; can be null
- INDEX: Indexes a field providing faster retrieval of records
- PRIMARY KEY: Uniquely identifies each record in a table, must contain unique, non-null values; a table in SQL is restricted to have one and only one primary key, comprised of single or multiple fields
- FOREIGN KEY: Ensures referential integrity for a record in another table; can be a single or collection of fields that refer to the primary key of another table """

    },

    7: {
        "Q": '\n\n7. What is a join in SQL and what are the different types?',
        "A": """

Combines records from two or more tables based on a related column between the two

- (INNER) JOIN: Retrieves records with matching values in both tables involved in the join
- LEFT JOIN: Retrieves all records from the left table and matched records from the right
- RIGHT JOIN: Retrieves all records from the right table and matched records from the left
- FULL JOIN: Retrieves all records from both tables with matches displayed once
- CROSS JOIN: Cartesian Product of two tables
- SELF JOIN: A table joined with itself """

    },

    8: {
        "Q": '\n\n8. What is an index and what are the different types in SQL?',
        "A": """

Data structure used for quick lookup of data in a table

- Unique Index: Maintain data integrity by ensure that no two records of a table has identical key values
- Non-unique Index: Used to improve query performance by maintaining a sorted order of data values that are used frequently
- Clustered Indexes: Indexes whose order of the rows in the database correspond to the order of the rows in the index; only one can exist in a given table; used for easy and speedy retrieval of data
- Non-clustered Indexes: Creates separate entity within the table which references the original table; a table can have multiple non-clustered indexes """

    },

    9: {
        "Q": '\n\n9. What is data integrity?',
        "A": """

The assurance of accuracy and consistency of data over its entire lifecycle """

    },

    10: {
        "Q": '\n\n10. What is a query?',
        "A": """

A request for data from a database table or combination of tables """

    },

    11: {
        "Q": '\n\n11. What is a SQL cursor?',
        "A": """

A control structure that allows for traversal of records in a database query result-set one-by-one.

- Implicit Cursor: Declared automatically when DML statements are executed
-  Explicit Cursor: Have to be manually declared when SELECT statements returning more than one row are executed """

    },

    12: {
        "Q": '\n\n12. What is a SQL trigger?',
        "A": """

A stored procedure in a database that automatically invokes whenever a special event occurs  """

    },

    13: {
        "Q": '\n\n13. Entity vs Relationship?',
        "A": """

Entity: An identifiable object with associated properties that provide it an identity
Relationship: Links between entities that have something to do with each other """

    },

    14: {
        "Q": '\n\n14. What are the 3 types of relationships in a database(multiplicity)?',
        "A": """

- One-to-One: Each record in one table is associated with a maximum of one record in another
- One-to-Many: Record in a table is associated with multiple records in the other table
- Many-to-Many: Multiple instances on both sides are needed for defining a relationship """

    },

    15: {
        "Q": '\n\n15. What is an alias in SQL?',
        "A": """

Temporary name assigned to the table or table columns to hide the real names  """

    },

    16: {
        "Q": '\n\n16. What is a view in SQL?',
        "A": """

Virtual table based on the result-set of a SQL statement """

    },

    17: {
        "Q": '\n\n17. What is denormalization?',
        "A": """

Technique of adding redundant data to tables to avoid costly joins when querying the database """

    },

    18: {
        "Q": '\n\n18. What are data anomalies?',
        "A": """

Issues that arise from DML statements.

- Update anomaly: Data inconsistency due to data redundancy resulting in a partial update
- Delete anomaly: Unintended loss of data due to delete
- Insert anomaly: Inability to add data due to missing other data """

    },

    19: {
        "Q": '\n\n19. What is normalization?',
        "A": """

Method of organizing structured data in a database efficiently """

    },

    20: {
        "Q": '\n\n20. What are the normal forms?',
        "A": """

- First Normal Form: Every record is unique and every attribute in a field is a single-valued attribute, i.e. there cannot be multiple book issued in a record per student, should have a record per student per book issued
- Second Normal Form: Satisfies first normal form and cannot have partial dependency where a non-candidate key depends on a candidate key of the table, i.e. book issued depends on the student so they should be separated into two tables, one student and one books issued; usually solved by using a single primary key
- Third Normal Form: Satisfies second normal form and cannot have transitive dependency between non-candidate attributes, like having separate fields for zip code and address.
- Boyce-Codd Normal Form: For every functional dependency in the table, the left-hand side is the super key  """

    },

    21: {
        "Q": '\n\n21. Aggregate vs Scalar functions in SQL',
        "A": """

- Aggregate functions: Performs operations on a collection of values to return a single scalar value: AVG(), COUNT(), MIN(), MAX(), SUM(), FIRST(), LAST()
- Scalar functions: Returns a single value based on input value: LEN(), UCASE(), LCASE(), MID(), CONCAT(), RAND(), ROUND(), NOW(), FORMAT() """

    },

    22: {
        "Q": '\n\n22. What is a database transaction?',
        "A": """

A single unit of work for a DBMS which represents some kind of change in a database; can be made up of several operations  """

    },

    23: {
        "Q": '\n\n23. What does ACID stand for?',
        "A": """

ACID stands for a set of standards for transactions

- Atomicity: Transaction must succeed completely or fail completely
- Consistency: Data written to the database must be valid for all defined rules: constraints, cascades, triggers, etc.
- Isolation: Concurrently execution of transactions leaves the database in the same state as if transactions were executed sequentially
- Durability: Once a transaction is committed, it will remain committed even if the system fails; i.e. stored in non-volatile memory """

    },

    24: {
        "Q": '\n\n24. What is sharding?',
        "A": """

Partitioning data into smaller databases to have faster access to data, this allows faster data fetching """

    },

    25: {
        "Q": '\n\n25. What is the CAP theorem?',
        "A": """

CAP Theorem: States three basic requirements for an application with distributed architecture
- Consistency: Data in the database must be consistent before and after execution of operation
- Availability: System should always be up and running
- Partition Tolerance: System should work even if servers are unreliable """

    },

    26: {
        "Q": '\n\n26. What are some common clauses used with SELECT query in SQL?',
        "A": """

WHERE is used to filter records based on specific conditions, ORDER BY is used to sort the records based on some fields in ascending or descending order, GROUP BY is used to group records with identical data in a field, HAVING is used with the GROUP BY to further filter aggregated records """

    },

    27: {
        "Q": '\n\n27. What are UNION, MINUS, and INTERSECT commands?',
        "A": """

UNION combines and return the result-set of two or more SELECT statements, MINUS removes duplicates from the first result-set that are also found in the second result-set, INTERSECT combines the result-sets where records match each other """

    },

    28: {
        "Q": '\n\n28. Compare NoSQL and SQL',
        "A": """

NoSQL is less organized and structured, more scalable and flexible, limited in querying due to lack of joins, and stored using key-value pairs, documents, columns, XML, and graphs. SQL is organized and structured, not as scalable, handles complex queries better, and stores the data in tables """

    },

    29: {
        "Q": '\n\n29. What are the types of NoSQL databases?',
        "A": """

- Key-value store: Database is essentially a large hash-table of keys and values (i.e. Amazon S3)
- Document: Stores documents of tagged elements (i.e. MongoDB)
- Column: Each storage block contains a single column of data (i.e. Cassandra)
- Graph: Uses edges and nodes to represent data (i.e. Neo4J) """

    }
}

html = {

    1: {
        "Q": '\n\n1. What is HTTP?',
        "A": """

The Hypertext Transfer Protocol (HTTP) is an application protocol for distributed, collaborative, hypermedia information systems such as the world wide web. """

    },

    2: {
        "Q": '\n\n2. What is HTML?',
        "A": """

Hyper Text Markup Language; standard text formatting language which is used to create and display pages on the web """

    },

    3: {
        "Q": '\n\n3. What is an HTML element?',
        "A": """

Individual component of HTML web page or document representing semantics/meaning; i.e. title """

    },

    4: {
        "Q": '\n\n4. What is a HTML tag?',
        "A": """

Root of HTML document which is used to specify that the document is HTML; i.e. head; Also used to format text placed between tags.
- HTML 5 introduced semantic tags header, nav, section, article, and footer """

    },

    5: {
        "Q": '\n\n5. What is a HTML attribute?',
        "A": """

Additional keywords that can be used after the name of a tag to change the way the tag behaves or is displayed; some only accept predefined values, others can accept numerical values """

    },

    6: {
        "Q": '\n\n6. Block-level vs in-line element?',
        "A": """

- Block-Level Element: Drawn as a block that stretches to fill the full width available to it; i.e. <div>, <img>, <section>, <form>, <nav>
- In-Line Element: Drawn where they are defined, only taking up the space that is absolutely needed; i.e. <span>, <b>, <strong>, <a>, <input> """

    },

    7: {
        "Q": '\n\n7. Types of lists in HTML?',
        "A": """

Ordered(numbered), unordered(bulleted), definition (definition indenting), menu, directory
Character Entities: Replacements for reserved characters in HTML """

    },

    8: {
        "Q": '\n\n8. Types of forms and input types in HTML?',
        "A": """

Tag that allows for user input

- Elements: form, input, textarea, label, fieldset, legend, select, optgroup, option, button, datalist, output
- Input types: button, checkbox, color, date, datetime-local, email, file, hidden, image, month, number, password, radio, range, reset, search, submit, tel, text, time, url, week """

    },

    9: {
        "Q": '\n\n9. What is an HTML image map?',
        "A": """

Image Map: Allows linking different pages using a single image through a mapping of shapes layered on top of the image. """

    },

    10: {
        "Q": '\n\n10. What’s a hyperlink in HTML?',
        "A": """

Created using an anchor tag; links one page to another; <a href = “link target”> Link text</a>; can link to different sections of a page setting link target to “#top” with an anchor tag at the top of the page <a name=”top”> """

    },

    11: {
        "Q": '\n\n11. What’s an iFrame in HTML?',
        "A": """

Tag used to display a nested webpage """

    },

    12: {
        "Q": '\n\n12. What is <!DOCTYPE> in HTML?',
        "A": """

<!DOCTYPE> - used to instruct the web browser about what type of html the page is in. """

    },

    13: {
        "Q": '\n\n13. What media formats does HTML support?',
        "A": """

Supported Media Formats:
- Images– png, jpg, jpeg, gif, apng, svg, bmp, BMP ico, png ico
- Audio– MIDI, RealAudio, WMA, AAC, WAV, Ogg, MP3, MP4
- Video– MPEG, AVI, WMV, QuickTime, RealVideo, Flash, Ogg, WebM, MPEG-4 or MP4 """

    },

    14: {
        "Q": '\n\n14. What types of storage is offered in HTML 5?',
        "A": """

Local storage (cache) and session storage (Deleted every session) """

    },

    15: {
        "Q": '\n\n15. What is WAI-ARIA?',
        "A": """

WAI-ARIA, the Accessible Rich Internet Applications Suite, defines a way to make Web content and Web applications more accessible to people with disabilities. It especially helps with dynamic content and advanced user interface controls developed with Ajax, HTML, JavaScript, and related technologies. """

    }
}

css = {

    1: {
        "Q": '\n\n1. What is CSS?',
        "A": """

Cascading Style Sheets; styling language for web design that is maintained by the World Wide Web Consortium """

    },

    2: {
        "Q": '\n\n2. What are some limitations of CSS?',
        "A": """

Cannot ascend by selectors, limits in vertical control, no expressions, no column declarations, cannot target specific text """

    },

    3: {
        "Q": '\n\n3. What are some benefits of CSS?',
        "A": """

- Efficient for bandwidth
- Site-wide consistency
- Page reformatting
- Accessibility
- Content separation from presentation  """

    },

    4: {
        "Q": '\n\n4. What is a CSS property?',
        "A": """

A style that changes an aspect of an element; i.e. font, dimension """

    },

    5: {
        "Q": '\n\n5. What is a CSS selector?',
        "A": """

String equivalent of HTML elements so that the HTML element can be linked to a specific style sheet, specific selectors take precedence over more general selectors """

    },

    6: {
        "Q": '\n\n6. What are the types of CSS selectors?',
        "A": """

- Universal: Associated with all elements in a document, *
- Class: Associated with the class attribute of an element, can be used for many elements; i.e. .pagination
- ID: Associated with a specific id of an element; can only be used once; i.e. #p2
- Ruleset: Selectors can be grouped to other selected to be identified by a ruleset
- Combinator: Explains the relationship between successive selectors:
    - descendent (‘ ‘): an element within another element
    - child(‘>’): elements that are children of another element
    - adjacent sibling(‘+’): elements place immediately after another element
    - general sibling(‘~’): all elements that are siblings of another element """

    },

    7: {
        "Q": '\n\n7. What are some CSS font properties?',
        "A": """

Font Properties - font-style, font-variant, font-weight, font-size, font-family, caption, icon """

    },

    8: {
        "Q": '\n\n8. What are some CSS dimension properties?',
        "A": """

height, max-height, max-width, min-height, min-width, width """

    },

    9: {
        "Q": '\n\n9. What are CSS media types/queries?',
        "A": """

The design and customization of documents rendered by different types of media displays so corresponding styles can be applied to the content; Types: aural, print, projection, handheld, screen """

    },

    10: {
        "Q": '\n\n10. What is the CSS Box Model?',
        "A": """

From outer to inner: margin (space added around the border), border, padding (space added around content), content """

    }
}

javascript = {

    1: {
        "Q": '\n\n1. What is JavaScript?',
        "A": """

Client-side, scripting language for web-pages, run by the browser; Powerful, high-level, lightweight, dynamically typed, interpreted language with first-class functions """

    },

    2: {
        "Q": '\n\n2. What are the advantages of JavaScript?',
        "A": """

Less server interaction, immediate feedback to visitors, increased interactivity, richer interfaces """

    },

    3: {
        "Q": '\n\n3. What is functional programming?',
        "A": """

Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data """

    },

    4: {
        "Q": '\n\n4. What data types does JavaScript support?',
        "A": """

Supports undefined, null, boolean, string, symbol, number, object
- Primitive (Still objects, but passed by value): Boolean, Null, Undefined, Number, String, Symbol
- Object (Passed by reference): Object, Array, Function, RegExp, Math, Set, etc. """

    },

    5: {
        "Q": '\n\n5. Why is it bad practice to operate on decimals in JavaScript?',
        "A": """

Numbers are treated with floating point precision so operations on decimals may not yield expected results """

    },

    6: {
        "Q": '\n\n6. What are some array methods used in JavaScript?',
        "A": """

List object type created using [] or new Array()
- .push(): Appends elements to end of array
- .pop(): Removes element from end of an array
- .unshift(): Adds elements to the front of an array
- .shift(): Removes element from front of an array
- .splice(): Insertion and removal between two indices of an array
- .slice(): Removes items from the array and returns those removed items as a new array """

    },

    7: {
        "Q": '\n\n7. What is modularity in JavaScript?',
        "A": """

JavaScript code should be separated into independent modules
- Achieved using import and exports to split code into multiple files """

    },

    8: {
        "Q": '\n\n8. What is an anonymous function in JavaScript?',
        "A": """

Function declared without a named identifier, becomes inaccessible after its declaration """

    },

    9: {
        "Q": '\n\n9. What is an arrow function in JavaScript?',
        "A": """

Anonymous functions that offer a short and concise way to write function expressions; cannot be used for constructors; does not support super, this, or new """

    },

    10: {
        "Q": '\n\n10. Difference between window and document in JavaScript?',
        "A": """

Window: Global object that holds variables, functions, history, and location; root of the document object model
Document: Main object of rendered document object model; property of the window """

    },

    11: {
        "Q": '\n\n11. What is negative infinity in JavaScript?',
        "A": """

Number in JavaScript derived by dividing a negative number by zero that is lower than any other number """

    },

    12: {
        "Q": '\n\n12. What is a callback?',
        "A": """

JavaScript function passed to a method as an argument or option, that is to be executed after another function has finished executing """

    },

    13: {
        "Q": '\n\n13. What are timers used for in JavaScript?',
        "A": """

Used to execute a piece of code as a set time or repeat the code in a given interval of time, using setTimeout, setInterval, clearInterval. """

    },

    14: {
        "Q": '\n\n14. What is a closure in JavaScript?',
        "A": """

Created whenever a variable defined outside the current scope is accessed from within some inner scope, giving you access to an outer function’s scope from an inner function. It is the combination of a function bundled together with references to its surrounding state. i.e. a function factory """

    },

    15: {
        "Q": '\n\n15. What is event bubbling in JavaScript?',
        "A": """

Event propagation in the HTML DOM, so that when an event occurs inside a nested element and both layers have registered a handle for that event, the event is first captured and handled by the innermost element and the propagated to outer elements """

    },

    16: {
        "Q": '\n\n16. What is a promise?',
        "A": """

Object which is used to produce either a resolved value or an exception at some point in the future, can be one of three states: fulfilled, rejected, or pending. Callbacks can be attached to handle the rejection or fulfillment. """

    },

    17: {
        "Q": '\n\n17. Difference between local storage and session storage?',
        "A": """

- Local Storage: Data not set back to the server, reduces the amount of traffic between client and server, i.e. cookies
- Session Storage: Data stored in the session which gets cleared when the page session ends """

    },

    18: {
        "Q": '\n\n18. What are the different types of errors in JavaScript?',
        "A": """

- (Syntax) Load Time Errors: Errors which come up when loading a web-page like improper syntax
- Run Time Errors: Errors that come due to misuse of commands inside the HTML language, calling method that doesn’t exist, etc.
- Logical Errors: Errors that occur due to bad logic performed """

    },

    19: {
        "Q": '\n\n19. What are the different types of declarations in JavaScript?',
        "A": """

- Const: Block scoped, cannot be updated or re-declared, hoisted declarations without initialization
- Let: Block scoped, hoisted declaration without an initialization, can be updated, but not re-declared
- Var: Globally scoped, hoisted declaration and initialized to undefined, and allows re-declaration and updating """

    },

    20: {
        "Q": '\n\n20. What does ‘Use Strict’ do in JavaScript?',
        "A": """

Uses strict mode for error-checking: checks for implicitly declared variables, assigning values to read-only properties, adding properties to non-extensible objects """

    },

    21: {
        "Q": '\n\n21. List ways of accessing HTML elements using JavaScript code?',
        "A": """

- getElementById(‘idname’)
- getElementsByClass(‘classname’)
- getElementsByTagName(‘tagname’)
- querySelector() """

    },

    22: {
        "Q": '\n\n22. What’s the difference between innerHTML and innerText?',
        "A": """

Using innerHTML will process the tag and innerText will not process the tag, just the text between the tags. """

    },

    23: {
        "Q": '\n\n23. What’s the downside of using InnerHTML?',
        "A": """

InnerHTML replaces content everywhere, re-parsing and building the elements, making it very slow; does not provide validation """

    },

    24: {
        "Q": '\n\n24. Promises vs Callbacks?',
        "A": """

Promises are a cleaner way for running asynchronous tasks to look more like synchronous and also provide a catching mechanism which are not in callbacks. Promises are built over callbacks. Promises are a very mighty abstraction, allow cleaner and better, functional code with less error-prone boilerplate. """

    },

    25: {
        "Q": '\n\n25. Difference between == vs ===?',
        "A": """

‘===’, or strict equality operator, compares types in addition to ‘==’, equality operator, comparing value """

    },

    26: {
        "Q": '\n\n26. Null vs Undefined vs Undeclared vs NaN:',
        "A": """

- Undefined is a type that means that a variable has been declared but not yet assigned a value.
- Null is an assignment value, in the form of an object, that represents no value.
- Undeclared variables do not exist in a program
- NaN, or ‘Not a Number’, is an object that always compares unequal to any number. """

    },

    27: {
        "Q": '\n\n27. Window.onload vs onDocumentReady:',
        "A": """

- Onload does not run until all the information on the page is loaded, leading to a delay before code is executed
- onDocumentReady loads just after the DOM is loaded, allowing for quicker manipulation of the code """

    },

    28: {
        "Q": '\n\n28. .call() vs .apply():',
        "A": """

- .call() is used when the number of a function’s arguments are known:
    -method.call(function, 1, 2, 3)

- .apply() is used when the number is unknown, expecting an array as the second argument
    - method.apply(function, [1, 2, 3]) """

    },

    29: {
        "Q": '\n\n29. What is linting?',
        "A": """

Linting is the process of running a program that analyzes code for potential errors. """

    },

    30: {
        "Q": '\n\n30. What is Gulp for?',
        "A": """

Toolkit for automating time-consuming tasks in the development workflow. It reads files as streams and pipes the streams to different tasks. """

    },

    31: {
        "Q": '\n\n31. What is Babel for?',
        "A": """

Babel is a transcompiler or transpiler that can transform JavaScript into older versions/standards and can transform JSX code into JavaScript as well. """

    },

    32: {
        "Q": '\n\n32. What are truthy and falsy?',
        "A": """

Each object in JS has an inherent boolean value that allows for loose comparisons. False, 0, undefined, empty string, null, NaN are all falsy and everything else is truthy. This allows for an if statement checking if an object is null, etc. """

    },

    33: {
        "Q": '\n\n33. What does the this keyword refer to in JS?',
        "A": """

It depends on how it is used. In a method, this refers to the owner object. Alone, this refers to the global object. In a function, this refers to the global object. In a function, in strict mode, this is undefined. In an event, this refers to the element that received the event. """

    },

    34: {
        "Q": '\n\n34. What is async and await keywords?',
        "A": """

An ‘async’ keyword is a declaration defining an asynchronous function and returns an ‘AsyncFunction’ object. Await is a keyword used within an asynchronous function that waits for a promise to settle (resolved or rejected). """

    }
}

nodejs = {

    1: {
        "Q": '\n\n1. What is Node.js?',
        "A": """

A powerful, single-threaded, open source server environment framework written in C, C++, and JavaScript """

    },

    2: {
        "Q": '\n\n2. How does Node.js work?',
        "A": """

Node JS is a run-time environment that includes everything, including the virtual machine, needed to execute a JavaScript program. It works on a single-threaded event loop and non-blocking I/O to handle a large number of concurrent requests. """

    },

    3: {
        "Q": '\n\n3. What are the benefits of using Node.js?',
        "A": """

- Speed due to being built on Google’s V8 JavaScript Engine
- Asynchronous: Never waits for an API to return data
- Non-blocking: I/O operations immediately respond with whatever data is available, in case an answer isn’t retrieved, the API returns an error immediately
- Scalable: Largely due to its asynchronous, non-blocking operations """

    },

    4: {
        "Q":'\n\n4. What is a JavaScript engine?',
        "A": """

A program that converts code written in JS to computer code the CPU understands """

    },

    5: {
        "Q": '\n\n5. What is ECMAScript?',
        "A": """

The standard on which JavaScript abides by """

    },

    6: {
        "Q": '\n\n6. What is NPM?',
        "A": """

Node Package Manager, used for installing/updating packages of JavaScript """

    },

    7: {
        "Q": '\n\n7. What is event-driven programming?',
        "A": """

Programming approach that heavily makes use of events (mouse clicks, key press, hover, etc.) for triggering various functions. When an event occurs, a registered call-back function is executed """

    },

    8: {
        "Q": '\n\n8. How does the event loop work?',
        "A": """

JavaScript is single-threaded, non-blocking, and asynchronous because of the event loop. The event loop constantly checks the call stack to see if there’s any function that needs to run. If the call stack is empty, the message queue, where user-initiated events are queued, is polled to check for new events. When a new event occurs, the callback is added to the call stack and the process repeats. """

    },

    9: {
        "Q": '\n\n9. What is REPL?',
        "A": """

Read, Eval, Print, Loop. It represents a computer environment (shell, bash, powershell, etc.) where any command can be entered and the system can respond with an output. Node.js comes bundled with a REPL environment """

    },

    10:{
        "Q": '\n\n10. What is callback hell?',
        "A": """

Pattern caused by intensively nested callbacks which are not human readable and unwieldy. """

    },

    11: {
        "Q": '\n\n11. What is Express in Node?',
        "A": """

Flexible Node.js framework that provides features for web development in Node including handling web requests and routing based on URI and request methods.  """

    },

    12: {
        "Q": '\n\n12. What’s the importance of Package.json?',
        "A": """

JSON file present in the root directory of any Node application used to define the properties of the package, including name, version, dependencies, keywords, etc. """

    }
}

reactjs = {

    1: {
        "Q": '\n\n1. What is React?',
        "A": """

Open source, front end JS library developed by Facebookfor building complex, interactive UI’s that follows a component-based approach to build reusable UI components.  """

    },

    2: {
        "Q": '\n\n2. What are some features of React?',
        "A": """

Virtual DOM, server-side rendering, uni-directional data flow """

    },

    3: {
        "Q": '\n\n3. What is the virtual DOM?',
        "A": """

Programming concept where a virtual representation of an UI is kept in memory and synced with the real DOM by the ReactDOM through reconciliation. In React, it’s a lightweight JS object which starts as a copy of the real DOM as a node tree of React components, this tree is updated in response to state changes. """

    },

    4: {
        "Q": '\n\n4. How does the virtual DOM work?',
        "A": """

1. When underlying state/data changes, the entire UI is re-rendered in the Virtual DOM
2. The differences between the previous DOM and new DOM is calculated
3. The real DOM is then updated with the differences """

    },

    5: {
        "Q": '\n\n5. What are the benefits of the virtual DOM vs the physical/real DOM?',
        "A": """

- Faster updating
- Doesn’t create a new DOM on updates
- DOM manipulation is very easy, no memory wastage """

    },

    6: {
        "Q": '\n\n6. What is JSX?',
        "A": """

JavaScript XML. Dialect of JavaScript that embeds raw HTML templates inside JavaScript code. Cannot be read by the browser, must be transpiled into traditional JavaScript using additional tools like Babel and webpack """

    },

    7: {
        "Q": '\n\n7. What are the benefits of JSX?',
        "A": """

Highly declarative and reduces code complexity """

    },

    8: {
        "Q": '\n\n8. What is a component in React?',
        "A": """

A JS class or function that accepts inputs and returns a React element that describes how a section of the UI should appear """

    },

    9: {
        "Q": '\n\n9. What is the lifecycle of a component in React?',
        "A": """

1. Initialization(Mounting)
2. State/Property Updates
3. Destructions(Unmounting) """

    },

    10: {
        "Q": '\n\n10. What are component lifecycle methods in React?',
        "A": """

- render()
- componentDidMount()
- componentDidUpdate()
- componentWillUnmount() """

    },

    11: {
        "Q": '\n\n11. Why are keys important when it comes to React lists?',
        "A": """

Keys help React identify which items in a list have changed, been added, or been removed. Keys should be unique to each list element in order to give it a stable identity. Indexes should be used as a last resort as they are not stable and may change if the order of the items change. """

    },

    12: {
        "Q": '\n\n12. Stateless vs stateful vs higher order components',
        "A": """

- Stateless Components: Pure functions that render DOM based solely on the properties provided for them
- Stateful Components: Stores information about component’s state change in memory in order to render DOM based on the state
- Higher Order Components: A custom stateless component that takes a component and returns a new wrapped component. They do not modify or copy behavior from their input components """

    },

    13: {
        "Q": '\n\n13. What is a controlled component in React?',
        "A": """

A controlled component is an input form element whose value is controlled by React to ensure a single source of truth. For example for a textbox, a handleChange function is used to set the state of the component whenever the textbox changes to keep the state updated with what is being rendered. """

    },

    14: {
        "Q": '\n\n14. What is lifting state up in React?',
        "A": """

Lifting state up is the idea of sharing state between components by moving it up to the closest common ancestor of the components that need it so it can be passed down to the descendants that need the shared state. """

    },

    15: {
        "Q": '\n\n15. Composition vs Inheritance in React',
        "A": """

Two fundamental ways of relating classes. Composition is a has a relationship and inheritance is an is a relationship. """

    },

    16: {
        "Q": '\n\n16. What is FLUX?',
        "A": """

Architectural pattern that enforces unidirectional data flow, to control derived data so that multiple components can interact with it without risking pollution.
Follows: Action -> Dispatcher -> Store -> View

- The Store is the central authority for all data, any mutations to the data must occur in the store, which is then broadcast to subscribing Views through events. The views then update themselves based on the new state of received data. To request changes to Store data, an Action must be fired from the View to the Dispatcher, a singleton manager, who controls broadcasting the registered callbacks of the actions and invokes them in order to tell its subscribed stores to update their data """

    },

    17: {
        "Q": '\n\n17. Advantages of FLUX over MVC?',
        "A": """

- More clearly defined data flow for easier debugging
- Better data integrity since data can only be mutated in the store after passing through the action to dispatcher chain """

    },

    18: {
        "Q": '\n\n18. What is the importance of the render() method in React?',
        "A": """

Each React Component must have a render() method that returns a single React element that represents a DOM component. """

    },

    19: {
        "Q": '\n\n19. What are props in React?',
        "A": """

Shorthand for Properties in React; Read only components that must be immutable passed from parent to children components throughout the app. Children components can never send a prop back to the parent. Used to maintain unidirectional data flow. """

    },

    20: {
        "Q": '\n\n20. What are states in React?',
        "A": """

Sources of data that determine components rendering and behavior; they are mutable and help create dynamic and interactive components """

    },

    21: {
        "Q": '\n\n21. What are refs in React?',
        "A": """

Short for references, an attribute which helps store a reference to a particular React element or component to directly access the DOM or React element. They are used in cases where we want to change the value of a child component without using props """

    },

    22: {
        "Q": '\n\n22. What is the purpose of using super() with props?',
        "A": """

Allows child class constructor to make use of this.props binding of parent constructor.  """

    }
}

maven = {

    1: {
        "Q": '\n\n1. What is Maven?',
        "A": """

Maven is a project management and comprehension tool. Maven provides developers a complete build lifecycle framework """

    },

    2: {
        "Q": '\n\n2. JAR vs WAR vs EAR',
        "A": """

- Java Application Archive (JAR): Only requires a valid JRE
- Web Application Archive (WAR): Requires fully JEE web profile compliant server
- Enterprise Application Archive (EAR): Requires fully JEE compliant server  """

    },

    3: {
        "Q": '\n\n3. What is a POM file?',
        "A": """

POM stands for Project Object Model. It is a fundamental Unit of Work in Maven. It is an XML file. It always resides in the base directory of the project as pom.xml. It contains information about the project and various configuration details used by Maven to build the project(s). """

    },

    4: {
        "Q": '\n\n4. What is a Maven artifact?',
        "A": """

An artifact is a file, usually a JAR that gets deployed to a Maven repository. A Maven build produces one or more artifacts, such as a compiled JAR and a "sources" JAR. """

    },

    5: {
        "Q": '\n\n5. What are the phases of a Maven Build lifecycle',
        "A": """

- validate − validate the project is correct and all necessary information is available.
- compile − compile the source code of the project.
- test − test the compiled source code using a suitable unit testing framework. These tests should not require the code be packaged or deployed
- package − take the compiled code and package it in its distributable format, such as a JAR.
- integration-test − process and deploy the package if necessary into an environment where integration tests can be run.
- verify − run any checks to verify the package is valid and meets quality criteria.
- install − install the package into the local repository, for use as a dependency in other projects locally.
- deploy − done in an integration or release environment, copies the final package to the remote repository for sharing with other developers and projects. """

    },

    6: {
        "Q": '\n\n6. What is a Maven repository?',
        "A": """

A repository is a place i.e. directory where all the project jars, library jar, plugins or any other project specific artifacts are stored and can be used by Maven easily. Three types: local, central, remote. """

    },

    7: {
        "Q": '\n\n7. What is a Maven plugin?',
        "A": """

Plugins are what Maven is built on. Plugins are used to: create jar files, create war files, compile code, unit test code, create project documentation, and on and on. """

    },

    8: {
        "Q": '\n\n8. What are different dependency scopes in Maven?',
        "A": """

- compile − This scope indicates that dependency is available in the classpath of a project. It is default scope.
- provided − This scope indicates that dependency is to be provided by JDK or web-Server/Container at runtime.
- runtime − This scope indicates that dependency is not required for compilation, but is required during execution.
- test − This scope indicates that the dependency is only available for the test compilation and execution phases.
- system − This scope indicates that you have to provide the system path.
- import − This scope is only used when dependency is of type pom. This scope indicates that the specified POM should be replaced with the dependencies in that POM's <dependencyManagement> section. """

    }
}

linux = {

    1: {
        "Q": '\n\n1. What are the types of virtualization?',
        "A": """

- Full virtualization: Simulates hardware to allow an unmodified guest OS to be run in isolation
- Para virtualization: Does not simulate the hardware for the virtual machines and the guest OS is aware that it is a guest in the environment
- Hybrid virtualization """

    },

    2: {
        "Q": '\n\n2. What is Linux?',
        "A": """

Linux is an operating system based on UNIX. """

    },

    3: {
        "Q": '\n\n3. What is BASH?',
        "A": """

BASH is short for Bourne Again SHell. It was written by Steve Bourne as a replacement to the original Bourne Shell (represented by /bin/sh). It combines all the features from the original version of Bourne Shell, plus additional functions to make it easier and more convenient to use. It has since been adapted as the default shell for most systems running Linux. """

    },

    4: {
        "Q": '\n\n4. What is Linux Kernel?',
        "A": """

The Linux Kernel is a low-level systems software whose main role is to manage hardware resources for the user. It is also used to provide an interface for user-level interaction. """

    },

    5: {
        "Q": '\n\n6. What is LILO?',
        "A": """

Linux Loader (LILO) is a boot loader for Linux. It is used mainly to load the Linux operating system into main memory so that it can begin its operations. """

    },

    6: {
        "Q": '\n\n6. What is a swap space?',
        "A": """

Swap space is a certain amount of space used by Linux to temporarily hold some programs that are running concurrently. This happens when RAM does not have enough memory to hold all programs that are executing. """

    },

    7: {
        "Q": '\n\n7. What is the advantage of open source?',
        "A": """

Open source allows you to distribute your software, including source codes freely to anyone who is interested. People would then be able to add features and even debug and correct errors that are in the source code. They can even make it run better and then redistribute these enhanced source code freely again. This eventually benefits everyone in the community. """

    },

    8: {
        "Q": '\n\n8. What are the basic components of Linux?',
        "A": """

Just like any other typical operating system, Linux has all of these components: kernel, shells and GUIs, system utilities, and an application program. What makes Linux advantageous over other operating systems is that every aspect comes with additional features and all codes for these are downloadable for free. """

    },

    9: {
        "Q": '\n\n9. What is the root account?',
        "A": """

The root account is like a systems administrator account and allows you full control of the system. Here you can create and maintain user accounts, assigning different permissions for each account. It is the default account every time you install Linux. """

    },

    10: {
        "Q": '\n\n10. What is CLI?',
        "A": """

CLI is short for Command Line Interface. This interface allows the user to type declarative commands to instruct the computer to perform operations. CLI offers greater flexibility. However, other users who are already accustomed to using GUI find it difficult to remember commands including attributes that come with it. """

    },

    11: {
        "Q": '\n\n11. What is GUI?',
        "A": """

GUI, or Graphical User Interface, make use of images and icons that users click and manipulate as a way of communicating with the computer. Instead of having to remember and type commands, the use of graphical elements makes it easier to interact with the system, as well as adding more attraction through images, icons, and colors. """

    },

    12: {
        "Q": '\n\n12. How can you find out how much memory Linux is using?',
        "A": """

From a command shell, use the "concatenate" command: cat /proc/meminfo for memory usage information. You should see a line starting something like Mem: 64655360, etc. This is the total memory Linux thinks it has available to use. You can also use commands free - m, vmstat, top, or htop to find current memory usage """

    },

    13: {
        "Q": '\n\n13. What is a typical size for a swap partition under a Linux system?',
        "A": """

The preferred size for a swap partition is twice the amount of physical memory available on the system. If this is not possible, then the minimum size should be the same as the amount of memory installed. """

    },

    14: {
        "Q": '\n\n14. What are symbolic links?',
        "A": """

Symbolic links act similarly to shortcuts in Windows. Such links point to programs, files or directories. It also allows you instant access to it without having to go directly to the entire pathname. """

    },

    15: {
        "Q": '\n\n15. How do you change permissions under Linux?',
        "A": """

Assuming you are the system administrator or the owner of a file or directory, you can grant permission using the chmod command. Use + symbol to add permission or – symbol to deny permission, along with any of the following letters: u (user), g (group), o (others), a (all), r (read), w (write) and x (execute). For example, the command chmod go+rw FILE1.TXT grants read and write access to the file FILE1.TXT, which is assigned to groups and others. """

    },

    16: {
        "Q": '\n\n16. What are hard links?',
        "A": """

Hard links point directly to the physical file on disk, and not on the pathname. This means that if you rename or move the original file, the link will not break since the link is for the file itself, not the path where the file is located. """

    },

    17: {
        "Q": '\n\n17. What is the maximum length for a filename under Linux?',
        "A": """

Any filename can have a maximum of 255 characters. This limit does not include the path name, so therefore the entire pathname and filename could well exceed 255 characters. """

    },

    18: {
        "Q": '\n\n18. What are filenames that are preceded by a dot?',
        "A": """

In general, filenames that are preceded by a dot are hidden files. These files can be configuration files that hold important data or setup info. Setting these files as hidden makes it less likely to be accidentally deleted. """

    },

    19: {
        "Q": '\n\n19. What does a nameless (empty) directory represent?',
        "A": """

This empty directory name serves as the nameless base of the Linux file system. This serves as an attachment for all other directories, files, drives, and devices. """

    },

    20: {
        "Q": '\n\n20. What is the pwd command?',
        "A": """

The pwd command is short for print working directory command. """

    },

    21: {
        "Q": '\n\n21. What are daemons?',
        "A": """

Daemons are services that provide several functions that may not be available under the base operating system. Its main task is to listen for service requests and at the same time to act on these requests. After the service is done, it is then disconnected and waits for further requests. """

    },

    22: {
        "Q": '\n\n22. What are the kinds of permissions under Linux?',
        "A": """

There are 3 kinds of permissions under Linux:- Read: users may read the files or list the directory- Write: users may write to the file of new files to the directory- Execute: users may run the file or lookup a specific file within a directory """

    },

    23: {
        "Q": '\n\n23. What are environmental variables?',
        "A": """

Environmental variables are global settings that control the shell's function as well as that of other Linux programs. Another common term for environmental variables is global shell variables. """

    },

    24: {
        "Q": '\n\n24. What is redirection?',
        "A": """

Redirection is the process of directing data from one output to another. It can also be used to direct an output as an input to another process. """

    },

    25: {
        "Q": '\n\n25. What is grep command?',
        "A": """

grep a search command that makes use of pattern-based searching. It makes use of options and parameters that are specified along with the command line and applies this pattern in searching the required file output. """

    },

    26: {
        "Q": '\n\n26. What are the contents of /usr/local?',
        "A": """

It contains locally installed files. This directory matters in environments where files are stored on the network. Specifically, locally-installed files go to /usr/local/bin, /usr/local/lib, etc.). Another application of this directory is that it is used for software packages installed from source, or software not officially shipped with the distribution. """

    },

    27: {
        "Q": '\n\n27. How do you terminate an ongoing process?',
        "A": """

Every process in the system is identified by a unique process id or pid. Use the kill command followed by the pid to terminate that process. To terminate all process at once, use kill 0. """

    },

    28: {
        "Q": '\n\n28. What is command grouping and how does it work?',
        "A": """

You can use parentheses to group commands. For example, if you want to send the current date and time along with the contents of a file named OUTPUT to a second file named MYDATES, you can apply command grouping as follows: (date cat OUTPUT) > MYDATES """

    },

    29: {
        "Q": '\n\n29. How do you execute more than one command or program from a single command line entry?',
        "A": """

You can combine several commands by separating each command or program using a semicolon symbol """

    },

    30: {
        "Q": '\n\n30. What is the command to calculate the size of a folder?',
        "A": """

To calculate the size of a folder uses the command: du –sh folder1. """

    },

    31: {
        "Q": '\n\n31. How can you find the status of a process?',
        "A": """

Use the command: ps ux """

    },

    32: {
        "Q": '\n\n32. How can you check the memory status?',
        "A": """

You can use the command
free -m to display output in MB
free -g to display output in GB   """

    },

    33: {
        "Q": '\n\n33. How can you append one file to another in Linux?',
        "A": """

To append one file to another in Linux you can use command cat file2 >> file 1. The operator >> appends the output of the named file or creates the file if it is not created """

    },

    34: {
        "Q": '\n\n34. Explain how you can find a file using Terminal?',
        "A": """

To find a file you have to use a command: find . –name "process.txt" .  """

    },

    35: {
        "Q": '\n\n35. Explain how you can create a folder using Terminal?',
        "A": """

To create a folder, you have to use command: mkdir """

    },

    36: {
        "Q": '\n\n36. How can you run a Linux program in the background simultaneously when you start your Linux Server?',
        "A": """

By using nohup. It will stop the process receiving the NOHUP signal and thus terminating it you log out of the program which was invoked with. & runs the process in the background. """

    },

    37: {
        "Q": '\n\n37. Explain how to uninstall the libraries in Linux?',
        "A": """

To uninstall the libraries in Linux, you can use command sudo apt-get remove library_name """

    },

    38: {
        "Q": '\n\n38. Favorite Linux Commands/Aliases?',
        "A": """

- Alias tcn=’mv --force -t ~/.local/share/Trash’ moves a file to the Trash. Helps avoid usage of rm command which may remove file permanently.
- Alias gh=’history | grep’ searches previously used commands for certain keyword """

    }
}

aws = {

    1: {
        "Q": '\n\n1. What is AWS?',
        "A": """

AWS stands for Amazon Web Service; it is a collection of remote computing services also known as a cloud computing platform.  """

    },

    2: {
        "Q": '\n\n2. What’s the difference between SNS and SQS?',
        "A": """

- SNS is a distributed publish-subscribe system. Messages are pushed to subscribers as and when they are sent by publishers to SNS.
- SQS is distributed queuing system. Messages are NOT pushed to receivers. Receivers have to poll or pull messages from SQS. Messages can't be received by multiple receivers at the same time. Any one receiver can receive a message, process and delete it. Other receivers do not receive the same message later.  """

    },

    3: {
        "Q": '\n\n3. What are some of the DB engines which can be used in AWS RDS?',
        "A": """

MS-SQL DB, MariaDB, MySQL DB, Aurora, OracleDB, PostgreDB """

    },

    4: {
        "Q": '\n\n4. What are the differences between IAM users, roles, and groups?',
        "A": """

Users are IAM entities that must be assigned an access and secret key in order to access AWS services depending on policies assigned to the user. Roles are used to avoid storing credentials, that are used by users, by assigning a role to an entity such as an EC2 instance so that it can access other services. Groups are a set of policies that can be assigned to any user that is a member of a group. """

    },

    5: {
        "Q": '\n\n5. What are regions and availability zones?',
        "A": """

Regions and AZ’s are how AWS categorizes it’s worldwide locations. Each region is completely independent of the other and each availability zone is isolated as well. But all the availability zones in a particular region are interconnected through multiple low latency links. """

    },

    6: {
        "Q": '\n\n6. What is Amazon EC2 Root Device Volume?',
        "A": """

The root device volume has the image that was used to boot up an EC2 instance. There are two types of AMIs or Amazon Machine Images that are available:

    1. EBS based storage, and
    2. Instance store-backed AMI """

    },

    7: {
        "Q": '\n\n7. What is a security group?',
        "A": """

Security groups in Amazon EC2 are one of the ways through which the security of the cloud network is protected. They act as a firewall and are used for controlling both the inbound as well as outbound traffic at the level of the instance. """

    },

    8: {
        "Q": '\n\n8. How is the buffer used in Amazon web services?',
        "A": """

The buffer is used to make the system more robust to manage traffic or load by synchronizing different components.  Usually, components receive and process the requests in an unbalanced way. With the help of buffer, the components will be balanced and will work at the same speed to provide faster services. """

    },

    9: {
        "Q": '\n\n9. What is S3?',
        "A": """

S3 stands for Simple Storage Service. You can use S3 interface to store and retrieve any amount of data, at any time and from anywhere on the web.  For S3, the payment model is “pay as you go.” """

    },

    10: {
        "Q": '\n\n10. What’s the difference between S3 and EBS?',
        "A": """

- S3 is an object store that can store files and "folders" but can't have locks, permissions etc like you would with a traditional file system. S3 is slower in reading and writing than EBS volumes.
- EBS is a block storage system where each block is like a hard drive that is attached to EC2 instances and can only be used with one EC2 instance at a time. """

    },

    11: {
        "Q": '\n\n11. What is VPC?',
        "A": """

VPC stands for Virtual Private Cloud. It allows you to customize your networking configuration. It is a network which is logically isolated from another network in the cloud. It allows you to have your IP address range,  internet gateways, subnet and security groups. """

    },

    12: {
        "Q": '\n\n12. What is a subnet?',
        "A": """

A large section of IP Address divided into chunks is known as subnets. """

    },

    13: {
        "Q": '\n\n13. What are the different types of cloud services generally?',
        "A": """

- Software as a Service (SaaS),
- Data as a Service (DaaS)
- Platform as a Service (PaaS)
- Infrastructure as a Service (IaaS). """

    },

    14: {
        "Q": '\n\n14. What is an AMI?',
        "A": """

AMI stands for Amazon Machine Image.  It’s a template that provides the information (an operating system, an application server, and applications) required to launch an instance, which is a copy of the AMI running as a virtual server in the cloud.  You can launch instances from as many different AMIs as you need. """

    },

    15: {
        "Q": '\n\n15. What are key-pairs in AWS?',
        "A": """

Key-pairs are secure login information for your virtual machines. To connect to the instances, you can use key-pairs which contain a public-key and private-key. """

    },

    16: {
        "Q": '\n\n16. What are the different types of instances?',
        "A": """

- General purpose
- Computer Optimized
- Memory Optimized
- Storage Optimized
- Accelerated Computing """

    },

    17: {
        "Q": '\n\n17. What’s the difference between an instance and AMI?',
        "A": """

From a single AMI, you can launch multiple types of instances.  An instance type defines the hardware of the host computer used for your instance. Each instance type provides different computer and memory capabilities.  Once you launch an instance, it looks like a traditional host, and we can interact with it as we would with any computer. """

    },

    18: {
        "Q": '\n\n18. What does an AMI include?',
        "A": """

- A template for the root volume for the instance
- Launch permissions decide which AWS accounts can avail the AMI to launch instances
- A block device mapping that determines the volumes to attach to the instance when it is launched """

    },

    19: {
        "Q": '\n\n19. How can you send a request to Amazon S3?',
        "A": """

Amazon S3 is a REST service, and you can send a request by using the REST API or the AWS SDK wrapper libraries that wrap the underlying Amazon S3 REST API. """

    },

    20: {
        "Q": '\n\n20. Can you vertically scale an Amazon instance? How?',
        "A": """

Yes, you can vertically scale on Amazon instance. For that

- Spin up a new larger instance than the one you are currently running
- Pause that instance and detach the root webs volume from the server and discard
- Then stop your live instance and detach its root volume
- Note the unique device ID and attach that root volume to your new server
- And start it again """

    },

    21: {
        "Q": '\n\n21. What are T2 instances and how are they special?',
        "A": """

T2 instances are general purpose EC2 instances designed to provide moderate baseline performance and the capability to burst to higher performance as required by the workload. """

    },

    22: {
        "Q": '\n\n22. What is the difference between a spot, reserved, and on-demand instance?',
        "A": """

- Spot Instances are spare EC2 instances that are offered at a steep discount to bidders. If the bid exceeds the spot price, the instance is launched, but is taken down once the spot price exceeds the bid with a 2 minutes notice.
- On-demand Instances offer pay as you go EC2 instances that are billed per hour from start to termination
- Reserved Instances are cheaper than On-Demand Instances but require long-term commitments of over a year. """

    },

    23: {
        "Q": '\n\n23. What is the difference between vertical and horizontal scaling?',
        "A": """

Vertical scaling is adding more power to the existing resources, horizontal scaling is adding more resources. """

    },

    24: {
        "Q": '\n\n24. What is auto-scaling and how does it work?',
        "A": """

Auto-scaling is one of the most important features that Amazon Web Service provides that gives you an allowance to configure and automatically stipulate and also twists new instances without even your intervention. """

    },

    25: {
        "Q": '\n\n25. What is Amazon Cloudwatch?',
        "A": """

Amazon CloudWatch is a management tool and is a part of the Amazon Web Services family. It is basically a monitoring service for AWS cloud resources and all applications run on the AWS platform. CloudWatch can be used to track and collect metrics, set alarms, collect and monitor log files, and also monitor resources such as EC2 instances, RDS DB instances, and DynamoDB tables. """

    },

    26: {
        "Q": '\n\n26. What’s the difference between classic and application load balancers?',
        "A": """

- Classic load balancer is a level 4 load balancer that follows HTTP, HTTPS, TCP, and SSL protocols that routes traffic to separate EC2 instances without looking into the HTTP request header.
- Application load balancer is a level 7 load balancer that follows only HTTP and HTTPS protocols and can route traffic to different ports on the same instance depending on the HTTP request header.  """

    },

    27: {
        "Q": '\n\n27. What is CloudFormation?',
        "A": """

CloudFormation is an infrastructure as a code AWS provides, that allows you to model and set up your AWS resources, such as EC2 instances and auto-scaling groups, through a JSON or YAML template.  """

    }
}

docker = {

    1: {
        "Q": '\n\n1. What is Docker?',
        "A": """

Docker is an open-source lightweight containerization technology. It allows you to automate the deployment of applications in lightweight and portable containers. """

    },

    2: {
        "Q": '\n\n2. What are the advantages of using Docker containers?',
        "A": """

- Offers an efficient and easy initial set up
- Allows you to describe your application lifecycle in detail
- Simple configuration and interacts with Docker Compose
- Documentation provides every bit of information """

    },

    3: {
        "Q": '\n\n3. What are the important features of Docker?',
        "A": """

- Easy Modeling
- Version control
- Placement/Affinity
- Application Agility
- Developer Productivity
- Operational Efficiencies """

    },

    4: {
        "Q": '\n\n4. What are the main drawbacks of Docker?',
        "A": """

- Doesn't provide a storage option
- Offers a poor monitoring option.
- No automatic rescheduling of inactive Nodes
- Complicated automatic horizontal scaling set up """

    },

    5: {
        "Q": '\n\n5. What is a Docker image?',
        "A": """

The Docker image is a template used to create Docker containers. Docker images are stored in the Docker registry. """

    },

    6: {
        "Q": '\n\n6. Docker image vs Docker container?',
        "A": """

An image is a set of layers describing how to start a docker container, a sort of snapshot of a container. When an image is run, it runs as a Docker container.  """

    },

    7: {
        "Q": '\n\n7. What is Docker Engine?',
        "A": """

Docker daemon or Docker engine represents the server. The docker daemon and the clients should be run on the same or remote host, which can communicate through command-line client binary and full RESTful API. """

    },

    8: {
        "Q": '\n\n8. What are registries?',
        "A": """

Two types: public registry, private registry. Docker's public registry is called Docker hub, which allows you to store images privately. In Docker hub, you can store millions of images. """

    },

    9: {
        "Q": '\n\n9. What command should you run to see all running containers in Docker?',
        "A": """

$ docker ps """

    },

    10: {
        "Q": '\n\n10. What is the command to stop a docker container?',
        "A": """

$ sudo docker stop container name """

    },

    11: {
        "Q": '\n\n11. What is the command to run the image as a container?',
        "A": """

$ sudo docker run -i -t alpine /bin/bash """

    },

    12: {
        "Q": '\n\n12. What is a Dockerfile?',
        "A": """

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Using docker build, users can create an automated build that executes several command-line instructions in succession. """

    },

    13: {
        "Q": '\n\n13. What is Docker compose?',
        "A": """

Docker Compose is a YAML file which contains details about the services, networks, and volumes for setting up the Docker application. So, you can use Docker Compose to create separate containers, host them and get them to communicate with each other. Each container will expose a port for communicating with other containers. """

    },

    14: {
        "Q": '\n\n14. What is the lifecycle of a Docker container?',
        "A": """

Create container, run container, pause/unpause container, start container, stop container, restart container, kill container, destroy container. """

    },

    15: {
        "Q": '\n\n15. What is a memory-swap flag?',
        "A": """

Memory-swap is a modified flag that only has meaning if- memory is also set. Swap allows the container to write express memory requirements to disk when the container has exhausted all the RAM which is available to it. """

    },

    16: {
        "Q": '\n\n16. What is Docker Swarm?',
        "A": """

Docker Swarm is native clustering for Docker. It turns a pool of Docker hosts into a single, virtual Docker host. Docker Swarm serves the standard Docker API, any tool that already communicates with a Docker daemon can use Swarm to transparently scale to multiple hosts. """

    },

    17: {
        "Q": '\n\n17. What is Docker Machine?',
        "A": """

Docker machine is a tool that lets you install Docker Engine on virtual hosts. These hosts can now be managed using the docker-machine commands. Docker machine also lets you provision Docker Swarm Clusters. """

    },

    18: {
        "Q": '\n\n18. What are the states of Docker containers?',
        "A": """

Running, Paused, Restarting, Exited """

    },

    19: {
        "Q": '\n\n19. What is Docker hub?',
        "A": """

Docker hub is a cloud-based registry which helps you to link to code repositories. It allows you to build, test, store your image in Docker cloud. You can also deploy the image to your host with the help of Docker hub. """

    },

    20: {
        "Q": '\n\n20. What is Virtualization?',
        "A": """

Virtualization is a method of logically dividing mainframes to allow multiple applications to run simultaneously. """

    },

    21: {
        "Q": '\n\n21. What is Hypervisor?',
        "A": """

The hypervisor allows you to create a virtual environment in which the guest virtual machines operate. It controls the guest systems and checks if the resources are allocated to the guests as necessary. """

    },

    22: {
        "Q": '\n\n22. What are Docker object labels?',
        "A": """

Docker object labels is a method for applying metadata to docker objects including, images, containers, volumes, network, swam nodes, and services. """

    },

    23: {
        "Q": '\n\n23. How does communication happen between Docker client and Docker Daemon?',
        "A": """

You can communicate between Docker client and Docker Daemon with the combination of Rest API, socket.IO, and TCP. """

    },

    24: {
        "Q": '\n\n24. Difference between Entrypoint and CMD in Docker?',
        "A": """

Both define what executable should be run when a container is started from your image. However, CMD can be overridden and ENTRYPOINT is always executed. """

    },

    25: {
        "Q": '\n\n25. How do you expose a port in docker?',
        "A": """

--expose -p host:container """

    }
}

devops = {

    1: {
        "Q": '\n\n1. Agile vs Waterfall SDLC:',
        "A": """

Agile, known for its flexibility, follows an incremental procedure for developing software, working in short sprints continuously developing features for a project. Waterfall is a sequential design process, following specific phases to complete a single project. Agile is better for projects with ever-changing requirements while waterfall is better for smaller projects with strict requirements.  """

    },

    2: {
        "Q": '\n\n2. What is Berkshelf?',
        "A": """

Dependency management tool for Cookbooks in Chef. The berksfile is used to download dependency cookbooks from Chef’s supermarket and upload the cookbook to the cookbook repository as well.  """

    },

    3: {
        "Q": '\n\n3. What is a Test Kitchen in Chef?',
        "A": """

Chef’s Test Kitchen is a testing tool that provides a way for you to test your cookbook recipes on a local virtual machine, setup through kitchen.yml, without having to spin up a new server.  """

    },

    4: {
        "Q": '\n\n4. What is the Test Kitchen workflow?',
        "A": """

Create -> Converge(Applying cookbook) -> Login (SSH) -> Verify -> Destroy """

    },

    5: {
        "Q": '\n\n5. What is a data bag in Chef?',
        "A": """

An arbitrary collection of data, stored in a JSON file, which one can use with cookbooks. Data bags are used to avoid hardcoding attributes such as passwords, licenses, lists of users, or groups, in recipes. They also allow Chef to share data between nodes.  """

    },

    6: {
        "Q": '\n\n6. Define the characteristics of Ansible:',
        "A": """

- Change management: define and enforce ‘System state’
- Provisioning: prepare a system to be ready
- Automation: Defines task that would be executed automatically
- Orchestration:Coordinating automation between systems. """

    }
}

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen. From http://code.activestate.com/recipes/134892/"""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            try:
                self.impl = _GetchMacCarbon()
            except(AttributeError, ImportError):
                self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:

    def __init__(self):
        import tty, sys, termios # import termios now or else you'll get the Unix version on the Mac

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        keys = {
            b'\x1b[A': 'UP',
            b'\x1b[B': 'DOWN',
            b'\x1b[C': 'RIGHT',
            b'\x1b[D': 'LEFT',
            b'\x1b'  : 'ESC'
        }

        try:

            tty.setcbreak(sys.stdin)

            i,o,e = select.select([sys.stdin],[],[],1800)

            key = i[0].buffer.read1(3)

            if key in keys.keys():
                key = keys[key]

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return key

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

class _GetchMacCarbon:
    """
    A function which returns the current ASCII key that is down;
    if no ASCII key is down, the null string is returned.  The
    page http://www.mactech.com/macintosh-c/chap02-1.html was
    very helpful in figuring out how to do this.
    """
    def __init__(self):
        import Carbon
        Carbon.Evt #see if it has this (in Unix, it doesn't)

    def __call__(self):
        import Carbon
        if Carbon.Evt.EventAvail(0x0008)[0]==0: # 0x0008 is the keyDownMask
            return ''
        else:
            #
            # The event contains the following info:
            # (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
            #
            # The message (msg) contains the ASCII char which is
            # extracted with the 0x000000FF charCodeMask; this
            # number is converted to an ASCII character with chr() and
            # returned
            #
            (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
            return chr(msg & 0x000000FF)


def clear():

    if platform.system() == 'Linux':
        os.system('clear')

    elif platform.system() == 'Windows':
        os.system('cls')

    elif platform.system() == 'Darwin':
        os.system("'clear && printf '\e[3J'")

def proctor(test):

    keyEvent = _Getch()
    question = 1

    try:
        while(True):

            clear()

            print("|> ESC: exit to menu <|> Down arrow: show answer <|> Up arrow: hide answer <|> Right arrow: next question <|> Left arrow: previous question <|")

            print(test[question]["Q"])

            key = keyEvent()

            if key == "UP":
                clear()

            elif key == "DOWN":
                print(test[question]["A"])
                key = keyEvent()
                if key == "UP":
                    continue
                else:
                    question += 1

            elif key == "RIGHT":
                question += 1

            elif key == "LEFT":
                question -= 1

            elif key == "ESC":
                break

            else:
                continue

    except Exception:
        print("*********[> ERROR <]*********")
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))


if __name__ == "__main__":

    test = {
        "1": java,
        "2": spring,
        "3": aop,
        "4": spring_security,
        "5": databases,
        "6": html,
        "7": css,
        "8": javascript,
        "9": nodejs,
        "10": reactjs,
        "11": maven,
        "12": linux,
        "13": aws,
        "14": docker,
        "15": devops
    }

    while(True):

        clear()

        for index, set in enumerate(QUESTION_SET, 1):
            print(f'{index}: {set}')

        selected = input("\n\nSelect test (q to quit): ")

        if selected == "q":
            break
        elif selected in test.keys():
            proctor(test[selected])
        else:
            print("Invalid choice")
