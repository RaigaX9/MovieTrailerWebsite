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

#Creating various movie trailers based on their title, storyline, poster image and trailer video

#Star Wars Episode VII: The Force Awakens
starwars7 = MTW("Star Wars Episode VII: The Force Awakens",
                "Return of the REAL Star Wars saga.",
                "http://vignette2.wikia.nocookie.net/starwars/images/f/fd/Star_Wars_Episode_VII_The_Force_Awakens.jpg/revision/latest?cb=20151018162823",
                "https://www.youtube.com/watch?v=sGbxmsDFVnE")

#WALL-E
wallE = MTW("WALL-E",
            "Pixar's beloved animated robot love and adventure story.",
            "http://mtv.mtvnimages.com/shared/media/images/acovers/standard/dra300/a317/a31768yolvd.jpg",
            "https://www.youtube.com/watch?v=alIq_wG9FNk")

#Dragonball Z: Resurrection 'F'
dbzrF = MTW("Dragonball Z: Resurrection 'F'",
            "After the events of Battle of Gods, Goku and the other Z fighters must now face their old and greatest enemy again, Frieza.",
            "http://www.dragonballinsider.com/wp-content/uploads/2015/07/dbzrfjpg.jpg",
            "https://www.youtube.com/watch?v=WiONylGn8Xw")

#The Dark Knight
darkKnight = MTW("The Dark Knight",
                 "After the events of Batman Begins, Batman, or Bruce Wayne, must now face a bigger threat against the Joker.",
                "https://smilingldsgirl.files.wordpress.com/2013/06/xemphimso_ky-si-bong-dem-1.jpg",
                "https://www.youtube.com/watch?v=yrJL5JxEYIw")

#Deadpool
deadpool = MTW("Deadpool",
               "Marvel's super awesome, action-packed, fourth wall breaking, merc with the mouth Deadpool finally has his own movie!",
                "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/02cc1333658190.56b2c8ea3720a.png",
                "https://www.youtube.com/watch?v=ONHBaC-pfsk")

#The Avengers
avengers = MTW("The Avengers", "Join Iron Man, Captain America, Black Widow, Hulk, Thor, and Hawkeye teaming up to become the Avengers to fight against Loki and his evil army.",
                "http://billal-chendar.esy.es/img/culture/film/avengers.jpg",
                "https://www.youtube.com/watch?v=eOrNdBpGMv8")

#Print story lines for each movie
print starwars7.storyline
print wallE.storyline
print dbzrF.storyline
print darkKnight.storyline
print deadpool.storyline
print avengers.storyline

#Sets up the array for displaying each of the movie trailers
mymovies = [starwars7, wallE, dbzrF, darkKnight, deadpool, avengers]

#Create and run the HTML file
fresh_tomatoes.open_movies_page(mymovies)