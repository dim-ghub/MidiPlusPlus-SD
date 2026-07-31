from ..PlaybackAction import PlaybackAction
import globals as gl
from loguru import logger as log
import os

class LoadSongAction(PlaybackAction):
    def on_ready(self) -> None:
        pass
        
    def on_key_down(self) -> None:
        settings = self.get_settings()
        song_index = settings.get("song_index")
        
        if song_index is not None:
            self.send_command(f"LOAD_SONG {song_index}")
            
        # Return to original page
        if not hasattr(self.plugin_base, 'original_page_path') or not self.plugin_base.original_page_path:
            return
            
        page_path = self.plugin_base.original_page_path
        if not os.path.exists(page_path):
            return
            
        page = gl.page_manager.get_page(path=page_path, deck_controller=self.deck_controller)
        if page:
            self.plugin_base.original_page_path = None
            self.deck_controller.load_page(page)
