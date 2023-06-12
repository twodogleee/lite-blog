from dao import MenuDao
from entity.MenuEntity import DbMenu, Menu
from service import BasicService as basicService
import time


def get_menu_by_id(id: int):
    return basicService.success(MenuDao.get_menu_by_id(id))


def save_menu(menu: Menu):
    menu.id = int(time.time())
    return basicService.success(True) if MenuDao.save_menu(DbMenu(**menu.dict())) else basicService.fail('操作失败')


def del_menu(id: int):
    return basicService.success(True) if MenuDao.del_menu(id) else basicService.fail('操作失败')


def get_menu_list():
    return basicService.success(MenuDao.get_menu_list())
