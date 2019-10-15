from openstack import connection

conn = connection.Connection(
        auth_plugin = 'YOUR_CLOUD_PROVIDER',
        username = 'YOUR_USERNAME',
        password = 'YOUR_PASSWORD',
        project_name = 'YOUR_PROJECT_NAAME',
        profile = prof)
