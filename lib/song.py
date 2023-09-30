class Song():
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre) -> None:       
        self.name, self.artist, self.genre = name, artist, genre
        Song.count += 1
        Song.genres.append(genre)
        Song.artists.append(artist)        
        Song.genre_count[genre] = Song.genre_count[genre] + 1 if genre in Song.genre_count else 1
        Song.artist_count[artist] = Song.artist_count[artist] + 1 if artist in Song.artist_count else 1
        

        