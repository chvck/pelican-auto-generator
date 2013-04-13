import argparse
import logging
import os
import Queue
import threading

from pyinotify import IN_MOVED_TO, Notifier, WatchManager

from handler import EventHandler
from logs import start_logging
from worker import worker


FIREHOSE = '/var/log/pag/log.log'


log = logging.getLogger('pag.main')

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('path')
parser.add_argument('git_path')
args = parser.parse_args()

if __name__ == '__main__':
    start_logging(FIREHOSE, debug=args.debug)

    q = Queue.Queue()

    t = threading.Thread(target=worker, args=(q, args.path, args.git_path))
    t.daemon = True
    t.start()

    watch_manager = WatchManager()
    handler = EventHandler(args.path, q)

    notifier = Notifier(watch_manager, handler)

    # watch this directory, with mask(s)
    wdd = watch_manager.add_watch(args.path, IN_MOVED_TO, rec=True, auto_add=True)

    # setup options
    notifier.loop(daemonize=False)

