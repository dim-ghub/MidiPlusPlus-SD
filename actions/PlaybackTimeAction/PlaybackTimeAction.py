from ..PlaybackAction import PlaybackAction
import json

class PlaybackTimeAction(PlaybackAction):
    def on_ready(self) -> None:
        pass
        
    def on_tick(self) -> None:
        raw_json = self.send_command("GET_TIME")
        if not raw_json: return
        
        try:
            data = json.loads(raw_json.strip())
            cur = int(data.get("current", 0))
            tot = int(data.get("total", 0))
            spd = data.get("speed", 1.0)
            
            text = f"{cur // 60}:{cur % 60:02d} / {tot // 60}:{tot % 60:02d}\n({spd:.2f}x)"
            self.set_center_label(text)
        except:
            pass
