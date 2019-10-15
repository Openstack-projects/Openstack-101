from openstack import connection
from openstack import profile

prof = profile.Profile()
prof.set_region(prof.ALL, "SomeRegion")

conn = connection.Connection(
        auth_url = 'http://YOUR_floating_IP:5000/v2.0',
        username = 'YOUR_USERNAME',
        password = 'YOUR_PASSWORD',
        project_name = 'YOUR_PROJECT_NAAME',
        profile = prof)
