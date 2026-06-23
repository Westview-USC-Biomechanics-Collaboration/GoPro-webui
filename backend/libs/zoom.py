

async def top_camera_zoom(CameraManager, zoom):
    try: 
        top_gopro = CameraManager.top_gopro

        await top_gopro.http_command.set_digital_zoom(zoom/100)

        return {
            "status": 200
        }
    except Exception as e:
        return {
            "status": 500,
            "error": repr(e)
        }





