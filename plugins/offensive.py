from yapsy.IPlugin import IPlugin

class wire(command):
    shortdesc = "Accurately simulates a Vikhir missile"
    longdesc = "Good luck hitting anything"
    
    @classmethod
    def execute(cls, target = None, user = None, client = None):
        if target is None:
            messages = [
                "launches a Vikhir at empty space. Can't be worse than aiming at something."
            ]
            return "%s %s" % (user, choice(messages))
        elif target.lower() == user.lower():
            messages = [
                "manages to fire a Vikhir at themself. Lasers aren't for pointing into cockpits. Doesn't mattter much though, it still missed."
            ]
            return "%s %s" % (user, choice(messages)) 
        else:
            messages = [
                "but they crashed for no good reason",
                "it plowed into the ground",
                "it overshot the target",
                "it undershot the target",
                "but their laser burned out",
                "however their tail fell off",
                "but their autopilot flipped out",
                "but their trim reset",
                "and it hit the target! .... nah",
                "but it fell in love with a passing Hind and they embraced awkwardly"
            ]
            return "%s launched a Vikhir at %s, %s." % (user, target, choice(messages))
            
class rifle(command):
    shortdesc = "Fire a AGM-65"
    longdesc = "No arguments fires one into the great blue yonder. [<target>]:  attempts to destroy <target>"

    @classmethod
    def execute(cls, target = None, user = None, client=None):
        if target is None:
            return '(M) BBBBEEEEEEPPPPPP!  EVERYONE FLIP THE FUCK OUT'
        try:
            message = '%s slews over to the burning hot flesh-sack that is %s with an AGM-65 seeker....\n' % (user, target)
            message += '(M) BBBBEEEEEEPPPPPP!  EVERYONE FLIP THE FUCK OUT\n'
            if random.randint(0,100) > 33:
                message += '%s obliterated %s with a well aimed Maverick.' % (user, target)
            else:
                message += '%s missed, the seeker locked onto a nearby moose in flight.' % user
        except Exception, ex:
            print ex
            message = '(M) BBBBEEEEEEPPPPPP!  EVERYONE FLIP THE FUCK OUT'

        return message

class pickle(command):
    shortdesc = "Drop the bombs of peace onto the target of desperation"
    longdesc = "Like this will ever hit anything"
    
    @classmethod
    def execute(cls, target = None, user = None, client = None):
        if target is None:
            messages = [
                'dropped his bombs without looking, and demolished an elementary school.  The horror is etched into the minds of generations to come.',
                'dropped his bombs with no target and and destroyed the penguin exhibit at the local zoo.  The screams can still be heard to this day',
                'dropped his bombs without looking, inadvertanly starting a war with New Zealand.'
            ]

            message = messages[random.randint(0,2)]
            return user + ' ' + message
        elif target.lower() == user.lower():
           client.kick('hoggit', user, 'Self-immolation is not the way forward')
           return "%s rolls 180 degrees and drops his bombs... before realising what a silly mistake he made" % user
        bombs = [
            'Mk. 82',
            'Mk. 84',
            'CBU-87',
            'CBU-97',
            'GBU-10',
            'GBU-12',
            'GBU-38',
            'GBU-31'
        ]
        types = [ 'CCIP', 'CCRP' ]
        message = '%s released a %s %s toward %s\n' % (user, choice(types), choice(bombs), target)
        if random.randint(0,100) > 33:
            message += '%s obliterated %s with a well aimed Drop.' % (user, target)
        else:
            message += '%s missed, read the 9-line noob!' % user

        return message
        
class guns(command):
    shortdesc = "Strike down a target with great vengeance and furious anger"
    longdesc = "Seriously, great vengeance and furious anger"

    @classmethod
    def execute(cls, target = None, user = None, client=None):
        if target is None:
            return 'BBBRRRRRRRAAAAPPPPPPPPPP!!!!'
        try:
            message =  "%s sets up a gun run...\n" % (user)

            if random.randint(0,100) > 33:
                message += "BBBRRRRRRRAAAAPPPPPPPPPP!!!! \n"
                message += "%s pulverized %s with great vengeance and furious anger" % (user, target)
            elif random.randint(0,100) > 60:
                message += "%s screwed up their attack run, but managed to pull out." % (user)
            else: 
                message += "%s ignored the VMU's 'PULL UP' and smashed into %s" % (user, target)
                client.kick('hoggit', user, 'Is no more.')
        except Exception, ex:
            print ex
            message = "%s screwed up their attack run, but managed to pull out." % (user)

        return message
        
class lightning(command):
    shortdesc = "THUNDER STRIKE"
    longdesc = "http://www.youtube.com/watch?v=j_ekugPKqFw"
    @classmethod
    def execute(cls, target = None, user = None, client = None):
        return "LIGHTNING BOLT! %s takes %d damage" % (target, random.randint(0,9999))