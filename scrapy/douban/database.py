import pymysql

MYSQL_HOST = "localhost"
MYSQL_DATABASE = "douban"
MYSQL_USER = "root"
MYSQL_PASSWORD = "melo"
MYSQL_PORT = 3306

connection = pymysql.connect(MYSQL_HOST,
                                  MYSQL_USER,
                                  MYSQL_PASSWORD,
                                  MYSQL_DATABASE,
                                  charset='utf8mb4',
                                  port=MYSQL_PORT)