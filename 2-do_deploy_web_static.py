#!/usr/bin/env python3
from fabric import task, Connection
from fabric import Serial
import os

# Define the list of web servers
WEB_SERVERS = ['<IP web-01>', '<IP web-02>']

@task
def do_deploy(ctx, archive_path):
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
        for server in WEB_SERVERS:
            # Establish a connection
            conn = Connection(host=server, connect_kwargs={"key_filename": "<path_to_your_ssh_key>", "username": "<your_username>"})

            # Upload the archive to /tmp/
            print(f"Uploading {archive_path} to {server}...")
            conn.put(archive_path, tmp_path)

            # Create the release directory
            print(f"Creating directory {release_path} on {server}...")
            conn.run(f"mkdir -p {release_path}")

            # Uncompress the archive
            print(f"Extracting {tmp_path} to {release_path} on {server}...")
            conn.run(f"tar -xzf {tmp_path} -C {release_path}")

            # Remove the archive from the server
            print(f"Removing archive {tmp_path} from {server}...")
            conn.run(f"rm {tmp_path}")

            # Move the files from web_static to the release directory
            print(f"Moving files from web_static to {release_path} on {server}...")
            conn.run(f"mv {release_path}web_static/* {release_path}")

            # Remove the web_static folder
            print(f"Removing {release_path}web_static on {server}...")
            conn.run(f"rm -rf {release_path}web_static")

            # Remove the current symbolic link
            print(f"Removing current symlink on {server}...")
            conn.run(f"rm -rf /data/web_static/current")

            # Create a new symbolic link
            print(f"Creating new symlink on {server}...")
            conn.run(f"ln -s {release_path} /data/web_static/current")

            print(f"Deployment on {server} completed.")

        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
