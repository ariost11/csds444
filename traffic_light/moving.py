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
        self.carsYUp = []
        self.carsYDown = []
        self.pedestrianRight = []
        self.pedestrianDown = []

        self.drawTrafficLights()

        car = self.drawCarXRight(250, 380, 'blue')
        self.carsXRight.append(car)
        

        car = self.drawCarXLeft(1000, 310, 'yellow')
        self.carsXLeft.append(car)

        car = self.drawCarYDown(790, 600, 'orange')
        self.carsYDown.append(car)

        car = self.drawCarYUp(720, 70, 'purple')
        self.carsYUp.append(car)

        # 0 is for sideways, 1 is for up
        ped = self.drawPedestrian(600, 180, 0)
        self.pedestrianRight.append(ped)

        ped = self.drawPedestrian(600, 600, 1)
        self.pedestrianDown.append(ped)
        
        self.after(self.greenRedTime, self.update_traffic_lights1)
        self.move_cars_schedule()

    
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

    def move_car_x_right(self):
        if self.canvas.itemcget(self.greenOdd[0], 'fill') == 'green':
            for car in self.carsXRight:
                self.canvas.move(car, 25, 0)
            for car in self.carsXLeft:
                self.canvas.move(car, -25, 0)
            for ped in self.pedestrianRight:
                self.canvas.move(ped, 10, 0)
        
        
        if self.canvas.itemcget(self.greenEven[0], 'fill') == 'green':
            for car in self.carsYUp:
                self.canvas.move(car, 0, 20)
            for car in self.carsYDown:
                self.canvas.move(car, 0, -20)
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



"""
import tkinter as tk

class TrafficSimulation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Traffic Simulation")
        self.geometry("800x600")

        # Create a canvas to draw the roads and cars
        self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack()

        # Draw roads
        self.draw_road(50, 200, 750, 200)
        self.draw_road(750, 200, 750, 400)
        self.draw_road(750, 400, 50, 400)
        self.draw_road(50, 400, 50, 200)

        # Draw traffic lights
        self.draw_traffic_light(400, 200)
        self.draw_traffic_light(400, 400)

        # Initialize car
        self.car = self.draw_car(100, 300)

        # Schedule car movement
        self.move_car()

    def draw_road(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, fill="black", width=5)

    def draw_traffic_light(self, x, y):
        self.canvas.create_rectangle(x - 10, y - 20, x + 10, y + 20, fill="black")
        self.red_light = self.canvas.create_oval(x - 5, y - 15, x + 5, y - 5, fill="red")
        self.green_light = self.canvas.create_oval(x - 5, y + 5, x + 5, y + 15, fill="green")

    def draw_car(self, x, y):
        # Draw multiple rectangles to represent the car
        car_body = self.canvas.create_rectangle(x, y, x + 40, y + 20, fill="blue")
        car_window = self.canvas.create_rectangle(x + 5, y + 5, x + 15, y + 15, fill="white")
        car_wheel1 = self.canvas.create_oval(x + 5, y + 18, x + 15, y + 28, fill="black")
        car_wheel2 = self.canvas.create_oval(x + 25, y + 18, x + 35, y + 28, fill="black")
        
        # Return a tuple containing all parts of the car
        return car_body, car_window, car_wheel1, car_wheel2

    def move_car(self):
        # Check the state of the traffic light
        traffic_light_state = self.canvas.itemcget(self.red_light, "fill")

        if traffic_light_state == "green":
            # Move the entire car forward
            self.canvas.move(self.car[0], 5, 0)  # Move the car body
            self.canvas.move(self.car[1], 5, 0)  # Move the car window
            self.canvas.move(self.car[2], 5, 0)  # Move wheel 1
            self.canvas.move(self.car[3], 5, 0)  # Move wheel 2

        # Schedule the next movement
        self.after(100, self.move_car)

if __name__ == "__main__":
    app = TrafficSimulation()
    app.mainloop()
"""