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