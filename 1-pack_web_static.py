from fabric import task
import os

@task
def do_pack(ctx):
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    local_time = time.strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{local_time}.tgz"
    archive_path = f"versions/{archive_name}"

    print(f"Packing web_static to {archive_path}")
    if not os.path.exists('versions'):
        os.makedirs('versions')
    
    result = ctx.run(f"tar -czvf {archive_path} web_static")
    if result.ok:
        print(f"web_static packed: {archive_path}")
    else:
        print("Packing failed")
