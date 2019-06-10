from migrate.service import service_user, service_goods, service_order

if __name__ == "__main__":
    user_id_map = service_user.User.user_no_order()
    user_id_map_have, goods_id_map = service_user.User.user_have_order()
    user_id_map.update(user_id_map_have)
    food_id_map = service_goods.Goods.food_info()
    service_goods.Goods.food_item(food_id_map, goods_id_map)
    service_goods.Goods.purchase_history(food_id_map, user_id_map)
    service_order.Order.back_history()
