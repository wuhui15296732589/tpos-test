import cx_Oracle



con = cx_Oracle.connect('POSP_ZXB','e7749cc','47.112.231.248:1621/ORCL','POSP_ZXB')
cursor = con.cursor()
cursor.execute('SELECT * FROM CIF_POS_CUS_RATE WHERE CUSTOMER_ID IN (7520,7573,7671,7677,7955)')
data = cursor.fetchone()
print(data)
cursor.close()
con.close()