from migrate import conn_commons


class Order:

    @staticmethod
    def select_old_coupon(user_ids_str):
        sql = "select * from t_coupon_user where user_mark in %s"
        coupon_conn = conn_commons.Commons()
        return coupon_conn.select_old_data(sql % user_ids_str, None)

    @staticmethod
    def insert_batch_new_coupon(coupon_list):
        sql = """insert into t_user_coupon (mark_id,user_id,start_time,stop_time,use_time,limit_price,coupon_price,coupon_name,coupon_type) 
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        coupon_conn = conn_commons.Commons()
        coupon_conn.insert_batch_db_order(sql, coupon_list)

    @staticmethod
    def select_old_order(user_ids_str):
        sql = "select * from t_order_info where user_mark in %s"
        order_conn = conn_commons.Commons()
        return order_conn.select_old_data(sql % user_ids_str, None)

    @staticmethod
    def select_old_item(order_ids_str):
        sql = "select * from t_order_item where order_mark in %s"
        item_conn = conn_commons.Commons()
        return item_conn.select_old_data(sql % order_ids_str, None)

    @staticmethod
    def insert_new_order(order_list):
        sql = """insert into t_order_info (mark_id,order_no,user_id,order_amount,delivery_amount,pay_amount,order_time,
            pay_time,cancel_time,delivery_date,send_time,arrive_time,remark,order_type,order_status,coupon_id,order_source)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        order_conn = conn_commons.Commons()
        order_conn.insert_batch_db_order(sql, order_list)

    @staticmethod
    def insert_new_item(item_list):
        sql = """insert into t_order_item (mark_id,order_id,product_id,product_type,product_name,specification_ids,
        quantity,base_price,sale_price,pay_amount,coupon_id)
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        item_conn = conn_commons.Commons()
        item_conn.insert_batch_db_order(sql, item_list)

    @staticmethod
    def insert_new_delivery(delivery_list):
        sql = """insert into t_order_delivery (mark_id,order_id,contact,delivery_date,phone,delivery_address,delivery_area,remark,order_type)
                values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        delivery_conn = conn_commons.Commons()
        delivery_conn.insert_batch_db_order(sql, delivery_list)

    @staticmethod
    def select_old_back():
        sql = """select * from t_back_history"""
        back_conn = conn_commons.Commons()
        return back_conn.select_old_data(sql, None)

    @staticmethod
    def insert_batch_new_back(back_list):
        sql = """insert into t_back_history (mark_id,order_no,add_time,pay_status,cid)
                values (%s,%s,%s,%s,%s)"""
        back_conn = conn_commons.Commons()
        back_conn.insert_batch_db_order(sql, back_list)
