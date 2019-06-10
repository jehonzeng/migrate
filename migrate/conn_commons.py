from migrate import mysql_conn


class Commons:
    def __init__(self):
        self.old_host = 'localhost'
        self.old_user = 'root'
        self.old_passwd = '123456'
        self.old_db = 't_hands_formal'

        self.new_host = 'localhost'
        self.new_user = 'root'
        self.new_passwd = '123456'

        self.new_db_base = 'db_base'
        self.new_db_user = 'db_user'
        self.new_db_order = 'db_order'
        self.new_db_goods = 'db_goods'
        self.new_db_activity = 'db_activity'

    """旧数据库操作"""

    def select_old_data(self, sql, arg):
        conn_constructor = mysql_conn.MysqlOperate(self.old_host, self.old_user, self.old_passwd, self.old_db)
        return conn_constructor.search(sql, arg)

    """创建基础连接"""

    def create_new_conn(self, db):
        conn_constructor = mysql_conn.MysqlOperate(self.new_host, self.new_user, self.new_passwd, db)
        return conn_constructor

    """基础模块数据库操作"""

    def select_db_base(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_base)
        return conn_constructor.search(sql, arg)

    def insert_db_base(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_base)
        conn_constructor.insert(sql, arg)

    def insert_batch_db_base(self, sql, args):
        conn_constructor = self.create_new_conn(self.new_db_base)
        conn_constructor.insert_batch(sql, args)

    def update_db_base(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_base)
        conn_constructor.update(sql, arg)

    def delete_db_base(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_base)
        conn_constructor.delete(sql, arg)

    """订单模块数据库连接"""

    def select_db_order(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_order)
        return conn_constructor.search(sql, arg)

    def insert_db_order(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_order)
        conn_constructor.insert(sql, arg)

    def insert_batch_db_order(self, sql, args):
        conn_constructor = self.create_new_conn(self.new_db_order)
        conn_constructor.insert_batch(sql, args)

    def update_db_order(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_order)
        conn_constructor.update(sql, arg)

    def delete_db_order(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_order)
        conn_constructor.delete(sql, arg)

    """用户模块数据库连接"""

    def select_db_user(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_user)
        return conn_constructor.search(sql, arg)

    def insert_db_user(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_user)
        conn_constructor.insert(sql, arg)

    def insert_batch_db_user(self, sql, args):
        conn_constructor = self.create_new_conn(self.new_db_user)
        conn_constructor.insert_batch(sql, args)

    def update_db_user(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_user)
        conn_constructor.update(sql, arg)

    def delete_db_user(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_user)
        conn_constructor.delete(sql, arg)

    """商品模块数据库连接"""

    def select_db_goods(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_goods)
        return conn_constructor.search(sql, arg)

    def insert_db_goods(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_goods)
        conn_constructor.insert(sql, arg)

    def insert_batch_db_goods(self, sql, args):
        conn_constructor = self.create_new_conn(self.new_db_goods)
        conn_constructor.insert_batch(sql, args)

    def update_db_goods(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_goods)
        conn_constructor.insert(sql, arg)

    def delete_db_goods(self, sql, arg):
        conn_constructor = self.create_new_conn(self.new_db_goods)
        conn_constructor.delete(sql, arg)

if __name__=='__main__':
    comm = Commons()
    result = comm.select_old_data("select * from t_user_info")
    print(result)