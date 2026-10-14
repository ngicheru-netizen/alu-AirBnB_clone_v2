#!/usr/bin/python3
"""Pack and deploy the web_static directory."""

import importlib.util

from fabric.api import env


env.hosts = ["184.73.19.238", "35.175.218.108"]


def _load_function(filename, function_name):
    """Load a function from a script whose name contains hyphens."""
    spec = importlib.util.spec_from_file_location(filename, filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)


do_pack = _load_function("1-pack_web_static.py", "do_pack")
do_deploy = _load_function("2-do_deploy_web_static.py", "do_deploy")


def deploy():
    """Create an archive and deploy it to all configured web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
