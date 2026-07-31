from ..PlaybackAction import PlaybackAction

import os
import json

class PlayPauseAction(PlaybackAction):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_custom_image_fallback = True

    def on_ready(self) -> None:
        self.update_icon(True)
        
    def update_icon(self, is_paused: bool):
        filename = "play.png" if is_paused else "pause.png"
        icon_path = os.path.join(self.plugin_base.PATH, "assets", filename)
        self.set_media(media_path=icon_path, size=0.85)

    def on_key_down(self) -> None:
        self.send_command("PLAY_PAUSE")

    def on_tick(self) -> None:
        raw_json = self.send_command("GET_TIME")
        if not raw_json: return
        try:
            data = json.loads(raw_json.strip())
            is_paused = data.get("paused", True)
            self.update_icon(is_paused)
        except:
            pass
