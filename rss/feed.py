import feedparser
import datetime
import dateutil.parser as parser

class Feed:

    def __init__(self, url): 
        try: 
            self.data = feedparser.parse(url)
        except:
            print("Error. Could not parse URL")

    def getTitle(self):
        try:
            title = self.data.feed.title
        except: 
            title = "No title available"
        finally:
            return title

    def getLink(self):
        try:
            link = self.data.feed.link
        except:
            link = "No link available"
        finally: 
            return link

    def getDescription(self):
        try:
            description = self.data.feed.description
        except:
            description = "No description"
        finally:
            return description
    
    def getInfo(self):
        try:
            description = self.data.feed.info
        except:
            description = "No descripton available"
        finally:
            return description
    

    def getPublished(self):
        try:
            published = parser.parse(self.data.feed.published).strftime("%A %d-%m-%Y %H:%M")
        except:
            published = "No publish date available"
        finally:
            return published

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
                summary = entry.summary
            except:
                summary = "No entry summary available"
            try: 
                published = entry.published
            except:
                published = "No entry publish date available"
            
            entry = Entry(title, link, summary, published)
            
        except:
            entry = Entry("No entry title available", "No entry link available", "No entry summary available", "No entry publish date available")

        finally:
            return entry

    def getLength(self):
        try:
            length = len(self.data.entries)
        except:
            length = 0
        finally:
            return length

        
    def getEntries(self):
        entries = []

        for i in range(self.getLength()):
            entries.append(self.getEntry(i))
        
        return entries

        
    def getImage(self):
        try:
            image = self.data.feed.image
        except:
            image = "No image available"
        print(image)
        return image

class Entry:

    def __init__(self, title, link, description, published):
        self.title = title
        self.link = link
        self.description = description
        self.published = published

    def getTitle(self):
        return self.title

    def getLink(self):
        return self.link

    def getDescription(self):
        return self.description
    
    def getPublished(self):
        return parser.parse(self.published).strftime("%A %d-%m-%Y %H:%M")


    

    
