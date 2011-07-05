#!/usr/bin/python

import os

# ./.obs.cnf and ~/.obs.cnf
project_conf_name = '.obs.cnf'
# /etc/obs.cnf
system_conf_name = '/etc/obsidian.cnf'


def find_conf_file():
    conf_file = find_in_parent_dir(project_conf_name)
    if(conf_file):
        return conf_file

    conf_file = os.path.expanduser(os.path.join('~', project_conf_name))
    if os.path.exists(conf_file):
        return open(conf_file, 'r')

    if os.path.exists(system_conf_name):
        return open(system_conf_name, 'r')
        
    return None

def find_in_parent_dir(fname):
    """
    Look in the current directory and then each parent
    until root.
    Inspired from 'findrepo()' in http://selenic.com/hg/file/2c9f5897d4b7/mercurial/cmdutil.py
    """
    p = os.path.abspath(os.path.curdir)
    
    while not os.path.exists(os.path.join(p, project_conf_name)):
        oldp, p = p, os.path.dirname(p)
        if p == oldp:
            return None
    
    return open(os.path.join(p, project_conf_name), 'r') 

"""
Sets the environment variables specified in the following format:
ENV_NAME1=loc1, ENV_NAME2=loc2
"""
def set_env(env_str):
    env_list = env_str.replace(" ","")
    env_list = env_list.split(",")
    for setting in env_list:
        split = setting.split("=")
        os.environ[split[0]] = split[1]

class ConfigError(Exception):
    def __init__(self, message):
        self.message = message
