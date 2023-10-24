import time


ScriptName = "Now playing"
Website = "https://github.com/EllieTheYeen"
Description = "Post current playing song name in chat"
Creator = "EllieTheYeen"
Version = "1.0.0.0"

# Just to make linter not complain
try:
        Parent
except:
        Parent = None

lasttick = None
lastsong = None

def Init(): pass
    
def Execute(data): pass
    
def Tick():
    global lasttick
    nowtick = int(time.time())
    if not lasttick:
        lasttick = nowtick
    if abs(nowtick - lasttick) >= 5:
        lasttick = nowtick
        SecondsTick()
    
def SecondsTick():
    global lastsong
    current = Parent.GetNowPlaying()
    currentsong = current.Key
    if currentsong and currentsong != lastsong:
        lastsong = currentsong
        Parent.SendStreamMessage('Now playing: %s' % (currentsong,))
