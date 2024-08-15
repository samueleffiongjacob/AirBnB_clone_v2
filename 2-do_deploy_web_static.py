#!/usr/bin/env python3
from fabric import task
import os

@task
def do_deploy(ctx, archive_path):
    if not os.path.exists(archive_path):
        print("Archive file does not exist.")
        return False

    filename = os.path.basename(archive_path)
    filename_no_ext = filename.split('.')[0]
    tmp_path = f"/tmp/{filename}"
    release_path = f"/data/web_static/releases/{filename_no_ext}/"
    
    try:
        conn = ctx.connection

        print(f"Uploading {archive_path} to localhost...")
        conn.put(archive_path, tmp_path)

        print(f"Creating directory {release_path} on localhost...")
        conn.run(f"mkdir -p {release_path}")

        print(f"Extracting {tmp_path} to {release_path} on localhost...")
        conn.run(f"tar -xzf {tmp_path} -C {release_path}")

        print(f"Removing archive {tmp_path} from localhost...")
        conn.run(f"rm {tmp_path}")

        print(f"Moving files from web_static to {release_path} on localhost...")
        conn.run(f"mv {release_path}web_static/* {release_path}")

        print(f"Removing {release_path}web_static on localhost...")
        conn.run(f"rm -rf {release_path}web_static")

        print(f"Removing current symlink on localhost...")
        conn.run(f"rm -rf /data/web_static/current")

        print(f"Creating new symlink on localhost...")
        conn.run(f"ln -s {release_path} /data/web_static/current")

        print(f"Deployment on localhost completed.")

        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
