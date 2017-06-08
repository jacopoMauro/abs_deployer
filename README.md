# abs_deployer
Tool to automatically generate the ABs deployment code base on a declarative
specification.  This tool has been integrated in the abstool tool-chain.
To install it we invite the user to follow the instruction presented at
https://github.com/abstools/abstools


Limitations
-----------

The input file needs to be a abs program that can be parsed following the ABS grammar.

All the annotaitons and the classes needs to be defined in one abs file.
SmartDeployCost classes and all the interfaces that they extend need to be defined in the same module
(module.name to define their name is allowed)

SmartDeployCost classes can not have a add/remove method to add a reference to an object of interface I if they have
arguments requiring an object or a list of objects of interface I.



