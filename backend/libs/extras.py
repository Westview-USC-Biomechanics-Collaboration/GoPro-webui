from .connect import *
from open_gopro import *

async def clear_gopros(CameraManager):
    try:
        front_gopro = CameraManager.front_gopro
        top_gopro = CameraManager.top_gopro
        short_gopro = CameraManager.short_gopro

        gopros = [front_gopro, top_gopro, short_gopro]

        for gopro in gopros:
            await gopro.http_command.delete_all_media()
        
        return {
            "status": 200
        }
    except Exception as e:
        return {
            "status": 500,
            "error": repr(e)
        }
    
async def set_keep_alive(CameraManager):
    try:
        front_gopro = CameraManager.front_gopro
        top_gopro = CameraManager.top_gopro
        short_gopro = CameraManager.short_gopro

        gopros = [front_gopro, top_gopro, short_gopro]

        for gopro in gopros:
            await gopro.http_command.set_keep_alive()
        
        return {
            "status": 200
        }
    except Exception as e:
        return {
            "status": 500,
            "error": repr(e)
        }
    
async def get_preset(CameraManager):
    try:
        """
        front_gopro = CameraManager.front_gopro
        top_gopro = CameraManager.top_gopro
        short_gopro = CameraManager.short_gopro

        gopros = [front_gopro, top_gopro, short_gopro]

        for gopro in gopros:
            await gopro.http_command.set_keep_alive()
        """
        
        return {
            "status": 200,
            "presets": {
                "top_gopro": {
                    "fps": 120,
                    "resolution": "4k_16_9",
                    "lens_mode": "Ultrawide"
                },
                "short_gopro": {
                    "fps": 120,
                    "resolution": "4k_16_9",
                    "lens_mode": "Ultrawide"
                },
                "front_gopro": {
                    "fps": 120,
                    "resolution": "4k_16_9",
                    "lens_mode": "Ultrawide"
                },


            }
        }
    except Exception as e:
        return {
            "status": 500,
            "error": repr(e)
        }

