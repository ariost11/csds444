import tkinter as tk
from PIL import Image, ImageTk
import time

class TrafficSimulation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Traffic Simulation")
        self.geometry("1540x730") 
        self.canvas = tk.Canvas(self, width=1550, height=740, bd=0, highlightthickness=0)
        self.image = tk.PhotoImage(file='traffic_light/background.png')
        self.image_id = self.canvas.create_image(770,360, image=self.image)
        self.canvas.pack()

        self.greenRedTime = 5000
        self.yellowTime = 1000

        self.redOdd = []
        self.yellowOdd = []
        self.greenOdd = []
        self.redEven = []
        self.yellowEven = []
        self.greenEven = []

        self.crossWalkEven = []
        self.crossWalkOdd = []

        self.carsXRight = []
        self.carsXLeft = []
        self.carsXLeftTurn = []
        self.carsYUp = []
        self.carsYDown = []
        self.carsYLeftTurn = []
        self.pedestrianRight = []
        self.pedestrianDown = []

        self.drawTrafficLights()

        
            
        self.make_cars()   
        
       
        self.update_traffic_lights_for_left_turn_NS()
        self.move_cars_schedule()

        


    def make_cars(self):
            car = self.drawCarXLeft(1000, 310, 'black')
            self.carsXLeftTurn.append(car)

            car = self.drawCarYDown(790, 600, 'gray')
            self.carsYLeftTurn.append(car)
            car = self.drawCarXRight(250, 380, 'blue')
            self.carsXRight.append(car)
            

            car = self.drawCarXLeft(1100, 310, 'yellow')
            self.carsXLeft.append(car)

            car = self.drawCarYDown(790, 680, 'orange')
            self.carsYDown.append(car)

            car = self.drawCarYUp(720, 70, 'purple')
            self.carsYUp.append(car)

            # 0 is for sideways, 1 is for up
            ped = self.drawPedestrian(600, 180, 0)
            self.pedestrianRight.append(ped)

            ped = self.drawPedestrian(600, 600, 1)
            self.pedestrianDown.append(ped)
            self.after(32000, self.make_cars)

    def drawTrafficLights(self):
        x = 550
        y = 200
        self.crossWalkOdd.append(self.canvas.create_rectangle(x, y, x+20, y+20, fill='red'))
        self.crossWalkOdd.append(self.canvas.create_rectangle(x, y+300, x+20, y+320, fill='red'))
        self.crossWalkOdd.append(self.canvas.create_rectangle(x+420, y, x+440, y+20, fill='red'))
        self.crossWalkOdd.append(self.canvas.create_rectangle(x+420, y+300, x+440, y+320, fill='red'))

        x = 610
        y = 140
        self.crossWalkEven.append(self.canvas.create_rectangle(x, y, x+20, y+20, fill='red'))
        self.crossWalkEven.append(self.canvas.create_rectangle(x, y+420, x+20, y+440, fill='red'))
        self.crossWalkEven.append(self.canvas.create_rectangle(x+300, y, x+320, y+20, fill='red'))
        self.crossWalkEven.append(self.canvas.create_rectangle(x+300, y+420, x+320, y+440, fill='red'))

        x = 650
        y = 390
        self.trafficLightBG(x, y, x+25, y+70)
        self.redOdd.append(self.canvas.create_oval(x+3, y+46, x+22, y+66, fill='red'))
        self.yellowOdd.append(self.canvas.create_oval(x+3, y+25, x+22, y+45, fill='gray'))
        self.greenOdd.append(self.canvas.create_oval(x+3, y+4, x+22, y+24, fill='gray'))
        
        x = 865
        y = 260
        self.trafficLightBG(x, y, x+25, y+70)
        self.redOdd.append(self.canvas.create_oval(x+3, y+4, x+22, y+24, fill='red'))
        self.yellowOdd.append(self.canvas.create_oval(x+3, y+25, x+22, y+45, fill='gray'))
        self.greenOdd.append(self.canvas.create_oval(x+3, y+46, x+22, y+66, fill='gray'))

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

        
    def update_traffic_lights_for_left_turn_NS(self):
        # Activate NS left turn by setting NS green lights to blue
        for greenLight in self.greenOdd:
            self.canvas.itemconfigure(greenLight, fill='blue')
        # Set all other lights to their inactive states
        for redLight in self.redEven:
            self.canvas.itemconfigure(redLight, fill='red')
        for redLight in self.redOdd:
            self.canvas.itemconfigure(redLight, fill='gray')
        for yellowLight in self.yellowOdd + self.yellowEven:
            self.canvas.itemconfigure(yellowLight, fill='gray')
        for greenLight in self.greenEven:
            self.canvas.itemconfigure(greenLight, fill='gray')
        # Ensure all pedestrian lights are red
        for crossWalk in self.crossWalkOdd + self.crossWalkEven:
            self.canvas.itemconfigure(crossWalk, fill='red')

        self.after(self.greenRedTime, self.update_traffic_lights_for_left_turn_EW)

    def update_traffic_lights_for_left_turn_EW(self):
        # Activate EW left turn by setting EW green lights to blue
        for greenLight in self.greenEven:
            self.canvas.itemconfigure(greenLight, fill='blue')
        # Set all other lights to their inactive states
        for redLight in self.redOdd :
            self.canvas.itemconfigure(redLight, fill='red')
        for redLight in self.redEven:
            self.canvas.itemconfigure(redLight, fill='gray')
        for yellowLight in self.yellowOdd + self.yellowEven:
            self.canvas.itemconfigure(yellowLight, fill='gray')
        for greenLight in self.greenOdd:
            self.canvas.itemconfigure(greenLight, fill='gray')

        for crossWalk in self.crossWalkOdd + self.crossWalkEven:
            self.canvas.itemconfigure(crossWalk, fill='red')
        self.after(self.greenRedTime, self.update_traffic_lights1)


    def update_traffic_lights1(self):

        for yellowLight, greenLight, redLight in zip(self.yellowOdd, self.greenOdd + self.greenEven, self.redOdd):
            self.canvas.itemconfigure(yellowLight, fill='gray')
            self.canvas.itemconfigure(greenLight, fill='gray')
            self.canvas.itemconfigure(redLight, fill='red')
        
        self.after(self.greenRedTime, self.update_traffic_lights2)

   

    def update_traffic_lights2(self):
        for redLight, yellowLight in zip(self.redOdd, self.yellowOdd):
            self.canvas.itemconfigure(redLight, fill='red')
            self.canvas.itemconfigure(yellowLight, fill='gray')

        for crossWalk in self.crossWalkEven:
            self.canvas.itemconfigure(crossWalk, fill='red')
        
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
        
        self.after(self.greenRedTime, self.update_traffic_lights5)
            
    def update_traffic_lights5(self):
        for redLight, yellowLight in zip(self.redEven, self.yellowEven):
            self.canvas.itemconfigure(redLight, fill='red')
            self.canvas.itemconfigure(yellowLight, fill='gray')

        for crossWalk in self.crossWalkOdd:
            self.canvas.itemconfigure(crossWalk, fill='red')
        
        self.after(self.yellowTime, self.update_traffic_lights6)

    def update_traffic_lights6(self):
        for redLight, greenLight in zip(self.redOdd, self.greenOdd):
            self.canvas.itemconfigure(redLight, fill='gray')
            self.canvas.itemconfigure(greenLight, fill='green')

        for crossWalk in self.crossWalkEven:
            self.canvas.itemconfigure(crossWalk, fill='green')
        
        self.after(self.greenRedTime, self.update_traffic_lights_for_left_turn_NS)


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

    def move_car_x_right(self):
        if self.canvas.itemcget(self.greenOdd[0], 'fill') == 'green':
            for car in self.carsXRight:
                self.canvas.move(car, 25, 0)
            for car in self.carsXLeft:
                self.canvas.move(car, -25, 0)
        if self.canvas.itemcget(self.crossWalkEven[0], 'fill') == 'green':
            for ped in self.pedestrianRight:
                self.canvas.move(ped, 10, 0)

        if self.canvas.itemcget(self.greenOdd[0], 'fill') == 'blue':
            for car in self.carsXLeftTurn:
                current_coords = self.canvas.coords(car)
                # Check if the car has already moved left by 250 units
                if current_coords[0] <= 700:  # Assuming the starting X position is 740 and needs to move left to 490 (740 - 250)
                    # If the car has reached its leftward position, start moving it down
                    self.canvas.move(car, 0, 25)
                else:
                    # If the car has not yet moved 250 units left, continue moving it left
                    self.canvas.move(car, -25, 0)

        if self.canvas.itemcget(self.greenEven[0], 'fill') == 'blue':
            for car in self.carsYLeftTurn:
                current_coords = self.canvas.coords(car)
                # Check if the car has already moved left by 250 units
                if current_coords[1] >= 320:  # Assuming the starting X position is 740 and needs to move left to 490 (740 - 250)
                    # If the car has reached its leftward position, start moving it down
                    self.canvas.move(car, 0, -25)
                else:
                    # If the car has not yet moved 250 units left, continue moving it left
                    self.canvas.move(car, -25, 0)
        
        if self.canvas.itemcget(self.greenEven[0], 'fill') == 'green' :
            for car in self.carsYUp:
                self.canvas.move(car, 0, 20)
            for car in self.carsYDown:
                self.canvas.move(car, 0, -20)
        if self.canvas.itemcget(self.crossWalkOdd[0], 'fill') == 'green':        
            for ped in self.pedestrianDown:
                self.canvas.move(ped, 0, -10)

    def move_cars_schedule(self):
        self.move_car_x_right()
        self.after(100, self.move_cars_schedule) 

    def drawCarXRight(self, x1, y1, color):
        x2 = x1 + 50
        y2 = y1 + 30
        radius = 5
       
        return self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 30, fill=color)
    


    def drawCarXLeft(self, x1, y1, color):
        x2 = x1 + 50
        y2 = y1 + 30
        radius = 5
        # body
        return self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 30, fill=color)

    def drawCarYDown(self, x1, y1, color):
        x2 = x1 + 50
        y2 = y1 + 30
        radius = 5
       
        return self.canvas.create_rectangle(x1, y1, x1 + 30, y1 + 50, fill=color)

    def drawCarYUp(self, x1, y1, color):
        x2 = x1 + 50
        y2 = y1 + 30
        radius = 5
        
        return self.canvas.create_rectangle(x1, y1, x1 + 30, y1 + 50, fill=color)

    def drawPedestrian(self, x1, y1, dir):
        radius = 5
        if dir == 0:
            x2 = x1 + 10
            y2 = y1 + 24
        else:
            x2 = x1 + 24
            y2 = y1 + 10
        # body
        if dir == 0:
            return self.canvas.create_oval(x1 - 1, y1 + 6, x2 + 1, y1 + 18, fill='gray')
        else:
            return self.canvas.create_oval(x1 + 6, y1 - 1, x1 + 18, y2 + 1, fill='gray')
        
        


if __name__ == "__main__":
    app = TrafficSimulation()
    app.mainloop()