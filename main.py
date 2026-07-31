# Import StreamController modules
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder

# Import actions
from .actions.PlayPauseAction.PlayPauseAction import PlayPauseAction
from .actions.SkipAction.SkipAction import SkipAction
from .actions.RewindAction.RewindAction import RewindAction
from .actions.RestartAction.RestartAction import RestartAction
from .actions.OpenSongSelectorAction.OpenSongSelectorAction import OpenSongSelectorAction
from .actions.CloseSongSelectorAction.CloseSongSelectorAction import CloseSongSelectorAction
from .actions.LoadGeneratedPageAction.LoadGeneratedPageAction import LoadGeneratedPageAction
from .actions.LoadSongAction.LoadSongAction import LoadSongAction

import os

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()
        
        self.original_page_path = None

        self.play_pause_holder = ActionHolder(
            plugin_base = self,
            action_base = PlayPauseAction,
            action_id = "com_midiplusplus_Controller::PlayPause",
            action_name = "Play/Pause",
        )
        self.add_action_holder(self.play_pause_holder)
        
        self.skip_holder = ActionHolder(
            plugin_base = self,
            action_base = SkipAction,
            action_id = "com_midiplusplus_Controller::Skip",
            action_name = "Skip (+10s)",
        )
        self.add_action_holder(self.skip_holder)
        
        self.rewind_holder = ActionHolder(
            plugin_base = self,
            action_base = RewindAction,
            action_id = "com_midiplusplus_Controller::Rewind",
            action_name = "Rewind (-10s)",
        )
        self.add_action_holder(self.rewind_holder)
        
        self.restart_holder = ActionHolder(
            plugin_base = self,
            action_base = RestartAction,
            action_id = "com_midiplusplus_Controller::Restart",
            action_name = "Restart Song",
        )
        self.add_action_holder(self.restart_holder)
        
        self.open_selector_holder = ActionHolder(
            plugin_base = self,
            action_base = OpenSongSelectorAction,
            action_id = "com_midiplusplus_Controller::OpenSongSelector",
            action_name = "Open Song Selector",
        )
        self.add_action_holder(self.open_selector_holder)
        
        # Internal actions (not typically placed manually by users but registered)
        self.close_selector_holder = ActionHolder(
            plugin_base = self,
            action_base = CloseSongSelectorAction,
            action_id = "com_midiplusplus_Controller::CloseSongSelector",
            action_name = "Close Song Selector",
        )
        self.add_action_holder(self.close_selector_holder)
        
        self.load_gen_page_holder = ActionHolder(
            plugin_base = self,
            action_base = LoadGeneratedPageAction,
            action_id = "com_midiplusplus_Controller::LoadGeneratedPage",
            action_name = "Load Gen Page",
        )
        self.add_action_holder(self.load_gen_page_holder)
        
        self.load_song_holder = ActionHolder(
            plugin_base = self,
            action_base = LoadSongAction,
            action_id = "com_midiplusplus_Controller::LoadSong",
            action_name = "Load Song",
        )
        self.add_action_holder(self.load_song_holder)

        # Register plugin
        self.register(
            plugin_name = "MIDI++ Controller",
            github_repo = "https://github.com/dim-ghub/MIDIPlusPlus-SD",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )
        
        # Create pages directory if it doesn't exist
        os.makedirs(os.path.join(self.PATH, "pages"), exist_ok=True)