import tkinter as tk
from itertools import cycle

class TrafficSimulationApp:
    def __init__(self, master):
        self.master = master
        self.cycle_interval = 5000  # Interval for cycling through lights, adjustable
        master.title("Traffic Simulation")

        self.canvas = tk.Canvas(master, width=600, height=600, bg='white')
        self.canvas.pack()
        self.draw_intersection()
        self.traffic_lights = self.init_traffic_lights()
        self.pedestrian_signals = self.init_pedestrian_signals()

        self.start_button = tk.Button(master, text="Start", command=self.start_simulation)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_simulation)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_simulation)
        self.reset_button.pack(side=tk.LEFT)

        self.running = False
        self.current_phase = None

    def draw_crosswalk(self, x1, y1, x2, y2):
        spacing = 40  # Adjust spacing accordingly
        width = 10
        length = 30
        if x1 == x2:  # Vertical crosswalk
            for i in range(y1, y2, spacing):
                self.canvas.create_rectangle(x1-width/2, i, x1+width/2, i+length, fill='white')
        else:  # Horizontal crosswalk
            for i in range(x1, x2, spacing):
                self.canvas.create_rectangle(i, y1-width/2, i+length, y1+width/2, fill='white')

    def draw_intersection(self):
        # Crosswalks
        self.draw_crosswalk(190, 0, 190, 200)  # North crosswalk
        self.draw_crosswalk(410, 0, 410, 200)  # North crosswalk
        self.draw_crosswalk(190, 400, 190, 600)  # South crosswalk
        self.draw_crosswalk(410, 400, 410, 600)  # South crosswalk
        self.draw_crosswalk(0, 190, 200, 190)  # West crosswalk
        self.draw_crosswalk(0, 410, 200, 410)  # West crosswalk
        self.draw_crosswalk(400, 190, 600, 190)  # East crosswalk
        self.draw_crosswalk(400, 410, 600, 410)  # East crosswalk
        
        # Intersection
        self.canvas.create_rectangle(200, 0, 400, 600, fill='gray')
        self.canvas.create_rectangle(0, 200, 600, 400, fill='gray')
        
        # Road markings
        for i in range(10, 600, 20):
            self.canvas.create_line(i, 300, i+10, 300, fill='white')
            self.canvas.create_line(300, i, 300, i+10, fill='white')

    def init_traffic_lights(self):
        coords = [(300, 50), (550, 300), (300, 550), (50, 300)]
        return [TrafficLight(self.canvas, x, y) for x, y in coords]

    def init_pedestrian_signals(self):
        coords = [(300, 150), (450, 300), (300, 450), (150, 300)]
        return [PedestrianSignal(self.canvas, x, y) for x, y in coords]

    def start_simulation(self):
        if not self.running:
            self.running = True
            self.simulate_traffic()

    def stop_simulation(self):
        self.running = False

    def reset_simulation(self):
        self.stop_simulation()
        for light in self.traffic_lights:
            light.set_state('red')
        for signal in self.pedestrian_signals:
            signal.set_state('stop')

    def simulate_traffic(self):
        if not self.running:
            return
        phases = cycle([('green', 'red'), ('yellow', 'red'), ('red', 'green'), ('red', 'yellow')])
        self.current_phase = self.current_phase or next(phases)
        ns_state, ew_state = self.current_phase

        for i, light in enumerate(self.traffic_lights):
            light.set_state(ns_state if i % 2 == 0 else ew_state)

        for i, signal in enumerate(self.pedestrian_signals):
            signal.set_state('walk' if self.traffic_lights[i].state == 'red' else 'stop')

        self.current_phase = next(phases)
        self.master.after(self.cycle_interval, self.simulate_traffic)

class TrafficLight:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.state = 'red'
        self.ovals = [
            canvas.create_oval(x-10, y-30, x+10, y-10, fill='red'),
            canvas.create_oval(x-10, y, x+10, y+20, fill='gray'),
            canvas.create_oval(x-10, y+30, x+10, y+50, fill='gray')
        ]

    def set_state(self, state):
        self.state = state
        colors = {'red': 'red', 'yellow': 'yellow', 'green': 'green', 'gray': 'gray'}
        for oval, color in zip(self.ovals, ['red', 'yellow', 'green']):
            self.canvas.itemconfig(oval, fill=colors['gray'] if state != color else colors[color])

class PedestrianSignal:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.state = 'stop'
        self.signal = canvas.create_rectangle(x-20, y-20, x+20, y+20, fill='red')
        self.text = canvas.create_text(x, y, text='STOP', fill='white')

    def set_state(self, state):
        self.state = state
        color = 'green' if state == 'walk' else 'red'
        text = 'WALK' if state == 'walk' else 'STOP'
        self.canvas.itemconfig(self.signal, fill=color)
        self.canvas.itemconfig(self.text, text=text, fill='white' if state == 'walk' else 'black')

def main():
    root = tk.Tk()
    app = TrafficSimulationApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
