# SMART DEPLOYER
Smart Deployer is a tool to automatically generate the ABS deployment code based on a declarative
specification.  This tool has been integrated in the abstool tool-chain.

It is already integrated in the ABS toolchain and therefore, to install it, we invite the user
to follow the instruction presented at [https://github.com/abstools/abstools](https://github.com/abstools/abstools)

A description of the old version of the functionalies of the tool is available at
[here](http://heim.ifi.uio.no/~jacopom/publication/dblpconf__esocc__gouwmnz16/).
The description of the current version is under publication and will be available soon. For more details please
contact the author at <mauro.jacopo@gmail.com>.

## Installation usig Docker

To install Smart Deployer it is possible to use [Docker](https://www.docker.com) available for
the majority of the operating systems.

The Docker image is availabe in Docker Hub. To install it please run the
following commands.
```
sudo docker pull jacopomauro/abs_deployer
```

To interact with Smart Deployer, it is possible to run the docker container getting
a direct access to the bash. This can be done by running the following command.
```
sudo docker run --entrypoint="/bin/bash" -i --rm -t jacopomauro/abs_deployer
```
This will give access to the bash and SUNNY-CP can be invoked by running the
`python abs_deployer.py` command. A test use case is available by running

```
python abs_deployer.py test/FRHErlang.abs
```

To move the abs files within the container
the `scp` command can be used or, alternatively, it is possible also to 
start the container with some shared volume (see
[Docker documentation](https://docs.docker.com/engine/admin/volumes/volumes/)
for more information.)

## Limitations

The input file needs to be a abs program that can be parsed, following the ABS grammar.

SmartDeployCost classes (i.e., the classes that are referred using a SmartDeployCost annotation)
and all their interfaces (including the extended ones) need to be defined in the file.
These classes and interfaces need to have a simple name, i.e., the notation module_name.interface_name or 
module_name.class_name is not allowed.

SmartDeployCost classes can not have a add/remove method to add a reference to an object of interface I if they have
parameters requiring an object or a list of objects of interface I.