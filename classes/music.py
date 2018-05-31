## @package Music
#  Documentation for this module.
#
# The Music class descibe the path of the song and all of the datas about his lyrics
class Music:
    
    ## @var song
    #  variable containing the path of the song 
    
    ## @var dictionnary
    #  variable containing the dictionnary ( key : time, values : lyrics)   
    
    ## The constructor
    def __init__(self,song,dictionnary):
        self.name = song
        self.lyrics = dictionnary
    
    ## getSong function
    #  Return the path of the song    
    def getSong():
        return name
    
    ## getHeight function
    #  @param self The object pointer
    #  @param time the instant in seconds
    #  Return the lyrics at this period    
    def getHeight(self,time):
        height = None
        if time in self.lyrics:
            height = self.lyrics[time]
        return height