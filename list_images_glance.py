from glanceclient.v2 import client

conn= client.Client(auth_url, token)

for image in conn.images.list():
    print(image["name"])
