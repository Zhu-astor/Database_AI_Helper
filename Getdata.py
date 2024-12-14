import pymysql
import json
# 連結 SQL
import pymysql

# 連結 SQL
connect_db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', charset='utf8', db='dlmodel')

file = open("train_data.jsonl",'w',encoding="utf-8")
    
def getdata_from_database(instruction):
    # print("pass")
    with connect_db.cursor() as cursor:
        sql = instruction
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        print("getdata-------")
        return str(data)
    connect_db.close()
