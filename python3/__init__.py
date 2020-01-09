import pymysql

db = pymysql.connect("127.0.0.1", "root", "123456", "python3", port=3306, charset='utf8')
cursor = db.cursor()
# 创建sql
sql = '''CREATE TABLE IF NOT EXISTS user (
         id bigint(20) NOT NULL AUTO_INCREMENT,
         name  CHAR(20),
         age INT,  
         sex CHAR(1),
         salary FLOAT, 
         PRIMARY KEY (id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4'''
try:
    cursor.execute(sql)
except Exception as e:
    db.rollback()  # 如果出错就回滚并且抛出错误收集错误信息。
    print("Error!:{0}".format(e))
finally:
    db.close()
