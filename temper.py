import mysql.connector

conn= mysql.connector.connect(host='10.0.0.17' ,user='temper' ,password='temper' ,db='test')

a= conn.cursor()

sql = "INSERT INTO tempsense (temp, stamp, host) VALUES ('80', '2018-06-19 9:11:25', 'livingroom')"

countrow = a.execute(sql)
