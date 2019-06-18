#encoding=utf8

import MySQLdb
try:
        con =MySQLdb.connect(
                host = "主机ID",
                port = 3306,
                user = "数据库用户名",
                db = '数据库名',
                passwd = "数据库密码",
                charset = 'utf8')
        chaxun = con.cursor()
        chaxun.execute("SELECT VERSION()")
        chaxun.execute("DROP TABLE IF EXISTS EMPLOYEE")
        print('创建EMPLOYEE数据表')
        print('创建完成，开始写入表头')
        sql = """CREATE TABLE EMPLOYEE (
                 FIRST_NAME  CHAR(20) NOT NULL,
                 LAST_NAME  CHAR(20),
                 AGE INT,  
                 SEX CHAR(1),
                 INCOME FLOAT )"""
        chaxun.execute(sql)
        print('写入数据表头完成')
        print('开始写入数据')
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
                 LAST_NAME, AGE, SEX, INCOME)
                 VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        try:
            # 执行sql语句
            chaxun.execute(sql)
            # 提交到数据库执行
            con.commit()
        except:
            # Rollback in case there is any error
            con.rollback()
        print('写入数据完成')
        print('读取中')
        rest = chaxun.fetchone()
        jieguo = chaxun.execute('SELECT * FROM `EMPLOYEE`')
        print(rest)
        print('读取完毕')
        con.close()
except MySQLdb.Error as e:
    print('error : %s'%e)
