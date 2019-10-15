from openstack import connection

conn = connection.Connection(
        auth_url = 'http://YOUR_floating_IP:5000/v2.0',
        username = 'YOUR_USERNAME',
        password = 'YOUR_PASSWORD',
        project_name = 'YOUR_PROJECT_NAAME')
        
img = conn.compute.find_image("cirros")
flv = conn.compute.find_flavor("m1.small")

conn.compute.create_server(name="MyServer1", image=img, flavor=flv)
