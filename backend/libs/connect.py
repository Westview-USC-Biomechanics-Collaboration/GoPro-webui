from open_gopro import *
from .conf import *
import json
import os

conf = get_conf()

async def get_front_gopro():
    gopro_front = WiredGoPro(conf["FRONT_CAMERA_SERIAL"])
    await gopro_front.open()
    return gopro_front

async def get_top_gopro():
    gopro_top = WiredGoPro(conf["TOP_CAMERA_SERIAL"])
    await gopro_top.open()
    return gopro_top

async def get_short_gopro():
    gopro_short = WiredGoPro(conf["SHORT_CAMERA_SERIAL"])
    await gopro_short.open()
    return gopro_short


