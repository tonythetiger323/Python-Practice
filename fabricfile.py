from fabric.api import *

def greeting(msg):
    print 'Good %s' % msg

def system_info():
    print 'Disk Space'
    local('df -h')

    print 'Memory Free'
    local('free -m')

    print 'System uptime'
    local('uptime')

def remote_exec():
    print 'Get system info'
    run('hostname')
    run('uptime')
    run('df -h')
    run('free -m')

    sudo('yum install mariadb-server -y')
    sudo('systemctl start mariadb')
    sudo('systemctl enable mariadb')

def web_setup(WEBURL, DIRNAME):
    print '######################################################################'
    local('apt install zip unzip -y')

    print '######################################################################'
    print 'Installing Dependencies'
    print '######################################################################'
    sudo('yum install httpd wget unzip -y')

    print '######################################################################'
    print 'Start & enable service.'
    print '######################################################################'
    sudo('systemctl start httpd')
    sudo('systemctl enable httpd')

    print '######################################################################'
    print 'Downloading and pushing website to webservers'
    print '######################################################################'
    local(('wget -O website.zip %s') % WEBURL)
    local('unzip -o website.zip')

    with lcd(DIRNAME):
        local('zip -r tooplate.zip *')
        put('tooplate.zip', '/var/www/html/', use_sudo=True)

    with cd('/var/www/html/'):
        sudo('unzip -o tooplate.zip')

    sudo('systemctl restart httpd')

    print 'Website setup is done.'
