from textual.app import App, ComposeResult
from textual import events
from textual.binding import Binding
from textual.widgets import Button, Header, Label, Footer, Static, Tabs
from random import randint


class EventApp(App[str]):
    CSS = """
Tabs {
    dock: top;
}
    
Screen {
    layout: grid;
    grid-size: 2;
    padding: 2;
    align: center middle;
}

#logo {
    width: 100%;
    height: 100%;
    column-span: 2;
    content-align: center middle;
    text-style: bold;
}

"""

    logos = [r"""
 __      __          _       _ 
 \ \    / /         (_)     | |
  \ \  / /    ___    _    __| |
   \ \/ /    / _ \  | |  / _` |
    \  /    | (_) | | | | (_| |
     \/      \___/  |_|  \__,_|""",
     r"""
 __     __                        __              __ 
|  \   |  \                      |  \            |  \
| $$   | $$        ______         \$$        ____| $$
| $$   | $$       /      \       |  \       /      $$
 \$$\ /  $$      |  $$$$$$\      | $$      |  $$$$$$$
  \$$\  $$       | $$  | $$      | $$      | $$  | $$
   \$$ $$        | $$__/ $$      | $$      | $$__| $$
    \$$$          \$$    $$      | $$       \$$    $$
     \$            \$$$$$$        \$$        \$$$$$$$
     """,  
     r"""
                                                   
  _/      _/                    _/            _/   
 _/      _/        _/_/                  _/_/_/    
_/      _/      _/    _/      _/      _/    _/     
 _/  _/        _/    _/      _/      _/    _/      
  _/            _/_/        _/        _/_/_/       
                                                   
     
     """,
     r"""
                                                                                        
_______    ______               ____              ____________          ____________    
\      |  |      |          ____\_  \__          /            \         \           \   
 |     /  /     /|         /     /     \        |\___/\  \\___/|         \           \  
 |\    \  \    |/         /     /\      |        \|____\  \___|/          |    /\     | 
 \ \    \ |    |         |     |  |     |              |  |               |   |  |    | 
  \|     \|    |         |     |  |     |         __  /   / __            |    \/     | 
   |\         /|         |     | /     /|        /  \/   /_/  |          /           /| 
   | \_______/ |         |\     \_____/ |       |____________/|         /___________/ | 
    \ |     | /          | \_____\   | /        |           | /        |           | /  
     \|_____|/            \ |    |___|/         |___________|/         |___________|/   
                           \|____|                                                      
"""]



    TABS = [
        "Menu",
        "Channels",
        "DM's",
        "Settings"
    ]    
    
    TITLE = "Void"
    SUB_TITLE = "Welcome To Void"

    COLORS = [
        "white",
        "black"
    ]
    
    currColor = "black"
    def on_mount(self) -> None:
        self.screen.styles.background = "black"
        
        
    tuiColor = "ctrl+t"
    def on_key(self, event: events.Key) -> None:
        if event.key == self.tuiColor:
            if self.currColor == "black":
                self.screen.styles.background = "white"
                self.currColor = "white"
            else:
                self.screen.styles.background = "black"    
                self.currColor = "black"   
                
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label(self.logos[randint(0,3)], id="logo")
        #yield Footer()
        yield Tabs(self.TABS[0])
        
                
    
            

if __name__ == "__main__":
    app = EventApp()
    reply = app.run()
    print(reply)