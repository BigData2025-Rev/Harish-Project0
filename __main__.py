import csv
import sys
import pandas as pd
from track import Track

track_list = []
tournament = []
not_complete = True

with open('circuits.csv', 'r') as circuits:
    csv_reader = csv.reader(circuits)
    next(csv_reader, None)
    for id, ref, name, location, country, lat, lng, alt, url in csv_reader:
        track_list.append(Track(id, ref, name, location, country, lat, lng, alt, url))
df = pd.DataFrame.from_records([track.to_dict() for track in track_list])
df.rename(columns={'id' : 'ID', 'ref' : 'Reference', 'name' : 'Name', 'location' : 'Location', 'country' : 'Country', 'lat' : 'Latitude', 'lng' : 'Longitude', 'alt' : 'Altitude', 'url' : 'URL'}, inplace=True)

print('Welcome to the International Racing Tournament Planner!\n\nYou can use this to design your own tournament by selecting tracks from around the world. Duplicating tracks isn\'t allowed. You must have between 3 to 5 tracks.')

def view_all():
    with pd.option_context('display.max_rows', None):
                print(df.to_string(index=False))

def current():
    df_tourney = pd.DataFrame.from_records([track.to_dict() for track in tournament])
    df_tourney.rename(columns={'id' : 'ID', 'ref' : 'Reference', 'name' : 'Name', 'location' : 'Location', 'country' : 'Country', 'lat' : 'Latitude', 'lng' : 'Longitude', 'alt' : 'Altitude', 'url' : 'URL'}, inplace=True)
    print('Current Tournament:\n')
    print(df_tourney.to_string(index=False))
    print('\n')

def add():
    result = None
    if len(tournament) < 5:
        while result == None:
            current()
            text = input('Type the Reference of the track you want to add: ')
            result = next((x for x in track_list if x.ref == text), None)
            if(result == None): print('That track doesn\'t exist. Please check the track list and try again.\n')
            else: 
                check = next((x for x in tournament if x.ref == text), None)
                if check == None: 
                    tournament.append(result)
                    print(result.name + ' added!')
                else: 
                    print('That track has already been added. Choose another one.\n')
                    result = None
    else: print('Maximum number of tracks reached. To add another track, delete one first.')

def delete():
    result = None
    if len(tournament) > 0:
        current()
        text = input('Type the Reference of the track you want to delete: ')
        result = next((x for x in tournament if x.ref == text), None)
        while result == None: 
            text = input('That track doesn\'t exist in your tournament. Check your list and try again: ')
            result = next((x for x in tournament if x.ref == text), None)
        tournament.remove(result)
        print(result.name + ' deleted!')
    else: print('Your tournament is empty, there\'s nothing to delete.')

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

while not_complete:
    try:
        text = input('\nOptions:' +
      '\n\t- Type \"view\" to view all tracks.' +
      '\n\t- Type \"add\" to add a track to your tournament.' +
      '\n\t- Type \"delete\" to remove a track from your tournament.' +
      '\n\t- Type \"current\" to view your current tournament.' +
      '\n\t- Type \"done\" to finalize your tournament.' +
      '\n\t- Type \"exit\" to cancel and quit.\n')
    except ValueError:
        print("Oops! Invalid input detected.")
        continue
    else:
        if text == 'view':
            view_all()
        elif text == 'add':
            add()
        elif text == 'delete':
            delete()
        elif text == 'current':
            current()
        elif text == 'done':
            print('hey')
        elif text == 'exit':
            exit_program()
        else:
            print('Not a valid option! Check the options and try again.')