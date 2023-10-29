#!/usr/bin/python3
"""A .tgz archive from contents of web_static generation."""
from fabric.api import local
import time


def do_pack():
    """An tgz archive Generation"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None
