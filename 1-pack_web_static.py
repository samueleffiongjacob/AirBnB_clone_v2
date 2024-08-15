#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, task

@task
def do_pack():
    """Archives the static files."""
    if not os.path.exists("versions"):
        os.makedirs("versions")

    d_time = datetime.now().strftime("%Y%m%d%H%M%S")
    output = "versions/web_static_{}.tgz".format(d_time)

    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
        return output
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
