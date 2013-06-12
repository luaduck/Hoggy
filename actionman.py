from setup import quotes, times, engine
from random import choice
import re
import random
import requests
import time
import urllib
import BeautifulSoup
import praw
from sidebar import template
from time import gmtime

# config read
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('config.ini')

# plugin init code
from yapsy.PluginManager import PluginManager
plugman = PluginManager()
plugman.setPluginPlaces(["plugins"])
plugman.collectPlugins()
for pluginInfo in plugman.getAllPlugins():
    plugman.activatePluginByName(pluginInfo.name)

class ActionException(Exception):
    def __init__(self, message):
        super(ActionException, self).__init__(message)

class command(object):
    shortdesc = "No help available"
    longdesc = "No help available, try !eject"

    def execute(self, *args):
        raise NotImplementedError

class Commander(object):
    actions = {
        '!hoggy':hoggy,
        '!guns' : guns,
        '!rifle': rifle,
        '!pickle': pickle,
        '!eject':eject,
        '!help': print_help,
        '!no':no,
        '!grab': grab,
        '!blame' : blame,
        '!wire' : wire,
        '!hug' : hug,
        '!ron' : ron,
        '!thanks' : thanks,
        '!ron': ron,
        '!bolt': lightning,
        '!new': new,
        '!when': when,
        '!settime':settime,
        '!ud': urbandictionary,
        '!ping':ping
    }
    for plugin in plugman.getAllPlugins():
        actions[plugin.plugin_object.trigger] = plugin.plugin_object

    def __init__(self, client):
        self.client = client


    """def getYoutubeTitle(self, user, id):
        r = requests.get("".join(["http://gdata.youtube.com/feeds/api/videos/", id, "?v=2&alt=json"]))
        if r.status_code != 200:
            if r.status_code == 400:
                return user + ", why you gotta make life hard? Make it a good link."
            return "Youtube Hoozin'ed it up. (HTTP %d)" % r.status_code
        try:
            sec = int(r.json()['entry']['media$group']['media$content'][0]['duration'])
            minutes = sec / 60
            hr = minutes / 60
            sec = sec % 60
            minutes = minutes % 60
            title = r.json()['entry']['media$group']['media$title']['$t'].encode('utf-8')
            if hr != 0:
                return "%s [%02d:%02d:%02d]" % (title, hr, minutes, sec)
            else:
                return "%s [%02d:%02d]" % (title, minutes, sec)
        except IndexError:
            return user + ", that video isn't available or doesn't exist."""

    def recv(self, message, user):
        if message.startswith('!'):
            # Awww snap, it's a hoggy action
            try:
                # split up the command into action and args
                command_array = message.split(' ')
                command = command_array[0]
                
                # Check that there are args, if not args is empty list
                if len(command_array) > 1:
                    try:
                        args = command_array[1:]
                    except:
                        args = []
                else:
                    args = []

                # Attempt to find a corresonding registered action
                try:
                    action = self.actions[command]
                except:
                    raise ActionException('Invalid command: ' + command)

                return action.execute(*args, user=user, client=self.client)
            except ActionException, ex:
                return str(ex)
            except Exception, ex:
                return "Hoozin'ed it up: unexpected exception: {0}".format(str(ex))
        else:
            if  ' r/' in message or '/r/' in message:
                obj = re.search(r'[/]?r/[^\s\n]*',message)
                sub = obj.group()
                if sub.startswith('/'):
                    sub = sub[1:]
                return "http://reddit.com/%s" % sub

            if  ' u/' in message or '/u/' in message:
                obj = re.search(r'[/]?u/[^\s\n]*',message)
                sub = obj.group()
                if sub.startswith('/'):
                    sub = sub[1:]
                return "http://reddit.com/%s" % sub
            
            #our youtube lookups, short and long have different formats
            website = "http" in message
            if website:
                parts = message.split()
                for part in parts:
                    if part.startswith('http:') or part.startswith('https:'):                        
                        soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(part))
                        return "Title: {0}".format(soup.title.string.encode('ascii', 'ignore'))

