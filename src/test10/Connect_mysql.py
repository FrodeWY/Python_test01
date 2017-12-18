import mysql.connector as connector


def connect():
    conn = connector.connect(user='root', password='123456', database='wangyang01', host='127.0.0.1', port='3306')
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()

    DB_NAME = 'EMPLOYEE'
    try:
        # cursor.execute('DROP TABLE IF EXISTS %s' % DB_NAME)
        # sql = "CREATE TABLE %s (id INT PRIMARY KEY,first_name VARCHAR(20),age INT(3),sex TINYINT)"
        # cursor.execute(sql % DB_NAME)
        sql2 = "INSERT INTO %s (id,first_name,age,sex) VALUES('%d','%s','%d','%d')"
        cursor.execute(sql2 % (DB_NAME, 3, "wy", 12, 1))
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    cursor.close()
    conn.close()


def select():
    conn=connector.connect(user='root',password='123456',database='wangyang01',host='127.0.0.1',port='3306')
    curse=conn.cursor()
    sql="select *  from EMPLOYEE a WHERE a.age='%d'"
    age=12
    curse.execute(sql %age)
    values=curse.fetchall()
    print(values)
    curse.close()
    conn.close



if __name__ == '__main__':
    connect()
    select()
