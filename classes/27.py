#multiple method
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites") #name=Favorites
my_playlist.add_song("Bohemian Rhapsody") #Added: Bohemian Rhapsody
my_playlist.add_song("Stairway to Heaven") #Added: Stairway to Heaven
my_playlist.show_songs() #Playlist 'Favorites':
#- Bohemian Rhapsody
#- Stairway to Heaven