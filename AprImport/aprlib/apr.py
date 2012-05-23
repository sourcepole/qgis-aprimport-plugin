import apr_parser

class Entry:
    "APR entry containing key/value properties"
    def __init__(self, apr,  e):
        self.__apr = apr
        self.tag = e['tag']
        self.id = e['id']
        self.properties = e['properties']
    
    def value(self, key):
        "Value of property with given name"
        return self.properties[key]

    def ref(self, key):
        "Entry referenced by property with given name"
        return self.__apr.entry(self.value(key))

    def refs(self, key):
        "Entries referenced by id list property with given name"
        return self.__list_entries(self.value(key))

    def nested_properties(self):
        "Automatic derefenced properties"
        props = {}
        for key, val in self.properties.iteritems():
            refentry = self.__apr.checked_entry(key, val)
            if refentry is not None:
                props[key] = refentry
            else:
                props[key] = val
        return props

    def __list_entries(self, idlist):
        "All Entries with id from idlist"
        return map(lambda k: self.__apr.entry(k), idlist) #map(self.__apr.entry(id) for id in idlist) #

    def __repr__(self):
        try:
            return ('%s.%d=' + str(self.nested_properties())) % (self.tag, self.id)
        except TypeError:
            return '((TypeError))'


REF_TAGS = ['AttrRules', 'BandStats', 'BgColor', 'BTab', 'Class', 'Child', 'ClrMap', 'Color', 'Colors', 'Dpy', 'FieldNames', 'Fields', 'FileName', 'FormatNumb', 'Graphics', 'Legend', 'MapBox', 'MouseLoc', 'Name', 'NullSym', 'NullValues', 'OutlineColor', 'PixelLUT', 'SelBits', 'Source', 'Symbols', 'StatValues', 'Threshold', 'TOCWidth', 'TxPos', 'Type', 'Win'] #Cause recursion: 'Btab', 'Client', 'FSrc'
BACKREF_TAGS = ['View']

class Apr:
    "APR file reader"
    def __init__(self, fn):
        self.fn = fn
        self.__entries = {}
    
    def parse(self):
        f = open(self.fn)
        entries = apr_parser.parse('apr', f.read())
        self.version = entries.pop(0)
        for entry in entries:
            self.__entries[entry['id']] = Entry(self, entry)
    
    # --- entry access

    def entry(self, id):
        "Entry with a given id"
        return self.__entries[int(id)]

    def checked_entry(self, tag, id):
        "Entry with a given tag and id"
        if isinstance(id, list):
            return map(lambda k: self.checked_entry(tag, k), id)
        entry = None
        try:
            entry = self.__entries[int(id)]
            if (entry.tag != tag) and (not tag in REF_TAGS) or (tag in BACKREF_TAGS):
                #print "Found tag '%s' does not match given tag '%s'" % (entry.tag, tag)
                entry = None
        except ValueError:
            pass
        except KeyError:
            pass
        except TypeError:
            pass
        return entry

    def tag_entries(self, tag):
        "All entries with a given tag"
        return filter(lambda x: x.tag == tag, self.__entries.values())

    # --- APR information queries
    
    def views(self):
        return self.tag_entries('View')


if __name__ == '__main__':
    from sys import argv, stdin
    if len(argv) >= 2:
        aprreader = Apr(argv[1])
        aprreader.parse()
        for view in aprreader.views():
            print "View '%s':" % view.value('Name')
            for theme in view.refs('Theme'):
                print "  %s" % theme.value('Name')
    else: print >>sys.stderr, 'Args: <filename>'
