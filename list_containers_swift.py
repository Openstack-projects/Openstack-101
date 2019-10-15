from swiftclient import client

conn = client.Connection(authurl, user, key,
                          tenant_name,
                          auth_version)
                          
header, containers = conn.get_account()

for container in containers:
    print(container["name'])
