import apr_parser

RESOLVE_LIST = {
               'FTheme': ['Source'], 
               'ITheme': ['Source'], 
               'ShpSrc': ['Name',  'FTab'], 
               'FTab': ['BTab',  'FSrc'], 
               'GSrc': ['Name'], 
               'SrcName': ['FileName'], 
               'dBASE': ['FileName']
               }

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

    def resolve(self, key):
        "Replace reference with resolved entry"
        self.properties[key] = self.ref(key)
        return self

    def resolve_properties(self):
        "Replace important properties"
        if RESOLVE_LIST.has_key(self.tag):
            for key in RESOLVE_LIST[self.tag]:
              self.resolve(key)

    def __repr__(self):
        return ('%s.%d=' + str(self.properties)) % (self.tag, self.id)


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
        for entry in self.__entries.values(): entry.resolve_properties()
    
    # --- entry access

    def entry(self, id):
        return self.__entries[int(id)]

    def tag_entries(self, tag):
        return filter(lambda x: x.tag == tag, self.__entries.values())

    def list_entries(self, idlist):
        return map(lambda k: self.entry(k), idlist) #map(self.entry(id) for id in idlist) #

    # --- APR information queries
    
    def views(self):
        return self.tag_entries('View')
        
    def themes(self, view):
        return self.list_entries(view.value('Theme'))


if __name__ == '__main__':
    from sys import argv, stdin
    if len(argv) >= 2:
        apr = Apr(argv[1])
        apr.parse()
        for view in apr.views():
            print view
            for th in apr.themes(view): print th
    else: print >>sys.stderr, 'Args: <filename>'
