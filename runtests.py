import argparse
import requests
from io import BytesIO

parser = argparse.ArgumentParser()
parser.add_argument('APPVEYOR_JOB_ID')

args = parser.parse_args()

#print(args)
#print('APPVEYOR_JOB_ID', args.APPVEYOR_JOB_ID)

import subprocess
res = subprocess.Popen(['tests\\release\\tests', '-xunitxml'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = res.communicate()
fail = False
if res.returncode == 1:
    open('.fail', 'w').close()
    fail = True
"""
with open('TEST1.xml','wb') as f:
    f.write(stdout)
"""
resp = requests.post('https://ci.appveyor.com/api/testresults/junit/{}'.format(args.APPVEYOR_JOB_ID), files={'file':stdout})
print(resp)