from novaclient.v1_1 import client

conn = client.Client(user, password, project, auth_url)

for server in conn.servers.list():
    print(server.name)
