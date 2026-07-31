from ..PlaybackAction import PlaybackAction

class RestartAction(PlaybackAction):
    def on_ready(self) -> None:
        pass
        
    def on_key_down(self) -> None:
        self.send_command("RESTART")
