#!/usr/bin/env python3
from fabric import task, Connection
from fabric import Serial
import os
from pathlib import Path

# Define the list of web servers
WEB_SERVERS = ['3.85.141.200', '54.236.190.52']

def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """
    # Convert number to integer
    try:
        number = int(number)
    except ValueError:
        number = 1  # Default to 1 if conversion fails

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
    for server in WEB_SERVERS:
        conn = Connection(host=server, connect_kwargs={"key_filename": "~/.ssh/id_rsa", "username": "ubuntu"})
        # List archives in the remote release directory
        result = conn.run("ls -tr /data/web_static/releases/web_static_*.tgz", hide=True)
        archives = result.stdout.split()
        archives_to_delete = archives[:-number]

        for archive in archives_to_delete:
            print(f"Deleting remote archive: {archive} on {server}")
            conn.run(f"rm {archive}")

@task
def clean(ctx, number=0):
    """
    Task to call do_clean with the number of archives to keep.
    """
    do_clean(number)
