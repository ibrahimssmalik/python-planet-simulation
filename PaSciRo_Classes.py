import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt
from IPython import get_ipython  
import numpy as np
import random
import time
import csv
import math
import os

##############################################################################
# Class to form each lifeform
class lifeform():
    # Defining attributes of each lifeform
    def __init__(self, steps, XMAX, YMAX, one, two, three, four, color):
        self.steps = steps
        self.XMAX = XMAX
        self.YMAX = YMAX
        self.one = one
        self.two = two
        self.three = three
        self.four = four
    # Method to color code and move code lifeform
    def col(self):
        if self.three == 0:
            self.steps = 4
            self.color = "tomato"
        elif self.three == 1:
            self.steps = 3
            self.color = "yellow"
        elif self.three == 2:
            self.steps = 2
            self.color = "royalblue"
    # Method to color code and move code lifeform for 3D Simulation        
    def col2(self):
        if self.four == 0:
            self.steps = 5
            self.color = "tomato"
        elif self.four == 1:
            self.steps = 4
            self.color = "yellow"
        elif self.four == 2:
            self.steps = 3
            self.color = "royalblue"
    # Method to move lifeform
    def move(self, lifeforms):
        a = self.one
        b = self.two
        c = self.three
        d = self.four
        
        e = [a, b, c, d]                                                       # Stores updated lifeform co-ordinates
        
        self.steps = int(self.steps)
        
        self.one = self.one + random.randint(-self.steps, self.steps)
        while self.one > self.XMAX-1 or self.one < 1:                          # To make lifeform stay within XMAX 
            self.one = self.one + random.randint(-self.steps, self.steps)
      
        self.two = self.two + random.randint(-self.steps, self.steps) 
        while self.two > self.YMAX-1 or self.two < 1:                          # To make lifeform stay within YMAX
            self.two = self.two + random.randint(-self.steps, self.steps) 
    
        f = np.where((lifeforms == e).all(1))[0]                               # Locates index of lifeform in Lifeforms Array
        lifeforms[f,0] = self.one                                              # 
        lifeforms[f,1] = self.two                                              # Updates lifeform by adding new co-ordinates into same index of Lifeforms Array
        lifeforms[f,2] = self.three                                            #
    # Method to move lifeform for 3D Simulation
    def move2(self):
        self.three = self.three + random.randint(-self.steps, self.steps)
        while self.three not in range(self.XMAX):                              # To make lifeform stay within ZMAX
            self.three = self.three + random.randint(-self.steps, self.steps)

##############################################################################
# Class to form each intruder
class intruder():
    # Defining attributes of each object
    def __init__(self, XMAX, YMAX, radius, color, px):
        self.XMAX = XMAX
        self.YMAX = YMAX
        self.radius = radius
        self.color = color
        self.px = px
    # Forming the x and y co-ordinates of the intruders   
    def position(self, xs, ys):
        xs = xs + random.randint(-10, 10)
        ys = ys + random.randint(-10, 10)
        while xs > self.XMAX-self.radius or xs < self.radius:                  # To make sure intruders stay within XMAX
            xs = xs + random.randint(-10, 10)
        while ys > self.YMAX-self.radius or ys < self.radius:                  # To make sure intruders stay within YMAX
            ys = ys + random.randint(-10, 10)
            
        self.x = xs                                                            # Updating the x and y attributes of the intruder
        self.y = ys
    # Creating and plotting the intruder
    def character(self):
        circle1 = plt.Circle((self.x, self.y), self.radius, color = self.color) # Creating the body of the intruder
        
        self.px.set_aspect(1)
        self.px.add_artist(circle1)                                            # Plotting the intruder on a pre-made figure: px
    # Formula to calculate distance between intruder and given x and y value
    def distance(self, x2, y2):
        x1 = int(self.x)
        y1 = int(self.y)

        dx = x1 - x2
        dy = y1 - y2
        
        return math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))                    # Formula to calculate distance

