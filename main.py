import pygame
from Window import *
from multiprocessing import Process
from threading import Thread
   

if __name__ == '__main__':
    window = Window()
    playerProcess = Thread(target=window.runPlayers,args=())
    bubbleProcess = Thread(target=window.runBubble,args=())

    playerProcess.start()
    bubbleProcess.start()
    