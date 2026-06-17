from .connect import *

class CameraManager:
    @classmethod
    async def create(cls):
        self = cls()
        self.front_gopro = await get_front_gopro()
        self.short_gopro = await get_short_gopro()
        self.top_gopro = await get_top_gopro()

        return self
