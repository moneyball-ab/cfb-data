#requires the following python packages:
#   sqlalchemy
#   to install: "sudo pip install sqlalchemy" in CLI
#
#   mysql-connector
#   to install: "sudo pip install mysql-connector" in CLI
#
#also requires a MySQL or MariaDB database with
#connection parameters defined in a dbconfig.ini file

import pandas as pd
import sqlalchemy
import configparser
config = configparser.ConfigParser()
config.read('./config/dbconfig.ini')

def __connect():
    # set connection parameters based on /config/dbconfig.ini
    prefix = config['CONNECTION']['prefix']
    un = config['CONNECTION']['un']
    pw = config['CONNECTION']['pw']
    ip = config['CONNECTION']['ip']
    db = config['CONNECTION']['db']

    #create the connection object    
    con = sqlalchemy.create_engine(
        '{0}{1}:{2}@{3}/{4}'.format(prefix, un, pw, ip, db)
    )

    #clear the connection parameters for security
    un = ''
    pw = ''
    ip = ''
    db = ''

    #return the connection object
    return con

def test():
    #load simple query to df and print to screen
    df = pd.read_sql('SELECT * FROM test02', con=__connect())
    print(df)

#run the test
test()
