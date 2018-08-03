
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os
import sys
import requests
from aws_requests_auth.aws_auth import AWSRequestsAuth



Scheduler=BackgroundScheduler()
def collector():

    print("collector")
    # let's talk to our AWS Elasticsearch cluster
    auth = AWSRequestsAuth(aws_access_key='AKIAJGRWOA2XINFDNXCA',
                           aws_secret_access_key='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',
                           aws_host='jk80xeof06.execute-api.us-east-1.amazonaws.com',
                           aws_region='us-east-1',
                           aws_service='es')

    #response = requests.post('https://jk80xeof06.execute-api.us-east-1.amazonaws.com/iam/',auth=auth)

    response = requests.post('https://jk80xeof06.execute-api.us-east-1.amazonaws.com/beta1/',auth=auth)
    print(response.text)


def _pause():
    print("pauseXxxx")
    try:
        Scheduler.pause()
    except:
        return ("!!!!!!")
def _resume():
    print("resumeX")
    Scheduler.resume()
def _remove():
    print("removeX")
    Scheduler.remove()
def _down():
    print("downX")
    Scheduler.shutdown()



def startJob():

    Scheduler.add_job(collector,'interval',seconds=5)

    Scheduler.start()
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        a=1
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        Scheduler.shutdown()

#startJob()