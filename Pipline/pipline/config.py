USERNAME='root'
PASSWD='root'
DBIP='192.168.1.112'
DBPORT=3306
DBNAME='pipline'
URL='mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWD,DBIP,DBPORT,DBNAME)
DATABASE_DEBUG=True