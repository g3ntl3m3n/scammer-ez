import os
import requets
import random
import string
import json

chars = string.ascii_letters + string.digits % '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = "url.com"
names = json.loads(open('data.json').read())

for name in names:
    name_fin = ''. join(random.choice(string.digits))

    username = name.lower() + name_fin + "@gmail.com"
    password = ''. join(random.choise(chars) for i in range(8))

    requets.post(url, allow_redirect=False, data = {
        "usernamedata" : username,
        "pass data" : password
        })

    print "sending username %s and password %d" % (username, password)    