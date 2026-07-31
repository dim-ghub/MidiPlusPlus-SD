from ..PlaybackAction import PlaybackAction
import json
import os
import globals as gl
from loguru import logger as log

class OpenSongSelectorAction(PlaybackAction):
    def on_ready(self) -> None:
        pass
        
    def generate_pages(self, songs):
        try:
            cols = self.deck_controller.deck.key_layout()[0]
            rows = self.deck_controller.deck.key_layout()[1]
        except:
            cols = 5
            rows = 3
            
        keys_per_page = (cols * rows) - 2
        if keys_per_page <= 0:
            keys_per_page = 13
            
        pages = []
        for i in range(0, len(songs), keys_per_page):
            pages.append(songs[i:i + keys_per_page])
            
        page_paths = []
        for p_idx, page_songs in enumerate(pages):
            page_data = {"keys": {}}
            
            # Back/Cancel button at 0x0
            page_data["keys"]["0x0"] = {
                "states": {
                    "0": {
                        "actions": [{"id": "com_midiplusplus_Controller::CloseSongSelector", "settings": {}}],
                        "text": "Cancel"
                    }
                }
            }
            
            # Next button
            if p_idx < len(pages) - 1:
                next_x = cols - 1
                next_y = rows - 1
                page_data["keys"][f"{next_x}x{next_y}"] = {
                    "states": {
                        "0": {
                            "actions": [
                                {
                                    "id": "com_midiplusplus_Controller::LoadGeneratedPage", 
                                    "settings": {"page_idx": p_idx + 1}
                                }
                            ],
                            "text": "Next ->"
                        }
                    }
                }
            
            # Previous button
            if p_idx > 0:
                prev_x = 0
                prev_y = rows - 1
                page_data["keys"][f"{prev_x}x{prev_y}"] = {
                    "states": {
                        "0": {
                            "actions": [
                                {
                                    "id": "com_midiplusplus_Controller::LoadGeneratedPage", 
                                    "settings": {"page_idx": p_idx - 1}
                                }
                            ],
                            "text": "<- Prev"
                        }
                    }
                }
            
            # Populate songs
            song_idx = 0
            for y in range(rows):
                for x in range(cols):
                    if x == 0 and y == 0: continue
                    if p_idx < len(pages) - 1 and x == cols - 1 and y == rows - 1: continue
                    if p_idx > 0 and x == 0 and y == rows - 1: continue
                    
                    if song_idx < len(page_songs):
                        global_idx = (p_idx * keys_per_page) + song_idx
                        song_name = page_songs[song_idx]
                        display_name = song_name[:12] + "..." if len(song_name) > 15 else song_name
                            
                        page_data["keys"][f"{x}x{y}"] = {
                            "states": {
                                "0": {
                                    "actions": [
                                        {
                                            "id": "com_midiplusplus_Controller::LoadSong",
                                            "settings": {"song_index": global_idx}
                                        }
                                    ],
                                    "text": display_name,
                                    "text-alignment": "center",
                                    "font-size": 9
                                }
                            }
                        }
                        song_idx += 1
                        
            page_path = os.path.join(self.plugin_base.PATH, "pages", f"SongSelector_{p_idx}.json")
            with open(page_path, "w") as f:
                json.dump(page_data, f, indent=4)
            page_paths.append(page_path)
            
        return page_paths

    def on_key_down(self) -> None:
        raw_json = self.send_command("LIST_SONGS")
        if not raw_json: return
        try:
            songs = json.loads(raw_json.strip())
        except:
            log.error("Failed to parse song list JSON")
            return
            
        if len(songs) == 0:
            log.warning("No songs found")
            return
            
        page_paths = self.generate_pages(songs)
        if not page_paths: return
        
        if hasattr(self.deck_controller, 'active_page') and self.deck_controller.active_page:
            self.plugin_base.original_page_path = self.deck_controller.active_page.json_path
            
        page = gl.page_manager.get_page(path=page_paths[0], deck_controller=self.deck_controller)
        if page:
            self.deck_controller.load_page(page)
