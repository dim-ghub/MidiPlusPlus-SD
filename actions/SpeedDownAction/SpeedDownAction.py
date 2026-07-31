from ..PlaybackAction import PlaybackAction

class SpeedDownAction(PlaybackAction):
    def on_ready(self) -> None:
        pass
        
    def on_key_down(self) -> None:
        self.send_command("SPEED_DOWN")
