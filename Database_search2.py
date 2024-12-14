import pymysql
import json
# 連結 SQL
import pymysql

# 連結 SQL
connect_db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', charset='utf8', db='dlmodel')

file = open("train_data2.jsonl",'w',encoding="utf-8")

size1 = "12x5x8"
age1 = "元朝"
random_number = "5"

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
    col = 0
    for row in data:
        print(col)
        col = col + 1
        name = row[0]
        number = row[1]
        age = row[2]
        type = row[3]
        size = row[4]
        boolean = row[5]
      # 打印结果
    #   print("name=%s"%name)
    #   print ("name=%s,number=%s,age=%s,type=%s,size=%s,boolean=%s"%(name, number, age, type, size,boolean ))
    

    

        # 單一條件查詢
        messages1 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品名稱為{name}的展品尺寸是什麼？"},
            {"role": "assistant", "content": f"SELECT 展品尺寸 FROM museumexhibits WHERE 展品名稱 = '{name}'"}
        ]

        messages2 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品名稱為{name}的展品年分是什麼？"},
            {"role": "assistant", "content": f"SELECT 展品年分 FROM museumexhibits WHERE 展品名稱 = '{name}'"}
        ]

        messages3 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品名稱為{name}的展品類型是什麼？"},
            {"role": "assistant", "content": f"SELECT 展品類型 FROM museumexhibits WHERE 展品名稱 = '{name}'"}
        ]

        messages4 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品名稱為{name}支援影像辨識模型嗎？"},
            {"role": "assistant", "content": f"SELECT 支援影像辨識模型 FROM museumexhibits WHERE 展品名稱 = '{name}'"}
        ]

        messages5 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品名稱為{name}的登錄號是什麼？"},
            {"role": "assistant", "content": f"SELECT 登陸號 FROM museumexhibits WHERE 展品名稱 = '{name}'"}
        ]

        # 查詢所有展品
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

        # 複合條件查詢
        messages10 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找登陸號為{number}且展品年分為{age}的展品是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 登陸號 = '{number}' AND 展品年分 = '{age}'"}
        ]

        messages11 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品類型為{type}且展品尺寸為{size}的所有展品是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 展品類型 = '{type}' AND 展品尺寸 = '{size}'"}
        ]

        messages12 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品名稱為{name}且支援影像辨識模型為{boolean}的資訊是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 展品名稱 = '{name}' AND 支援影像辨識模型 = '{boolean}'"}
        ]

        messages13 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品類型為{type}且展品年分為{age}的展品是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 展品類型 = '{type}' AND 展品年分 = '{age}'"}
        ]

        messages14 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品年分為{age}且展品名稱為{name}的資訊是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 展品年分 = '{age}' AND 展品名稱 = '{name}'"}
        ]

        # 範圍查詢
        messages15 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品尺寸範圍為{size}到{size1}的展品是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 展品尺寸 BETWEEN '{size}' AND '{size1}'"}
        ]

        messages16 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找展品年分範圍為{age}到{age1}的展品是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 展品年分 BETWEEN '{age}' AND '{age1}'"}
        ]

        # 排序查詢
        messages17 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表查詢所有展品，按展品年分降序排列，顯示前{random_number}個展品是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits ORDER BY 展品年分 DESC LIMIT {random_number}"}
        ]

        # 聚合查詢
        messages18 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表計算展品的總數是多少？"},
            {"role": "assistant", "content": "SELECT COUNT(*) FROM museumexhibits"}
        ]

        messages19 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表計算展品類型為{type}的總數是多少？"},
            {"role": "assistant", "content": f"SELECT COUNT(*) FROM museumexhibits WHERE 展品類型 = '{type}'"}
        ]

        messages20 = [
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": f"從museumexhibits資料表找登陸號為{number}且展品年分為{age}的是什麼？"},
            {"role": "assistant", "content": f"SELECT * FROM museumexhibits WHERE 登陸號 = '{number}' AND 展品年分 = '{age}'"}
        ]


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
        file.write(json.dumps({"messages": messages12}, ensure_ascii=False) + "\n")
        file.write(json.dumps({"messages": messages13}, ensure_ascii=False) + "\n")
        file.write(json.dumps({"messages": messages14}, ensure_ascii=False) + "\n")
        file.write(json.dumps({"messages": messages15}, ensure_ascii=False) + "\n")
        file.write(json.dumps({"messages": messages16}, ensure_ascii=False) + "\n")
        file.write(json.dumps({"messages": messages17}, ensure_ascii=False) + "\n")
        file.write(json.dumps({"messages": messages18}, ensure_ascii=False) + "\n")
        file.write(json.dumps({"messages": messages19}, ensure_ascii=False) + "\n")
        file.write(json.dumps({"messages": messages20}, ensure_ascii=False) + "\n")


        

# 關閉 SQL 連線
connect_db.close()
file.close()
