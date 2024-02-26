import unittest
from unittest.mock import MagicMock

class TrafficSimulation:
    def __init__(self, canvas):
        self.canvas = canvas
        self.carXR, self.carXL, self.carYD, self.carYU = [], [], [], []
        self.pedXR, self.pedXL, self.pedYD, self.pedYU = [], [], [], []
        self.greenOdd, self.greenEven, self.crossWalkEven, self.crossWalkOdd = [], [], [], []

    def moveCar(self):
        for car in self.carXR + self.carXL:
            if car in self.carXR:
                if self.greenOdd and self.canvas.itemcget(self.greenOdd[0], "fill") == 'green' or self.canvas.coords(car)[0] < 470:
                    self.canvas.move(car, 10, 0)
            elif car in self.carXL:
                if self.greenEven and self.canvas.itemcget(self.greenEven[0], "fill") == 'green' or self.canvas.coords(car)[0] > 530:
                    self.canvas.move(car, -10, 0)

    def movePedestrian(self):
        for ped in self.pedXR + self.pedXL:
            if ped in self.pedXR:
                if self.crossWalkEven and (self.canvas.itemcget(self.crossWalkEven[0], "fill") == 'green' or self.canvas.coords(ped)[0] < 600):
                    self.canvas.move(ped, -5, 0)
            elif ped in self.pedXL:
                if self.crossWalkOdd and (self.canvas.itemcget(self.crossWalkOdd[0], "fill") == 'green' or self.canvas.coords(ped)[0] > 400):
                    self.canvas.move(ped, 5, 0)

class TestTrafficSimulation(unittest.TestCase):
    def setUp(self):
        self.canvas = MagicMock()
        self.simulation = TrafficSimulation(self.canvas)

    def test_moveCar_greenLight(self):
        self.simulation.carXR = ['car1']
        self.canvas.itemcget.return_value = 'green'
        self.canvas.coords.return_value = [460, 0]   

        self.simulation.moveCar()
        self.canvas.move.assert_called_with('car1', 10, 0)

    def test_moveCar_redLight_within_boundary(self):
        self.simulation.carXL = ['car2']
        self.canvas.itemcget.return_value = 'red'
        self.canvas.coords.return_value = [540, 0]   

        self.simulation.moveCar()
        self.canvas.move.assert_called_with('car2', -10, 0)


    def test_no_movement_beyond_boundary_carXR(self):
        self.simulation.carXR = ['car3']
        self.canvas.coords.return_value = [470, 0]   

        self.simulation.moveCar()
        self.canvas.move.assert_not_called()

    def test_no_movement_beyond_boundary_carXL(self):
        self.simulation.carXL = ['car4']
        self.canvas.coords.return_value = [530, 0]   

        self.simulation.moveCar()
        self.canvas.move.assert_not_called()

    def test_no_movement_beyond_boundary_pedXR(self):
        self.simulation.pedXR = ['ped3']
        self.canvas.coords.return_value = [600, 0]   

        self.simulation.movePedestrian()
        self.canvas.move.assert_not_called()

    def test_no_movement_beyond_boundary_pedXL(self):
        self.simulation.pedXL = ['ped4']
        self.canvas.coords.return_value = [400, 0]   

        self.simulation.movePedestrian()
        self.canvas.move.assert_not_called()
    
    def test_no_movement_beyond_boundary_pedYR(self):
        self.simulation.pedXR = ['ped5']
        self.canvas.coords.return_value = [600, 0]   

        self.simulation.movePedestrian()
        self.canvas.move.assert_not_called()

    def test_no_movement_beyond_boundary_pedYL(self):
        self.simulation.pedXL = ['ped6']
        self.canvas.coords.return_value = [400, 0]   

        self.simulation.movePedestrian()
        self.canvas.move.assert_not_called()

    
    def test_moveCar_green(self):
        self.simulation.carXR = ['car4']
        self.canvas.itemcget.return_value = 'green'
        self.canvas.coords.return_value = [460, 0]   

        self.simulation.moveCar()
        self.canvas.move.assert_called_with('car4', 10, 0)

    def test_moveCar_red(self):
        self.simulation.carXL = ['car5']
        self.canvas.itemcget.return_value = 'red'
        self.canvas.coords.return_value = [540, 0]   

        self.simulation.moveCar()
        self.canvas.move.assert_called_with('car5', -10, 0)

    

if __name__ == '__main__':
    unittest.main()
