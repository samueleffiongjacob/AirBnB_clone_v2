#!/usr/bin/env python3
from fabric.api import env, local, run, put, task
from datetime import datetime
import os

# Define the list of web servers
env.hosts = ['3.85.141.200', '54.236.190.52']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_pack():
    """
    Creates an archive of the web_static directory.
    Returns the path of the created archive or None if the archive creation fails.
    """
    if not os.path.exists("versions"):
        os.makedirs("versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{timestamp}.tgz"
    
    print(f"Packing web_static to {archive_path}")
    result = local(f"tar -cvzf {archive_path} web_static")
    
    if result.failed:
        print("Failed to create archive.")
        return None
    
    print(f"web_static packed: {archive_path} -> {os.path.getsize(archive_path)}Bytes")
    return archive_path

@task
def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.
    """
    if not os.path.exists(archive_path):
        print("Archive file does not exist.")
        return False

    # Extract the filename without the extension
    filename = os.path.basename(archive_path)
    filename_no_ext = filename.split('.')[0]
    
    # Path for the temporary and release directories
    tmp_path = f"/tmp/{filename}"
    release_path = f"/data/web_static/releases/{filename_no_ext}/"
    
    try:
        # Upload the archive to /tmp/
        put(archive_path, tmp_path)

        # Create the release directory
        run(f"mkdir -p {release_path}")

        # Uncompress the archive
        run(f"tar -xzf {tmp_path} -C {release_path}")

        # Remove the archive from the server
        run(f"rm {tmp_path}")

        # Move the files from web_static to the release directory
        run(f"mv {release_path}web_static/* {release_path}")

        # Remove the web_static folder
        run(f"rm -rf {release_path}web_static")

        # Remove the current symbolic link
        run(f"rm -rf /data/web_static/current")

        # Create a new symbolic link
        run(f"ln -s {release_path} /data/web_static/current")

        print("Deployment completed.")
        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False

@task
def deploy():
    """
    Creates and distributes an archive to web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
