#!/usr/bin/python
import os
import sys

def main():
    numb = os.environ['BUILD_NUMBER']
    enumerate(numb, 1) # Start counting from 1

    if int(numb) % 3 == 0:
       print "Jenkins job name is "+os.environ['JOB_NAME']
       print "Jenkins run number is "+os.environ['BUILD_NUMBER']
    else:
       print "Jenkins job name is "+os.environ['JOB_NAME']
       print "Jenkins run number is "+os.environ['BUILD_NUMBER']
       sys.exit(1)

if __name__ == "__main__":
    main()
