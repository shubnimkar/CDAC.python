import time
while True:
    from datetime import datetime
    now = datetime.now()  
    print ("%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)) 
    time.sleep(1)
