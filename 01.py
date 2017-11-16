import pymysql.cursors

# Exemplo de um conexão com banco de dados

config = {'host': '192.168.1.20',
          'user': 'root',
          'password': '131970hc',
          'db': 'erphost_erpsp',
          'charset': 'utf8mb4',
          'cursorclass': pymysql.cursors.DictCursor}

connection = pymysql.connect(**config)
cursor = connection.cursor()
cursor.execute("select * from entidades")
recordset = cursor.fetchall()
for item in recordset:
    print(item)
