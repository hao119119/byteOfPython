from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = 'cc'
env.hosts = ['10.106.1.74', '10.106.1.75']
env.password = 'hao119119'


@runs_once
def tar_task():
    with lcd('/home/cc'):
        local('tar -czf test.tar.gz test')


@task
def put_task():
    run('mkdir -p /home/cc/test')
    with cd('/home/cc/test'):
        with settings(warn_only=True):
            result = put('/home/cc/test.tar.gz', '/home/cc/test')
        if result.failed and not confirm('put file failed, Continue[Y/N]?'):
            abort('Aborting file put task!')


@task
def check_task():
    with settings(warn_only=True):
        lmd5 = local('md5sum /home/cc/test.tar.gz', capture=True).split(' ')[0]
        rmd5 = run('md5sum /home/cc/test/test.tar.gz').split(' ')[0]
        if lmd5 == rmd5:
            print 'OK'
        else:
            print 'Error'


@task
def go():
    tar_task()
    put_task()
    check_task()
