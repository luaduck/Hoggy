from yapsy.IPlugin import IPlugin

class ron(IPlugin):
    trigger = '!ron'
    shortdesc = "Why the fuck would you use this command? It's a complete waste of time."
    longdesc = "Kill yourself"
    
    @classmethod
    def execute(cls, target = None, user = None, client = None):
        if target is not None:
            return "%s, you little fuck." % (target)
        else:
            messages = [
                "I would smack you in the mouth if I wouldn't feel bad for hitting a retard afterwards.",
                "If you project Excel, there better be fucking numbers in it somewhere.",
                "I would trade 3 of you for a talking version of Wikipedia or Wolfram Alpha. Seriously, don't get comfortable fucksticks.",
                "It's not rape if you yell out \"SURPRISE!\"",
                "Windows Vista was like a whore house when the ships come in",
                "\"Hush you I'm recalling the time Ron sent me cocaine via USPS\"",
                "\"\"Listen,\" he said, leaning closer, \"I\'m a fucking piranha in this pool. All these other socially awkward people, I eat them up. That\'s right, fucker,\" he added. \"That\'s just how I roll.\" He grabbed a woman seated to his right. A tattoo of a tree covered her back. George pointed. I looked. A small R.G. was nestled on one of the branches.  --RonUSMC\"",
                "Ron doesn\'t miss you, fuck you.",
                "Ron\'s a fucking piranha in this pool",
                "What\'s up, faggots? --Ron"
            ]  
            return "%s" % (choice(messages))