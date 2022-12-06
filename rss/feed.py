import feedparser
import datetime
import dateutil.parser as parser

class Feed:
    
    # constructor retrieves and parses data from given url
    def __init__(self, url): 
        try: 
            self.data = feedparser.parse(url)
        except:
            print("Error. Could not parse URL")

    # Exception returns title from parsed feed data
    def getTitle(self):
        try:
            title = self.data.feed.title
        except: 
            title = "No title available"
        finally:
            return title

    # Exception returns link from parsed feed data
    def getLink(self):
        try:
            link = self.data.feed.link
        except:
            link = "No link available"
        finally: 
            return link

    # Exception returns description from parsed feed data
    def getDescription(self):
        try:
            description = self.data.feed.description
        except:
            description = "No description"
        finally:
            return description
    
    # Exception returns publish date from parsed feed data
    def getPublished(self):
        try:
            published = parser.parse(self.data.feed.published).strftime("%d-%m-%Y")
        except:
            published = "No publish date available"
        finally:
            return published

    # Exception returns title, link, summary, and publish date into Entry class
    def getEntry(self, i):
        try:
            entry = self.data.entries[i]
            try: 
                title = entry.title
            except:
                title = "No entry title available"
            try: 
                link = entry.link
            except:
                link = "No entry link available"
            try: 
                description = entry.description
            except:
                description = "No entry summary available"
            try: 
                published = entry.published
            except:
                published = "No entry publish date available"
            
            entry = Entry(title, link, description, published)
            
        except:
            entry = Entry("No entry title available", "No entry link available", "No entry description available", "No entry publish date available")

        finally:
            return entry

    # Exception returns length of feed entries list
    def getLength(self):
        try:
            length = len(self.data.entries)
        except:
            length = 0
        finally:
            return length

    # Returns all the feeds entries as a list   
    def getEntries(self):
        entries = []

        for i in range(self.getLength()):
            entries.append(self.getEntry(i))
        
        return entries

    # Exception returns feed image    
    def getImage(self):
        try:
            image = self.data.feed.image
        except:
            image = "No image available"
        return image

class Entry:

    def __init__(self, title, link, description, published):
        self.title = title
        self.link = link
        self.description = description
        self.published = published
    
    # Method returns entry title
    def getTitle(self):
        return self.title

    # Method returns entry link
    def getLink(self):
        return self.link

    # Method returns entry description
    def getDescription(self):
        return self.description
    
    # Method parses and returns entry publish date
    def getPublished(self):
        return parser.parse(self.published).strftime("%d-%m-%Y")


    

    
