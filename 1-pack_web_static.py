#!/usr/bin/env python3
import os
from datetime import datetime
from fabric import task

@task
def do_pack(c):
    """Archives the static files."""
    
    # Ensure the 'versions' directory exists
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    
    # Generate the filename based on the current date and time
    d_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_time.year,
        str(d_time.month).zfill(2),
        str(d_time.day).zfill(2),
        str(d_time.hour).zfill(2),
        str(d_time.minute).zfill(2),
        str(d_time.second).zfill(2)
    )
    
    try:
        # Print the location of the archive being created
        print(f"Packing web_static to {output}")
        
        # Run the tar command to create the archive
        c.run(f"tar -cvzf {output} web_static")
        
        # Get the size of the archive file
        size = os.stat(output).st_size
        
        # Print confirmation of the archive's creation
        print(f"web_static packed: {output} -> {size} Bytes")
    except Exception as e:
        print(f"Failed to pack web_static: {e}")
        output = None
    
    return output
