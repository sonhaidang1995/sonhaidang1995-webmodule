import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds125502.mlab.com:25502/muadongkhonglanh-c4e20

host = "ds125502.mlab.com"
port = 25502
db_name = "muadongkhonglanh-c4e20"
user_name = "admin"
password = "admin1234"


def connect():
    mongoengine.connect(
        db_name, 
        host=host, 
        port=port, 
        username=user_name, 
        password=password
    )
