from migrate import conn_commons


class User:

    """查询旧数据库所有用户信息"""
    @staticmethod
    def select_old_user():
        sql = "select * from t_user_info where mark_id in (select user_mark from t_order_info)"
        user_conn = conn_commons.Commons()
        return user_conn.select_old_data(sql, None)

    @staticmethod
    def select_old_user_no():
        sql = "select * from t_user_info where mark_id not in (select user_mark from t_order_info)"
        user_conn = conn_commons.Commons()
        return user_conn.select_old_data(sql, None)

    # @staticmethod
    # def insert_new_user(param):
    #     sql = """insert into t_user_info(mark_id,nick_name,real_name,phone,header_img,gender,city,province,country,language,user_level,
    #               cook_level,wopen_id,xopen_id,union_id,create_time,wechat_status)
    #               values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    #     user_conn = conn_commons.Commons()
    #     user_conn.insert_db_user(sql, param)

    @staticmethod
    def insert_batch_new_user(user_list):
        sql = """insert into t_user_info(mark_id,nick_name,real_name,phone,header_img,gender,wopen_id,xopen_id,union_id,create_time,wechat_status) 
                          values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        user_conn = conn_commons.Commons()
        user_conn.insert_batch_db_user(sql, user_list)

    @staticmethod
    def select_old_address(user_ids_str):
        sql = """select * from t_address_info where user_mark in %s"""
        address_conn = conn_commons.Commons()
        return address_conn.select_old_data(sql % user_ids_str, None)

    @staticmethod
    def insert_batch_new_address(address_list):
        sql = """insert into t_user_address 
        (mark_id,user_name,phone,area,city,province,user_address,address_type,user_id,create_time,default_or,server_status)
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        address_conn = conn_commons.Commons()
        address_conn.insert_batch_db_order(sql, address_list)

if __name__=='__main__':
    result = User.select_old_user()
    print(result)
