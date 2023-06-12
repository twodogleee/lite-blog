from entity.MenuEntity import Menu
from fastapi_utils.inferring_router import InferringRouter
from service import MenuService as menuService

# 生成路由 这个路由可以匹配返回的model不用手动申明
menuController = InferringRouter()


# 新增菜单
@menuController.post('/add')
async def add_menu(menu: Menu):
    return menuService.save_menu(menu)


# 根据id查询菜单信息
@menuController.get('/getMenuById/{id}')
async def get_menu_by_id(id: int):
    return menuService.get_menu_by_id(id)


# 删除菜单
@menuController.post('/delMenu/{id}')
async def del_menu(id: int):
    return menuService.del_menu(id)


@menuController.get('/getMenuList')
async def get_menu_list():
    return menuService.get_menu_list()
