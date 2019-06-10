import pymysql
from migrate import id_handler


class MysqlOperate:

    def __init__(self, host='localhost', user='root', passwd='123456', db='t_hands_formal'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

    def search(self, sql, arg):
        conn = pymysql.connect(host=str(self.host), port=3306, user=str(self.user), passwd=str(self.passwd),
                               db=str(self.db),
                               charset="utf8mb4")
        cur = conn.cursor()
        try:
            cur.execute(sql, arg)
            result = cur.fetchall()
        except Exception as err:
            print("MySQL Error: unable to fecth data of station_stock " + err)
            result = ()
        cur.close()
        conn.close()
        return result

    def insert(self, sql, arg):
        conn = pymysql.connect(host=str(self.host), port=3306, user=str(self.user), passwd=str(self.passwd),
                               db=str(self.db),
                               charset="utf8mb4")
        cur = conn.cursor()
        try:
            cur.execute(sql, arg)
            cur.close()
            conn.commit()
            conn.close()
        except Exception as err:
            print("MySQL Error :unable to insert data " + err)

    def insert_batch(self, sql, args):
        conn = pymysql.connect(host=str(self.host), port=3306, user=str(self.user), passwd=str(self.passwd),
                               db=str(self.db),
                               charset="utf8mb4")
        cur = conn.cursor()
        try:
            cur.executemany(sql, args)
            cur.close()
            conn.commit()
            conn.close()
        except Exception as err:
            print("MySQL Error :unable to insert data " + err)

    def update(self, sql, arg):
        conn = pymysql.connect(host=str(self.host), port=3306, user=str(self.user), passwd=str(self.passwd),
                               db=str(self.db),
                               charset="utf8mb4")
        cur = conn.cursor()
        try:
            cur.execute(sql, arg)
            cur.close()
            conn.commit()
            conn.close()
        except:
            print("MySQL Error :unable to update data")

    def delete(self, sql, arg):
        conn = pymysql.connect(host=str(self.host), port=3306, user=str(self.user), passwd=str(self.passwd),
                               db=str(self.db),
                               charset="utf8")
        cur = conn.cursor()
        try:
            cur.execute(sql, arg)
            cur.close()
            conn.commit()
            conn.close()
        except Exception as err:
            print("MySQL Error :unable to delete data " + err)


if __name__ == "__main__":
    id_worker = id_handler.IdWorker()
    mysql_operate = MysqlOperate('localhost', 'root', '123456', 't_hands_formal')
    # result = mysqloperate.execute_select_all('select * from t_order_info')
    # for row in result:
    #     print(row)
    #     print(id_worker.get_id('jenho'))
    result = mysql_operate.search(
        "select * from t_order_info where mark_id='fffe4b2f-d69a-4dc5-b0b9-b63c439dd3b3'")
    print(result)
