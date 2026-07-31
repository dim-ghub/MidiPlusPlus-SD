from src.backend.PluginManager.ActionBase import ActionBase
import socket
from loguru import logger as log

class PlaybackAction(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def send_command(self, cmd: str):
        try:
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            sock_path = os.path.expanduser('~/.midiplusplus.sock')
            s.connect(sock_path)
            s.sendall(f"{cmd}\n".encode('utf-8'))
            response = s.recv(1024).decode('utf-8')
            s.close()
            return response
        except Exception as e:
            log.error(f"[MIDI++ Controller] Failed to send command {cmd}: {e}")
            return None
