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
        self.phases = cycle([('green', 'red', 'walk'), ('yellow', 'red', 'stop'), ('red', 'green', 'walk'), ('red', 'yellow', 'stop')])
        self.current_phase = next(self.phases)


    def draw_intersection(self):
        
        # Intersection
        self.canvas.create_rectangle(200, 0, 400, 600, fill='gray')
        self.canvas.create_rectangle(0, 200, 600, 400, fill='gray')
        
        # Road markings
        for i in range(10, 600, 20):
            self.canvas.create_line(i, 300, i+10, 300, fill='white')
            self.canvas.create_line(300, i, 300, i+10, fill='white')

        for i in range(1,11):
            self.canvas.create_rectangle(205 + 20*(i-1),160,215 + 20*(i-1),190, fill='white')
            self.canvas.create_rectangle(205 + 20*(i-1),410,215 + 20*(i-1),440, fill='white')
            self.canvas.create_rectangle(155,205 + 20*(i-1),185,215 + 20*(i-1), fill='white')
            self.canvas.create_rectangle(405,205 + 20*(i-1),435,215 + 20*(i-1), fill='white')

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
        self.current_phase = next(self.phases)  # Reset the phase

    def simulate_traffic(self):
        if not self.running:
            return

        ns_state, ew_state, ped_state = self.current_phase

        for i, light in enumerate(self.traffic_lights):
            light.set_state(ns_state if i % 2 == 0 else ew_state)

        for i, signal in enumerate(self.pedestrian_signals):
            signal.set_state(ped_state if self.traffic_lights[i].state in ['red', 'yellow'] else 'stop')

        self.current_phase = next(self.phases)
        self.master.after(self.cycle_interval, self.simulate_traffic)

class TrafficLight:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.state = 'red'
        self.ovals = [
            canvas.create_oval(x-10, y-30, x+10, y-10, fill='red'),  # Red light
            canvas.create_oval(x-10, y, x+10, y+20, fill='gray'),  # Yellow light
            canvas.create_oval(x-10, y+30, x+10, y+50, fill='gray')  # Green light
        ]

    def set_state(self, state):
        self.state = state
        colors = {'red': 'red', 'yellow': 'yellow', 'green': 'green', 'gray': 'gray'}
        for oval, color in zip(self.ovals, ['red', 'yellow', 'green']):
            self.canvas.itemconfig(oval, fill=colors[color] if state == color else colors['gray'])

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
