Pelican-auto-generator
====

Pelican auto generator is a tool built for use with Pelican python, the static blog generator.
This tool is designed to allow for posts to be created and automatically pushed to the blog
remotely.

At present the tool is quite rigid toward my personal workflow. I use a dropbox directory for my
pelican source directory (other solutions than dropbox should work just fine, so long as the filesystem
sees it as a folder then all is good). I wanted a way where I could write a post on my phone, stick it
in dropbox and see it a few minutes later on my blog - that's what this tool does.

At present the tool only supports publishing to things that use git push. The tool also requires a git hook
to be created on the commit action (I'm hoping to extend this to work with other things via a config file).

Install
-------
Ensure that your blog project is a git repository

Create a commit hook to push up to whatever host service you use

Install into `/opt`:

    cd /opt
    git clone git@github.com:chvck/pelican-auto-generator.git


Create a virtual env:

    virtualenv --distribute venv

Activate the virtual env

    source venv/bin/activate
    
Install dependencies

    pip install -r requirements.txt


Create a log directory:

    sudo mkdir /var/log/pag
    sudo chown <user>:<group> /var/log/pag


Create a supervisor config in `/etc/supervisor/conf.d/pelican-auto-generator.conf`:

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
