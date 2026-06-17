from .connect import *
from open_gopro.models import constants
import asyncio

async def front_preview(CameraManager):
    gopro = CameraManager.front_gopro
    await gopro.http_command.set_shutter(shutter=constants.Toggle.ENABLE)
    await asyncio.sleep(0.1)
    await gopro.http_command.set_shutter(shutter=constants.Toggle.DISABLE)
    video = await gopro.http_command.get_last_captured_media()
    return f"http://{gopro.ip_address}:8080//videos/DCIM/{video.data.folder}/{video.data.file}"

async def top_preview(CameraManager):
    gopro = CameraManager.top_gopro
    await gopro.http_command.set_shutter(shutter=constants.Toggle.ENABLE)
    await asyncio.sleep(0.1)
    await gopro.http_command.set_shutter(shutter=constants.Toggle.DISABLE)
    video = await gopro.http_command.get_last_captured_media()
    return f"http://{gopro.ip_address}:8080//videos/DCIM/{video.data.folder}/{video.data.file}"

async def short_preview(CameraManager):
    gopro = CameraManager.short_gopro
    await gopro.http_command.set_shutter(shutter=constants.Toggle.ENABLE)
    await asyncio.sleep(0.1)
    await gopro.http_command.set_shutter(shutter=constants.Toggle.DISABLE)
    video = await gopro.http_command.get_last_captured_media()
    return f"http://{gopro.ip_address}:8080//videos/DCIM/{video.data.folder}/{video.data.file}"

async def get_preview(CameraManager):
    try:
        previews = await asyncio.gather(
            top_preview(CameraManager),
            short_preview(CameraManager),
            front_preview(CameraManager)
        )
    
        return {
            "status": 200,
            "previews": previews
        }
    except Exception as e:
        return {
            "status": 500,
            "error": repr(e)
        }
        
        
