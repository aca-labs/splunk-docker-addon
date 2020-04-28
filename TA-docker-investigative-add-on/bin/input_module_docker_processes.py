
# encoding = utf-8

import os
import sys
import time
import datetime



'''
    IMPORTANT
    Edit only the validate_input and collect_events functions.
    Do not edit any other part in this file.
    This file is generated only once when creating the modular input.
'''

def validate_input(helper, definition):
    """Implement your own validation logic to validate the input stanza configurations"""
    # This example accesses the modular input variable
    # list_of_long_container_ids = definition.parameters.get('list_of_long_container_ids', None)
    pass
    
    
def collect_events(helper, ew):
    module_path = helper.get_arg('module_path')
    sys.path.append(module_path + '/docker-3.7.2')
    sys.path.append(module_path + '/websocket_client-0.56.0')
    sys.path.append(module_path + '/dockerpy-creds-master')
    sys.path.append(module_path + '/backports.ssl_match_hostname-3.7.0.1')
    import docker
    import json
    import re
    
    
    opt_docker_api_version = helper.get_arg('docker_api_version')
    opt_container_ids = helper.get_arg('container_ids')
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    
    client.version(opt_docker_api_version)
    
    ids = opt_container_ids.split()
    outr1 = ""
    for id in ids:
        out = str(client.top(id, 'aux')).replace("u\'","\'").replace("\'", "\"")
        out = out.split("[[")[1].split("]]")[0]
        out = "[" + out + "]"
        brackets = out.count("[")
        
        while brackets > 0:
            outro = out.split("[")[brackets].split("]")[0]
            outr1 = outr1 + "{ \"Timestamp\": " + str(datetime.datetime.now()) + "," + "\"Process information\": [" + outro + "], \"Container ID\": \"" + str(id) + "\"}\n"
            brackets = brackets - 1
        
    event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=helper.get_sourcetype(), data=outr1, done=True, unbroken=True)
    ew.write_event(event)
