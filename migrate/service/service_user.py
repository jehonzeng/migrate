from migrate import id_handler
from migrate.service import service_base, service_order, service_goods
from migrate.provider import provider_user


class User:

    # 操作无订单的用户
    @staticmethod
    def user_no_order():
        id_worker = id_handler.IdWorker()
        user_list = provider_user.User.select_old_user_no()
        new_user_list = []
        img_id_list = []
        user_id_map = {}
        for user_row in user_list:
            header_img = user_row[6]
            img_id_list.append(header_img)
        img_id_map = service_base.Base.user_img(img_id_list)
        for user_row in user_list:
            user_id = user_row[0]
            new_user_id = id_worker.get_id()
            user_id_map[user_id] = new_user_id
            header_img = user_row[6]
            new_header_img = None
            if header_img in img_id_map:
                new_header_img = img_id_map[header_img]
            new_user_list.append((new_user_id, user_row[1].replace('\\', '\\\\').replace('\"', '\\"'), '',
                                  user_row[2], new_header_img, None, user_row[3], user_row[9], user_row[8], user_row[4], user_row[7]))
        service_order.Order.user_coupon(user_id_map)
        service_order.Order.user_address(user_id_map)
        provider_user.User.insert_batch_new_user(new_user_list)
        return user_id_map

        # 操作有订单的用户
    @staticmethod
    def user_have_order():
        id_worker = id_handler.IdWorker()
        user_list = provider_user.User.select_old_user()
        new_user_list = []
        img_id_list = []
        user_id_map = {}
        for user_row in user_list:
            header_img = user_row[6]
            img_id_list.append(header_img)
        img_id_map = service_base.Base.user_img(img_id_list)
        for user_row in user_list:
            user_id = user_row[0]
            new_user_id = id_worker.get_id()
            user_id_map[user_id] = new_user_id
            header_img = user_row[6]
            new_header_img = None
            if header_img in img_id_map:
                new_header_img = img_id_map[header_img]
            new_user_list.append((new_user_id, user_row[1], '',
                              user_row[2], new_header_img, None,
                              user_row[3], user_row[9], user_row[8], user_row[4], user_row[7]))
        coupon_id_map = service_order.Order.user_coupon(user_id_map)
        service_order.Order.user_address(user_id_map)
        provider_user.User.insert_batch_new_user(new_user_list)  # 批量添加用户
        goods_id_map, accessory_id_map, meal_id_map, new_goods_list, new_accessory_list, new_meal_list = User.operate_goods()
        order_id_map = service_order.Order.user_order(user_id_map, coupon_id_map)
        service_order.Order.order_item(order_id_map, goods_id_map, meal_id_map, accessory_id_map, new_goods_list, new_accessory_list, new_meal_list)
        goods_id_map.update(accessory_id_map)
        goods_id_map.update(meal_id_map)
        service_goods.Goods.goods_judge(user_id_map, goods_id_map, order_id_map)
        service_goods.Goods.meal_judge(user_id_map, goods_id_map, order_id_map)
        return user_id_map, goods_id_map

    @staticmethod
    def operate_goods():
        goods_id_map, new_goods_list = service_goods.Goods.goods_info()
        service_goods.Goods.goods_content(goods_id_map)
        service_goods.Goods.goods_img(goods_id_map)
        accessory_id_map, new_accessory_list = service_goods.Goods.accessory_info()
        # goods_id_map.update(accessory_id_map)
        meal_id_map, new_meal_list = service_goods.Goods.meal_info()
        service_goods.Goods.meal_item(meal_id_map, goods_id_map)
        service_goods.Goods.meal_content(meal_id_map)
        service_goods.Goods.meal_img(meal_id_map)
        # goods_id_map.update(meal_id_map)
        return goods_id_map, accessory_id_map, meal_id_map, new_goods_list, new_accessory_list, new_meal_list