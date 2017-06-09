# abs_deployer
Tool to automatically generate the ABs deployment code base on a declarative
specification.  This tool has been integrated in the abstool tool-chain.
To install it we invite the user to follow the instruction presented at
https://github.com/abstools/abstools


Limitations
-----------

The input file needs to be a abs program that can be parsed, following the ABS grammar.

All the annotations and the classes need to be defined in one abs file.
SmartDeployCost classes (i.e., the classes that are referred using a SmartDeployCost annotation)
and all their interfaces (including the extended ones) need to be defined in the file.
These classes and interfaces need to have a simple name, i.e., the notation module_name.interface_name or 
module_name.class_name is not allowed.

SmartDeployCost classes can not have a add/remove method to add a reference to an object of interface I if they have
paramteters requiring an object or a list of objects of interface I.


