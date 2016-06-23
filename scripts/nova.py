import os
import re
from keystoneclient.v2_0 import client as kc
from novaclient import client as nc
from quantumclient.v2_0 import client as qc
from glanceclient.v2 import client as gc
import requests
import subprocess

kv_pattern = re.compile(r'\s*export\s+([A-Za-z_]+)\=(.*)\s*$')


class BaremetalService(object):
    def __init__(self, keystone):
        self.keystone = keystone
        
    def list_nodes(self):
        nova_url = self.keystone.service_catalog.get_endpoints()['compute'][0]['adminURL']
        return requests.get(nova_url + '/os-baremetal-nodes', headers={ 'X-Auth-Token': self.keystone.auth_token }).json()['nodes']

class ClientFactory(object):
    def __init__(self, authinfo):
        self.authinfo = authinfo
        
    def keystone(self):
        return kc.Client(auth_url=self.authinfo['OS_AUTH_URL'], username=self.authinfo['OS_USERNAME'],
                         password=self.authinfo['OS_PASSWORD'], tenant_name=self.authinfo['OS_TENANT_NAME'])
    
    def nova(self):
        return nc.Client('2', self.authinfo['OS_USERNAME'], self.authinfo['OS_PASSWORD'], self.authinfo['OS_TENANT_NAME'],
                         auth_url=self.authinfo['OS_AUTH_URL'])
    
    def quantum(self):
        return qc.Client(auth_url=self.authinfo['OS_AUTH_URL'], username=self.authinfo['OS_USERNAME'],
                         password=self.authinfo['OS_PASSWORD'], tenant_name=self.authinfo['OS_TENANT_NAME'])
    
    def glance(self):
        keystone = self.keystone()
        return gc.Client(endpoint=keystone.service_catalog.get_endpoints()['image'][0]['publicURL'], token=keystone.auth_token)
    
    def nova_baremetal(self):
        return BaremetalService(self.keystone())

def get_client_factory(aic_auth_path):
    authinfo = {}
    with open(os.path.expanduser(aic_auth_path), 'r') as f:
        for line in f.readlines():
            m = kv_pattern.match(line)
            if m:
                authinfo[m.group(1)] = m.group(2)
    return ClientFactory(authinfo)
            
def run_client(envfile, cmd):
    env = os.environ.copy()
    with open(os.path.expanduser(envfile), 'r') as f:
        for line in f.readlines():
            m = kv_pattern.match(line)
            if m:
                env[m.group(1)] = m.group(2)
    return subprocess.check_output(cmd, env=env).split('\n')
