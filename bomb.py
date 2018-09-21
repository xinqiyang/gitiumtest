import json
import logging
import logging.config as log_conf
import sys
import threading
import time
import traceback

import requests

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


# -H 'Origin: file://'
# -H 'Accept-Encoding: gzip, deflate'
# -H 'Accept-Language: zh-CN'
# -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) gitium/2.1.3 Chrome/59.0.3071.115 Electron/1.8.2 Safari/537.36'
# -H 'Content-Type: application/json;charset=UTF-8'
# -H 'Accept: application/json, text/plain, */*' -H 'X-IOTA-API-Version: 1'
# -H 'Proxy-Connection: keep-alive'
# -H 'X-DevTools-Request-Id: 21152.153'
def doPost():
    url = 'http://www.gitium.io/gitium/charge/saveCharge'
    body = {
        "receivedAddress": "9QMWBHRSVEATKGNBFI9CKUOSEVYU9ZZCY9LRWOWHLJACQSYKEY9EKTG9RKOLX9SFZLQPWMLLPALJCTBBCLFQQKEGMY9QMWBHRSVEATKGNBFI9CKUOSEVYU9ZZCY9LRWOWHLJACQSYKEY9EKTG9RKOLX9SFZLQPWMLLPALJCTBBCLFQQKEGMY9QMWBHRSVEATKGNBFI9CKUOSEAAAAADDDDDDSFADFSFADFASFSFADSFASDFADSFAAAAAAAABBBB",
        "currency": "GIT",
        "value": 1312852829198,
        "status": "0",
        "phone": "",
        "chargeValue": 1,
        "useCurrency": "Bitcoin",
        "chargeAddress": "9QMWBHRSVEATKGNBFI9CKUOSEVYU9ZZCY9LRWOWHLJACQSYKEY9EKTG9RKOLX9SFZLQPWMLLPALJCTBBCLFQQKEGMY9QMWBHRSVEATKGNBFI9CKUOSEVYU9ZZCY9LRWOWHLJACQSYKEY9EKTG9RKOLX9SFZLQPWMLLPALJCTBBCLFQQKEGMY9QMWBHRSVEATKGNBFI9CKUOSEAAAAADDDDDDSFADFSFADFASFSFADSFASDFADSFAAAAAAAABBBB",
        "userPayAddress": "9QMWBHRSVEATKGNBFI9CKUOSEVYU9ZZCY9LRWOWHLJACQSYKEY9EKTG9RKOLX9SFZLQPWMLLPALJCTBBCLFQQKEGMY9QMWBHRSVEATKGNBFI9CKUOSEVYU9ZZCY9LRWOWHLJACQSYKEY9EKTG9RKOLX9SFZLQPWMLLPALJCTBBCLFQQKEGMY9QMWBHRSVEATKGNBFI9CKUOSEAAAAADDDDDDSFADFSFADFASFSFADSFASDFADSFAAAAAAAABBBB"
    }
    # body = body.encode(encoding="utf-8")
    headers = {
        'Origin': "file://",
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': "zh-CN",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) gitium/2.1.3 Chrome/59.0.3071.115 Electron/1.8.2 Safari/537.36",
        'Content-Type': "application/json;charset=UTF-8",
        'Accept': "application/json, text/plain, */*' -H 'X-IOTA-API-Version: 1",
        'Proxy-Connection': "keep-alive"
    }

    response = requests.post(url, data=json.dumps(body), headers=headers)
    log.info(response.text)


def runLogic(arg):
    log.debug('thread ' + str(arg) + " running....")
    try:
        exec('{}()'.format('doPost'))
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("{}".format(repr(traceback.format_exception(exc_type, exc_value, exc_traceback))))


if __name__ == '__main__':
    postCount = 10
    while True:
        for i in range(0, postCount):
            t = threading.Thread(target=runLogic, args=(i,))
            t.start()
            # if i == 'www_upbit_com' or i == 'blog_coinbase_com' or i == 'coinone_co_kr' or i == 'medium_com_gemini':
            #     time.sleep(10)
            break
        time.sleep(13)
