Pelican-auto-generator
====

Install
-------
Install into `/opt`:

    cd /opt
    git clone git@github.com:chvck/pelican-auto-generator.git


Create a virtual env:

    virtualenv --distribute venv


Create a log directory:

    sudo mkdir /var/log/pag
    sudo chown <user>:<group> /var/log/pag


Create a supervisor config in `/etc/supervisor/conf.d/tvrd.conf`:

    [program:pelican-auto-generator]
    command=/opt/pelican-auto-generator/venv/bin/python /opt/pelican-auto-generator/main.py <folder to watch> <git folder>
    user=<user>
    autostart=true
    autorestart=true
    redirect_stderr=True


Update supervisor:

    sudo supervisorctl update


Set up log rotation in `/etc/logrotate.d/pelican-auto-generator` (with sudo):

    /var/log/pag/* {
        missingok
        nocompress
        rotate 5
        size 100M
    }


Profit.
