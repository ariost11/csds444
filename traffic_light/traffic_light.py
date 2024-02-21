
import tkinter as tk

class TrafficSimulation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Traffic Simulation")
        self.geometry("400x400")
        self.canvas = tk.Canvas(self, width=400, height=400, bg='white')
        self.canvas.pack()
        self.draw_traffic_lights()
        self.change_lights()

    def draw_traffic_lights(self):
        self.canvas.create_rectangle(140, 100, 160, 300, fill='black')  # Vertical pole
        self.canvas.create_rectangle(100, 140, 300, 160, fill='black')  # Horizontal pole

        # Red lights
        self.red_light_north = self.canvas.create_oval(140, 100, 160, 120, fill='red')
        self.red_light_south = self.canvas.create_oval(140, 280, 160, 300, fill='red')
        self.red_light_west = self.canvas.create_oval(100, 140, 120, 160, fill='red')
        self.red_light_east = self.canvas.create_oval(280, 140, 300, 160, fill='red')

        # Yellow lights
        self.yellow_light_north = self.canvas.create_oval(140, 140, 160, 160, fill='gray')
        self.yellow_light_south = self.canvas.create_oval(140, 260, 160, 280, fill='gray')
        self.yellow_light_west = self.canvas.create_oval(140, 140, 160, 160, fill='yellow')
        self.yellow_light_east = self.canvas.create_oval(240, 140, 260, 160, fill='yellow')

        # Green lights
        self.green_light_north = self.canvas.create_oval(140, 220, 160, 240, fill='gray')
        self.green_light_south = self.canvas.create_oval(140, 180, 160, 200, fill='gray')
        self.green_light_west = self.canvas.create_oval(180, 140, 200, 160, fill='gray')
        self.green_light_east = self.canvas.create_oval(120, 140, 140, 160, fill='gray')

    def change_lights(self):
        self.switch_lights()
        self.after(5000, self.change_lights)

    def switch_lights(self):
        # Switching to green
        self.canvas.itemconfigure(self.red_light_north, fill='red')
        self.canvas.itemconfigure(self.red_light_south, fill='red')
        self.canvas.itemconfigure(self.red_light_west, fill='red')
        self.canvas.itemconfigure(self.red_light_east, fill='red')

        self.canvas.itemconfigure(self.green_light_north, fill='green')
        self.canvas.itemconfigure(self.green_light_south, fill='green')
        self.canvas.itemconfigure(self.green_light_west, fill='green')
        self.canvas.itemconfigure(self.green_light_east, fill='green')

        self.after(5000, self.switch_to_yellow)

    def switch_to_yellow(self):
        # Switching to yellow
        self.canvas.itemconfigure(self.green_light_north, fill='gray')
        self.canvas.itemconfigure(self.green_light_south, fill='gray')
        self.canvas.itemconfigure(self.green_light_west, fill='gray')
        self.canvas.itemconfigure(self.green_light_east, fill='gray')

        self.canvas.itemconfigure(self.yellow_light_north, fill='yellow')
        self.canvas.itemconfigure(self.yellow_light_south, fill='yellow')
        self.canvas.itemconfigure(self.yellow_light_west, fill='yellow')
        self.canvas.itemconfigure(self.yellow_light_east, fill='yellow')

        self.after(2000, self.switch_to_red)

    def switch_to_red(self):
        # Switching to red
        self.canvas.itemconfigure(self.yellow_light_north, fill='gray')
        self.canvas.itemconfigure(self.yellow_light_south, fill='gray')
        self.canvas.itemconfigure(self.yellow_light_west, fill='gray')
        self.canvas.itemconfigure(self.yellow_light_east, fill='gray')

        self.canvas.itemconfigure(self.red_light_north, fill='red')
        self.canvas.itemconfigure(self.red_light_south, fill='red')
        self.canvas.itemconfigure(self.red_light_west, fill='red')
        self.canvas.itemconfigure(self.red_light_east, fill='red')

if __name__ == "__main__":
    app = TrafficSimulation()
    app.mainloop()
