from ..PlaybackAction import PlaybackAction
import globals as gl
import os

class LoadGeneratedPageAction(PlaybackAction):
    def on_ready(self) -> None:
        pass
        
    def on_key_down(self) -> None:
        settings = self.get_settings()
        page_idx = settings.get("page_idx", 0)
        
        page_path = os.path.join(self.plugin_base.PATH, "pages", f"SongSelector_{page_idx}.json")
        if not os.path.exists(page_path):
            return
            
        page = gl.page_manager.get_page(path=page_path, deck_controller=self.deck_controller)
        if page:
            self.deck_controller.load_page(page)
