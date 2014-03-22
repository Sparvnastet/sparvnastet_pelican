from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
from settings import SSH_USER, SSH_HOST, SITE_ROOT, CALENDAR_OUTPUT_DIR, CALENDAR_INPUT_DIR

# Local path configuration (can be absolute or relative to fabfile)
HOST_SPARVNASTET = '%s@%s' % (SSH_USER, SSH_HOST)

env.hosts = [HOST_SPARVNASTET]
env.user = SSH_USER
env.port = 22

# Use SSH Key forwarding?
env.forward_agent = True
env.sparv_deploypath = SITE_ROOT

DEPLOY_PATH = env.sparv_deploypath


def clean():
    """
    Delete the deploy path and remake it again
    """
    # if os.path.isdir(DEPLOY_PATH):
    #     local('rm -rf {deploy_path}'.format(**env))
    #     local('mkdir {deploy_path}'.format(**env))
    #
    pass


def build():
    #local('pelican -s pelicanconf.py')
    local('make html')
    # copy the calendar

    # Copy calendar
    calendar_source = os.path.join(CALENDAR_INPUT_DIR, 'calendar.json')
    calendar_target = os.path.join(CALENDAR_OUTPUT_DIR, 'calendar.json')
    local('echo copying %s to %s ' % (calendar_source, calendar_target))
    shutil.copyfile(calendar_source, calendar_target)


def rebuild():
    clean()
    build()


def regenerate():
    local('pelican -r -s pelicanconf.py')


def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))


def reserve():
    build()
    serve()


def preview():
    local('pelican -s publishconf.py')


#@hosts(production)
def publish():
    #local('pelican -s publishconf.py')

    run('echo "running remotely"')
    build()
    with cd("{sparv_deploypath}".format(**env)):
        run(". ../env/bin/activate")
        run("git pull origin master -v")
        run("make html")
        run("make publish")



