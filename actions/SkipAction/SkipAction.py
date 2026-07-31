from ..PlaybackAction import PlaybackAction

import os

class SkipAction(PlaybackAction):
    def on_ready(self) -> None:
        icon_path = os.path.join(self.plugin_base.PATH, "assets", "forward_10.png")
        self.set_media(media_path=icon_path, size=0.85)
        
    def on_key_down(self) -> None:
        self.send_command("SKIP")
