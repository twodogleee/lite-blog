from dao import MenuDao
from entity.MenuEntity import DbMenu, Menu, MenuVo
from service import BasicService as basicService
import time


# 根据id查询菜单信息
def get_menu_by_id(id: int):
    return basicService.success(MenuDao.get_menu_by_id(id))


# 保存菜单信息
def save_menu(menu: Menu):
    menu.id = int(time.time())
    return basicService.success(True) if MenuDao.save_menu(DbMenu(**menu.dict())) else basicService.fail('操作失败')


# 删除菜单信息
def del_menu(id: int):
    return basicService.success(True) if MenuDao.del_menu(id) else basicService.fail('操作失败')


# 获取菜单集合
def get_menu_list():
    return basicService.success(MenuDao.get_menu_list())


# 修改菜单信息
def update_menu(menu: Menu):
    return basicService.success(True) if MenuDao.update_menu(DbMenu(**menu.dict())) else basicService.fail("操作失败")


# 获取树形结构的菜单
def get_menu_tree():
    menu_list = MenuDao.get_menu_list()
    menu_dict = {}
    menu_root = []

    # 将所有菜单按照id存储到字典中
    for menu in menu_list:
        menu_dict[menu.id] = MenuVo(menu)

    # 遍历每个菜单，将其添加到其父菜单的子节点中
    for menu in menu_list:
        if menu.sup_id == 0 or menu.level == 1:
            menu_root.append(menu_dict[menu.id])
        else:
            parent = menu_dict[menu.sup_id]
            parent.children.append(menu_dict[menu.id])
    return basicService.success(menu_root)
