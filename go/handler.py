class UnixHandler:
    def __call__(self):
        import sys
        import tty
        import termios

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

class WinHandler:
    def __init__(self):
        import msvcrt
    
    def __call__(self):
        import msvcrt

        return msvcrt.getch()

class EventHandler:
    def __init__(self):
        try:
            self.system_type = WinHandler()
        except ImportError:
            self.system_type = UnixHandler()
    
    def __call__(self):
        return self.system_type()

get_key = EventHandler()