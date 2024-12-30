import csv
import sys
import pandas as pd
from track import Track

track_list = []
not_complete = True

with open('circuits.csv', 'r') as circuits:
    csv_reader = csv.reader(circuits)
    next(csv_reader, None)
    for circuitId, circuitRef, name, location, country, lat, lng, alt, url in csv_reader:
        track_list.append(Track(circuitId, circuitRef, name, location, country, lat, lng, alt, url))

df = pd.DataFrame.from_records([track.to_dict() for track in track_list])
df.rename(columns={'id' : 'ID', 'ref' : 'Reference', 'name' : 'Name', 'location' : 'Location', 'country' : 'Country', 'lat' : 'Latitude', 'lng' : 'Longitude', 'alt' : 'Altitude', 'url' : 'URL'}, inplace=True)

print('Welcome to the International Racing Tournament Planner!\n\nYou can use this to design your own tournament by selecting tracks from around the world. Duplicating tracks isn\'t allowed. You must have between 3 to 5 tracks.')

while not_complete:
    try:
        text = input('\n\nOptions:' +
      '\n\t- Type \"view\" to view all tracks.' +
      '\n\t- Type \"add\" to add a track to your tournament.' +
      '\n\t- Type \"delete\" to remove a track from your tournament.' +
      '\n\t- Type \"random\" to add a random number of tracks to your tournament.' +
      '\n\t- Type \"filter\" to filter tracks by country.' +
      '\n\t- Type \"done\" to finalize your tournament.' +
      '\n\t- Type \"exit\" to cancel and quit.\n\n')
    except ValueError:
        print("oops!")
        continue
    else:
        if text == 'view':
            with pd.option_context('display.max_rows', None):
                print(df.to_string(index=False))
        elif text == 'add':
            print('hey')
        elif text == 'delete':
            print('hey')
        elif text == 'random':
            print('hey')
        elif text == 'filter':
            print('hey')
        elif text == 'done':
            print('hey')
        elif text == 'exit':
            print('hey')

def exit_program():
    print("Exiting the program...")
    sys.exit(0)