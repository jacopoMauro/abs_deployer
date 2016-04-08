"""
settings.py: file containing some variables used by other modules 
"""
__author__ = "Jacopo Mauro"
__copyright__ = "Copyright 2016, Jacopo Mauro"
__license__ = "ISC"
__version__ = "0.1"
__maintainer__ = "Jacopo Mauro"
__email__ = "mauro.jacopo@gmail.com"
__status__ = "Prototype"

SEPARATOR = "___"

#default scenario name
DEFAULT_SCENARIO_NAME = "Def"

# prefix for random generated DC
DC_PREFIX = "DC_"
# number of DC if not specifid in the abs program
DEFAULT_NUMBER_OF_DC = 4

# DC where the intial objects will be deployed
DEFAULT_INITIAL_DC = { "___initial_DC": {
      "num": 1,
      "resources": {
        "initial_obj_resource": 1000
      },
      "cost": 0
    }}

OBJ_PREFIX = "o"
