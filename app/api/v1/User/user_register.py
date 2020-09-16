"""
yonghuzhuce

"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_user_html():
    pass


@router.post("/user/register/", summary="")
async def user_register():
    pass
