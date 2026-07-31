from ..PlaybackAction import PlaybackAction
import globals as gl
from loguru import logger as log
import os

class CloseSongSelectorAction(PlaybackAction):
    def on_ready(self) -> None:
        pass
        
    def on_key_down(self) -> None:
        if not hasattr(self.plugin_base, 'original_page_path') or not self.plugin_base.original_page_path:
            log.warning("No original page path to return to.")
            return
            
        page_path = self.plugin_base.original_page_path
        if not os.path.exists(page_path):
            log.error("Could not find original page.")
            return
            
        page = gl.page_manager.get_page(path=page_path, deck_controller=self.deck_controller)
        if page:
            self.plugin_base.original_page_path = None
            self.deck_controller.load_page(page)
