from migrate.provider import provider_goods
from migrate.service import service_base
from migrate import id_handler


class Goods:

    @staticmethod
    def goods_info():
        id_worker = id_handler.IdWorker()
        goods_list = provider_goods.Goods.select_old_goods(0)
        new_goods_list = []
        goods_id_map = {}
        for goods_row in goods_list:
            new_goods_id = id_worker.get_id()
            goods_id = goods_row[0]
            name = goods_row[1]
            cost_price = goods_row[2]
            base_price = goods_row[3]
            server_status = goods_row[5]  # 状态
            if server_status == 0:
                server_status = 'ZT03'
            else:
                server_status = 'ZT02'
            add_time = goods_row[10]
            description = goods_row[11]
            sort = goods_row[15]
            goods_id_map[goods_id] = new_goods_id
            new_goods_list.append(
                (new_goods_id, name, description, server_status, 0, cost_price / 100.00, base_price / 100.00, 'DW03',
                 add_time, sort))
        provider_goods.Goods.insert_batch_new_goods(new_goods_list)
        return goods_id_map, new_goods_list

    #  添加商品详情
    @staticmethod
    def goods_content(goods_id_map):
        id_worker = id_handler.IdWorker()
        content_list = provider_goods.Goods.select_old_content(str(tuple(goods_id_map)))
        new_content_list = []
        for content_row in content_list:
            content_id = content_row[0]
            goods_mark = content_row[1]
            content = content_row[2]
            new_content_list.append((id_worker.get_id(), goods_id_map[goods_mark], content))
        provider_goods.Goods.insert_batch_new_content(new_content_list)

    #  添加商品图片
    @staticmethod
    def goods_img(goods_id_map):
        id_worker = id_handler.IdWorker()
        img_list = provider_goods.Goods.select_old_img(str(tuple(goods_id_map)))
        path_id_list = []
        for img_row in img_list:
            img_path = img_row[4]
            path_id_list.append(img_path)
        path_id_map = service_base.Base.user_img(path_id_list)
        new_img_list = []
        for img_row in img_list:
            server_type = img_row[1]
            type = None
            if server_type == 0:
                type = 2
            elif server_type == 1:
                type = 1
            elif server_type == 2:
                type = 0
            else:
                continue
            sort = img_row[2]
            goods_mark = img_row[3]
            img_path = img_row[4]
            new_img_list.append((id_worker.get_id(), goods_id_map[goods_mark], path_id_map[img_path], type, sort))
        provider_goods.Goods.insert_batch_new_img(new_img_list)

    @staticmethod
    def goods_judge(user_id_map, goods_id_map, order_id_map):
        id_worker = id_handler.IdWorker()
        judge_list = provider_goods.Goods.select_old_judge(str(tuple(goods_id_map)))
        new_judge_list = []
        for judge_row in judge_list:
            add_time = judge_row[1]
            server_status = judge_row[2]
            star = judge_row[3]
            sort = judge_row[4]
            description = judge_row[5]
            goods_mark = judge_row[6]
            goods_id = None
            if goods_mark in goods_id_map:
                goods_id = goods_id_map[goods_mark]
            else:
                continue
            user_mark = judge_row[7]
            user_id = None
            if user_mark in user_id_map:
                user_id = user_id_map[user_mark]
            order_mark = judge_row[8]
            order_id = None
            if order_mark in order_id_map:
                order_id = order_id_map[order_mark]
            new_judge_list.append((id_worker.get_id(), goods_id, order_id,user_id, server_status, description, None, add_time, star, sort))
        provider_goods.Goods.insert_batch_new_judge(new_judge_list)

    @staticmethod
    def accessory_info():
        id_worker = id_handler.IdWorker()
        accessory_list = provider_goods.Goods.select_old_goods(1)
        accessory_id_list = []
        for accessory_row in accessory_list:
            accessory_id_list.append(accessory_row[0])
        accessory_img_map = service_base.Base.accessory_img(str(tuple(accessory_id_list)))
        new_accessory_list = []
        accessory_id_map = {}
        for accessory_row in accessory_list:
            new_accessory_id = id_worker.get_id()
            accessory_id = accessory_row[0]
            accessory_id_map[accessory_id] = new_accessory_id
            name = accessory_row[1]
            cost_price = accessory_row[2]
            base_price = accessory_row[3]
            server_type = 1
            if base_price > 0:
                server_type = 0
            server_status = accessory_row[5]  # 状态
            if server_status != 0:
                server_status = 1
            description = accessory_row[11]
            stock_size = accessory_row[12]
            sort = accessory_row[15]
            image_path = None
            if accessory_id in accessory_img_map:
                image_path = accessory_img_map[accessory_id]
            new_accessory_list.append(
                (new_accessory_id, name,server_type, server_status, cost_price / 100.00, base_price / 100.00, description, stock_size,
                 image_path, sort))
        provider_goods.Goods.insert_batch_new_accessory(new_accessory_list)
        return accessory_id_map, new_accessory_list

    @staticmethod
    def meal_info():
        id_worker = id_handler.IdWorker()
        meal_list = provider_goods.Goods.select_old_goods(2)
        new_meal_list = []
        meal_id_map = {}
        for meal_row in meal_list:
            new_meal_id = id_worker.get_id()
            meal_id = meal_row[0]
            meal_id_map[meal_id] = new_meal_id
            name = meal_row[1]
            cost_price = meal_row[2]
            base_price = meal_row[3]
            server_status = meal_row[5]
            if server_status != 0:
                server_status = 1
            description = meal_row[11]
            stock_size = meal_row[12]
            sort = meal_row[15]
            new_meal_list.append((
                new_meal_id, name, cost_price / 100.00, base_price / 100.00, stock_size, server_status,
                description, sort))
        provider_goods.Goods.insert_batch_new_meal(new_meal_list)
        return meal_id_map, new_meal_list

    @staticmethod
    def meal_item(meal_id_map, goods_id_map):
        id_worker = id_handler.IdWorker()
        item_list = provider_goods.Goods.select_old_meal_item(str(tuple(meal_id_map)))
        new_item_list = []
        for item_row in item_list:
            mark_id = item_row[0]
            goods_mark = item_row[1]
            meal_mark = item_row[2]
            quantity = item_row[3]
            sort = item_row[4]
            new_item_list.append((id_worker.get_id(), meal_id_map[meal_mark], goods_id_map[goods_mark], quantity, sort))
        provider_goods.Goods.insert_batch_new_meal_item(new_item_list)

    @staticmethod
    def meal_content(meal_id_map):
        id_worker = id_handler.IdWorker()
        content_list = provider_goods.Goods.select_old_content(str(tuple(meal_id_map)))
        new_content_list = []
        for content_row in content_list:
            content_id = content_row[0]
            goods_mark = content_row[1]
            content = content_row[2]
            new_content_list.append((id_worker.get_id(), content, meal_id_map[goods_mark]))
        provider_goods.Goods.insert_batch_new_meal_content(new_content_list)

    @staticmethod
    def meal_img(meal_id_map):
        id_worker = id_handler.IdWorker()
        img_list = provider_goods.Goods.select_old_img(str(tuple(meal_id_map)))
        path_id_list = []
        for img_row in img_list:
            img_path = img_row[4]
            path_id_list.append(img_path)
        path_id_map = service_base.Base.user_img(path_id_list)
        new_img_list = []
        for img_row in img_list:
            server_type = img_row[1]
            type = None
            if server_type == 0:
                type = 2
            elif server_type == 1:
                type = 1
            elif server_type == 2:
                type = 0
            else:
                continue
            sort = img_row[2]
            goods_mark = img_row[3]
            img_path = img_row[4]
            new_img_list.append((id_worker.get_id(), meal_id_map[goods_mark], type, path_id_map[img_path], sort))
        provider_goods.Goods.insert_batch_new_meal_img(new_img_list)

    @staticmethod
    def meal_judge(user_id_map, meal_id_map, order_id_map):
        id_worker = id_handler.IdWorker()
        judge_list = provider_goods.Goods.select_old_judge(str(tuple(meal_id_map)))
        new_judge_list = []
        for judge_row in judge_list:
            add_time = judge_row[1]
            server_status = judge_row[2]
            star = judge_row[3]
            sort = judge_row[4]
            description = judge_row[5]
            goods_mark = judge_row[6]
            if not goods_mark in meal_id_map:
                continue
            user_mark = judge_row[7]
            user_id = None
            if user_mark in user_id_map:
                user_id = user_id_map[user_mark]
            order_mark = judge_row[8]
            order_id = None
            if order_mark in order_id_map:
                order_id = order_id_map[order_mark]
            new_judge_list.append((id_worker.get_id(), order_id, meal_id_map[goods_mark],
                                   user_id, add_time, server_status, description, None, star, sort))
        provider_goods.Goods.insert_batch_new_meal_judge(new_judge_list)

    @staticmethod
    def food_info():
        id_worker = id_handler.IdWorker()
        food_list = provider_goods.Goods.select_old_food()
        img_id_list = []
        for food_row in food_list:
            if food_row[4] is not None:
                img_id_list.append(food_row[4])
        img_id_map = {}
        if len(img_id_list):
            img_id_map = service_base.Base.user_img(img_id_list)
        new_food_list = []
        food_id_map = {}
        for food_row in food_list:
            food_id = food_row[0]
            new_food_id = id_worker.get_id()
            food_id_map[food_id] = new_food_id
            name = food_row[1]
            base_size = food_row[2]
            unit_name = food_row[3]
            lab_path = food_row[4]
            img_path = None
            if lab_path in img_id_map:
                img_path = img_id_map[lab_path]
            new_food_list.append((new_food_id,name,1,base_size / 100.00,unit_name,img_path))
        provider_goods.Goods.insert_batch_new_food(new_food_list)
        return food_id_map

    @staticmethod
    def food_item(food_id_map, goods_id_map):
        id_worker = id_handler.IdWorker()
        item_list = provider_goods.Goods.select_old_food_item()
        new_item_list = []
        for item_row in item_list:
            item_id = item_row[0]
            food_mark = item_row[1]
            food_id = None
            if food_mark in food_id_map:
                food_id = food_id_map[food_mark]
            else:
                continue
            goods_mark = item_row[2]
            good_id = None
            if goods_mark in goods_id_map:
                good_id = goods_id_map[goods_mark]
            else:
                continue
            use_size = item_row[3]
            new_item_list.append((id_worker.get_id(),food_id,good_id,None,use_size/100.00,1))
        provider_goods.Goods.insert_batch_new_food_item(new_item_list)

    @staticmethod
    def purchase_history(food_id_map, user_id_map):
        id_worker = id_handler.IdWorker()
        purchase_list = provider_goods.Goods.select_old_purchase()
        new_purchase_list = []
        for purchase_row in purchase_list:
            mark_id = purchase_row[0]
            food_mark = purchase_row[1]
            food_id = None
            if food_mark in food_id_map:
                food_id = food_id_map[food_mark]
            else:
               continue
            buy_total = purchase_row[2]
            buy_time = purchase_row[3]
            user_mark = purchase_row[4]
            user_id = None
            if user_mark in user_id_map:
                user_id = user_id_map[user_mark]
            new_purchase_list.append((id_worker.get_id(),food_id,buy_total/100.00,buy_time,user_id))
        provider_goods.Goods.insert_batch_new_purchase(new_purchase_list)