##############################################################################
# Function to simulate peaceful planet
def simulate(POP, XMAX, YMAX, STEPS, STEPS_TIME, figs, save):
   
    p = str(POP)
    s = str(STEPS)
    # Forming the main arrays
    lifeforms = np.zeros((POP, 4), dtype=int)
    xvals = np.zeros((STEPS, POP), dtype=int)                                  # Where the xvalues for each STEP are stored
    yvals = np.zeros((STEPS, POP), dtype=int)                                  # Where the yvalues for each STEP are stored
    # Filling up the lifeforms array
    for i in range(POP):
        randX = random.randint(0, XMAX)
        randY = random.randint(0, YMAX)
        randTYPE = random.randint(0, 2)
        lifeforms[i, 0] = randX
        lifeforms[i, 1] = randY
        lifeforms[i, 2] = randTYPE
    # Code carried out if user wants it to
    if figs == "Y" and save != "D":
        dir = "Saved Simulations"                                              #
        if dir not in os.listdir():                                            # If main saving directory not present, it is created and gone into
            os.mkdir(dir)                                                      #
        os.chdir(dir)
        name = "S_" + "POP-" + p + "_" + "STEPS-" + s
        dir = str(name)
        if dir not in os.listdir():                                            # Creates directory specific to the simulation taking place in the main saving directory
            os.mkdir(dir)
        os.chdir(dir)
        if save == "A" or save == "ABC":
            pdf = matplotlib.backends.backend_pdf.PdfPages(name + ".pdf")      # Opens a PDF file
        if save == "B" or save == "ABC":
            dir = "Images"
            if dir not in os.listdir():                                        # Creates a directory within specific directory to start saving each image of time step
                os.mkdir(dir)
        if save == "C" or save == "ABC":
            file = open(name + ".csv", "w", newline = '')                      # Opens a CSV file to record each lifeform
            writer = csv.writer(file, delimiter = ",")
    # Creating Space for the planet
    fig = plt.figure("Simulation")                                             #
    get_ipython().run_line_magic('matplotlib', 'qt')                           #
    time.sleep(1)                                                              #
    print("\nGenerating external window...")                                   # This set of code opens a figure and then maximises it to display planet
    time.sleep(3)                                                              #
    figManager = plt.get_current_fig_manager()                                 #
    figManager.window.showMaximized()                                          #
    
    for i in range(STEPS):
        if save == "C" or save == "ABC":
            writer.writerow(["Time Step " + str(i + 1)])                       # Title for the current time step recorded in the CSV file
        xvalues = []                                                           # Array to store x value of each lifeform
        yvalues = []                                                           # Array to store y value of each lifeform
        colours = []                                                           # Array to store color of each lifeform
        for l in lifeforms:
            l = lifeform(0, XMAX, YMAX, l[0], l[1], l[2], l[3], "color")       # Lifeform object created
            l.col()                                                            # Lifeform color coded based on value
            l.move(lifeforms)                                                  # Lifeform moved from previous place
            for x in xvalues:                                                  # Starts the collision detection
                ind = xvalues.index(x)
                if l.one == x or l.one == x + 2 or l.one == x - 2:
                    y = yvalues[ind]                                           # If x values same then compare y values
                    if l.two == y or l.two == y + 2 or l.two == y - 2:         # Incase of same lifeforms on top of or close to each other, move them
                        l.move(lifeforms)    
            xvalues.append(l.one)                                              # Adds x co-ordinate of lifeform into xvalues array
            yvalues.append(l.two)                                              # Adds y co-ordinate of lifeform into yvalues array
            colours.append(l.color)                                            # Adds color of lifeform into colours array
            if save == "C" or save == "ABC":
                writer.writerow([l.one, l.two, l.three])                       # Stores lifeform for current time step into CSV file (happens for all lifeform objects)
        xvals[i:] = xvalues                                                    # Transfers x values for particular step into xvals array
        yvals[i:] = yvalues                                                    # Transfers y values for particular step into yvals array
        plt.title("### TIMESTEP " + str(i + 1) + " ###\n", fontsize = 22)      # PLanet plotting initiated
        plt.scatter(xvalues, yvalues, c = colours)
        plt.gca().set_facecolor("powderblue")
        plt.xlim(-40, XMAX + 40)                                               # Alternating the x-axis limits to show limits of planet
        plt.ylim(-40, YMAX + 40)                                               # Alternating the y-axis limits to show limits of planet
        plt.grid(linestyle = '--', linewidth = '0.5', color = 'gray')
        if figs == "Y" and save != "D":
            if save == "A" or save == "ABC":
                pdf.savefig()                                                  # Saves current time step into PDF
            if save == "B" or save == "ABC":
                os.chdir("Images")
                plt.savefig("Time-Step " + str(i + 1) + ".jpg")                # Saves current time step as jpg image in "Images" directory and then exits the directory
                os.chdir('..')
            if save == "C" or save == "ABC":
                writer.writerow([" ", " ", " "])                               # Enters empty break in CSV File between time steps
        plt.pause(STEPS_TIME)
        plt.clf()
   
    plt.close()
    
    if figs == "Y" and save != "D":
        if save == "A" or save == "ABC":
            pdf.close()                                                        # Closes the PDF File
        if save == "C" or save == "ABC":
            file.close()                                                       # Closes the CSV File
        os.chdir('..')
        os.chdir('..')
        time.sleep(1)
        print("\n\nSaved!")
        
    time.sleep(2)
    threeD = input("\nWould you like to simulate the 3D-version [y/n]: ")
    threeD = threeD.upper()
        
    if threeD == "Y":
        three(lifeforms, POP, STEPS, STEPS_TIME, XMAX, YMAX, xvals, yvals, figs, save)      #Initiates 3D plotting if input os "y"
 
