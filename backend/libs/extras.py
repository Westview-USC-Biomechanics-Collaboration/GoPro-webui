from .connect import *
from open_gopro import *

async def clear_gopros():
    try:
        front_gopro  = get_front_gopro()
        top_gopro = get_top_gopro()
        short_gopro = get_short_gopro()

        gopros = [front_gopro, top_gopro, short_gopro]

        for gopro in gopros:
            await gopro.http_command.delete_all_media()
        
        return {
            "status": 200
        }
    except Exception as e:
        return {
            "status": 500
        }
    
async def set_keep_alive():
    try:
        front_gopro  = get_front_gopro()
        top_gopro = get_top_gopro()
        short_gopro = get_short_gopro()

        gopros = [front_gopro, top_gopro, short_gopro]

        for gopro in gopros:
            await gopro.http_command.set_keep_alive()
        
        return {
            "status": 200
        }
    except Exception as e:
        return {
            "status": 500
        }