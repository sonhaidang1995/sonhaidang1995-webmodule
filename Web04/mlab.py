# import mongoengine

# # mongodb://<dbuser>:<dbpassword>@ds233228.mlab.com:33228/cms-app

# host = 'ds233228.mlab.com'
# port = 33228
# db_name = 'cms-app'
# user_name = 'admin'
# password = 'admin1234'

# def connect():
#     mongoengine.connect(
#         db_name,
#         host = host,
#         port = port,
#         username = user_name,
#         password = password
#     )

import mongoengine
host = 'ds233228.mlab.com'
port = 33228
db_name = 'cms-app'
user_name = 'admin'
password = 'admin1234'

def connect():
    mongoengine.connect(
        db_name,
        host = host,
        port = port,
        username = user_name,
        password = password
    )