##############################################################################
# Function to simulate 3D-version of peaceful planet
def three(lifeforms, POP, STEPS, STEPS_TIME, XMAX, YMAX, xvals, yvals, figs, save):  
   
    p = str(POP)
    s = str(STEPS)
    
    ZMAX = 200
    
    if POP > 500:
        ZMAX = ZMAX + 200
    elif POP > 200:
        ZMAX = ZMAX + 100
    
    for i in range(POP):
        lifeforms[i, 3] = lifeforms[i, 2]
        lifeforms[i, 2] = 0
    
    for i in range(POP):
        randZ = random.randint(0, ZMAX)
        lifeforms[i, 2] = randZ
    
    if figs == "Y" and save != "D":
        dir = "Saved Simulations"
        if dir not in os.listdir():
            os.mkdir(dir)
        os.chdir(dir)
        name = "3D_" + "POP-" + p + "_" + "STEPS-" + s
        dir = str(name)
        if dir not in os.listdir():
            os.mkdir(dir)
        os.chdir(dir)
        if save == "A" or save == "ABC":
            pdf = matplotlib.backends.backend_pdf.PdfPages(name + ".pdf")
        if save == "B" or save == "ABC":
            dir = "Images"
            if dir not in os.listdir():
                os.mkdir(dir)
        if save == "C" or save == "ABC":
            file = open(name + ".csv", "w", newline = '')
            writer = csv.writer(file, delimiter = ",")
            
    fig = plt.figure()
    get_ipython().run_line_magic('matplotlib', 'qt')
    time.sleep(1)
    print("\nGenerating external window...")
    time.sleep(3)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    
    for i in range(STEPS):
        if save == "C" or save == "ABC":
            writer.writerow(["Time Step " + str(i + 1)])
        xvalues = xvals[i]                                                     # Takes x values from the simple simulation that were stored in xvals
        yvalues = yvals[i]                                                     # Takes y values from the simple simulation that were stored in yvals
        zvalues = []
        colours = []
        rcols = []
        for l in lifeforms:
            l = lifeform(0, XMAX, YMAX, l[0], l[1], l[2], l[3], "color")
            l.col2()
            l.move2()
            zvalues.append(l.three)
            colours.append(l.color)
            rcols.append(l.four)
        if save == "C" or save == "ABC":
            for z in range(POP):
                writer.writerow([xvalues[z], yvalues[z], zvalues[z], rcols[z]])
        ax = plt.axes(projection = '3d',facecolor = "silver")
        plt.title("### TIMESTEP " + str(i + 1) + " ###\n\n", fontsize=22)
        ax.scatter(xvalues, yvalues, zvalues, c = colours)
        ax.set_xlim(-25, XMAX + 25)
        ax.set_ylim(-25, YMAX + 25)
        ax.set_zlim(-25, ZMAX + 25)
        if figs == "Y" and save != "D":
            if save == "A" or save == "ABC":
                pdf.savefig()
            if save == "B" or save == "ABC":
                os.chdir("Images")
                plt.savefig("Time-Step " + str(i + 1) + ".jpg")
                os.chdir('..')
            if save == "C" or save == "ABC":
                writer.writerow([" ", " ", " ", " "])
        plt.pause(STEPS_TIME)
        plt.clf()
    
    plt.close()
    
    if figs == "Y" and save != "D":
        if save == "A" or save == "ABC":
            pdf.close()
        if save == "C" or save == "ABC":
            file.close()
        os.chdir('..')
        os.chdir('..')
        time.sleep(1)
        print("\n\nSaved!")

