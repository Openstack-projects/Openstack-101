from openstack import connection

conn = connection.Connection(
        auth_url = 'http://YOUR_floating_IP:5000/v2.0',
        username = 'YOUR_USERNAME',
        password = 'YOUR_PASSWORD',
        project_name = 'YOUR_PROJECT_NAAME')
        
srv = conn.compute.get_server("YOUR_RESOURCES_ID")
srv = conn.compute.get_server(srv)
