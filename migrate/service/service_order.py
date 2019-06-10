from migrate.provider import provider_order
from migrate import id_handler


class Order:

    @staticmethod
    def user_coupon(user_id_map):
        id_worker = id_handler.IdWorker()
        coupon_list = provider_order.Order.select_old_coupon(str(tuple(user_id_map)))
        new_coupon_list = []
        coupon_id_map = {}
        for coupon_row in coupon_list:
            coupon_id = coupon_row[0]
            name = coupon_row[1]
            user_mark = coupon_row[2]
            create_time = coupon_row[3]
            use_time = coupon_row[4]
            use_time = use_time
            end_time = coupon_row[5]
            limit_size = coupon_row[6]
            coupon_size = coupon_row[7]
            new_coupon_id = id_worker.get_id()
            coupon_id_map[coupon_id] = new_coupon_id
            new_coupon_list.append((new_coupon_id, user_id_map[user_mark], create_time, end_time,
                                    use_time, limit_size / 100.00, coupon_size / 100.00, name, 1))
        provider_order.Order.insert_batch_new_coupon(new_coupon_list)
        return coupon_id_map

    # 操作用户订单
    @staticmethod
    def user_order(user_id_map, coupon_id_map):
        id_worker = id_handler.IdWorker()
        order_list = provider_order.Order.select_old_order(str(tuple(user_id_map)))
        new_order_list = []
        order_id_map = {}
        new_delivery_list = []
        for order_row in order_list:
            new_order_id = id_worker.get_id()
            order_id = order_row[0]
            order_id_map[order_id] = new_order_id
            order_no = order_row[1]
            add_time = order_row[2]
            cannel_time = order_row[3]
            delivery_time = order_row[4]
            arrive_time = order_row[5]
            remark = order_row[6]
            user_mark = order_row[7]
            base_price = order_row[8]
            pay_price = order_row[9]
            freight_price = order_row[10]
            server_status = order_row[11]
            server_type = order_row[12]
            pay_type = order_row[13]
            if server_type == 0 or server_type == 1 or server_type == 2:
                order_type = 1
            else:
                order_type = 2
            client_status = order_row[14]
            user_coupon_mark = order_row[19]
            coupon_id = None
            if user_coupon_mark in coupon_id_map:
                coupon_id = coupon_id_map[user_coupon_mark]
            order_source = order_row[20]
            pay_time = None
            cancel_time = None
            if server_status == 0:
                cancel_time = cannel_time
            else:
                pay_time = cannel_time
            order_status = None
            if server_status == -3:
                order_status = 'OT11'
            elif server_status == -2:
                order_status = 'OT09'
            elif server_status == -1:
                order_status = 'OT07'
            elif server_status == 0 and cannel_time is not None:
                order_status = 'OT10'
            elif server_status == 0:
                order_status = 'OT01'
            elif server_status == 1:
                order_status = 'OT02'
            elif server_status == 2:
                order_status = 'OT03'
            elif server_status == 3:
                order_status = 'OT04'
            elif server_status == 4:
                order_status = 'OT05'
            elif server_status == 5:
                order_status = 'OT06'
            new_order_list.append((new_order_id, order_no, user_id_map[user_mark], base_price / 100.00,
                                   freight_price / 100.00, (pay_price + freight_price) / 100.00,
                                   add_time, pay_time, cancel_time, delivery_time, None, arrive_time, remark,
                                   order_type, order_status, coupon_id, order_source))
            user_address = order_row[15]
            user_name = order_row[16]
            user_area = order_row[17]
            user_phone = order_row[18]
            new_delivery_list.append((id_worker.get_id(), new_order_id, user_name, delivery_time, user_phone,
                                      user_address, user_area, remark, 0))
        provider_order.Order.insert_new_order(new_order_list)
        provider_order.Order.insert_new_delivery(new_delivery_list)
        return order_id_map

    @staticmethod
    def order_item(order_id_map, goods_id_map, meal_id_map, accessory_id_map, new_goods_list, new_accessory_list, new_meal_list):
        id_worker = id_handler.IdWorker()
        item_list = provider_order.Order.select_old_item(str(tuple(order_id_map)))
        new_item_list = []
        for item_row in item_list:
            mark_id = item_row[0]
            order_mark = item_row[1]
            goods_mark = item_row[2]
            if goods_mark in goods_id_map:
                product_id = goods_id_map[goods_mark]
                product_type = 0
                for goods_row in new_goods_list:
                    if goods_row[0] == product_id:
                        product_name = goods_row[1]
                        break
            elif goods_mark in accessory_id_map:
                product_id = accessory_id_map[goods_mark]
                product_type = 3
                for accessory_row in new_accessory_list:
                    if accessory_row[1] == product_id:
                        product_name = accessory_row[1]
                        break
            elif goods_mark in meal_id_map:
                product_id = meal_id_map[goods_mark]
                product_type = 2
                for meal_row in new_meal_list:
                    if meal_row[0] == product_id:
                        product_name = meal_row[1]
                        break
            quantity = item_row[3]
            pay_price = item_row[4]
            base_price = item_row[5]
            cost_price = item_row[6]
            exchange_mark = item_row[7]
            coupon_count = item_row[8]
            new_item_list.append(
                (id_worker.get_id(), order_id_map[order_mark], product_id, product_type, product_name, None, quantity,
                 cost_price / 100.00, base_price / 100.00, pay_price / 100.00, exchange_mark))
        provider_order.Order.insert_new_item(new_item_list)

    @staticmethod
    def back_history():
        id_worker = id_handler.IdWorker()
        back_list = provider_order.Order.select_old_back()
        new_back_list = []
        for back_row in back_list:
            mark_id = back_row[0]
            order_no = back_row[1]
            add_time = back_row[2]
            pay_status = back_row[3]
            cid = back_row[4]
            new_back_list.append((id_worker.get_id(),order_no,add_time,pay_status,cid))
        provider_order.Order.insert_batch_new_back(new_back_list)