##############################################################################
# Function to simulate war on the planet  
def war(POP, XMAX, YMAX, STEPS, STEPS_TIME, figs, save):
    
    p = str(POP)
    s = str(STEPS)
    
    lifeforms = np.zeros((POP, 4), dtype=int)
    
    for i in range(POP):
        randX = random.randint(0, XMAX)
        randY = random.randint(0, YMAX)
        randTYPE = random.randint(0, 2)
        lifeforms[i, 0] = randX
        lifeforms[i, 1] = randY
        lifeforms[i, 2] = randTYPE
    
    if figs == "Y" and save != "D":
        dir = "Saved Simulations"
        if dir not in os.listdir():
            os.mkdir(dir)
        os.chdir(dir)
        name = "W_" + "POP-" + p + "_" + "STEPS-" + s
        dir = str(name)
        if dir not in os.listdir():
            os.mkdir(dir)
        os.chdir(dir)
        if save == "A" or save == "ABC":
            pdf = matplotlib.backends.backend_pdf.PdfPages(name + ".pdf")
        if save == "B" or save == "ABC":
            dir = "Images"
            if dir not in os.listdir():
                os.mkdir(dir)
        if save == "C" or save == "ABC":
            file = open(name + ".csv", "w", newline = '')
            writer = csv.writer(file, delimiter = ",")

    fig = plt.figure("War")
    get_ipython().run_line_magic('matplotlib', 'qt')
    time.sleep(1)
    print("\nGenerating external window...")
    time.sleep(3)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    
    TDR = 0                                                                    # Total Number of dead reds for entire simulation
    TDY = 0                                                                    # Total Number of dead yellows for entire simulation
    TDB = 0                                                                    # Total Number of dead blues for entire simulation
    
    for i in range(STEPS):
        if save == "C" or save == "ABC":
            writer.writerow(["Time Step " + str(i + 1)])
        xvalues = []
        yvalues = []
        colours = []
        DR = 0                                                                 # Dead Reds for this particular time step
        DY = 0                                                                 # Dead Yellows for this particular time step
        DB = 0                                                                 # Dead Blues for this particular time step
        for l in lifeforms:
            l = lifeform(0, XMAX, YMAX, l[0], l[1], l[2], l[3], "color")
            l.col()
            l.move(lifeforms)
            if save == "C" or save == "ABC":
                writer.writerow([l.one, l.two, l.three])
            # Collision detection
            for x in xvalues:
                ind = xvalues.index(x)
                if l.one == x or l.one == x + 3 or l.one == x - 3:             # Lifeforms within 3 steps is considered as a collision
                    y = yvalues[ind]
                    if l.two == y or l.two == y + 3 or l.two == y - 3:
                        c = colours[ind]
                        if l.three == 0 and c == "royalblue" or l.three == 1 and c == "tomato" or l.three == 2 and c == "yellow":     # Criteria for defeat (l is being defeated here)
                            d = np.where((lifeforms == [l.one, l.two, l.three, l.four]).all(1))[0]                                    # Finding l in the main array
                            lifeforms = np.delete(lifeforms, d, axis=0)                                                               # Deleteing l from the main array
                            if l.three == 0:
                                DR = DR + 1                                    #
                                TDR = TDR + 1                                  #
                            elif l.three == 1:                                 #
                                DY = DY + 1                                    # Dead lifeform statistics updated
                                TDY = TDY + 1                                  #
                            elif l.three == 2:                                 #
                                DB = DB + 1                                    #
                                TDB = TDB + 1                                  #
                        elif l.three == 2 and c == "tomato" or l.three == 0 and c == "yellow" or l.three == 1 and c == "royalblue":
                            if c == "tomato":
                                g = 0
                                DR = DR + 1                                    
                                TDR = TDR + 1 
                            if c == "yellow":
                                g = 1
                                DY = DY + 1                                    
                                TDY = TDY + 1
                            if c == "royalblue":
                                g = 2
                                DB = DB + 1                                    
                                TDB = TDB + 1
                            d = np.where((lifeforms == [x, y, g, 0]).all(1))[0]
                            lifeforms = np.delete(lifeforms, d, axis=0)
                        elif l.color == c:
                            l.move(lifeforms)
            xvalues.append(l.one)
            yvalues.append(l.two)
            colours.append(l.color)    
        r,c = lifeforms.shape                                                  # Extracting rows and columns of main array
        if r == 0:
            time.sleep(2)
            print("Empty Planet - Refreshing...")
            break
        else:
             print("### TIMESTEP " + str(i + 1) + " ###")
             print("Red Deaths: ", DR)
             print("Yellow Deaths: ", DY)
             print("Blue Deaths: ", DB)
             print()
             plt.title("### TIMESTEP " + str(i + 1) + " ###\n", fontsize=22)
             plt.scatter(xvalues, yvalues, c=colours)
             plt.gca().set_facecolor("lightpink")
             plt.xlim(-40, XMAX + 40)
             plt.ylim(-40, YMAX + 40)
             plt.grid(linestyle = '--', linewidth = '0.5', color = 'gray')        
             if figs == "Y" and save != "D":
                if save == "A" or save == "ABC":
                    pdf.savefig()
                if save == "B" or save == "ABC":
                    os.chdir("Images")
                    plt.savefig("Time-Step " + str(i + 1) + ".jpg")
                    os.chdir('..')
                if save == "C" or save == "ABC":
                    writer.writerow([" ", " ", " ", "Red Deaths: " + str(DR)])        #
                    writer.writerow([" ", " ", " ", "Yellow Deaths: " + str(DY)])     # Statistics are input into the CSV file
                    writer.writerow([" ", " ", " ", "Blue Deaths: " + str(DB)])       #
                    writer.writerow([" ", " ", " ", " "])
        plt.pause(STEPS_TIME)
        plt.clf()
    
    plt.close() 
    
    time.sleep(1)
    
    r,c = lifeforms.shape
    
    print("-----------------------------------")
    print("Total Red Deaths: ", TDR)                                           #
    print("Total Yellow Deaths: ", TDY)                                        # Displaying death statistics within the program
    print("Total Blue Deaths: ", TDB)                                          #
    
    time.sleep(2)
    print("\nTotal number of deaths: ", TDR+TDY+TDB)
    time.sleep(2)
    if r != POP:
        print("New Population: ", POP - (TDR+TDY+TDB))
    elif r == POP:
        print("Population remains the same: ", POP)
    
    if figs == "Y" and save != "D":
        if save == "A" or save == "ABC":
            pdf.close()
        if save == "C" or save == "ABC":
            writer.writerow([" "])
            writer.writerow([" "])
            writer.writerow([" "])
            writer.writerow(["Total Red Deaths: " + str(TDR)])                 #
            writer.writerow(["Total Yellow Deaths: " + str(TDY)])              # Adding further analysis into the CSV file
            writer.writerow(["Total Blue Deaths: " + str(TDB)])                #
            writer.writerow([" "])
            if r != POP:
                writer.writerow(["New Population: " + str(POP - (TDR+TDY+TDB))])
            elif r == POP:
                writer.writerow(["Population remains the same: " + str(POP)])
            file.close()
        os.chdir('..')
        os.chdir('..')
        time.sleep(1)
        print("\n\nSaved!")

