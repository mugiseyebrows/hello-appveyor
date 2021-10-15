import argparse


parser = argparse.ArgumentParser()
parser.add_argument('job-id')

args = parser.parse_args()

print('job-id', args.job_id)

import subprocess
res = subprocess.Popen(['tests\\release\\tests', '-xunitxml'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = res.communicate()
fail = False
if res.returncode == 1:
    open('.fail', 'w').close()
with open('TEST1.xml','wb') as f:
    f.write(stdout)