# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:45:42 2018

@author: utsharm
"""
""""
'By using the following materials or sample code you agree to be bound by the license terms below 
'and the Microsoft Partner Program Agreement the terms of which are incorporated herein by this reference. 
'These license terms are an agreement between Microsoft Corporation (or, if applicable based on where you 
'are located, one of its affiliates) and you. Any materials (other than sample code) we provide to you 
'are for your internal use only. Any sample code is provided for the purpose of illustration only and is 
'not intended to be used in a production environment. We grant you a nonexclusive, royalty-free right to 
'use and modify the sample code and to reproduce and distribute the object code form of the sample code, 
'provided that you agree: (i) to not use Microsoft’s name, logo, or trademarks to market your software product 
'in which the sample code is embedded; (ii) to include a valid copyright notice on your software product in 
'which the sample code is embedded; (iii) to provide on behalf of and for the benefit of your subcontractors 
'a disclaimer of warranties, exclusion of liability for indirect and consequential damages and a reasonable 
'limitation of liability; and (iv) to indemnify, hold harmless, and defend Microsoft, its affiliates and 
'suppliers from and against any third party claims or lawsuits, including attorneys’ fees, that arise or result 
'from the use or distribution of the sample code."  
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
 