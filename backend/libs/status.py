import json
from open_gopro import *
from .connect import *


async def get_status_front(CameraManager):
    try:
        gopro = CameraManager.front_gopro
        ip_address = gopro.ip_address
        if ip_address == "":
            return {
                "status": 500,
                "ip_address": ""
            }
        return {
            "status": 200,
            "ip_address": str(ip_address)
        }
    except Exception:
        return {
            "status": 500,
            "ip_address": ""
        }
    
async def get_status_short(CameraManager):
    try:
        gopro = CameraManager.short_gopro
        ip_address = gopro.ip_address

        if ip_address == "":
            return {
                "status": 500,
                "ip_address": ""
            }

        return {
            "status": 200,
            "ip_address": str(ip_address)
        }
    except Exception:
        return {
            "status": 500,
            "ip_address": ""
        }
    
async def get_status_top(CameraManager):
    try:
        gopro = CameraManager.top_gopro
        ip_address = gopro.ip_address
        if ip_address == "":
            return {
                "status": 500,
                "ip_address": ""
            }
        return {
            "status": 200,
            "ip_address": str(ip_address)
        }
    except Exception:
        return {
            "status": 500,
            "ip_address": ""
        }

async def get_status(CameraManager):
    top_status = await get_status_top(CameraManager)
    short_status = await get_status_short(CameraManager)
    front_status = await get_status_front(CameraManager)

    return {
        "front_camera_status": front_status["status"],
        "top_camera_status": short_status["status"],
        "short_camera_status": short_status["status"],

        "front_camera_ip": front_status["ip_address"],
        "top_camera_ip": top_status["ip_address"],
        "short_camera_ip": short_status["ip_address"],
    }
