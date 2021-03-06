import sys
import logging
import pymysql
import os
#rds settings
rds_host  = os.environ['DB_ENDPOINT']
name = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
db_port = int(os.environ['DB_PORT'])

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, port=db_port, user=name, passwd=password, connect_timeout=5)
    conn.cursor().execute('create database if not exists ' + db_name)
    conn.select_db(db_name)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        cur.execute("create table if not exists " + db_name + ".Employee ( EmpID  int NOT NULL auto_increment, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
        cur.execute('insert into Employee (Name) values("Joe")')
        cur.execute('insert into Employee (Name) values("Bob")')
        cur.execute('insert into Employee (Name) values("Mary")')
        conn.commit()
        cur.execute("select * from Employee")
        for row in cur:
            item_count += 1
            logger.info(row)
            #print(row)
    conn.commit()

    return "Added %d items from RDS MySQL table" %(item_count)