"""
这是一个测试Controller
"""

from fastapi import APIRouter

import service.TestService as testService

testController = APIRouter()


# 这是一个测试接口
@testController.get("/test/{name}")
async def test(name: str):
    return testService.test1(name)
