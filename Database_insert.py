import pymysql

batch_size=100
epoch=100
learning_rate=0.01
# 連結 SQL
connect_db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', charset='utf8', db='dlmodel')

with connect_db.cursor() as cursor:
    sql = """
    INSERT INTO museumexhibits (展品名稱,登陸號,展品年分,展品類型,展品尺寸,支援影像辨識模型) VALUES 
    ('蟠龍方壺','h0000286','春秋中期','銅器','88.8x45.6x35.8','Y'),
    ('獸形器座','h0000289','春秋中期','銅器','47x34x30','Y'),
    ('金柄銅短劍','h0000382','春秋','銅器','30.8x3.9x0.32','Y'),
    ('虎形尊','h0000282','春秋中期','銅器','35.8x21.9','Y'),
    ('三彩馬','h0000030','唐','陶器','74.8x73.5x38.4','Y'),
    ('三彩加藍人面鎮墓獸','90-00647','唐','陶器','127x57.2','Y'),
    ('畫琺瑯方盤','08482','民初','琺瑯','10x10x1.4','N'),
    ('燒泥模印菩薩長壽佛','07782','年代不明','陶器','4.5x3.2','N'),
    ('石灣日神','07025','清','陶器','93x42.5x43','N'),
    ('石刻送子觀音像','06898','北齊','石灰岩','15x21.5','N'),
    ('石雕天女散花','07031','清','白石','136x43','N'),
    ('浮雕石塊','07045','年代不明','玉石','121.5x27x11.5','N'),
    ('十字繡長命富貴紋煙草袋','101-00032','民初','編織','18.1x12.2','N'),
    ('銀鼎','06896','民國','群金','15.5x22','N'),
    ('燈','07041','其他','群金','88x38 (徑)','N'),
    ('鎏金佛','100-00058','北朝晚期','群金','3.7x10.6','N'),
    ('鐵釘','10092','清','群金','7.5','N'),
    ('銀鏤燒藍步搖','27460','清','群金','14x12x1','N'),
    ('木刻獅','06899','清','木','73x77x44','N'),
    ('木刻彌勒臥佛','07814','清','木','35x23x11','N'),
    ('竹雕水牛人物像','08460','民初','竹根','25x47.5','N'),
    ('黃楊木木雕如意','100-00054','清中期','竹木','26','N'),
    ('竹根雕壽星','08428','民初','竹根','29x57','N'),
    ('木刻孫中山先生像','10084','民國','木','97.2x74.5','N'),
    ('宮扇','30002','民國','木、紙','42.5x26','N'),
    ('楷書華嚴經摺扇','29920','民國','木、紙','30.5x49.5','N'),
    ('竹苞松茂窗門板','27430','清','木、玉','58x15.5','N'),
    ('竹苞松茂窗門板','102-00023','民初','竹木','26x63','N'),
    ('木刻太陽神像面具','30927','民國','木','36x33x9','N'),
    ('木刻佛像','10739','明','木','78x60.5','N'),
    ('七弦琴','31575','明','木','115x20x12.5','N'),
    ('山水摺扇','31676','民國','竹、紙','31.2x43.5x2.1','N'),
    ('或隱或現','32067','1970','竹木','108x36.7','N'),
    ('滿洲脛骨化石','06946','1943','牙骨','24x14.5x6.5','N'),
    ('宗喀巴','06929','清','銅器','15.9x12.8x9.9','N'),
    ('釋迦牟尼佛','06922','清','銅器','36x25.3x18.8','N'),
    ('銅佛','06930','清','銅器','9.3x7x4.9','N'),
    ('銅佛頭','06923','明','銅器','36.4x18.3x17.8','N'),
    ('觀音菩薩','07011','明','銅器','21.8x15.4x10.3','N'),
    ('銅爵','06886','西周早期','銅器','17.5x15.5x8.1','N'),
    ('銅小鑼','6925','清','銅器','20.1x20.4x2.7','N'),
    ('銅煙袋','06935','民國','銅器','29.5x14.4x3.9','N'),
    ('宣德爐','07001','清','銅器','11.5x8.7x12.4','N'),
    ('楚刀','08374','戰國','銅器','27.4x2','N'),
    ('帶鉤','08377','戰國','銅器','11.5x2.1x1.8','N'),
    ('銅瓶','07228','民國','銅器','30.1x14.8x11x8.5','N'),
    ('蕉葉紋銅香爐','08463','明','銅器','21.3x16.1x20.3','N'),
    ('轄','h0000360','春秋中期','印章','8','N'),
    ('蟠螭紋甬鐘','h0000329','春秋中期','印章','38.3x18x14.8','N'),
    ('龜紐紅白玉中官府印','07111','清','(未提供)','2.4x2.4x1.7','N'),
    ('戰國瓦紐銅印','08111','戰國','青銅','1.3x1.3x1','N'),
    ('瑪瑙章印材','07143','民國','印章','1.4x3.5','N'),
    ('瀛洲條墨','07147','(未提供)','雜項','6.1x2.8','N'),
    ('清黑墨','08306','清','雜項','6.1x3.4','N'),
    ('清黑墨','08308','清','雜項','6.3x2.2','N')
    """
            
# 執行 SQL 指令
    cursor.execute(sql)
            
# 提交至 SQL
    connect_db.commit()

# 關閉 SQL 連線
connect_db.close()

# sql = """
#     INSERT INTO reflectionremove (Dataset,Batch,Epoch,LearningRate,Attention) VALUES 
#     ('Datasettest',%s,%s,%s,'No attention in model architecture')
#     """