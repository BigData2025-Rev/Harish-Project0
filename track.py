class Track:

    def __init__(self, id, ref, name, location, country, lat, lng, alt, url):
        self.id = id
        self.ref = ref
        self.name = name
        self.location = location
        self.country = country
        self.lat = lat
        self.lng = lng
        self.alt = alt
        self.url = url

    def __repr__(self):
        return ("%-30s %4.1f") % ("ID: " + self.id + " | Ref: " + self.ref + " | Name: " + self.name + " | Location: " + self.location + " | Country: " + self.country + " | Latitude: " + self.lat + 
        " | Longitude: " + self.lng + " | Altitude: " + self.alt + " | URL: " + self.url+ "\n")
    
    def to_dict(self):
        return {
            'id' : self.id,
            'ref' : self.ref,
            'name' : self.name,
            'location' : self.location,
            'country' : self.country,
            'lat' : self.lat,
            'lng' : self.lng,
            'alt' : self.alt,
            'url' : self.url
        }
