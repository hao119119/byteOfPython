from fabric.colors import *
from fabric.api import *
env.user = 'cc'
env.roledefs = {
    'webservers': ['10.106.1.74', '10.106.1.75'],
    'debservers': ['10.106.1.76']
}

env.password = {
    'cc@10.106.1.74:22': 'hao119119',
    'cc@10.106.1.75:22': 'hao119119',
    'cc@10.106.1.76:22': 'hao119119'
}


@roles('webservers')
def webtask():
    print yellow('install nginx php php-fpm...')
    with settings(warn_only=True):
        run('yum -y install nginx')
        run('yum -y install php-fpm php-mysql')
        run('chkconfig --levels 235 php-fpm on')
        run('chkconfig --levels 235 nginx on')


@roles('dbservers')
def dbtask():
    print yellow('Install Mysql')
    with settings(warn_only=True):
        run('yum -y install mysql mysql-server')
        run('chkconfig --levels 235 mysqld on')


@roles('webservers', 'dbservers')
def publictask():
    print yellow('Install epel ntp...')
    with settings(warn_only=True):
        run('rpm -Uvh http://...')
        run('yum -y install ntp')


def deploy():
    execute(publictask)
    execute(webtask)
    execute(dbtask)


