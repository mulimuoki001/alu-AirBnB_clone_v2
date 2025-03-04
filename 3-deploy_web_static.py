#!/usr/bin/python3
"""fabric script based on the file 2-do_deploy_web_static.py"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ["3.91.153.139", "3.89.33.228"]


def do_pack():
    """ "generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        return "versions/web_static_{}.tgz".format(date)
    except:
        return None


def do_deploy(archive_path):
    """ "deploy an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(file_n, path, no_ext))
        run("rm /tmp/{}".format(file_n))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, no_ext))
        run("rm -rf {0}{1}/web_static/".format(path, no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
