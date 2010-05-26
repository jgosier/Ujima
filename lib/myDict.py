class myDict(dict):
    """A case insensitive dictionary that only permits strings as keys."""
    def __init__(self, indict={}):
        dict.__init__(self)
        self._keydict = {}                      # not self.__keydict because I want it to be easily accessible by subclasses
        for entry in indict:
            self[entry] = indict[entry]         # not dict.__setitem__(self, entry, indict[entry]) becasue this causes errors (phantom entries) where indict has overlapping keys... 

    def findkey(self, item):
        """A caseless way of checking if a key exists or not.
        It returns None or the correct key."""
        if not isinstance(item, str): raise TypeError('Keywords for this object must be strings. You supplied %s' % type(item))
        key = item.lower()
        try:
            return self._keydict[key]
        except:
            return None
    
    def changekey(self, item):
        """For changing the casing of a key.
        If a key exists that is a caseless match for 'item' it will be changed to 'item'.
        This is useful when initially setting up default keys - but later might want to preserve an alternative casing.
        (e.g. if later read from a config file - and you might want to write back out with the user's casing preserved).
        """
        key = self.findkey(item)           # does the key exist
        if key == None: raise KeyError(item)
        temp = self[key]
        del self[key]
        self[item] = temp
        self._keydict[item.lower()] = item
            
    def lowerkeys(self):
        """Returns a lowercase list of all member keywords."""
        return self._keydict.keys()

    def __setitem__(self, item, value):             # setting a keyword
        """To implement lowercase keys."""
        key = self.findkey(item)           # if the key already exists
        if key != None:
            dict.__delitem__(self,key)
        self._keydict[item.lower()] = item
        dict.__setitem__(self, item, value)

    def __getitem__(self, item):
        """To implement lowercase keys."""
        key = self.findkey(item)           # does the key exist
        if key == None: raise KeyError(item)
        return dict.__getitem__(self, key) 

    def __delitem__(self, item):                # deleting a keyword
        key = self.findkey(item)           # does the key exist
        if key == None: raise KeyError(item)
        dict.__delitem__(self, key)
        del self._keydict[item.lower()]

    def pop(self, item, default=None):
        """Correctly emulates the pop method."""
        key = self.findkey(item)           # does the key exist
        if key == None:
            if default == None:
                raise KeyError(item)
            else:
                return default
        del self._keydict[item.lower()]
        return dict.pop(self, key)
    
    def popitem(self):
        """Correctly emulates the popitem method."""
        popped = dict.popitem(self)
        del self._keydict[popped[0].lower()]
        return popped
    
    def has_key(self, item):
        """A case insensitive test for keys."""
        if not isinstance(item, str): return False               # should never have a non-string key
        return self._keydict.has_key(item.lower())           # does the key exist
        
    def __contains__(self, item):
        """A case insensitive __contains__."""
        if not isinstance(item, str): return False               # should never have a non-string key
        return self._keydict.has_key(item.lower())           # does the key exist

    def setdefault(self, item, default=None):
        """A case insensitive setdefault.
        If no default is supplied it sets the item to None"""
        key = self.findkey(item)           # does the key exist
        if key != None: return self[key]
        self.__setitem__(item, default)
        self._keydict[item.lower()] = item
        return default
    
    def get(self, item, default=None):
        """A case insensitive get."""
        key = self.findkey(item)           # does the key exist
        if key != None: return self[key]
        return default

    def update(self, indict):
        """A case insensitive update.
        If your dictionary has overlapping keys (e.g. 'FISH' and 'fish') then one will overwrite the other.
        The one that is kept is arbitrary."""
        for entry in indict:
            self[entry] = indict[entry]         # this uses the new __setitem__ method            

    def copy(self):
        """Create a new caselessDict object that is a copy of this one."""
        return caselessDict(self)

    def dict(self):
        """Create a dictionary version of this caselessDict."""
        return dict.copy(self)
    
    def clear(self):
        """Clear this caselessDict."""
        self._keydict = {}
        dict.clear(self)

    def __repr__(self):
        """A caselessDict version of __repr__ """
        return 'caselessDict(' + dict.__repr__(self) + ')'
    
    

    
##############################################################



## brief test stuff
#if __name__ == '__main__':
#    print 'caselessDict Tests'
#    b = { 'FISH' : 'fish' }
#    a = caselessDict(b)
#    print "An apparently standard dict."
#    print a
#    print "a['FisH'] = ", a['FisH']
#    b = {1 : 'fail'}
#    print "We will now check that creating a caselessDict with an integer key fails."
#    try:
#        print caselessDict(b)
#        print "oops - that shouldn't have worked"
#    except Exception, e:
#        print 'Exception : '
#        print e
#        print 'Good'
#    print 'Testing deleting a key'
#    del a['Fish']
#    print "del a['Fish']\na = ", a
#    a['FISH'] = 'fish'
#    print 'Reset a[\'FISH\'] again and then pop the value : ', a.pop('fish')
#    print 'Reset a[\'FISH\'] again and then test if it has the key : '
#    a['FISH'] = 'fish'
#    print 'a.has_key(\'fish\') : ', a.has_key('fish')
#    print 'Let\'s test the __contains__ method by doing an if \'FiSH\' in a test :', 'FiSH' in a
#    print 'setdefault, first with the keyword \'FISh\' and default of None. Then with keyword \'FROG\' and default None.'
#    print a.setdefault('FISh', None)
#    print a.setdefault('FROG', None)
#    print a
#    print 'Next get - but with keys \'FIsH\' and \'PIANO\' and default of False.'
#    print a.get('FIsH', False)
#    print a.get('PIANO', False)
#    print 'An update - we\'ll add the key \'PIANO\'.'
#    a.update({'PIANO' : ' A Piano'})
#    print a
#    print 'Popitem :', 
#    print a.popitem()
#    print a
#    b = a.copy()
#    b.clear()
#    b['FISH'] = 'fish'
#    print 'The following is a copy, then cleared (clear method), a new key added.'
#    print 'We then test the type of the new dictionary...'
#    print b
#    print type(b)
#    print 'The keys :'
#    print b.keys()
#    