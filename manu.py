import time
time1 = time.time()
time.sleep(1)
time2 = time.time()
print (time1)
print (time2)
resta = time2 - time1
print (resta)
time_resoult = time.time() - time1
time_push1 = time_resoult / 60
time_push2 = time_resoult % 60 
time_format1 = time_push1 + ""
time_format2 = time_push2 + ""
time_push =  time_format1 + time_format2
print (time_push)
