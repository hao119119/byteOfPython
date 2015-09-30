from fabric.api import *
env.hosts = [
    'cc@10.106.1.74',
    'cc@10.106.1.75',
]

env.gateway = 'cc@10.106.1.76'

env.passwords = {
    'cc@10.106.1.74:22': 'hao119119',
    'cc@10.106.1.75:22': 'hao119119',
}

@task
def echo():
    run('echo "hello,world"')
