from yapsy.IPlugin import IPlugin

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.ini')

class new(command):
    shortdesc = "Update the subreddit header with something extremely thought-provoking or insightful."
    longdesc = "Now with added sidebar garbling!"
    
    @classmethod
    def execute(cls, *args, **kwargs):
        if args[0] == '!hoggy':
            if int(args[1]):
                header = hoggy.execute(args[1])
            else:
                return "Usage: !new hoggy 15"
        else:
            header =  " ".join(args).replace("=","\=")
        
        manager = praw.Reddit("HoggyBot for /r/hoggit by /u/zellyman")
        manager.login(config.get('reddit', 'username'), config.get('reddit', 'password'))
        subreddit = manager.get_subreddit(config.get('reddit', 'subreddit'))
        settings = subreddit.get_settings()
        new_desc = "### %s \n=\n\n" % header
        new_desc += template
        
        subreddit.set_settings("Hoggit Fighter Wing", description=new_desc)

        return "Header updated."