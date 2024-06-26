import os
import boto3

# Initialize Boto3 client for Systems Manager
ssm = boto3.client('ssm', region_name='us-east-1')

# Function to retrieve database password from Parameter Store
def get_db_password():
    try:
        # Retrieve database password from Parameter Store
        response = ssm.get_parameter(Name='rds-db-password', WithDecryption=True)
        db_password = response['Parameter']['Value']
        return db_password
    except Exception as e:
        print(f"Error retrieving database password: {e}")
        return None



def get_rds_host():
    try:
        response = ssm.get_parameter(Name='rds_host', WithDecryption=True)
        db_host = response['Parameter']['Value']
        db_host = db_host[:-5]
        return db_host
    except Exception as e:
        print(f"Error retrieving database password: {e}")
        return None

    



custombucket = "sambhubucket"
table = "users"
databasehost = get_rds_host()
duser = "admin"
dpass = get_db_password()
s3database = "mydatabase"
dynamoDB_table = "My_Table"
# kapp = "http://3.228.220.21/"

print("host: {}, pass: {}".format(databasehost, dpass))