##############################################################################
# Function to simulate reproduction on the planet 
def reproduce(POP, XMAX, YMAX, STEPS, STEPS_TIME, figs, save):
    
    p = str(POP)
    s = str(STEPS)
    
    lifeforms = np.zeros((POP, 4), dtype=int)
    
    for i in range(POP):
        randX = random.randint(0, XMAX)
        randY = random.randint(0, YMAX)
        randTYPE = random.randint(0, 2)
        lifeforms[i, 0] = randX
        lifeforms[i, 1] = randY
        lifeforms[i, 2] = randTYPE
    
    if figs == "Y" and save != "D":
        dir = "Saved Simulations"
        if dir not in os.listdir():
            os.mkdir(dir)
        os.chdir(dir)
        name = "R_" + "POP-" + p + "_" + "STEPS-" + s
        dir = str(name)
        if dir not in os.listdir():
            os.mkdir(dir)
        os.chdir(dir)
        if save == "A" or save == "ABC":
            pdf = matplotlib.backends.backend_pdf.PdfPages(name + ".pdf")
        if save == "B" or save == "ABC":
            dir = "Images"
            if dir not in os.listdir():
                os.mkdir(dir)
        if save == "C" or save == "ABC":
            file = open(name + ".csv", "w", newline = '')
            writer = csv.writer(file, delimiter = ",")
    
    fig = plt.figure("Reproduction")
    time.sleep(1)
    print("\nGenerating external window...")
    time.sleep(3)
    get_ipython().run_line_magic('matplotlib', 'qt')
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    
    TNR = 0                                                                    # Total Number of new reds for entire simulation
    TNY = 0                                                                    # Total Number of new yellows for entire simulation
    TNB = 0                                                                    # Total Number of new blues for entire simulation
    
    for i in range(STEPS):
        if save == "C" or save == "ABC":
            writer.writerow(["Time Step " + str(i + 1)])
        xvalues = []
        yvalues = []
        colours = []
        NR = 0                                                                 # New Reds for this particular time step
        NY = 0                                                                 # New Yellows for this particular time step
        NB = 0                                                                 # New Blues for this particular time step
        for l in lifeforms:
            l = lifeform(0, XMAX, YMAX, l[0], l[1], l[2], l[3], "color")
            l.col()
            l.move(lifeforms)
            if save == "C" or save == "ABC":
                writer.writerow([l.one, l.two, l.three])
            for x in xvalues:
                ind = xvalues.index(x)
                if l.one == x or l.one == x + 1 or l.one == x - 1:             # Lifeforms within 1 step is considered as a collision
                    y = yvalues[ind]
                    if l.two == y or l.two == y + 1 or l.two == y - 1:
                        c = colours[ind]
                        if l.color == c:
                            n1 = random.randint(-5, 5)
                            n2 = random.randint(-5, 5)
                            lifeforms = np.insert(lifeforms, POP, [l.one+n1, l.two+n2, l.three, 0], axis=0)   # New lifeform added into the array and plotted randomly into the planet close to collision site
                            if l.color == "tomato":                            #
                                TNR = TNR + 1                                  #
                                NR = NR + 1                                    #
                            elif l.color == "yellow":                          #
                                TNY = TNY + 1                                  # New lifeform statistics updated
                                NY = NY + 1                                    #
                            elif l.color == "royalblue":                       #
                                TNB = TNB + 1                                  #
                                NB = NB + 1                                    #
                        else:
                            l.move(lifeforms)         
            xvalues.append(l.one)
            yvalues.append(l.two)
            colours.append(l.color)
        r,c = lifeforms.shape
        if r > 1000:
            time.sleep(2)
            print("Population Overflow - Refreshing...")
            break
        else:
             print("### TIMESTEP " + str(i + 1) + " ###")
             print("Red Deaths: ", NR)
             print("Yellow Deaths: ", NY)
             print("Blue Deaths: ", NB)
             print()
             plt.title("### TIMESTEP " + str(i + 1) + " ###", fontsize = 22)
             plt.scatter(xvalues, yvalues, c = colours)
             plt.gca().set_facecolor("lightpink")
             plt.xlim(-40, XMAX + 40)
             plt.ylim(-40, YMAX + 40)
             plt.grid(linestyle = '--', linewidth = '0.5', color = 'gray')
             if figs == "Y" and save != "D":
                if save == "A" or save == "ABC":
                    pdf.savefig()
                if save == "B" or save == "ABC":
                    os.chdir("Images")
                    plt.savefig("Time-Step " + str(i + 1) + ".jpg")
                    os.chdir('..')
                if save == "C" or save == "ABC":
                    writer.writerow([" ", " ", " ", "New Reds: " + str(NR)])
                    writer.writerow([" ", " ", " ", "New Yellows: " + str(NY)])
                    writer.writerow([" ", " ", " ", "New Blues: " + str(NB)])
                    writer.writerow([" ", " ", " ", " "])
             plt.pause(STEPS_TIME)
             plt.clf()
             
    plt.close()
    
    time.sleep(1)
    
    r,c = lifeforms.shape
    
    print("-----------------------------------")
    print("Total New Reds: ", TNR)
    print("Total New Yellows: ", TNY)
    print("Total New Blues: ", TNB)
    
    time.sleep(2)
    print("\nTotal number of new borns: ", TNR+TNY+TNB)
    time.sleep(2)
    
    if r != POP:
        print("New Population: ", POP + (TNR+TNY+TNB))
    elif r == POP:
        print("Population remains the same: ", POP)
    
    if figs == "Y" and save != "D":
        if save == "A" or save == "ABC":
            pdf.close()
        if save == "C" or save == "ABC":
            writer.writerow([""])
            writer.writerow([""])
            writer.writerow([""])
            writer.writerow(["Total New Reds: " + str(TNR)])
            writer.writerow(["Total New Yellows: " + str(TNY)])
            writer.writerow(["Total New Blues: " + str(TNB)])
            writer.writerow([" "])
            if r != POP:
                writer.writerow(["New Population: " + str(POP + (TNR+TNY+TNB))])
            elif r == POP:
                writer.writerow(["Population remains the same: " + str(POP)])
        os.chdir('..')
        os.chdir('..')
        time.sleep(1)
        print("\n\nSaved!")

