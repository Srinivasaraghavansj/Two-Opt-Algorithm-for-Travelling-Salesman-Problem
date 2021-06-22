"""
This file contains the code for PART 1. Although it has been developed for running with live visualization as ipynb,
the code works without visualization in this py file. For visualization please check the plots folder and
TSP_with_graphics.ipynb. The output of this py file is appended to appropriate text files in the results folder.
"""

import random
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from multiprocessing import Process
# from matplotlib import style
from multiprocessing import Pool
random.seed(195470)
# style.use('fivethirtyeight')
import os
from time import time
class tsp():
    #initialization
    def __init__(self,fName):
        self.fName = fName
        self.data = {}
        self.tour = []
        self.init_tour = []
        self.distance = None
        self.bestMove = None
        
    def euclideanDistance(self, c1, c2):
        """
        Distance between two cities
        """
        d1 = self.data[c1]
        d2 = self.data[c2]
        return math.sqrt( (d1[0]-d2[0])**2 + (d1[1]-d2[1])**2 )

    #Reads TSP file and randomly jumbles it as initialization of Tour
    def InitializeTour(self):
        self.readInstance()
        datac = self.data.copy()
        keys_ = list(datac.keys())
        random.shuffle(keys_)
        self.tour = keys_
        self.init_tour = keys_
        return keys_

    def readInstance(self):
        """
        Reading an instance from fName
        """
        THIS_FOLDER = os.getcwd()
        my_file = os.path.join(THIS_FOLDER, self.fName)
        file = open(my_file, 'r')
        self.genSize = int(file.readline())
        self.data = {}
        for line in file:
            (cid, x, y) = line.split()
            self.data[int(cid)] = (int(x), int(y))
        file.close()

    #Fetches tour cost    
    def getTourCost(self):
        return self.distance
    
    #It swaps given 2 edges and its respective tour cost
    def SwapCost(self,i,j,T):
        T_new = self.UpdateTour(T,[i-1,j+1]) #New temporary tour with the edge swap
        return self.computeTourCost_noSave(T_new) #returns cost of temp tour
    
    #Computes tour cost aka total distance in temporary variables
    def computeTourCost_noSave(self,T):
        distance  = self.euclideanDistance(T[0], T[len(T)-1])
        for i in range(1, len(T)-1):
            distance += self.euclideanDistance(T[i], T[i+1])
        return distance

    #Computes tour cost aka total distance
    def computeTourCost(self,T):
        self.distance  = self.euclideanDistance(T[0], T[len(T)-1])
        for i in range(1, len(T)-1):
            self.distance += self.euclideanDistance(T[i], T[i+1])
        return self.distance

    #Executes updation of tour with best move be swapping the edges
    def UpdateTour(self,T, bestMove): 
        i,j =  bestMove
        a = T[:] #Making a copy of T
        a[i:j]=T[j - 1:i - 1:-1]#When the edges get swapped, all the cities in-between get reversed as well
        #^Easy to understand when visualized
        return a

    #Given basic algorithm - just modified slightly to add prints and graphs
    def basic_two_opt_search(self):
        start = time()
        print("BASIC 2 OPT",self.fName)
        with open(f"results/{self.fName} VAR 0.txt", "a") as myfile:
                    myfile.write(f"\n\n\n\n")
        #To plot live graph for visualization
        fig = plt.figure(figsize=(10,10))
        ax1 = fig.add_subplot(1,1,1)
        plt.ion()
        fig.show()
        self.tour = self.InitializeTour()
        ax1.clear()
        X = []
        y = []
        for i in self.tour:
            X.append(self.data[i][0])
            y.append(self.data[i][1])
        X.append(self.data[1][0])
        y.append(self.data[1][1])
        ax1.plot(X,y)
        ax1.scatter(X,y)
        fig.canvas.draw()

        #Given algorithm   
        notOpt = True
        n = len(self.tour)
        while notOpt:
            notOpt = False
            i=1
            currBest = self.computeTourCost(self.tour)
            while i < n-2:
                j=i+2
                while j < n:
                    D = self.SwapCost(i + 1, j - 1, self.tour)
                    if D < currBest:
                        bestMove = [i,j]
                        currBest = D
                        notOpt = True
                    j+=1
                i+=1
            if notOpt:
                self.tour = self.UpdateTour(self.tour, bestMove)
                #To plot live graph for visualization
                ax1.clear()
                X = []
                y = []
                for i in self.tour:
                    X.append(self.data[i][0])
                    y.append(self.data[i][1])
                X.append(self.data[1][0])
                y.append(self.data[1][1])
                ax1.plot(X,y)
                ax1.scatter(X,y)
                fig.canvas.draw()
                #Printing and saving results in txt files
                print("Best Move",bestMove)
                print("Tour Cost",self.computeTourCost(self.tour))
                with open(f"results/{self.fName} VAR 0.txt", "a") as myfile:
                    myfile.write(f"\nBestMove: {bestMove}  Tour Cost: {self.computeTourCost(self.tour)}")
        with open(f"results/{self.fName} VAR 0 time.txt", "a") as myfile:
                    myfile.write(f"\nTime taken: {time()-start}")

    #Function for Variant 1 from question
    def var_1_edge_two_opt_search(self,Threshold=15,seed=195470):
        #seed: random seed; Threshold: Number of iterations to escape if stuck in local minima
        start = time()
        print("VAR 1",self.fName)
        with open(f"results/{self.fName} VAR 1.txt", "a") as myfile:
                    myfile.write(f"\n\n\n\n")
        random.seed(seed)
        #To plot live graph for visualization
        fig = plt.figure(figsize=(10,10))
        ax1 = fig.add_subplot(1,1,1)
        plt.ion()
        fig.show()
        self.tour = self.InitializeTour()
        ax1.clear()
        X = []
        y = []
        for i in self.tour:
            X.append(self.data[i][0])
            y.append(self.data[i][1])
        X.append(self.data[1][0])
        y.append(self.data[1][1])
        ax1.plot(X,y)
        ax1.scatter(X,y)
        fig.canvas.draw()
        notOpt = True
        n = len(self.tour)
        count = 0
        while True:
            notOpt = False
            i=random.randint(1,n-1)#Choose random edge to find swappable edge
            currBest = self.computeTourCost(self.tour)
            j=1
            while j < n:
                if abs(j-i)<=1:#if j&i make an edge or are the same, skip it
                    j+=1
                    continue
                D = self.SwapCost(i + 1, j - 1, self.tour)
                if D < currBest:
                    bestMove = [i,j]
                    currBest = D
                    notOpt = True
                j+=1
            if not notOpt:
                count+=1
            if count>=Threshold:#To limit iterations without improvement
                break
            if notOpt:
                self.tour = self.UpdateTour(self.tour, bestMove)
                #To plot live graph for visualization
                ax1.clear()
                X = []
                y = []
                for i in self.tour:
                    X.append(self.data[i][0])
                    y.append(self.data[i][1])
                X.append(self.data[1][0])
                y.append(self.data[1][1])
                ax1.plot(X,y)
                ax1.scatter(X,y)
                fig.canvas.draw()
                #Printing and saving results in txt files
                print("Best Move",bestMove)
                print("Tour Cost",self.computeTourCost(self.tour))
                with open(f"results/{self.fName} VAR 1.txt", "a") as myfile:
                    myfile.write(f"\nBestMove: {bestMove}  Tour Cost: {self.computeTourCost(self.tour)}")
        with open(f"results/{self.fName} VAR 1 time.txt", "a") as myfile:
                    myfile.write(f"\nTime taken: {time()-start}")

    #Function for varaint 2 from question - same as above, with minor change - marked below
    def var_2_first_edge_two_opt_search(self,Threshold=15,seed=195470):
        #seed: random seed; Threshold: Number of iterations to escape if stuck in local minima
        start = time()
        print("VAR 2",self.fName)
        with open(f"results/{self.fName} VAR 2.txt", "a") as myfile:
                    myfile.write(f"\n\n\n\n")
        random.seed(seed)
        #To plot live graph for visualization
        fig = plt.figure(figsize=(10,10))
        ax1 = fig.add_subplot(1,1,1)
        plt.ion()
        fig.show()
        self.tour = self.InitializeTour()
        ax1.clear()
        X = []
        y = []
        for i in self.tour:
            X.append(self.data[i][0])
            y.append(self.data[i][1])
        X.append(self.data[1][0])
        y.append(self.data[1][1])
        ax1.plot(X,y)
        ax1.scatter(X,y)
        fig.canvas.draw()
        notOpt = True
        n = len(self.tour)
        count = 0
        while True:
            notOpt = False
            i=random.randint(1,n-1)#Choose random edge to find swappable edge
            currBest = self.computeTourCost(self.tour)
            j=1
            while j < n:
                if abs(j-i)<=1:#if j&i make an edge or are the same, skip it
                    j+=1
                    continue
                D = self.SwapCost(i + 1, j - 1, self.tour)
                if D < currBest:
                    bestMove = [i,j]
                    currBest = D
                    notOpt = True
                    break#####Here is the change to choose the first seen improvement instead of searching for all possibilities and improving using the best one
                j+=1
            if not notOpt:
                count+=1
            if count>=Threshold:#To limit iterations without improvement
                break
            if notOpt:
                self.tour = self.UpdateTour(self.tour, bestMove)
                #To plot live graph for visualization
                ax1.clear()
                X = []
                y = []
                for i in self.tour:
                    X.append(self.data[i][0])
                    y.append(self.data[i][1])
                X.append(self.data[1][0])
                y.append(self.data[1][1])
                ax1.plot(X,y)
                ax1.scatter(X,y)
                fig.canvas.draw()
                #Printing and saving results in txt files
                print("Best Move",bestMove)
                print("Tour Cost",self.computeTourCost(self.tour))
                with open(f"results/{self.fName} VAR 2.txt", "a") as myfile:
                    myfile.write(f"\nBestMove: {bestMove}  Tour Cost: {self.computeTourCost(self.tour)}")
        with open(f"results/{self.fName} VAR 2 time.txt", "a") as myfile:
                    myfile.write(f"\nTime taken: {time()-start}")

