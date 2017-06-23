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

#log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)

REPETITIONS = 5
TEST_FILE = 'test_addquery.abs'

# doing a grid search
EUROPE = range(0,11)
USA = range(0,21)

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


def changefile(eu,us):
    f_name = '/tmp/' + uuid.uuid4().hex + '.abs'
    with open(f_name,'w') as f:
        for line in fileinput.input(TEST_FILE):
            line = re.sub(
                r"\(sum\s\?x\sin\s'\.\*us\.':\s\?x\.QueryServiceImpl\['live'\]\)\s=\s[0-9]+",
                "(sum ?x in '.*us.': ?x.QueryServiceImpl['live']) = " + unicode(us),
                line)
            line = re.sub(
                r"\(sum\s\?x\sin\s'\.\*eu':\s\?x\.QueryServiceImpl\['live'\]\)\s=\s[0-9]+",
                "(sum ?x in '.*eu': ?x.QueryServiceImpl['live']) = " + unicode(eu),
                line)
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
    return(",error" + str(res[2]) + ",error" + str(res[2]))
  else:
    return(',' + str(res[0]) + ',' + str(res[1]))
 
def main():
  
  # print first line of the table
  print 'eu,usa,',
  for i in CMDS:
    for j in range(len(i)):
      if i[j] == '-s':
        s = i[j+1]
        break
    print ',' + s + ',err',
  print ''

  # start performing the grid search
  for eu in EUROPE:
    for us in USA:
          
        # print the parameters of wordpress tested
        print str(eu) + ',' + str(us) + ',',

        # create the input file for zephyrus
        f = changefile(eu,us)
        log.debug('File ' + f + " generated for testing combination " + unicode((eu,us)))

        # run the solvers
        for i in range(len(CMDS)):
            cmd = CMDS[i] + OTHER_OPT + [ f ] + OTHER_ARGS
            res = run(cmd)
            print myprint(res),
            sys.stdout.flush()
        print ''

        # remove file
        if os.path.exists(f):
            os.remove(f)



main()   
