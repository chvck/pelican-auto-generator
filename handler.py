import logging
import os
import time

from pyinotify import ProcessEvent


log = logging.getLogger('pag.handler')


class EventHandler(ProcessEvent):

    def __init__(self, working_dir, queue):
        log.debug('create handler')
        self.queue = queue
        self.working_dir = working_dir

    def process_IN_MOVED_TO(self, event):
        log.debug('Detected file: {0}'.format(event.name))
        if os.path.isfile(event.pathname) and event.pathname.endswith('.md'):
            log.info('Queued file: {0}'.format(event.name))
            self.queue.put(event.pathname)
        time.sleep(0.5)


    def process_IN_CREATE(self, event):
        log.debug('Detected file: {0}'.format(event.name))
        if os.path.isfile(event.path) and event.path.endswith('.md'):
            log.info('Queued file: {0}'.format(event.name))
            self.queue.put(event.path)
        time.sleep(0.5)
        
    def process_IN_DELETE(self, event):
        log.debug('Detected file: {0}'.format(event.name))
        if os.path.isfile(event.path) and event.path.endswith('.md'):
            log.info('Queued file: {0}'.format(event.name))
            self.queue.put(event.path)
        time.sleep(0.5)
        
    def process_IN_MODIFY(self, event):
        log.debug('Detected file: {0}'.format(event.name))
        if os.path.isfile(event.path) and event.path.endswith('.md'):
            log.info('Queued file: {0}'.format(event.name))
            self.queue.put(event.path)
        time.sleep(0.5)