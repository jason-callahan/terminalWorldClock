# terminalWorldClock

terminal app for a world clock using textual for a TUI  
https://textual.textualize.io/  
https://github.com/Textualize/textual  

![alt text](image.png)

### Project Setup
```bash
git clone https://github.com/jason-callahan/terminalWorldClock.git
cd terminalWorldClock
python3 -m venv .venv
source .venv/bin/activate
pip install -r reqirements.txt
```

### Dev hot reload
hot-reload with pytest-watch:  
```bash
ptw --runner "textual run main.py --dev"  
```
