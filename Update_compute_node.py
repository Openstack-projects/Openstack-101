from openstack import connection

conn = connection.Connection(
        auth_url = 'http://YOUR_floating_IP:5000/v2.0',
        username = 'YOUR_USERNAME',
        password = 'YOUR_PASSWORD',
        project_name = 'YOUR_PROJECT_NAAME')
        
srv = conn.compute.find_server("MyServer1")

conn.compute.update_server(srv, name="BestServerEver")
