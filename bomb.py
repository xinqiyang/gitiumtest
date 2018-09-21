import logging
import logging.config as log_conf
import threading
import traceback

import sys, os
import time


checkTime = 3600
upbit_browser = None

log_config = {
    'version': 1.0,
    'formatters': {
        'detail': {
            'format': '%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'detail'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1024 * 5,
            'backupCount': 10,
            'filename': 'trace.log',
            'level': 'DEBUG',
            'formatter': 'detail',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'crawler': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'parser': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'other': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'storage': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'log': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    }
}

log_conf.dictConfig(log_config)
log = logging.getLogger('log')


def runShell():
    cmd = 'nohup sh bomb.sh >/dev/null 2>&1 &'
    ret = os.system(cmd)
    # log.info(ret)


def runLogic(arg):
    # log.debug('thread ' + str(arg) + " running....")
    try:
        exec('{}()'.format('runShell'))
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        log.warning("{}".format(repr(traceback.format_exception(exc_type, exc_value, exc_traceback))))


if __name__ == '__main__':
    count = 0
    postCount = 10
    while True:
        for i in range(0, postCount):
            t = threading.Thread(target=runLogic, args=(i,))
            t.start()
            count = count + 1
            if count % 100 == 0:
                log.info("do insert: {}".format(count))
            time.sleep(2)