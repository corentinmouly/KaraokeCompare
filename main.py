from classes.textparser import TextParser
from classes.soundcomparator import SoundComparator

from twisted.internet import task
from twisted.internet import reactor

from multiprocessing import Process

import threading

import pygame.mixer

import time,sys

timeout = 1 # Time in seconds

def doWork(mymusic):
    if __name__ != '__main__': # avoid that the main process execute that code
        SoundComparator().compare(mymusic)
    pass

def playMusic(name):
    fullname= "audio/"+name.rstrip()
    pygame.mixer.init()
    pygame.mixer.music.load(fullname)   # Loading music
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy(): #Play music until it finished
        i = 1    


if __name__ == '__main__': # if it is the main process
    if len(sys.argv) <= 1 :
        print("Erreur argument")
        exit()
    fileLy = TextParser(sys.argv[1])
    mymusic = fileLy.getMusic()

    print(mymusic.name)
    l = task.LoopingCall(doWork,mymusic)
    l.start(timeout) # call every second
    
    # Clean file
    filerec = open("score/party.txt", "w") 
    filerec.close()
    
    p = Process(target=playMusic, args=(str(mymusic.name),)) # process playing music
    p2 = Process(target=reactor.run, args=()) #process loop compare
    p2.start()    
    p.start()
    p.join()
    p2.terminate()

    #Count number of points
    filerec = open("score/party.txt", "r") 
    mesure = 0
    for data in filerec.readlines(): 
        mesure = mesure + int(data)
    filerec.close()
    print("Nombre de points totaux :",mesure)

