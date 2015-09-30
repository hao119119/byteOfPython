from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm


# env.user = 'cc'
env.gateway = 'cc@10.106.1.74'
env.hosts = [
    'cc@10.106.1.75',
    'cc@10.106.1.76',
]

# must add the :22, or the fab can't find the password
env.passwords = {
    'cc@10.106.1.74:22': 'hao119119',
    'cc@10.106.1.75:22': 'hao119119',
    'cc@10.106.1.76:22': 'hao119119',
}

# env.password = 'hao119119'

lpackpath = '/home/cc/test.tar.gz'
rpackpath = '/tmp/install'


@task
def put_task():
    run('mkdir -p /tmp/install')
    with settings(warn_only=True):
        result = put(lpackpath, rpackpath)
    if result.failed and not confirm('put file failed, Continue[Y/N]?'):
        abort('Aborting file put task')


@task
def run_task():
    with cd('/tmp/install'):
        run('tar -zxvf test.tar.gz')
        with cd('test/'):
            run('chmod 777 1.sh')
            run('./1.sh')

@task
def go():
    put_task()
    run_task()

