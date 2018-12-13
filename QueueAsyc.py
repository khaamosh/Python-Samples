# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:45:42 2018

@author: utsharm
"""
""""
'Not intended for Production Envrionments'  
"""
import asyncio
import datetime
from azure.storage.queue import *

async def inQueue(loop):
    end_time = loop.time() + 5.0
    while True:
        """
        myaccount-> storage account name
        account-key-> storage account key
        """
        queue_Service = QueueService(account_name='myaccount',account_key='account-key')
        queue_Service.create_queue('tasks')
        queue_Service.put_message('tasks','HelloWorld')
        print(datetime.datetime.now())
        print("MessageEntered")
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


loop = asyncio.get_event_loop()

# Blocking call which returns when the inQueue() coroutine is done
loop.run_until_complete(inQueue(loop))
loop.close()
 
