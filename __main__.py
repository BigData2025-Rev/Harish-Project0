import csv
import pandas as pd
from track import Track

track_list = []

with open('circuits.csv', 'r') as circuits:
    csv_reader = csv.reader(circuits)
    next(csv_reader, None)
    for circuitId, circuitRef, name, location, country, lat, lng, alt, url in csv_reader:
        track_list.append(Track(circuitId, circuitRef, name, location, country, lat, lng, alt, url))

df = pd.DataFrame.from_records([track.to_dict() for track in track_list])
df.rename(columns={'id' : 'ID', 'ref' : 'Reference', 'name' : 'Name', 'location' : 'Location', 'country' : 'Country', 'lat' : 'Latitude', 'lng' : 'Longitude', 'alt' : 'Altitude', 'url' : 'URL'}, inplace=True)

with pd.option_context('display.max_rows', None):
    print(df.to_string(index=False))