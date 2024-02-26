import tkinter as tk
from PIL import Image, ImageTk
import random

class TrafficSimulation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Traffic Simulation")
        self.geometry("1540x730") 
        self.canvas = tk.Canvas(self, width=1550, height=740, bd=0, highlightthickness=0)
        self.image = tk.PhotoImage(file='background.png')  # Update path as needed
        self.image_id = self.canvas.create_image(770,360, image=self.image)
        self.canvas.pack()

        self.greenRedTime = 9000
        self.yellowTime = 5000
        self.blueTime = 10000

        self.redOdd = []
        self.yellowOdd = []
        self.greenOdd = []
        self.redEven = []
        self.yellowEven = []
        self.greenEven = []
        self.crossWalkEven = []
        self.crossWalkOdd = []
        self.carXR = []
        self.carXL = []
        self.carYU = []
        self.carYD = []
        self.pedXR = []
        self.pedXL = []
        self.pedYU = []
        self.pedYD = []

        self.drawTrafficLights()
        
        self.carXR.extend(self.drawCarXRight(200, 380, 'blue'))
        self.carXR.extend(self.drawCarXRight(800, 380, 'yellow'))
        self.carXR.extend(self.drawCarXRight(1300, 380, 'green'))
        self.carXR.extend(self.drawCarXRight(400, 440, 'orange'))
        self.carXL.extend(self.drawCarXLeft(300, 310, 'cyan'))
        self.carXL.extend(self.drawCarXLeft(1400, 250, 'magenta'))
        self.carXL.extend(self.drawCarXLeft(650, 310, 'lime'))
        self.carYD.extend(self.drawCarYDown(720, 60, 'silver'))
        self.carYD.extend(self.drawCarYDown(660, 60, 'brown'))
        self.carYU.extend(self.drawCarYUp(790, 620, 'purple'))

        self.pedXR.extend(self.drawPedestrian(300, 180, 0))
        self.pedXR.extend(self.drawPedestrian(340, 200, 0))
        self.pedXR.extend(self.drawPedestrian(650, 190, 0))
        self.pedXR.extend(self.drawPedestrian(1300, 175, 0))
        self.pedXR.extend(self.drawPedestrian(250, 510, 0))
        self.pedXL.extend(self.drawPedestrian(750, 520, 0))
        self.pedXL.extend(self.drawPedestrian(1350, 525, 0))
        self.pedXL.extend(self.drawPedestrian(1130, 510, 0))
        self.pedYU.extend(self.drawPedestrian(600, 600, 1))
        self.pedYU.extend(self.drawPedestrian(590, 120, 1))
        self.pedYD.extend(self.drawPedestrian(930, 520, 1))
        self.pedYD.extend(self.drawPedestrian(920, 130, 1))

        self.moveCar()
        self.movePedestrian()
        self.addCar()
        self.addPedestrian()
        self.after(self.greenRedTime, self.update_traffic_lights1)
    
    def addCar(self):
        newCar = random.random()
        if newCar < 0.4:
            colors = ["green", "blue", "yellow", "orange", "purple", "pink", "cyan", "magenta", "brown", "turquoise", "gold", "silver", "navy", "olive", "maroon", "lime", "teal", "indigo"]
            color = random.choice(colors)
            vertOrHorz = random.random()
            if vertOrHorz < 0.5:
                upOrDown = random.random()
                if upOrDown < 0.5:
                    lanes = random.random()
                    if lanes < 0.5:
                        self.carYU.extend(self.drawCarYUp(790, 800, color))
                    else:
                        self.carYU.extend(self.drawCarYUp(850, 800, color))
                else:
                    lanes = random.random()
                    if lanes < 0.5:
                        self.carYD.extend(self.drawCarYDown(720, -100, color))
                    else:
                        self.carYD.extend(self.drawCarYDown(660, -100, color))
            else:
                leftOrRight = random.random()
                if leftOrRight < 0.5:
                    lanes = random.random()
                    if lanes < 0.5:
                        self.carXL.extend(self.drawCarXLeft(1500, 310, color))
                    else:
                        self.carXL.extend(self.drawCarXLeft(1500, 250, color))
                else:
                    lanes = random.random()
                    if lanes < 0.5:
                        self.carXR.extend(self.drawCarXRight(-100, 380, color))
                    else:
                        self.carXR.extend(self.drawCarXRight(-100, 440, color))
        self.after(500, self.addCar)

    def moveCar(self):
        if self.canvas.itemcget(self.greenOdd[0], "fill") == 'green':
            for i in range(0,len(self.carXR)):
               self.canvas.move(self.carXR[i], 10, 0)
            for i in range(0,len(self.carXL)):
               self.canvas.move(self.carXL[i], -10, 0)
        else:
            for i in range(0,int(len(self.carXR)/11)):
                if self.canvas.coords(self.carXR[2 + i*11])[0] != 470:
                    for j in range(0,11):
                        self.canvas.move(self.carXR[i*11 + j], 10, 0)
            for i in range(0,int(len(self.carXL)/11)):
                if self.canvas.coords(self.carXL[2 + i*11])[0] != 1020:
                    for j in range(0,11):
                        self.canvas.move(self.carXL[i*11 + j], -10, 0)

        if self.canvas.itemcget(self.greenEven[0], "fill") == 'green':
            for i in range(0,len(self.carYD)):
               self.canvas.move(self.carYD[i], 0, 10)
            for i in range(0,len(self.carYU)):
               self.canvas.move(self.carYU[i], 0, -10)
        else:
            for i in range(0,int(len(self.carYU)/11)):
                if self.canvas.coords(self.carYU[2 + i*11])[1] != 620:
                    for j in range(0,11):
                        self.canvas.move(self.carYU[i*11 + j], 0, -10)
            for i in range(0,int(len(self.carYD)/11)):
                if self.canvas.coords(self.carYD[2 + i*11])[1] != 60:
                    for j in range(0,11):
                        self.canvas.move(self.carYD[i*11 + j], 0, 10)

        # turns
                        
        if self.canvas.itemcget(self.redOdd[0], "fill") == 'blue':
            for i in range(0,int(len(self.carXR)/11)):
                if self.canvas.coords(self.carXR[2 + i*11])[0] == 470:
                    for j in range(0,11):
                        self.canvas.move(self.carXR[i*11 + j], 10, 0)
            #removeList = []
            for i in range(0,int(len(self.carXR)/11)):
                if self.canvas.coords(self.carXR[2 + i*11])[0] == 790 and self.canvas.coords(self.carXR[2 + i*11])[1] == 380:
                    color = self.canvas.itemcget(self.carXR[i*11], "fill")
                    self.carYU.extend(self.drawCarYUp(790, 380, color))
                if self.canvas.coords(self.carXR[2 + i*11])[0] == 660 and self.canvas.coords(self.carXR[2 + i*11])[1] == 440:
                    color = self.canvas.itemcget(self.carXR[i*11], "fill")
                    self.carYD.extend(self.drawCarYDown(660, 440, color))
                    #removeList.append(i)
            #for i in range(0,len(removeList)):
                #self.carXR = self.carXR[:removeList[i]*11] + self.carXR[removeList[i]*11 + 11:]
                #for item in self.carXR[removeList[i]*11-i*11:removeList[i]*11 + 11-i*11]:
                    #self.canvas.delete(item)
        elif self.canvas.itemcget(self.redOdd[1], "fill") == 'blue':
            for i in range(0,int(len(self.carXR)/11)):
                if self.canvas.coords(self.carXR[2 + i*11])[0] == 1020:
                    for j in range(0,11):
                        self.canvas.move(self.carXR[i*11 + j], 10, 0)
            #removeList = []
            for i in range(0,int(len(self.carXR)/11)):
                if self.canvas.coords(self.carXR[2 + i*11])[0] == 850 and self.canvas.coords(self.carXR[2 + i*11])[1] == 250:
                    color = self.canvas.itemcget(self.carXR[i*11], "fill")
                    self.carYU.extend(self.drawCarYUp(850, 250, color))
                if self.canvas.coords(self.carXR[2 + i*11])[0] == 720 and self.canvas.coords(self.carXR[2 + i*11])[1] == 310:
                    color = self.canvas.itemcget(self.carXR[i*11], "fill")
                    self.carYD.extend(self.drawCarYDown(720, 310, color))
        self.after(10, self.moveCar)

    def addPedestrian(self):
        newPed = random.random()
        if newPed < 0.3:
            changes = [-10, 0, 10]
            change = random.choice(changes)
            vertOrHorz = random.random()
            if vertOrHorz < 0.5:
                upOrDown = random.random()
                if upOrDown < 0.5:
                    lanes = random.random()
                    if lanes < 0.5:
                        self.pedYU.extend(self.drawPedestrian(600 + change, 750, 1))
                    else:
                        self.pedYU.extend(self.drawPedestrian(925 + change, 750, 1))
                else:
                    lanes = random.random()
                    if lanes < 0.5:
                        self.pedYD.extend(self.drawPedestrian(600 + change, -20, 1))
                    else:
                        self.pedYD.extend(self.drawPedestrian(925 + change, -20, 1))
            else:
                leftOrRight = random.random()
                if leftOrRight < 0.5:
                    lanes = random.random()
                    if lanes < 0.5:
                        self.pedXR.extend(self.drawPedestrian(-20, 185 + change, 0))
                    else:
                        self.pedXR.extend(self.drawPedestrian(-20, 510 + change, 0))
                else:
                    lanes = random.random()
                    if lanes < 0.5:
                        self.pedXL.extend(self.drawPedestrian(1550, 510 + change, 0))
                    else:
                        self.pedXL.extend(self.drawPedestrian(1550, 185 + change, 0))
        self.after(500, self.addPedestrian)

    def movePedestrian(self):
        if self.canvas.itemcget(self.crossWalkEven[0], "fill") == 'green':
            for i in range(0,len(self.pedXR)):
               self.canvas.move(self.pedXR[i], 5, 0)
            for i in range(0,len(self.pedXL)):
               self.canvas.move(self.pedXL[i], -5, 0)
        else:
            for i in range(0,int(len(self.pedXR)/7)):
                if self.canvas.coords(self.pedXR[i*7])[0] != 600:
                    for j in range(0,7):
                        self.canvas.move(self.pedXR[i*7 + j], 5, 0)
            for i in range(0,int(len(self.pedXL)/7)):
                if self.canvas.coords(self.pedXL[i*7])[0] != 930:
                    for j in range(0,7):
                        self.canvas.move(self.pedXL[i*7 + j], -5, 0)

        if self.canvas.itemcget(self.crossWalkOdd[0], "fill") == 'green':
            for i in range(0,len(self.pedYD)):
               self.canvas.move(self.pedYD[i], 0, 5)
            for i in range(0,len(self.pedYU)):
               self.canvas.move(self.pedYU[i], 0, -5)
        else:
            for i in range(0,int(len(self.pedYU)/7)):
                if self.canvas.coords(self.pedYU[i*7])[1] != 520:
                    for j in range(0,7):
                        self.canvas.move(self.pedYU[i*7 + j], 0, -5)
            for i in range(0,int(len(self.pedYD)/7)):
                if self.canvas.coords(self.pedYD[i*7])[1] != 190:
                    for j in range(0,7):
                        self.canvas.move(self.pedYD[i*7 + j], 0, 5)

        self.after(10, self.movePedestrian)

    def drawTrafficLights(self):
        x = 550
        y = 200
        self.crossWalkOdd.append(self.canvas.create_rectangle(x, y, x+20, y+20, fill='red'))
        self.crossWalkOdd.append(self.canvas.create_rectangle(x, y+300, x+20, y+320, fill='red'))
        self.crossWalkOdd.append(self.canvas.create_rectangle(x+420, y, x+440, y+20, fill='red'))
        self.crossWalkOdd.append(self.canvas.create_rectangle(x+420, y+300, x+440, y+320, fill='red'))

        x = 610
        y = 140
        self.crossWalkEven.append(self.canvas.create_rectangle(x, y, x+20, y+20, fill='green'))
        self.crossWalkEven.append(self.canvas.create_rectangle(x, y+420, x+20, y+440, fill='green'))
        self.crossWalkEven.append(self.canvas.create_rectangle(x+300, y, x+320, y+20, fill='green'))
        self.crossWalkEven.append(self.canvas.create_rectangle(x+300, y+420, x+320, y+440, fill='green'))

        x = 650
        y = 390
        self.trafficLightBG(x, y, x+25, y+70)
        self.redOdd.append(self.canvas.create_oval(x+3, y+46, x+22, y+66, fill='gray'))
        self.yellowOdd.append(self.canvas.create_oval(x+3, y+25, x+22, y+45, fill='gray'))
        self.greenOdd.append(self.canvas.create_oval(x+3, y+4, x+22, y+24, fill='green'))
        
        x = 865
        y = 260
        self.trafficLightBG(x, y, x+25, y+70)
        self.redOdd.append(self.canvas.create_oval(x+3, y+4, x+22, y+24, fill='gray'))
        self.yellowOdd.append(self.canvas.create_oval(x+3, y+25, x+22, y+45, fill='gray'))
        self.greenOdd.append(self.canvas.create_oval(x+3, y+46, x+22, y+66, fill='green'))

        x = 675
        y = 242
        self.trafficLightBG(x, y, x+70, y+25)
        self.redEven.append(self.canvas.create_oval(x+4, y+3, x+24, y+22, fill='red'))
        self.yellowEven.append(self.canvas.create_oval(x+25, y+3, x+45, y+22, fill='gray'))
        self.greenEven.append(self.canvas.create_oval(x+46, y+3, x+66, y+22, fill='gray'))

        x = 800
        y = 452
        self.trafficLightBG(x, y, x+70, y+25)
        self.redEven.append(self.canvas.create_oval(x+46, y+3, x+66, y+22, fill='red'))
        self.yellowEven.append(self.canvas.create_oval(x+25, y+3, x+45, y+22, fill='gray'))
        self.greenEven.append(self.canvas.create_oval(x+4, y+3, x+24, y+22, fill='gray'))
    

    def update_traffic_lights1(self):
        for yellowLight, greenLight in zip(self.yellowOdd, self.greenOdd):
            self.canvas.itemconfigure(yellowLight, fill='yellow')
            self.canvas.itemconfigure(greenLight, fill='gray')
        
        for crossWalk in self.crossWalkEven:
            self.canvas.itemconfigure(crossWalk, fill='red')
        
        self.after(self.greenRedTime, self.update_traffic_lights2)

    def update_traffic_lights2(self):
        for redLight, yellowLight in zip(self.redOdd, self.yellowOdd):
            self.canvas.itemconfigure(redLight, fill='red')
            self.canvas.itemconfigure(yellowLight, fill='gray')
        
        self.after(self.yellowTime, self.update_traffic_lights3)

    def update_traffic_lights3(self):
        for redLight, greenLight in zip(self.redEven, self.greenEven):
            self.canvas.itemconfigure(redLight, fill='gray')
            self.canvas.itemconfigure(greenLight, fill='green')
        
        for crossWalk in self.crossWalkOdd:
            self.canvas.itemconfigure(crossWalk, fill='green')
        
        self.after(self.greenRedTime, self.update_traffic_lights4)
    
    def update_traffic_lights4(self):
        for yellowLight, greenLight in zip(self.yellowEven, self.greenEven):
            self.canvas.itemconfigure(yellowLight, fill='yellow')
            self.canvas.itemconfigure(greenLight, fill='gray')

        for crossWalk in self.crossWalkOdd:
            self.canvas.itemconfigure(crossWalk, fill='red')
        
        self.after(self.greenRedTime, self.update_traffic_lights5)
            
    def update_traffic_lights5(self):
        for redLight, yellowLight in zip(self.redEven, self.yellowEven):
            self.canvas.itemconfigure(redLight, fill='red')
            self.canvas.itemconfigure(yellowLight, fill='gray')
        
        self.after(self.yellowTime, self.update_traffic_lights6)

    def update_traffic_lights6(self):
        self.canvas.itemconfigure(self.redOdd[0], fill='blue')
        self.canvas.itemconfigure(self.yellowOdd[0], fill='blue')
        self.canvas.itemconfigure(self.greenOdd[0], fill='blue')
        
        self.after(self.blueTime, self.update_traffic_lights7)

    def update_traffic_lights7(self):
        self.canvas.itemconfigure(self.redOdd[0], fill='red')
        self.canvas.itemconfigure(self.yellowOdd[0], fill='gray')
        self.canvas.itemconfigure(self.greenOdd[0], fill='gray')
        
        self.after(self.yellowTime, self.update_traffic_lights8)

    def update_traffic_lights8(self):
        self.canvas.itemconfigure(self.redEven[1], fill='blue')
        self.canvas.itemconfigure(self.yellowEven[1], fill='blue')
        self.canvas.itemconfigure(self.greenEven[1], fill='blue')
        
        self.after(self.blueTime, self.update_traffic_lights9)

    def update_traffic_lights9(self):
        self.canvas.itemconfigure(self.redEven[1], fill='red')
        self.canvas.itemconfigure(self.yellowEven[1], fill='gray')
        self.canvas.itemconfigure(self.greenEven[1], fill='gray')
        
        self.after(self.yellowTime, self.update_traffic_lights10)

    def update_traffic_lights10(self):
        self.canvas.itemconfigure(self.redOdd[1], fill='blue')
        self.canvas.itemconfigure(self.yellowOdd[1], fill='blue')
        self.canvas.itemconfigure(self.greenOdd[1], fill='blue')
        
        self.after(self.blueTime, self.update_traffic_lights11)

    def update_traffic_lights11(self):
        self.canvas.itemconfigure(self.redOdd[1], fill='red')
        self.canvas.itemconfigure(self.yellowOdd[1], fill='gray')
        self.canvas.itemconfigure(self.greenOdd[1], fill='gray')
        
        self.after(self.blueTime, self.update_traffic_lights12)
    
    def update_traffic_lights12(self):
        self.canvas.itemconfigure(self.redEven[0], fill='blue')
        self.canvas.itemconfigure(self.yellowEven[0], fill='blue')
        self.canvas.itemconfigure(self.greenEven[0], fill='blue')
        
        self.after(self.blueTime, self.update_traffic_lights13)

    def update_traffic_lights13(self):
        self.canvas.itemconfigure(self.redEven[0], fill='red')
        self.canvas.itemconfigure(self.yellowEven[0], fill='gray')
        self.canvas.itemconfigure(self.greenEven[0], fill='gray')
        
        self.after(self.blueTime, self.update_traffic_lights14)

    def update_traffic_lights14(self):
        for redLight, greenLight in zip(self.redOdd, self.greenOdd):
            self.canvas.itemconfigure(redLight, fill='gray')
            self.canvas.itemconfigure(greenLight, fill='green')

        for crossWalk in self.crossWalkEven:
            self.canvas.itemconfigure(crossWalk, fill='green')
        
        self.after(self.greenRedTime, self.update_traffic_lights1)

    def trafficLightBG(self, x1, y1, x2, y2):
        # Draw the main rectangle
        radius = 5
        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill='black')
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill='black')

        # Draw the rounded corners
        self.canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.PIESLICE, fill='black')
        self.canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.PIESLICE, fill='black')
        self.canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.PIESLICE, fill='black')
        self.canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill='black')

    def drawCarXRight(self, x1, y1, color):
        x2 = x1 + 50
        y2 = y1 + 30
        radius = 5
        # body
        body1 = self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=color)
        body2 = self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=color)

        # lights
        l1 = self.canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.PIESLICE, fill='red')
        l2 = self.canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.PIESLICE, fill='white')
        l3 = self.canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.PIESLICE, fill='red')
        l4 = self.canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill='white')

        # windows
        w1 = self.canvas.create_rectangle(x1 + 13, y1 + 2, x1 + 37, y1 + 3, fill='black')
        w2 = self.canvas.create_rectangle(x1 + 13, y2 - 2, x1 + 37, y2 - 3, fill='black')
        w3 = self.canvas.create_rectangle(x1 + 30, y1 + 6, x1 + 40, y1 + 24, fill='black')
        w4 = self.canvas.create_rectangle(x1 + 20, y1 + 7, x1 + 27, y1 + 23, fill='gray')
        w5 = self.canvas.create_rectangle(x1 + 7, y1 + 6, x1 + 12, y1 + 24, fill='black')

        return body1, body2, l1, l2, l3, l4, w1, w2, w3, w4, w5

    def drawCarXLeft(self, x1, y1, color):
        x2 = x1 + 50
        y2 = y1 + 30
        radius = 5
        # body
        body1 = self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=color)
        body2 = self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=color)

        # lights
        l1 = self.canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.PIESLICE, fill='white')
        l2 = self.canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.PIESLICE, fill='red')
        l3 = self.canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.PIESLICE, fill='white')
        l4 = self.canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill='red')

        # windows
        w1 = self.canvas.create_rectangle(x2 - 13, y1 + 2, x2 - 37, y1 + 3, fill='black')
        w2 = self.canvas.create_rectangle(x2 - 13, y2 - 2, x2 - 37, y2 - 3, fill='black')
        w3 = self.canvas.create_rectangle(x2 - 30, y1 + 6, x2 - 40, y1 + 24, fill='black')
        w4 = self.canvas.create_rectangle(x2 - 20, y1 + 7, x2 - 27, y1 + 23, fill='gray')
        w5 = self.canvas.create_rectangle(x2 - 7, y1 + 6, x2 - 12, y1 + 24, fill='black')

        return body1, body2, l1, l2, l3, l4, w1, w2, w3, w4, w5

    def drawCarYDown(self, x1, y1, color):
        x2 = x1 + 30
        y2 = y1 + 50
        radius = 5
        # body
        body1 = self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=color)
        body2 = self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=color)

        # lights
        l1 = self.canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.PIESLICE, fill='red')
        l2 = self.canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.PIESLICE, fill='red')
        l3 = self.canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.PIESLICE, fill='white')
        l4 = self.canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill='white')

        # windows
        w1 = self.canvas.create_rectangle(x1 + 2, y1 + 13, x1 + 3, y1 + 37, fill='black')
        w2 = self.canvas.create_rectangle(x2 - 2, y1 + 13, x2 - 3, y1 + 37, fill='black')
        w3 = self.canvas.create_rectangle(x1 + 6, y1 + 30, x1 + 24, y1 + 40, fill='black')
        w4 = self.canvas.create_rectangle(x1 + 7, y1 + 20, x1 + 23, y1 + 27, fill='gray')
        w5 = self.canvas.create_rectangle(x1 + 6, y1 + 7, x1 + 24, y1 + 12, fill='black')

        return body1, body2, l1, l2, l3, l4, w1, w2, w3, w4, w5

    def drawCarYUp(self, x1, y1, color):
        x2 = x1 + 30
        y2 = y1 + 50
        radius = 5
        # body
        body1 = self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=color)
        body2 = self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=color)

        # lights
        l1 = self.canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.PIESLICE, fill='white')
        l2 = self.canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.PIESLICE, fill='white')
        l3 = self.canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.PIESLICE, fill='red')
        l4 = self.canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill='red')

        # windows
        w1 = self.canvas.create_rectangle(x1 + 2, y1 + 13, x1 + 3, y1 + 37, fill='black')
        w2 = self.canvas.create_rectangle(x2 - 2, y1 + 13, x2 - 3, y1 + 37, fill='black')
        w3 = self.canvas.create_rectangle(x1 + 6, y2 - 30, x1 + 24, y2 - 40, fill='black')
        w4 = self.canvas.create_rectangle(x1 + 7, y2 - 20, x1 + 23, y2 - 27, fill='gray')
        w5 = self.canvas.create_rectangle(x1 + 6, y2 - 7, x1 + 24, y2 - 12, fill='black')

        return body1, body2, l1, l2, l3, l4, w1, w2, w3, w4, w5

    def drawPedestrian(self, x1, y1, dir):
        radius = 5
        if dir == 0:
            x2 = x1 + 10
            y2 = y1 + 24
        else:
            x2 = x1 + 24
            y2 = y1 + 10
        # body
        b1 = self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill='black')
        b2 = self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill='black')
        b3 = self.canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.PIESLICE, fill='black')
        b4 = self.canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.PIESLICE, fill='black')
        b5 = self.canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.PIESLICE, fill='black')
        b6 = self.canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill='black')
        if dir == 0:
            head = self.canvas.create_oval(x1 - 1, y1 + 6, x2 + 1, y1 + 18, fill='gray')
        else:
            head = self.canvas.create_oval(x1 + 6, y1 - 1, x1 + 18, y2 + 1, fill='gray')

        return b1, b2, b3, b4, b5, b6, head
        
        


if __name__ == "__main__":
    app = TrafficSimulation()
    app.mainloop()

