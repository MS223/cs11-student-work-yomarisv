class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def artist_of_song(self,artist):
        self.artist = artist

one_dance = Song(["you know that I don't play",
                   "streets not safe",
                   "but I never run away"])

controlla_a = Song(["I think I'd lie for you",
                      "I think I'd die for you",
                      "Jodeci Cry for you",])

one_dance.sing_me_a_song()
controlla_a.sing_me_a_song()
