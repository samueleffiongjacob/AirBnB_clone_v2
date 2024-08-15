#!/usr/bin/env python3
from fabric.api import env, run, local, task
import os
from pathlib import Path

# Define the list of web servers
env.hosts = ['3.85.141.200', '54.236.190.52']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """
    # Number of archives to keep
    if number < 1:
        number = 1

    # Local cleanup
    local_versions_dir = "versions"
    if os.path.exists(local_versions_dir):
        archives = sorted(Path(local_versions_dir).glob('web_static_*.tgz'), key=os.path.getmtime)
        archives_to_delete = archives[:-number]

        for archive in archives_to_delete:
            print(f"Deleting local archive: {archive}")
            os.remove(archive)

    # Remote cleanup
    for server in env.hosts:
        with env.host_string(server):
            # List archives in the remote release directory
            result = run("ls -tr /data/web_static/releases/web_static_*.tgz")
            archives = result.split()
            archives_to_delete = archives[:-number]

            for archive in archives_to_delete:
                print(f"Deleting remote archive: {archive} on {server}")
                run(f"rm {archive}")

@task
def clean(number=0):
    """
    Task to call do_clean with the number of archives to keep.
    """
    do_clean(number)
