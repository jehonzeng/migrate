from migrate import conn_commons


class Goods:
    @staticmethod
    def select_old_goods(server_type):
        sql = "select * from t_goods_info where server_type=%s"
        goods_conn = conn_commons.Commons()
        return goods_conn.select_old_data(sql, server_type)

    @staticmethod
    def select_old_content(goods_ids_str):
        sql = "select * from t_goods_content where goods_mark in %s"
        content_conn = conn_commons.Commons()
        return content_conn.select_old_data(sql % goods_ids_str, None)

    @staticmethod
    def select_old_img(goods_ids_str):
        sql = "select * from t_goods_image where goods_mark in %s"
        img_conn = conn_commons.Commons()
        return img_conn.select_old_data(sql % goods_ids_str, None)

    @staticmethod
    def select_old_judge(goods_ids_str):
        sql = "select * from t_goods_judge where goods_mark in %s"
        judge_conn = conn_commons.Commons()
        return judge_conn.select_old_data(sql % goods_ids_str, None)

    @staticmethod
    def select_old_meal_item(meal_ids_str):
        sql = """select * from t_meal_item where meal_mark in %s"""
        item_conn = conn_commons.Commons()
        return item_conn.select_old_data(sql % meal_ids_str, None)

    @staticmethod
    def insert_batch_new_goods(goods_list):
        sql = """insert into t_goods_info (mark_id,goods_name,description,server_status,server_type,base_price,sale_price,unit,create_time,sort)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        goods_conn = conn_commons.Commons()
        goods_conn.insert_batch_db_goods(sql, goods_list)

    @staticmethod
    def insert_batch_new_content(content_list):
        sql = """insert into t_goods_content (mark_id,goods_id,content) values (%s,%s,%s)"""
        content_conn = conn_commons.Commons()
        content_conn.insert_batch_db_goods(sql, content_list)

    @staticmethod
    def insert_batch_new_img(img_list):
        sql = """insert into t_goods_image (mark_id,goods_id,image_path,server_type,sort)
        values (%s,%s,%s,%s,%s)"""
        img_conn = conn_commons.Commons()
        img_conn.insert_batch_db_goods(sql, img_list)

    @staticmethod
    def insert_batch_new_judge(judge_list):
        sql = """insert into t_goods_judge (mark_id,goods_id,order_id,user_id,server_status,description,commentator,add_time,star,sort)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        judge_conn = conn_commons.Commons()
        judge_conn.insert_batch_db_goods(sql, judge_list)

    @staticmethod
    def insert_batch_new_accessory(accessory_list):
        sql = """insert into t_accessory_info (mark_id,theme,server_type,server_status,base_price,sale_price,description,stock_size,image_path,sort)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        accessory_conn = conn_commons.Commons()
        accessory_conn.insert_batch_db_goods(sql, accessory_list)

    @staticmethod
    def insert_batch_new_meal(meal_list):
        sql = """insert into t_meal_info (mark_id,theme,base_price,sale_price,stock_size,server_status,description,sort)
            values (%s,%s,%s,%s,%s,%s,%s,%s)"""
        meal_conn = conn_commons.Commons()
        meal_conn.insert_batch_db_goods(sql, meal_list)

    @staticmethod
    def insert_batch_new_meal_item(item_list):
        sql = """insert into t_meal_item (mark_id,meal_id,goods_id,quantity,sort) values (%s,%s,%s,%s,%s)"""
        item_conn = conn_commons.Commons()
        item_conn.insert_batch_db_goods(sql, item_list)

    @staticmethod
    def insert_batch_new_meal_content(content_list):
        sql = """insert into t_meal_content (mark_id,content,meal_id) values (%s,%s,%s)"""
        content_conn = conn_commons.Commons()
        content_conn.insert_batch_db_goods(sql, content_list)

    @staticmethod
    def insert_batch_new_meal_img(img_list):
        sql = """insert into t_meal_image (mark_id,meal_id,server_type,image_path,sort) values (%s,%s,%s,%s,%s)"""
        img_conn = conn_commons.Commons()
        img_conn.insert_batch_db_goods(sql, img_list)

    @staticmethod
    def insert_batch_new_meal_judge(judge_list):
        sql = """insert into t_meal_comment (mark_id,order_id,meal_id,user_id,add_time,server_status,description,commentator,star,sort)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        judge_conn = conn_commons.Commons()
        judge_conn.insert_batch_db_goods(sql, judge_list)

    @staticmethod
    def select_old_food():
        sql = """select * from t_food_info"""
        food_conn = conn_commons.Commons()
        return food_conn.select_old_data(sql, None)

    @staticmethod
    def insert_batch_new_food(food_list):
        sql = """insert into t_food_info (mark_id,food_name,server_status,purchase_rate,unit,image_path)
                values (%s,%s,%s,%s,%s,%s)"""
        food_conn = conn_commons.Commons()
        food_conn.insert_batch_db_goods(sql, food_list)

    @staticmethod
    def select_old_food_item():
        sql = """select * from t_food_item"""
        item_conn = conn_commons.Commons()
        return item_conn.select_old_data(sql, None)

    @staticmethod
    def insert_batch_new_food_item(item_list):
        sql = """insert into t_food_item (mark_id,food_id,goods_id,specification_ids,use_size,server_status)
            values (%s,%s,%s,%s,%s,%s)"""
        item_conn = conn_commons.Commons()
        item_conn.insert_batch_db_goods(sql, item_list)

    @staticmethod
    def select_old_purchase():
        sql = """select * from t_purchase_history"""
        purchase_conn = conn_commons.Commons()
        return purchase_conn.select_old_data(sql, None)

    @staticmethod
    def insert_batch_new_purchase(purchase_list):
        sql = """insert into t_purchase_history (mark_id,food_id,buy_total,buy_time,user_id)
            values (%s,%s,%s,%s,%s)"""
        purchase_conn = conn_commons.Commons()
        purchase_conn.insert_batch_db_goods(sql, purchase_list)
