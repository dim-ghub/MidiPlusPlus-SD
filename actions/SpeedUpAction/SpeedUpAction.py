import os

from ..PlaybackAction import PlaybackAction

class SpeedUpAction(PlaybackAction):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_custom_image_fallback = True

    def on_ready(self) -> None:
        self.set_media(media_path=os.path.join(self.plugin_base.PATH, "assets", "fast_forward.png"), size=0.8)
        
    def on_key_down(self) -> None:
        self.send_command("SPEED_UP")
