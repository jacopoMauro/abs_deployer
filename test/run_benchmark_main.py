#!/usr/bin/python

import json
from subprocess import Popen,PIPE
import uuid
import math
import logging as log
import sys
import fileinput
import re
import os
import itertools

# log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)

REPETITIONS = 1
TEST_FILE = 'test_mainquery.abs'

# doing a grid search

DCs = [ "c4_2xlarge_us2",
          "c4_2xlarge_us1",
          "m4_large_us2",
          "m4_large_us1",
          "c4_xlarge_us2",
          "c4_xlarge_us1",
          "m4_xlarge_us2",
          "m4_xlarge_us1",
          "c4_2xlarge_eu",
          "c4_xlarge_eu",
          "m4_large_eu",
          "m4_xlarge_eu" ]

grid_ranges = range(2,20)

TIMEOUT = 900

# OTHER_OPT
OTHER_OPT = []
OTHER_ARGS = []

CMDS = [
          # smt
          ['time', '-p', 'timeout', str(TIMEOUT),
           'python', '../abs_deployer.py',
           '-s', 'smt'],

          # chuffed
          ['time', '-p', 'timeout', str(TIMEOUT),
          'python', '../abs_deployer.py',
          '-s', 'chuffed'],

          # gecode
          ['time', '-p', 'timeout', str(TIMEOUT),
          'python', '../abs_deployer.py',
          '-s', 'gecode'],

        ]


def changefile(param):
    f_name = '/tmp/' + uuid.uuid4().hex + '.abs'
    with open(f_name,'w') as f:
        for line in fileinput.input(TEST_FILE):
            counter = 0
            for i in DCs:
                line = re.sub(
                    '\\\\"' + i + '\\\\":[0-9]+',
                    '\\\\"' + i + '\\\\":' + unicode(param),
                    line)
                counter += 1
            f.write(line)
    return f_name



def run_cmd(cmd):
  log.info("Running command: "  + str.join(' ',cmd))
  proc = Popen( cmd, stdout=PIPE, stderr=PIPE )
  out, err = proc.communicate()
  log.debug('Stdout')
  log.debug(out)
  log.debug('Stderr')
  log.debug(err)
  returncode = proc.returncode
  log.debug('Return code = ' + str(returncode))
  
  if returncode != 0:
    return -float(returncode)
  else:
    return float(re.search('real\s*([0-9\.]+)',err).group(1))


def run(cmd):
  times = []
  errors = []
  for _ in range(REPETITIONS):
    time = run_cmd(cmd)
    if time < 0.0:
      log.debug('Timeout or error')
      errors.append(time)
      break
    else:
      times.append(time)
  
  if len(errors) > 0:
    return (0,0, -errors[0])
  else:
    return (sum(times)/REPETITIONS, (max(times)- min(times))/2, 0)


def myprint(res):
  if res[2] > 0:
    return("& error" + str(res[2]) + " & error" + str(res[2]))
  else:
    return(' & ' + str(res[0]) + ' & ' + str(res[1]))
 
def main():
  
  # print first line of the table
  print 'param &',
  for i in CMDS:
    for j in range(len(i)):
      if i[j] == '-s':
        s = i[j+1]
        break
    print '& ' + s + ' & err',
  print '\\\\'

  # start performing the grid search

  combinations = []
  #for i in itertools.product(*grid_ranges):
  for i in grid_ranges:
      combinations.append(i)
  log.debug("Combinations = " + unicode(combinations))
  for i in combinations:

    # print the parameters of wordpress tested
    print unicode(i) + ' & ',

    # create the input file for zephyrus
    f = changefile(i)
    log.debug('File ' + f + " generated for testing combination " + unicode(i))

    # run the solvers
    for j in range(len(CMDS)):
        cmd = CMDS[j] + OTHER_OPT + [ f ] + OTHER_ARGS
        res = run(cmd)
        print myprint(res),
        sys.stdout.flush()
    print '\\\\'

    # remove file
    if os.path.exists(f):
        os.remove(f)



main()   
