from yapsy.IPlugin import IPlugin

class ping(IPlugin):
    trigger = '!ping'
    shorthelp = 'It\'s like Pong, but much more boring'
    longhelp = 'Space invaders 4lyf'
    def execute(cls, target=None, user = None, client = None):
        return choice(["pong", "pang", "poong", "ping?", "pop", "pa-pong!", "kill yourse- sorry, pong", "ta-ping!", "Wasn't that Mulan's fake name?"])
        
class no(command):
    longdesc = "For use in dire situations only."
    shortdesc = "For dire situations."
    
    @classmethod
    def execute(cls, *args, **kwargs):
        return "http://nooooooooooooooo.com/"
        
class blame(command):
    longdesc = "No seriously, fuck that guy."
    shortdesc = "Fuck that guy."

    @classmethod
    def execute(cls, *args, **kwargs):
        if not len(args):
            return "Usage: !blame <user>"
        if args[0].lower() == 'hoozin':
            return "^"
        elif args[0].lower() == 'hoggy':
            return "What'd I do?"
        messages = [
            "I concur, %s is absolutely responsible.",
            "Dammit, %s, now you've gone and Hoozin'ed it up."
        ]
        return choice(messages) % args[0]
        
class eject(command):
    shortdesc = "Get the hell out of Dodge!"
    longdesc = "Leave the room in style."

    @classmethod
    def execute(cls, user, client):
        client.kick('hoggit', user, 'Ejecting!')
        return "EJECT! EJECT! EJECT! {0} punched out.".format(user)

class thanks(command):
    shortdesc = "For polite people only"
    longdesc = "Like this ever gets any use"
    
    @classmethod
    def execute(cls, target = None, user = None, client=None):
        if target is not None:
            return "What about me?"
        else:
            return "No problem, %s" % (user)
            
class hug(command):
    shortdesc = "Hoggy is not responsible for any rape allegations that may arise from using this command"
    longdesc = "It makes me cringe when I think about it"
    
    @classmethod
    def execute(cls, target = None, user = None, client = None):
        if target is None:
            return "What, hug myself?"
        elif target.lower() == user.lower():
            return "Hugging yourself? Keep it clean!"
        else:
            return "%s gives %s a lingering hug. %s likes it. Likes it a lot...\nThey continue their embrace, %s gently stroking %s's face, and %s leans in for a kiss." % (user, target, target, target, user, user)