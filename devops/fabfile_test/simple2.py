from fabric.api import *

env.user = 'cc'
env.hosts = ['10.106.1.74', '10.106.1.75']
env.password = 'hao119119'


@runs_once
def input_raw():
    return prompt('please input directory name:', default='/home')


def worktask(dirname):
    run('ls -l '+dirname)


@task
def go():
    getdirname = input_raw()
    worktask(getdirname)
