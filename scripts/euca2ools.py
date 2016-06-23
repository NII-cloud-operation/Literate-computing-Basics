# helper functions for Euca2ools

import subprocess
import os
import time

def run_euca2ools(envfile, cmd):
    env = os.environ.copy()
    with open(os.path.expanduser(envfile), 'r') as f:
        for l in f.readlines():
            if l.startswith('export '):
                l = l[6:].strip()
                name, value = tuple(l.split('='))
                if value.startswith('"'):
                    value = value[1:-1]
                env[name] = value
    return subprocess.check_output(cmd, env=env).split('\n')
