import math,sys,os
from scipy.io import wavfile
import numpy
import matplotlib.pyplot as plt
from scipy.fftpack import fft

## @package SoundComparator
#  Documentation for this module.
#
# The SoundComparator extract the sound from the record.
# It converts the sound in the number of the fundamental
# It compares the heights of the two signals
# It prints the points on a file

class SoundComparator :
    
    
    ## @var number
    #  variable containing the actual time in seconds    
    number = -1
    
    ## @var lastfreq
    #  variable containing the last height analyze    
    lastfreq = None
    
    ## @var timeremain
    #  variable containing the time remaining before the new notes    
    timeremain = 0
    
    ## @var fundamental
    #  variable containing all of the fundamentals    
    fundamental=[16,17,18,19,20,21,23,24,26,27,29,30,
                 32,34,36,38,41,43,46,49,51,55,58,62,
                65,69,74,78,83,87,92,98,104,110,117,123,
                 131,139,147,156,165,175,185,196,208,220,233,247,
                 262,277,294,311,330,349,370,392,415,440,466,494,
                 523,554,587,622,659,698,740,784,831,880,932,988,
                 1046,1109,1175,1244,1318,1397,1480,1568,1661,1760,1865,1975,
                 2093,2217,2349,2489,2637,2794,2960,3126,3322,3520,3729,3951,
                 4186,4435,4698,4978,5274,5588,5920,6272,6645,7040,7458,7902,
                 8372,8870,9396,9956,10548,117176,11840,12544,13290,14080,14918,15804,
                 16744,17740,18792,19912,21098]
    
    ## @var fs
    #  variable containing frequency of sample
    
    ## @var data
    #  variable containing all of the data of the music
    
    fs, data = wavfile.read('audio/Rec.wav') #file of the recording
    
    ## calculateheight function
    #  @param high the frequency of the fundamental
    #  Return the height of the sound depending of the array fundamental     
    @staticmethod
    def calculateheight(high):
        mesure = high
        i = 0
        
        while (mesure > abs(high-SoundComparator.fundamental[i])):
            mesure =  abs(high-SoundComparator.fundamental[i])
            i=i+1
            
        return i
        
    ## compareFreq function
    #  @param frequency Height of the syllab
    #  Calculate the number of point won for this syllab and write it on a file        
    @staticmethod
    def compareFreq(frequency):
        point = 0
        # Method 1
        score = abs(frequency - SoundComparator.lastfreq)
        
        if score == 0 :
            point = 6
        elif score == 1 :
            point = 5
        elif score == 2 :
            point = 4
        elif score == 3 :
            point = 3
        elif score == 4 :
            point = 2
        elif score == 5 :
            point = 1        
        
        
        # Method 2
        #score2 = abs((frequency % 12) - (SoundComparator.lastfreq % 12))
        #print(score2)
        #if score == 0 :
        #    point = 6
        #elif score == 1 :
        #    point = 4
        #elif score == 2 :
        #    point = 2  
        
        
        if(point != 0):
            print(point," point(s) gagne(s) !!")
            filerec = open("score/party.txt", "a") # Save points in a file 
            filerec.write(str(point)+"\n")
            filerec.close()
             

    ## findHeight function
    # Get an extract of one second of the sound on time
    # Apply an Fast Fourrier Transform
    # Return the fundamental frequency extract from the FFT 
    @staticmethod
    def findHeight():
        try :
            ecart1 = SoundComparator.fs*SoundComparator.number
            ecart2 = SoundComparator.fs*(SoundComparator.number+1)
            
            datalocal = SoundComparator.data[ecart1:ecart2]
            a = datalocal.T[0] # first channel
            b=[(ele/2**8.)*2-1 for ele in a] 
            c = fft(b) # calculate fourier transform 
            d = len(c)/2  # delete the symetry
            plt.plot(abs(c[:(int(d)-1)]),'r') 
            ax = plt.gca()
            line = ax.lines[0]
            high=line.get_ydata().argmax()
            
            calcfreq=SoundComparator.calculateheight(high)
            SoundComparator.compareFreq(calcfreq)
            plt.clf() #clean matplot figure
            plt.close()
        except :
            print("Lyrics ended")
        
    
    ## compare function
    #  @param mymusic Music to compare
    #  Get the lyric on real time from the music and start the comparaison by using the others methods 
    @staticmethod       
    def compare(mymusic):
        if SoundComparator.lastfreq != None:
            SoundComparator.findHeight()
        SoundComparator.number += 1
        SoundComparator.timeremain -= 1
        if not(SoundComparator.timeremain > 0) :
            freq = (mymusic.getHeight(SoundComparator().number))
            if freq != None :
                SoundComparator.lastfreq = freq.height
                SoundComparator.timeremain = freq.duration
            else :
                SoundComparator.lastfreq = None
                SoundComparator.timeremain = 0
        sys.stdout.write("{0} : {1}\n".format(str(SoundComparator.number),str(SoundComparator.lastfreq)))  # same as print
        sys.stdout.flush()