#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.ios import run_commands

import re

def main():
    module = AnsibleModule(dict())

    commands = [ 'show version' ]
    responses = run_commands(module, commands)
    response = responses[0]
    match = re.search('Version ([^(]+)', response)
    version = match.group(1)

    module.exit_json(changed=False, success=True, responses=responses, version=version)

if __name__ == '__main__':
    main()

