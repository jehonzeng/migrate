from migrate import id_handler
from migrate.provider import provider_base


class Base:

    @staticmethod
    def user_img(img_id_list):
        id_worker = id_handler.IdWorker()
        img_list = provider_base.Base.select_old_img(str(tuple(img_id_list)))
        new_img_list = []
        img_id_map = {}
        for img_row in img_list:
            img_id = img_row[0]
            new_img_id = id_worker.get_id()
            img_id_map[img_id] = new_img_id
            img_path = img_row[1]
            new_img_list.append((new_img_id, img_path, img_path.split('.')[1]))
        provider_base.Base.insert_batch_new_img(new_img_list)
        return img_id_map

    @staticmethod
    def accessory_img(accessory_id_map):
        id_worker = id_handler.IdWorker()
        img_list = provider_base.Base.select_old_accessory_img(str(tuple(accessory_id_map)))
        new_img_list = []
        accessory_img_map = {}
        for img_row in img_list:
            img_id = img_row[0]
            new_img_id = id_worker.get_id()
            img_path = img_row[1]
            accessory_id = img_row[2]
            accessory_img_map[accessory_id] = new_img_id
            new_img_list.append((new_img_id, img_path, img_path.split('.')[1]))
        provider_base.Base.insert_batch_new_img(new_img_list)
        return accessory_img_map