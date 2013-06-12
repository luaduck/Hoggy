from yapsy.IPlugin import IPlugin

class ping(IPlugin):
    trigger = '!ping'
    shorthelp = 'It\'s like Pong, but much more boring'
    longhelp = 'Space invaders 4lyf'
    def execute(cls, target=None, user = None, client = None):
        return choice(["pong", "pang", "poong", "ping?", "pop", "pa-pong!", "kill yourse- sorry, pong", "ta-ping!", "Wasn't that Mulan's fake name?"])