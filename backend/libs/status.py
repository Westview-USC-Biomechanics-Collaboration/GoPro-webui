import json
from open_gopro import *
from connect import *


async def get_status_front():
    try:
        gopro = await get_front_gopro()
        ip_address = gopro.ip_address
        return {
            "status": 200,
            "ip_address": str(ip_address)
        }
    except Exception:
        return {
            "status": 500,
            "ip_address": ""
        }
    
async def get_status_short():
    try:
        gopro = await get_short_gopro()
        ip_address = gopro.ip_address
        return {
            "status": 200,
            "ip_address": str(ip_address)
        }
    except Exception:
        return {
            "status": 500,
            "ip_address": ""
        }
    
async def get_status_top():
    try:
        gopro = await get_top_gopro()
        ip_address = gopro.ip_address
        return {
            "status": 200,
            "ip_address": str(ip_address)
        }
    except Exception:
        return {
            "status": 500,
            "ip_address": ""
        }

async def get_status():
    top_status = await get_status_top()
    short_status = await get_status_short()
    front_status = await get_status_front()

    return {
        "front_camera_status": front_status["status"],
        "top_camera_status": short_status["status"],
        "short_camera_status": short_status["status"],

        "front_camera_ip": front_status["ip_address"],
        "top_camera_ip": top_status["ip_address"],
        "short_camera_ip": short_status["ip_address"],
    }
