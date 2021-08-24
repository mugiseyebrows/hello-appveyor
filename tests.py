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

basename = os.path.basename(args.bin)

# https://www.appveyor.com/docs/build-worker-api/

for line in stdout.decode('utf-8').split('\n'):
    if line.startswith('PASS') or line.startswith('FAIL'):
        stat, name = line.split(":", 1)
        fail = line.startswith('FAIL')
        status = "Passed" if not fail else "Failed"
        sp.run(["appveyor", "AddTest", "-Name", name, "-Framework", "NUnit", "-Filename", args.bin, "-Outcome", status])

exit(proc.returncode)
