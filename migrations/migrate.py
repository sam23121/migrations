import os
import psycopg2
import pymysql
pymysql.install_as_MySQLdb()

PG = {
    'name' : 'postgres',
    'user' : 'sam',
    'pass' : 'sam123',
    'host' : 'localhost',
}

MYSQL = {
    'db': 'mysql',
    'user': 'root',
    'passwd': 'Sam12345#',
    'host': 'localhost',
}

TABLES_LIST = [
    'objects',
    'objects_transformation'
]

def create_pg_connection():
    string = "dbname={name} user={user} password={pass}".format(**PG)
    conn = psycopg2.connect(string)
    cur = conn.cursor()
    return cur

def generate_tsv(table):
    file_ = open('/tmp/{0}.tsv'.format(table), 'w')
    kwargs = {
        'file': file_,
        'table': table,
    }
    cursor = create_pg_connection()
    cursor.copy_to(**kwargs)
    cursor.close()

def import_tsv(table):
    MYSQL.update({'table': table})
    mysql_command = 'mysqlimport --local --compress --user={user} --password={passwd} --verbose --host={host} {db} /tmp/{table}.tsv'.format(**MYSQL)
    os.system(mysql_command)

def create_mysql_connection():
    conn = pymysql.connect(**MYSQL)
    cursor = conn.cursor()
    return cursor

def create_tables(cursor):                                     
    # SQL query string
    # sqlQuery = "CREATE TABLE IF NOT EXISTS  objects(track_id INT Primary KEY, type1 varchar(20),traveled_d REAL,avg_speed REAL, lat REAL, lon REAL, speed REAL, lon_acc REAL, lat_acc REAL, time1 REAL)"   
    # Execute the sqlQuery
    with open('../data/create_table.sql', 'r') as sql_file:
        cursor.execute(sql_file.read(), multi=True)
    # cursor.execute(sqlQuery)




if __name__=="__main__":
    cursor = create_mysql_connection()
    create_tables(cursor)
    for table in TABLES_LIST:
        generate_tsv(table)
        import_tsv(table)
    
    # connectionObject = pymysql.connect(host='127.0.0.1', user='root', password='Sam12345#',
    #                                  db='mysql', charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)
    
    # try:
    #     # Create a cursor object
    #     cursorObject = connectionObject.cursor()                                     
    #     # SQL query string
    #     sqlQuery = "CREATE TABLE IF NOT EXISTS  objects(track_id INT Primary KEY, type1 varchar(20),traveled_d REAL,avg_speed REAL, lat REAL, lon REAL, speed REAL, lon_acc REAL, lat_acc REAL, time1 REAL)"   
    #     # Execute the sqlQuery
    #     cursorObject.execute(sqlQuery)
    # except Exception as e:
    #     print("Exeception occured:{}".format(e))

    



