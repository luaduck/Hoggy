from yapsy.IPlugin import IPlugin

class when(command):
    shortdesc = "Gets the current time for the given user"
    longdesc = "Try !when <user>, requires that user to have done a !settime first"
    @classmethod
    def execute(cls, target = None, user = None, client = None):
        low = target.lower()
        if low == "hoggy":
            return "I am beyond both time and space, mortal"
        
        time =  times.select().where(times.c.name==low).execute().fetchone()
        if not time:
            return "They don't appear to have set a time yet, sorry"
        time = get_adjusted_time(time.time)
        return "The local time in {0}-land is: {1}".format(target, time)

def get_adjusted_time(adjustment):
    adj = gmtime(time.time()+adjustment*60*60)
    return time.strftime("%a %H:%M", adj)

class settime(command):
    shortdesc = "Set your timezone"
    wanted = "!settime [UTC|GMT][+|-]hours" 
    longdesc = format
    @classmethod
    def execute(cls, time = None, user = None, client = None):
        if not time or not user:
            return 
        reg = re.compile("^(ZULU|GMT|UTC)(\+|-)[0-9]{1,2}[:|\.]{0,1}[0-9]{0,2}$")
        if not reg.match(time):
            return "Hey, try the format: {0}".format(settime.wanted)
        dir = 1
        if '-' in time:
            dir = -1
        time = time[4:]
        if ':' in time:
            parts = time.split(':')
            if len(parts[1]) != 2:
                return "Two digits for minutes, thank you very muchly"
            hours = int(parts[0]) + (float(parts[1]) / 60.0)
        elif '.' in time:
            hours = float(time)
        else:
            hours = int(time)
        user = user.lower()
        hours *= dir
        if times.select().where(times.c.name==user).execute().fetchone():
            times.update().where(times.c.name==user).values(time=hours).execute()
        else:
            ins = times.insert()
            ins.execute(name=user, time=hours)
        return "Your clock is now set at {0}".format(get_adjusted_time(hours))