tsp19_1 = tsp("inst-19.tsp")
tsp20_1 = tsp("inst-20.tsp")
tsp7_1 = tsp("inst-7.tsp")
tsp19_2 = tsp("inst-19.tsp")
tsp20_2 = tsp("inst-20.tsp")
tsp7_2 = tsp("inst-7.tsp")
tsp19_3 = tsp("inst-19.tsp")
tsp20_3 = tsp("inst-20.tsp")
tsp7_3 = tsp("inst-7.tsp")

"""
Since graphs will only work in ipynb version in browser, we can run the above operations parallely
without any issues.

Initializing runs for all 3 given TSP files with all variants parallely
"""

processes = []
p1 = Process(target=tsp19_1.var_1_edge_two_opt_search)
processes.append(p1)
p1.start()

p2 = Process(target=tsp19_2.var_2_first_edge_two_opt_search)
processes.append(p2)
p2.start()


p3 = Process(target=tsp20_1.var_1_edge_two_opt_search)
processes.append(p3)
p3.start()

p4 = Process(target=tsp20_2.var_2_first_edge_two_opt_search)
processes.append(p4)
p4.start()

p5 = Process(target=tsp7_1.var_1_edge_two_opt_search)
processes.append(p5)
p5.start()

p6 = Process(target=tsp7_2.var_2_first_edge_two_opt_search)
processes.append(p6)
p6.start()

p7 = Process(target=tsp19_3.basic_two_opt_search)
processes.append(p7)
p7.start()


p8 = Process(target=tsp20_3.basic_two_opt_search)
processes.append(p8)
p8.start()

p9 = Process(target=tsp7_3.basic_two_opt_search)
processes.append(p9)
p9.start()

for i in processes:
    i.join()