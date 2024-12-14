import pymysql
import json
# 連結 SQL
import pymysql

# 連結 SQL
connect_db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', charset='utf8', db='dlmodel')

file = open("train_data.jsonl",'w',encoding="utf-8")


with connect_db.cursor() as cursor:
    sql = """
    SELECT * from museumexhibits
    """
    sql1 = """
    SELECT 展品尺寸 FROM museumexhibits WHERE 展品類型 = '銅器'
    """
    # 執行 SQL 指令
    cursor.execute(sql)
    
    # 取出全部資料
    data = cursor.fetchall()
    for row in data:
      name = row[0]
      number = row[1]
      age = row[2]
      type = row[3]
      size = row[4]
      boolean = row[5]
      # 打印结果
    #   print("name=%s"%name)
    #   print ("name=%s,number=%s,age=%s,type=%s,size=%s,boolean=%s"%(name, number, age, type, size,boolean ))
    
    ###找展品的甚麼
      messages = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品名稱為{name}的展品尺寸是什麼？"},
            {"role": "assistant", "content": f"SELECT 展品尺寸 FROM museumexhibits WHERE 展品名稱 = '{name}'"}
        ]
      messages1 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品名稱為{name}的展品年分是什麼？"},
            {"role": "assistant", "content": f"SELECT 展品年分 FROM museumexhibits WHERE 展品名稱 = '{name}'"}
        ]
      messages2 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品名稱為{name}的展品類型是什麼？"},
            {"role": "assistant", "content": f"SELECT 展品類型 FROM museumexhibits WHERE 展品名稱 = '{name}'"}
        ]
      messages3 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品名稱為{name}支援影像辨識模型嗎？"},
            {"role": "assistant", "content": f"SELECT 支援影像辨識模型 FROM museumexhibits WHERE 展品名稱 = '{name}'"}
        ]
      messages4 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品名稱為{name}的登錄號是什麼？"},
            {"role": "assistant", "content": f"SELECT 登陸號 FROM museumexhibits WHERE 展品名稱 = '{name}'"}
        ]
      messages5 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品名稱為{name}的所有資訊是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 展品名稱 = '{name}'"}
        ]
      ###找全部
      messages6 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品類型為{type}的所有展品是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 展品類型 = '{type}'"}
        ]
      messages7 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品年分為{age}的所有展品是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 展品年分 = '{age}'"}
        ]
      messages8 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找支援影像辨識模型為{boolean}的所有展品是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 支援影像辨識模型 = '{boolean}'"}
        ]
      messages9 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找登陸號為{number}的所有資訊是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 登陸號 = '{number}'"}
        ]
      ###A且B
      messages10 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找登陸號為{number}且展品年分為{age}的展品是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 登陸號 = '{number}' AND 展品年分 = '{age}';"}
        ]
      messages11 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品類型為{type}且展品尺寸為{size}的所有展品是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 展品類型 = '{type}' AND 展品尺寸 = '{size}';"}
        ]
    
      file.write(json.dumps({"messages": messages}, ensure_ascii=False) + "\n")
      file.write(json.dumps({"messages": messages1}, ensure_ascii=False) + "\n")
      file.write(json.dumps({"messages": messages2}, ensure_ascii=False) + "\n")
      file.write(json.dumps({"messages": messages3}, ensure_ascii=False) + "\n")
      file.write(json.dumps({"messages": messages4}, ensure_ascii=False) + "\n")
      file.write(json.dumps({"messages": messages5}, ensure_ascii=False) + "\n")
      file.write(json.dumps({"messages": messages6}, ensure_ascii=False) + "\n")
      file.write(json.dumps({"messages": messages7}, ensure_ascii=False) + "\n")
      file.write(json.dumps({"messages": messages8}, ensure_ascii=False) + "\n")
      file.write(json.dumps({"messages": messages9}, ensure_ascii=False) + "\n")
      file.write(json.dumps({"messages": messages10}, ensure_ascii=False) + "\n")
      file.write(json.dumps({"messages": messages11}, ensure_ascii=False) + "\n")


        

# 關閉 SQL 連線
connect_db.close()
file.close()
