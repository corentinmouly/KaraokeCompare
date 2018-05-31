from classes.music import Music
from classes.lyric import Lyric
import sys

## @package TextParser
#  Documentation for this module.
#
#  The TextParser read the .txt containing all of the informations about the track
#  Only the GetMusic function need to be used by user the user
#  The others ones are made to delimate the differents segments of the file
#  The Headers : MP3 file location
#  The Lyrics : Duration and Height for each syllab 

class TextParser :
    
    ## @var text
    #  variable containing all of the content to parse   

    ## @var dictionnary
    #  Dictionnary of every syllab of the lyrics with their heights and duration
    #  The key of the dictionnary is the position in seconds (int) of the syllab
    #  The Value is an Lyric object containing all of the data 
    #  about the syllab (duration,height,text)    

    ## The constructor
    #  @param self The object pointer
    #  @param nameFile The Path to the text File
    #  Create an TextParser with the text file
    #  Read all the content of the file and put it on the variable text
    def __init__(self,nameFile):
        self.textFile = nameFile
        file = open(nameFile)
        self.text = file.readlines()
        file.close()        
        
    ## GetHeaders function
    #  @param self The object pointer
    #  Parse all of the text variable
    #  Headers are lines beginning by '#'
    #  Extract the needed information
    #  MP3  for MP3 file path 
    #  And return those informations
    def getHeaders(self):
        for line in self.text:
            if line.find("MP3") != -1 :
                song = line.split(":")[1]
                break
            if line[0] != '#':
                break
        return song;
     
    ## getVoice function
    #  @param self The object pointer
    #  Return a dictionnary containing all the lyrics
    #  and their positions on the track
    #  The key of the dictionnary is the position in seconds (int) of the syllab
    #  The Value is an Lyric object containing all of the data 
    #  about the syllab (duration,height,text)
    #  The format of the line is ": position duration height text" 
    #  So the function look only for the line beginning by ':'
    def getVoice(self):
        dictionnary={}
        for line in self.text:
            if line[0] == ':':
                voiceline=line.split(' ')
                lyric = Lyric(int(voiceline[2]),int(voiceline[3]),voiceline[4].strip())
                dictionnary[int(voiceline[1])] = lyric
        return dictionnary
        
    ## getMusic function
    #  @param self The object pointer
    #  Return a Music object containing all the datas provide by
    #  the GetHeader and GetVoice functions    
    def getMusic(self):
        song=self.getHeaders()
        dictionnary = self.getVoice()
        music = Music(song,dictionnary)
        return music
        