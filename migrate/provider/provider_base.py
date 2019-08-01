from migrate import conn_commons


class Base:

    @staticmethod
    def select_old_img(img_ids_str):
        sql = "select * from t_image_info where mark_id in %s"
        img_conn = conn_commons.Commons()
        return img_conn.select_old_data(sql % img_ids_str, None)

    # @staticmethod
    # def insert_new_img(img):
    #     sql = """insert into t_image_info (mark_id,image_path,file_type) values (%s,%s,%s)"""
    #     img_conn = conn_commons.Commons()
    #     img_conn.insert_db_base(sql, img)

    @staticmethod
    def insert_batch_new_img(img_list):
        sql = """insert into t_image_info (mark_id,image_path,file_type) values (%s,%s,%s)"""
        img_conn = conn_commons.Commons()
        img_conn.insert_batch_db_base(sql, img_list)

    @staticmethod
    def select_old_accessory_img(goods_ids_str):
        sql = """SELECT i.*, A.goods_mark FROM t_image_info i LEFT JOIN (
                SELECT * FROM t_goods_image WHERE server_type=0 AND goods_mark IN %s) A ON i.mark_id = A.img_path WHERE A.mark_id IS NOT NULL"""
        img_conn = conn_commons.Commons()
        return img_conn.select_old_data(sql % goods_ids_str, None)

    @staticmethod
    def select_area():
        sql = """SELECT * FROM t_area_info"""
        area_conn = conn_commons.Commons()
        return area_conn.select_db_base(sql, None)

if __name__=='__main__':
    pass
