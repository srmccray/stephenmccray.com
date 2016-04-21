from fabric.api import *
import os
import shutil
import sys
import SocketServer

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Port for `serve`
PORT = 8000
S3BUCKET = 'stephenmccray.com'


def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)


def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')


def rebuild():
    """`clean` then `build`"""
    clean()
    build()


def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')


def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()


def reserve():
    """`build`, then `serve`"""
    build()
    serve()


def publish():
    """Build production version of site"""
    clean()
    local('pelican -s publishconf.py')


def deploy():
    publish()
    with lcd(DEPLOY_PATH):
        local('aws s3 --profile personal --region us-west-2 sync . s3://%s --acl public-read' % S3BUCKET)

