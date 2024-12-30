import csv
import pandas as pd
from track import Track

track_list = []

with open('circuits.csv', 'r') as circuits:
    csv_reader = csv.reader(circuits)
    next(csv_reader, None)
    for circuitId, circuitRef, name, location, country, lat, lng, alt, url in csv_reader:
        track_list.append(Track(circuitId, circuitRef, name, location, country, lat, lng, alt, url))

#print(track_list)

df = pd.DataFrame.from_records([track.to_dict() for track in track_list])
df.rename(columns={'id' : 'ID'}, inplace=True)
print(df)