from ..PlaybackAction import PlaybackAction
import json

class SpeedDownAction(PlaybackAction):
    def on_ready(self) -> None:
        pass
        
    def on_key_down(self) -> None:
        self.send_command("SPEED_DOWN")

    def on_tick(self) -> None:
        raw_json = self.send_command("GET_TIME")
        if not raw_json: return
        try:
            data = json.loads(raw_json.strip())
            spd = data.get("speed", 1.0)
            self.set_bottom_label(f"{spd:.2f}x", [255, 255, 255, 255])
        except:
            pass
