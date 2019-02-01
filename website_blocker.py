import time
from datetime import datetime as dt
import os 

host_path = os.path.expanduser("~/../../etc/hosts")
redirect= "127.0.0.1"
websites = ["www.facebook.com", "facebook.com"]



while True:
    now = dt.now().time()
    if now.hour > 20 and now.hour < 22:
        with open(host_path, 'r+') as file:
            content = file.read()
            print(content)
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirect + " " + site +"\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines() 
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)   
            file.truncate()  
            print(content)

    time.sleep(10)

