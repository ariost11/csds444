import tkinter as tk
from PIL import Image, ImageTk
import time

class TrafficSimulation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Traffic Simulation")
        self.geometry("1540x730") 
        self.canvas = tk.Canvas(self, width=1550, height=740, bd=0, highlightthickness=0)
        self.image = tk.PhotoImage(file='/Users/omar/Library/Mobile Documents/com~apple~CloudDocs/Classes/spring24/CSDS444/csds444/traffic_light/background.png')  # Update path as needed
        self.image_id = self.canvas.create_image(770,360, image=self.image)
        self.canvas.pack()

        self.greenRedTime = 5000
        self.yellowTime = 3000

        self.redOdd = []
        self.yellowOdd = []
        self.greenOdd = []
        self.redEven = []
        self.yellowEven = []
        self.greenEven = []
        self.crossWalkEven = []
        self.crossWalkOdd = []

        self.cars = []
        self.pedestrians = []

        self.drawTrafficLights()

        self.cars.append(self.drawCarXRight(250, 380, 'blue'))
        self.cars.append(self.drawCarXLeft(300, 310, 'yellow'))
        self.cars.append(self.drawCarYDown(722, 600, 'orange'))
        self.cars.append(self.drawCarYUp(790, 70, 'purple'))

        self.pedestrians.append(self.drawPedestrian(300, 180, 0))
        self.pedestrians.append(self.drawPedestrian(600, 600, 1))

        self.after(self.greenRedTime, self.update_traffic_lights1)

    
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

        self.move_cars('EW')  # East-West cars can move
        self.move_pedestrians('NS')  # North-South pedestrians can move
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

    def move_cars(self, direction):
        # Logic to move cars based on direction
        speed = 5  # Adjust speed as needed
        for car in self.cars:
            if direction == 'EW':
                self.canvas.move(car, speed, 0)  # Move East-West cars
            elif direction == 'NS':
                self.canvas.move(car, 0, speed)  # Move North-South cars

    def move_pedestrians(self, direction):
        # Logic to move pedestrians based on direction
        speed = 3  # Adjust speed as needed
        for pedestrian in self.pedestrians:
            if direction == 'EW':
                self.canvas.move(pedestrian, speed, 0)  # Move East-West pedestrians
            elif direction == 'NS':
                self.canvas.move(pedestrian, 0, speed)  # Move North-South pedestrians


    def drawCarXRight(self, x1, y1, color):
        x2 = x1 + 50
        y2 = y1 + 30
        radius = 5
        # body
        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=color)
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=color)

        # lights
        self.canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.PIESLICE, fill='red')
        self.canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.PIESLICE, fill='white')
        self.canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.PIESLICE, fill='red')
        self.canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill='white')

        # windows
        self.canvas.create_rectangle(x1 + 13, y1 + 2, x1 + 37, y1 + 3, fill='black')
        self.canvas.create_rectangle(x1 + 13, y2 - 2, x1 + 37, y2 - 3, fill='black')
        self.canvas.create_rectangle(x1 + 30, y1 + 6, x1 + 40, y1 + 24, fill='black')
        self.canvas.create_rectangle(x1 + 20, y1 + 7, x1 + 27, y1 + 23, fill='gray')
        self.canvas.create_rectangle(x1 + 7, y1 + 6, x1 + 12, y1 + 24, fill='black')

    def drawCarXLeft(self, x1, y1, color):
        x2 = x1 + 50
        y2 = y1 + 30
        radius = 5
        # body
        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=color)
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=color)

        # lights
        self.canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.PIESLICE, fill='white')
        self.canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.PIESLICE, fill='red')
        self.canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.PIESLICE, fill='white')
        self.canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill='red')

        # windows
        self.canvas.create_rectangle(x2 - 13, y1 + 2, x2 - 37, y1 + 3, fill='black')
        self.canvas.create_rectangle(x2 - 13, y2 - 2, x2 - 37, y2 - 3, fill='black')
        self.canvas.create_rectangle(x2 - 30, y1 + 6, x2 - 40, y1 + 24, fill='black')
        self.canvas.create_rectangle(x2 - 20, y1 + 7, x2 - 27, y1 + 23, fill='gray')
        self.canvas.create_rectangle(x2 - 7, y1 + 6, x2 - 12, y1 + 24, fill='black')

    def drawCarYDown(self, x1, y1, color):
        x2 = x1 + 30
        y2 = y1 + 50
        radius = 5
        # body
        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=color)
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=color)

        # lights
        self.canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.PIESLICE, fill='red')
        self.canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.PIESLICE, fill='red')
        self.canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.PIESLICE, fill='white')
        self.canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill='white')

        # windows
        self.canvas.create_rectangle(x1 + 2, y1 + 13, x1 + 3, y1 + 37, fill='black')
        self.canvas.create_rectangle(x2 - 2, y1 + 13, x2 - 3, y1 + 37, fill='black')
        self.canvas.create_rectangle(x1 + 6, y1 + 30, x1 + 24, y1 + 40, fill='black')
        self.canvas.create_rectangle(x1 + 7, y1 + 20, x1 + 23, y1 + 27, fill='gray')
        self.canvas.create_rectangle(x1 + 6, y1 + 7, x1 + 24, y1 + 12, fill='black')

    def drawCarYUp(self, x1, y1, color):
        x2 = x1 + 30
        y2 = y1 + 50
        radius = 5
        # body
        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=color)
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=color)

        # lights
        self.canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.PIESLICE, fill='white')
        self.canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.PIESLICE, fill='white')
        self.canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.PIESLICE, fill='red')
        self.canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill='red')

        # windows
        self.canvas.create_rectangle(x1 + 2, y1 + 13, x1 + 3, y1 + 37, fill='black')
        self.canvas.create_rectangle(x2 - 2, y1 + 13, x2 - 3, y1 + 37, fill='black')
        self.canvas.create_rectangle(x1 + 6, y2 - 30, x1 + 24, y2 - 40, fill='black')
        self.canvas.create_rectangle(x1 + 7, y2 - 20, x1 + 23, y2 - 27, fill='gray')
        self.canvas.create_rectangle(x1 + 6, y2 - 7, x1 + 24, y2 - 12, fill='black')

    def drawPedestrian(self, x1, y1, dir):
        radius = 5
        if dir == 0:
            x2 = x1 + 10
            y2 = y1 + 24
        else:
            x2 = x1 + 24
            y2 = y1 + 10
        # body
        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill='black')
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill='black')
        self.canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.PIESLICE, fill='black')
        self.canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.PIESLICE, fill='black')
        self.canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.PIESLICE, fill='black')
        self.canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill='black')
        if dir == 0:
            self.canvas.create_oval(x1 - 1, y1 + 6, x2 + 1, y1 + 18, fill='gray')
        else:
            self.canvas.create_oval(x1 + 6, y1 - 1, x1 + 18, y2 + 1, fill='gray')
        
        


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
