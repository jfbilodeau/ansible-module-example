#!/usr/bin/env python

DOCUMENTATION = """
---
module: custom
author: J-F Bilodeau
description:
  - This is a sample module that calls the ping command
options:
  count:
    description: Number of pings to perform
    default: 1
  timeout:
    description: Seconds to wait before abandonning response
    default: 1
  host:
    description: The hostname or IP address to ping
"""


from ansible.module_utils.basic import AnsibleModule

import subprocess


def main():
    module = AnsibleModule(
        argument_spec = dict(
            count     = dict(default=1, type='int'),
            timeout   = dict(default=1, type='int'),
            host      = dict(required=True)
        )
    )

    count = module.params['count']
    timeout = module.params['timeout']
    host = module.params['host']

    print('Pinging', host)
    returncode = subprocess.call(['ping', '-c', str(count), '-W', str(timeout), host])

    success = returncode == 0

    module.exit_json(changed=False, success=success)


if __name__ == '__main__':
    main()
