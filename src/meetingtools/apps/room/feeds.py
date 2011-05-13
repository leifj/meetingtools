'''
Created on May 13, 2011

@author: leifj
'''

from django.contrib.syndication.views import Feed
from meetingtools.apps.room.models import Room
from tagging.models import TaggedItem
from meetingtools.settings import BASE_URL
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed

class TagsWrapper(object):
    
    def __init__(self,tn):
        self.tags = tn.split('+')
        self.rooms = TaggedItem.objects.get_by_model(Room, tn.split('+'))
        
    def title(self):
        return "Rooms tagged with %s" % " and ".join(self.tags)

    def description(self):
        return self.title()
    
    def link(self,ext):
        return "%s/room/+%s.%s" % (BASE_URL,"+".join(self.tags),ext)

class RoomTagFeed(Feed):
    
    item_author_name = 'SUNET e-meeting tools'
    
    def ext(self):
        if self.feed_type == Atom1Feed:
            return "atom"
        
        if self.feed_type == Rss201rev2Feed:
            return "rss"
        
        return "rss"
    
    def get_object(self,request,tn):
        return TagsWrapper(tn)
    
    def title(self,t):
        return t.title()
    
    def link(self,t):
        return t.link(self.ext())
    
    def description(self,t):
        return t.description()
    
    def items(self,t):
        return t.rooms
    
    def item_title(self,room):
        return room.name
    
    def item_description(self,room):
        return room.description
    
    def item_link(self,room):
        return room.go_url()
    
    def item_guid(self,room):
        return room.permalink()
    
    def item_pubdate(self,room):
        return room.lastupdated
    
    
class RoomAtomTagFeed(RoomTagFeed):
    feed_type = Atom1Feed
    
class RoomRSSTagField(RoomTagFeed):
    feed_type = Rss201rev2Feed