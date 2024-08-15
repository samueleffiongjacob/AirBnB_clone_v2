#!/usr/bin/env python3
import os
from datetime import datetime
from fabric import task
from invoke import run

@task
def do_pack(c):
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    
    d_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_time.year,
        d_time.month,
        d_time.day,
        d_time.hour,
        d_time.minute,
        d_time.second
    )
    
    try:
        print("Packing web_static to {}".format(output))
        run(f"tar -cvzf {output} web_static", hide=True)  # Hide output if desired
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception as e:
        print(f"Failed to pack web_static: {e}")
        output = None
    
    return output
