class Track:

    def __init__(self, id, ref, name, location, country, lat, lng, alt, url):
        self.__id = id
        self.__ref = ref
        self.__name = name
        self.__location = location
        self.__country = country
        self.__lat = lat
        self.__lng = lng
        self.__alt = alt
        self.__url = url

    @property
    def id(self):
        return self.__id
    
    @property
    def ref(self):
        return self.__ref
    
    @property
    def name(self):
        return self.__name
    
    @property
    def location(self):
        return self.__location
    
    @property
    def country(self):
        return self.__country
    
    @property
    def lat(self):
        return self.__lat
    
    @property
    def lng(self):
        return self.__lng
    
    @property
    def alt(self):
        return self.__alt
    
    @property
    def url(self):
        return self.__url
    
    def to_dict(self):
        return {
            'id' : self.__id,
            'ref' : self.__ref,
            'name' : self.__name,
            'location' : self.__location,
            'country' : self.__country,
            'lat' : self.__lat,
            'lng' : self.__lng,
            'alt' : self.__alt,
            'url' : self.__url
        }
