from .connect import *
import open_gopro
from open_gopro.models import constants
import asyncio

async def front_preview():
    gopro = await get_front_gopro()
    await gopro.http_command.set_shutter(shutter=constants.Toggle.ENABLE)
    await asyncio.sleep(0.1)
    await gopro.http_command.set_shutter(shutter=constants.Toggle.DISABLE)
    video = await gopro.http_command.get_last_captured_media()
    return f"http://{gopro.ip_address}:8080//videos/DCIM/{video.data.folder}/{video.data.file}"

async def top_preview():
    gopro = await get_top_gopro()
    await gopro.http_command.set_shutter(shutter=constants.Toggle.ENABLE)
    await asyncio.sleep(0.1)
    await gopro.http_command.set_shutter(shutter=constants.Toggle.DISABLE)
    video = await gopro.http_command.get_last_captured_media()
    return f"http://{gopro.ip_address}:8080//videos/DCIM/{video.data.folder}/{video.data.file}"

async def short_preview():
    gopro = await get_short_gopro()
    await gopro.http_command.set_shutter(shutter=constants.Toggle.ENABLE)
    await asyncio.sleep(0.1)
    await gopro.http_command.set_shutter(shutter=constants.Toggle.DISABLE)
    video = await gopro.http_command.get_last_captured_media()
    return f"http://{gopro.ip_address}:8080//videos/DCIM/{video.data.folder}/{video.data.file}"

async def get_preview():
    previews = await asyncio.gather(
        top_preview(),
        short_preview(),
        front_preview()
    )

    return {
        "previews": previews
    }