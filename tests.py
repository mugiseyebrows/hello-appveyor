import os
import sys
import subprocess as sp
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('bin')
parser.add_argument('log')

args = parser.parse_args()

proc = sp.Popen(args.bin, stdout=sp.PIPE, stderr=sp.PIPE)
stdout, stderr = proc.communicate()

with open(args.log, 'wb') as f:
    f.write(stdout)
    f.write(stderr)

#print('stdout',stdout)
#print('stderr',stderr)
#print('returncode', proc.returncode)

basename = os.path.basename(args.bin)

for line in stdout.decode('utf-8').split('\n'):
    if line.startswith('PASS') or line.startswith('FAIL'):
        stat, name = line.split(":", 1)
        fail = line.startswith('FAIL')
        status = "Passed" if not fail else "Failed"
        sp.run(["appveyor", "AddTest", "-Name", name, "-Framework", "NUnit", "-Filename", basename, "-Outcome", status, "-Duration", "0"])

exit(proc.returncode)
