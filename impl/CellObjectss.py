from services.Cell import cell


class PassiveGameObj(cell):

    def __init__(self, id, coordinates, designator):
        self.id = id

        self.coordinates = coordinates
        self.designator = designator

    def CoordinateUpdate(self, c):
        self.coordinates[0] = c[0]
        self.coordinates[1] = c[1]


class MovingGameObj(cell):

    def __init__(self, id, coordinates, designator):
        self.id = id
        self.life = 2

        self.coordinates = coordinates
        self.designator = designator
        self.previous_coordinates = coordinates.copy()

    def CoordinateUpdate(self, c):
        # print("inside p/CoordinateUpdate")
        self.coordinates[0] = c[0]
        self.coordinates[1] = c[1]

    def move(self, m):
        pass



    def CoordinateCalculate(self, move):
        pass
