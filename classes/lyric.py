## @package Lyric
#  Documentation for this module.
#
#  The Lyric oject describe a syllab of the lyrics of the music.
#  It contains severals attributes (duration,height,text) of this syllab.

class Lyric:
    
    ## @var duration
    #  variable containing the duration of the syllab
    
    ## @var height
    #  variable containing the height of the syllab 
    
    ## @var text
    #  variable containing the text of the syllab    
    
    ## The constructor
    def __init__(self,duration,height,text):
        self.duration = duration
        self.height = height
        self.text = text
    
    ## The representation of the object    
    def __repr__ (self):
        return "{0} sec at {1} ({2})".format(
                self.duration, self.height, self.text)        
    
    ## getDuration function
    #  @param self The object pointer
    #  Return the duration of the syllab
    def getDuration(self):
        return duration
    
    ## getHeight function
    #  @param self The object pointer
    #  Return the height of the syllab    
    def getHeight(self):
        return height
    
    ## getText function
    #  @param self The object pointer
    #  Return the text of the syllab    
    def getText(self):
        return text