from yapsy.IPlugin import IPlugin

class hoggy(command):
    longdesc = "with no arguments will display a random quote. [#] will display the quote with the specified ID. [add <quote>] will add the specified <quote> to the db. [search <string>] will look for that string in the db. [count] should show the number of hoggyisms stored."
    shortdesc = "Display or add Hoggyisms"

    # Hoggyism operations
    def add_quote(self, message):
        q = quotes.insert()
        q.execute(body=message)
        return engine.scalar("select max(id) from quotes")

    def get_random(self):
        q =  quotes.select(limit=1).order_by('RANDOM()')
        rs = q.execute()
        row = rs.fetchone()
        return row
    
    def search(self, message):
        q = quotes.select().order_by('id').where('body LIKE "%{0}%"'.format(message))
        rs = q.execute()
        rows = rs.fetchall()
        return rows

    def get_by_id(self, quoteId):
        q =  quotes.select().where('id=' + str(quoteId))
        rs = q.execute()
        row = rs.fetchone()
        return row

    def remove_quote(self, quoteId):
        q = quotes.delete().where("id={0}".format(str(quoteId)))
        q.execute()
    def count(self): return quotes.count()
        
    @classmethod
    def execute(cls, *args, **kwargs):
        hog = cls()
        argc = len(args)
        if argc == 0:
            row = hog.get_random()
            return '%s (#%d)' % (str(row['body']), row['id'])

        elif argc == 1:
            try:
                quoteId = int(args[0])
                row = hog.get_by_id(quoteId)
                return '%s (#%d)' % (str(row['body']), row['id'])
            except:
                return '!help for usage'

        elif args[0] == 'add':
            string = " ".join(args[1:])
            string = unicode(string)
            quoteId = hog.add_quote(string)

            return "Added {0} (#{1})".format(str(string), quoteId)

        elif args[0] == 'remove':
            try:
                quoteId = int(args[1])
            except:
                return '!help'
            if hog.remove_quote(quoteId):
                return "Deleted #%d" % quoteId
            else:
                return "No quote with id: %s" %quoteId
        elif args[0] == 'search':
            try:
                search_string = str(args[1])
                if (len(search_string) < 3):
                    return "Minimum search requires 3 letters"
            except:
                return "Your search string hoozed it up"
            
            results = hog.search(search_string)
            return_string = ""
            for result in results:
                return_string += "#%d: \"%s\"\n" % (result[0], result[1])   
              
            kwargs['client'].msg(kwargs['user'],return_string.encode('ascii','replace'))
        elif args[0] == 'count':
            number = hog.count()
            return "There are currently {0} hoggyisms stored!".format(number)
        else:
            return "You hoozed it up, do !help hoggy"


class grab(command):
    shortdesc = "Grab the last n lines of a specifc user and create a hoggyism"
    longdesc = "Usage: !grab <user> <number of lines>  number of lines defaults to 1"

    @classmethod
    def execute(cls, *args, **kwargs):
        if len(args) == 1:
            num_lines = 1
        else:
            try:
                num_lines = int(args[1])
            except:
                num_lines = 0

        if num_lines < 1:
            return "{0}... Don't be a dipshit.".format(kwargs['user'])

        if args[0].lower() == 'hoggy':
            return "Got no time to be playing with myself..."

        quote = kwargs['client'].grabber.grab(args[0], num_lines)
        return hoggy.execute('add', quote)