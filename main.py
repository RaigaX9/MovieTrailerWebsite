import fresh_tomatoes
import webbrowser

###########################################
#                 CLASS                   #
###########################################
#Setting up the class for MovieTrailerWebsite
class MTW():
    def __init__(self, title, storyline, poster, youtubetrailer):
        #Initializes up title, storyline??, poster, youtubetrailer
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = youtubetrailer
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)

###########################################
#            RETRIEVE MOVIES              #
###########################################

starwars7 = MTW("Star Wars Episode VII: The Force Awakens", "Return of the REAL Star Wars saga.",
                "http://vignette2.wikia.nocookie.net/starwars/images/f/fd/Star_Wars_Episode_VII_The_Force_Awakens.jpg/revision/latest?cb=20151018162823",
                "https://www.youtube.com/watch?v=sGbxmsDFVnE")
mymovies = [starwars7]
fresh_tomatoes.open_movies_page(mymovies)