##############################################################################
# Function to simulate the presence of intruders on planet
def intruderz(POP, XMAX, YMAX, STEPS, STEPS_TIME, figs, save):
    
    p = str(POP)
    s = str(STEPS)
    
    lifeforms = np.zeros((POP, 4), dtype = int)
    
    for i in range(POP):
        randX = random.randint(0, XMAX)
        randY = random.randint(0, YMAX)
        randTYPE = random.randint(0, 2)
        lifeforms[i, 0] = randX
        lifeforms[i, 1] = randY
        lifeforms[i, 2] = randTYPE
        
    xs = []                                                                    # List to hold x co-ordinates of each lifeform
    ys = []                                                                    # List to hold y co-ordinates of each lifeform
    pop = 8                                                                    # Population of intruders
        
    for i in range(pop):
        x = random.randint(0, XMAX)                                            # Randomly assigning x co-ordinate to each intruder
        y = random.randint(0, YMAX)                                            # Randomly assigning y co-ordinate to each intruder
        xs.append(x)
        ys.append(y)
        
    if figs == "Y" and save != "D":
        dir = "Saved Simulations"
        if dir not in os.listdir():
            os.mkdir(dir)
        os.chdir(dir)
        name = "I_" + "POP-" + p + "_" + "STEPS-" + s
        dir = str(name)
        if dir not in os.listdir():
            os.mkdir(dir)
        os.chdir(dir)
        if save == "A" or save == "ABC":
            pdf = matplotlib.backends.backend_pdf.PdfPages(name + ".pdf")
        if save == "B" or save == "ABC":
            dir = "Images"
            if dir not in os.listdir():
                os.mkdir(dir)
        if save == "C" or save == "ABC":
            file = open(name + ".csv", "w", newline = '')
            writer = csv.writer(file, delimiter = ",")
    
    time.sleep(1)
    print("\nGenerating external window...")
    time.sleep(3)
    get_ipython().run_line_magic('matplotlib', 'qt')              

    TDR = 0                                                                    
    TDY = 0                                                                    
    TDB = 0 

    for i in range(STEPS):
        if save == "C" or save == "ABC":
            writer.writerow(["Time Step " + str(i + 1)])
        
        fig, px = plt.subplots(1)
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        
        k1 = intruder(XMAX, YMAX, 10, "gray", px)                              #
        k2 = intruder(XMAX, YMAX, 11, "sandybrown", px)                        #
        k3 = intruder(XMAX, YMAX, 12, "sienna", px)                            #
        k4 = intruder(XMAX, YMAX, 13, "olive", px)                             # Creating the 8 intruders as objects from the "intruder()" class
        k5 = intruder(XMAX, YMAX, 10, "gray", px)                              #
        k6 = intruder(XMAX, YMAX, 11, "sandybrown", px)                        #
        k7 = intruder(XMAX, YMAX, 12, "sienna", px)                            #
        k8 = intruder(XMAX, YMAX, 13, "olive", px)                             #
        
        k1.position(xs[0], ys[0])
        xs[0] = k1.x                                                           # New x co-ordinate for the 1st intruder so it starts from here in the next step (repeated for all)
        ys[0] = k1.y                                                           # New y co-ordinate for the 1st intruder so it starts from here in the next step (repeated for all)
        k2.position(xs[1], ys[1])
        xs[1] = k2.x
        ys[1] = k2.y
        k3.position(xs[2], ys[2])
        xs[2] = k3.x
        ys[2] = k3.y
        k4.position(xs[3], ys[3])
        xs[3] = k4.x
        ys[3] = k4.y
        k5.position(xs[4], ys[4])
        xs[4] = k5.x
        ys[4] = k5.y
        k6.position(xs[5], ys[5])
        xs[5] = k6.x
        ys[5] = k6.y
        k7.position(xs[6], ys[6])
        xs[6] = k7.x
        ys[6] = k7.y
        k8.position(xs[7], ys[7])
        xs[7] = k8.x
        ys[7] = k8.y
        
        k1.character()                                                         # Adds intruder to the planet (by plotting - repeated for all)
        k2.character()
        k3.character()
        k4.character()
        k5.character()
        k6.character()
        k7.character()
        k8.character()
        
        xvalues = []
        yvalues = []
        colours = []
        DR = 0                                                                 
        DY = 0                                                                 
        DB = 0
        
        for l in lifeforms:
            d1 = k1.distance(l[0], l[1])                                       # Distance between lifeform and intruder 1 found using "distance()" method from "intruder()" class (repeated with all)
            d2 = k2.distance(l[0], l[1])
            d3 = k3.distance(l[0], l[1])
            d4 = k4.distance(l[0], l[1])
            d5 = k5.distance(l[0], l[1])
            d6 = k6.distance(l[0], l[1])
            d7 = k7.distance(l[0], l[1])
            d8 = k8.distance(l[0], l[1])
            
            if d1 <= k1.radius or d2 <= k2.radius or d3 <= k3.radius or d4 <= k4.radius or d5 <= k5.radius or d6 <= k6.radius or d7 <= k7.radius or d8 <= k8.radius:
                d = np.where((lifeforms == [l[0], l[1], l[2], l[3]]).all(1))[0]          # Removes or "eats" lifeform is distance with any intruder is less than or equal to radius (repeated with all)
                lifeforms = np.delete(lifeforms, d, axis = 0)
                if l[2] == 0:
                    DR = DR + 1                                    
                    TDR = TDR + 1                                  
                elif l[2] == 1:                                 
                    DY = DY + 1                                    
                    TDY = TDY + 1                                  
                elif l[2] == 2:                                 
                    DB = DB + 1                                    
                    TDB = TDB + 1     
            else:
                l = lifeform(0, XMAX, YMAX, l[0], l[1], l[2], l[3], "color")
                l.col()
                l.move(lifeforms)
                xvalues.append(l.one)
                yvalues.append(l.two)
                colours.append(l.color)
                if save == "C" or save == "ABC":
                    writer.writerow([l.one, l.two, l.three])
        
        if save == "C" or save == "ABC":
            writer.writerow(["Intruders"])                                     # Adding each intruder statistics into the CSV file
            writer.writerow([k1.x, k1.y])
            writer.writerow([k2.x, k2.y])
            writer.writerow([k3.x, k3.y])
            writer.writerow([k4.x, k4.y])
            writer.writerow([k5.x, k5.y])
            writer.writerow([k6.x, k6.y])
            writer.writerow([k7.x, k7.y])
            writer.writerow([k8.x, k8.y])
        
        r,c = lifeforms.shape
        if r == 0:
            time.sleep(2)
            print("Empty Planet - Refreshing...")
            break
        else:
            print("### TIMESTEP " + str(i + 1) + " ###")
            print("Red Deaths: ", DR)
            print("Yellow Deaths: ", DY)
            print("Blue Deaths: ", DB)
            print()
            plt.title("### TIMESTEP " + str(i+1) + " ###\n", fontsize = 22)
            plt.scatter(xvalues, yvalues, c = colours)
            px.set_facecolor("palegoldenrod")
            plt.xlim(-40, XMAX + 40)
            plt.ylim(-40, YMAX + 40)
            plt.grid(linestyle = '--', linewidth = '0.5', color = 'gray')
            if figs == "Y" and save != "D":
                if save == "A" or save == "ABC":
                    pdf.savefig()
                if save == "B" or save == "ABC":
                    os.chdir("Images")
                    plt.savefig("Time-Step " + str(i + 1) + ".jpg")
                    os.chdir('..')
                if save == "C" or save == "ABC":
                    writer.writerow([" ", " ", " ", "Red Deaths: " + str(DR)])
                    writer.writerow([" ", " ", " ", "Yellow Deaths: " + str(DY)])
                    writer.writerow([" ", " ", " ", "Blue Deaths: " + str(DB)])
                    writer.writerow([" ", " ", " ", " "])
            plt.pause(STEPS_TIME)
            plt.clf()
    
        plt.close()
    
    time.sleep(1)
    
    r,c = lifeforms.shape
    
    print("-----------------------------------")
    print("Total Red Deaths: ", TDR)
    print("Total Yellow Deaths: ", TDY)
    print("Total Blue Deaths: ", TDB)
    
    time.sleep(2)
    print("\nTotal number of deaths: ", TDR+TDY+TDB)
    time.sleep(2)
    if r != POP:
        print("New Population: ", POP - (TDR+TDY+TDB))
    elif r == POP:
        print("Population remains the same: ", POP)
    
    if figs == "Y" and save != "D":
        if save == "A" or save == "ABC":
            pdf.close()
        if save == "C" or save == "ABC":
            writer.writerow([" "])
            writer.writerow([" "])
            writer.writerow([" "])
            writer.writerow(["Total Red Deaths: " + str(TDR)])
            writer.writerow(["Total Yellow Deaths: " + str(TDY)])
            writer.writerow(["Total Blue Deaths: " + str(TDB)])
            writer.writerow([" "])
            if r != POP:
                writer.writerow(["New Population: " + str(POP - (TDR+TDY+TDB))])
            elif r == POP:
                writer.writerow(["Population remains the same: " + str(POP)])
            file.close()
        os.chdir('..')
        os.chdir('..')
        time.sleep(1)
        print("\n\nSaved!")

##############################################################################
