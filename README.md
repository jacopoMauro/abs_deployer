# abs_deployer
Tool to automatically generate the main file of an annotated ABS program

Required software:

antlr python runtime support
  install with:
  pip install antlr4-python2-runtime

  Or, you can download and untar the appropriate package from:
  https://pypi.python.org/pypi/antlr4-python2-runtime

Zephyrus: available from https://github.com/aeolus-project/zephyrus
Metis: available from https://github.com/aeolus-project/metis
MiniZinc suite 1.6: available from http://www.minizinc.org/g12distrib.html

In order to use Zephyrus the patch zephyrus.patch needs to be applied before compiling it.

Once installed to test the application please launch the following commands: 
python abs_deployer.py test/ex1.abs test/ex1_5.spec test/ex1_dc.json

To test the tool with the industrial use case provided by Fredhopper please launch the command:
python abs_deployer.py test/FRH_2Query.abs test/FRH_2Query.spec test/FRH_2Query_dc.json

