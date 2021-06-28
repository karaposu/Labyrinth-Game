from labyrinth import*
from random import randrange
from abc import *
import pickle
from impl.CellObjectss import *

import sys
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
print(sys.getrecursionlimit())
sys.setrecursionlimit(1000)


class GameLogic():
    def __init__(self,size):
        self.lab_size=size
        print("game ",self.lab_size)

        self.lab_obj = labyrinth(self.lab_size)
        self.maze=self.lab_obj.maze
        self.orig_maze=self.lab_obj.maze
        self.isLastCellWormHole=0
        self.Game_Completed=0
        self.treasure_captured=0
        self.lastcommand=0
        self.active_Wormhole_Number = 45
        self.Bear_active_Wormhole_Number= 99




    def Islastcoordinatewaswormhole(self,obj1,w_holes):


            print("----------------------------------------Islastcoordinatewaswormhole")
            # print("obj1.previous_coordinates",obj1.previous_coordinates)

            ll=list(w_holes.coordinates)
            # print("ll",ll)
            # print("obj1  current c : ",obj1.coordinates)
            # output=[0,0]
            output=0
            for i,coordinate in enumerate (ll):
                # print("i:",i)
                # print("coordinate:",coordinate)

                if obj1.previous_coordinates == coordinate:
                # if obj1.coordinates == coordinate:
                    # return 1,i
                    # output=[1,i]
                    output=1
                else:
                    pass
                    # print("else")

            return output

    def Collision_Status(self, movingobj,treasure, door,wormhole,bear ):

        # treasure_collision, door_is_reached, wormhole_collision, wormhole_number, bear_collision = self.Collision_Status(self.bear, self.treasure, self.door, self.wormsholes, self.player)



        treasure_captured = self.detect_collision_of_objects(movingobj, treasure)
        door_is_reached =   self.detect_collision_of_objects(movingobj, door)
        wormhole_collision, wormhole_number = self.detect_collision_of_objects(movingobj,wormhole)
        bear_collision = self.detect_collision_of_objects(movingobj, bear)

        return treasure_captured,door_is_reached,wormhole_collision,wormhole_number,bear_collision






    def detect_collision_of_objects(self,obj1,obj2):

        # print("----------------------------------------detect_collision_of_objects")
        # print("obj1.id ", obj1.id,  "obj2.id ", obj2.id," coordinates ",obj1.coordinates,"/" ,obj2.coordinates)

        if len(obj2.coordinates) > 2:
            ll=list(obj2.coordinates)
            # print("ll",ll)
            output=[0,0]
            for i,coordinate in enumerate (ll):
                if obj1.coordinates == coordinate:
                    output=[1,i]
                    # print("**** wormhole detected")

                else:
                    pass

            return output[0],output[1]


        if  obj1.coordinates==obj2.coordinates:
            return 1
        else:
            return 0

    def updateObjCoordinates(self,c, obj):
        # print('-' * 40, "updateObjCoordinates")
        # print(c)
        # print("b4 uppate ",obj.coordinates)

        obj.CoordinateUpdate(c)

        # print("after update ",obj.coordinates)


    def updateMazeWithObj(self,game_obj):

        # print("----------------------------------------updateMazeWithObj")
        # print("game_obj.id ", game_obj.id, ", Coordinates ",game_obj.coordinates)
        coor= game_obj.coordinates
        # print("len(coor) ", len(coor))
        # print("coor) ", coor)


        if game_obj.id==1:
        # if type(game_obj)==MovingGameObj :
        #     print("******************************* ")


            # print( "player previous Coordinates ", game_obj.previous_coordinates)
            # print( "player  Coordinates ", game_obj.coordinates)
            # restore last cell as "c"


            # print("w_holes", w_holes)
            # print("list(w_holes.coordinates) ", list(w_holes.coordinates))
            old_coor= game_obj.previous_coordinates

            # elif old_coor == self.door.coordinates:
            # self.maze[old_coor[0]][old_coor[1]] = "d"
            if old_coor in list(self.wormsholes.coordinates):

                self.maze[old_coor[0]][old_coor[1]] = "h"
            elif     old_coor==self.door.coordinates:
                self.maze[old_coor[0]][old_coor[1]] = "d"
            elif     old_coor==self.bear.coordinates:
                self.maze[old_coor[0]][old_coor[1]] = "b"
            else :
                self.maze[old_coor[0]][old_coor[1]] = "c"


        if game_obj.id==15:
        # if type(game_obj)==MovingGameObj :
        #     print("******************************* ")

            old_coor= game_obj.previous_coordinates

            if old_coor in list(self.wormsholes.coordinates):

                self.maze[old_coor[0]][old_coor[1]] = "h"
            elif     old_coor==self.door.coordinates:
                self.maze[old_coor[0]][old_coor[1]] = "d"
            elif     old_coor==self.treasure.coordinates:
                self.maze[old_coor[0]][old_coor[1]] = "t"
            else :
                self.maze[old_coor[0]][old_coor[1]] = "c"


            # print("aa ")
        if len(coor) >= 3:
            # print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb ")
            for a in range(len(coor)):

              c_w= coor[a]
              # print("c_w ", c_w)
              self.maze[c_w[0]][c_w[1]] = game_obj.designator

        else:
            # print("cccccccccccccccccccccccccccccc ")

            self.maze[coor[0]][coor[1]] = game_obj.designator

        self.lab_obj.maze =self.maze





    def CoordinateUpdate(self,c,obj):
        obj.coordinates[0]=c[0]
        obj.coordinates[1]=c[1]

    def NewCoordinateCalculateForObj(self,move,obj):
        # print("c cal move:", move)
        # print("self.coordinates[1]:", self.coordinates[1])
        if move==0:
             # goup
             y= obj.coordinates[1]
             x= obj.coordinates[0]-1
             return [x,y]
        if move ==1 :
            y = obj.coordinates[1] + 1
            x = obj.coordinates[0]
            return [x, y]

        if move==2:
            x = obj.coordinates[0]+1
            y = obj.coordinates[1]
            return [x, y]
        if move ==3 :
            y = obj.coordinates[1] - 1
            x = obj.coordinates[0]
            return [x, y]
        if move ==9 :
            y = obj.coordinates[1]
            x = obj.coordinates[0]
            return [x, y]


    def IsMoveLegit(self, c):
        size=int(self.lab_size)
        print("size",size)
        print("c[0]", c[0])
        print("c[1]", c[1])
        if size -1 >= c[0] and size -1 >= c[1] and 0<= c[1] and 0<= c[0]:


            if self.maze[c[0]][c[1]] != "w":
                return 0
            else:
                return 1
        else:
            return  1


    def randomMoveGenerator(self):
        l=[0,1,2,3]
        x = random.sample(l, 1)
        return x

    def MoveTheObject(self, m,id):
        print("-----------------------------------------------------------------------------------------------------")
        # obj = self.player
        message="  "
        if id==1:
            obj = self.player




        print("Obj:", obj.id, ",  Move:", m)
        normalmovelist = [0, 1, 2, 3, 9]
        if m in normalmovelist:

            message = "ok"





            New_c = self.NewCoordinateCalculateForObj(m, obj)
            # print("New C for MovingObj will be :", New_c)

            if self.IsMoveLegit(New_c) == 0:

                print(obj.previous_coordinates)
                # print("debugger james")
                obj.previous_coordinates = obj.coordinates.copy()
                self.updateObjCoordinates(New_c, obj)

                updated_c = obj.coordinates
                # print("Updated_c :", updated_c)

            else:
                message="Move not possible "


                return self.Game_Completed,message




        else:
                        print(" ---------Moving Through the Wormhole ")
                        message = "Wormhole"
                        print("zzzz:",message)
                        if self.active_Wormhole_Number == (len(self.wormsholes.coordinates) - 1):
                            next_worm_hole_coor = self.wormsholes.coordinates[0]
                            # print("looped wormholes")
                        else:

                            next_worm_hole_coor = self.wormsholes.coordinates[self.active_Wormhole_Number + 1]
                            # print(" Next_worm_hole_coor  ", next_worm_hole_coor)

                        obj.previous_coordinates = obj.coordinates.copy()
                        obj.CoordinateUpdate(next_worm_hole_coor)
                        updated_c = obj.coordinates
                        # print("New c after Wh:", updated_c)

        # ----------------------------------------------------------------------------Check Collision
        import traceback
        wormhole_collision = 0


        if id == 1:

            treasure_collision, door_is_reached, wormhole_collision, wormhole_number, bear_collision = self.Collision_Status(
             self.player,  self.treasure, self.door, self.wormsholes, self.bear)

            self.active_Wormhole_Number = wormhole_number






        if bear_collision == 1:
            self.player_life -= 1
            message = "********************    BEAR    ******************* "
            if self.player_life==0:
                return  1,"Game Failed.You used all of your life points."
            print("********************BEAR HIT******************* ")

        if treasure_collision == 1:
            self.treasure_captured = 1
            message="********************    You have the Treasure    ******************* "
            # print("********************You have the Treasure******************* ")

        if door_is_reached == 1:
            if self.treasure_captured == 1:
                print("You Win ")
                self.Game_Completed = 1
                message = "********************   Game_Completed    ******************* "
                # print("self.Game_Completed ")
            else:
                message = "You can't leave the labyrinth on attempt to pass through the exit without treasure "


        bypass = 0

        if m == 4:
            bypass = 1

        if wormhole_collision == 1:
            message="wormhole"
            if bypass == 0:
                # print("wormhole object collesion detected. Wormhole number: ", wormhole_number)

                self.updateMazeWithObj(obj)
                self.MoveTheObject(4,1)

                self.updateMazeWithObj(obj)
        else:
            # print("enes: ")
            self.updateMazeWithObj(obj)

        if m != 4:
            self.lab_obj.printMaze()

        # if self.lastcommand ==9 or m!=4:
        #     self.lab_obj.printMaze()

        # self.lastcommand = m

        print("self.Game_Completed", self.Game_Completed)
        return self.Game_Completed,message























    def BearMoveTheObject(self, m,id):

        # message=""
        # obj = self.player
        if id==15:
            obj = self.bear
            xx = self.randomMoveGenerator()
            m=xx[0]







        # print("Bear Obj:", obj.id, ",  Move:", m)
        normalmovelist = [0, 1, 2, 3, 9]
        if m in normalmovelist:


            old_c = obj.coordinates
            # print("old c:", old_c)
            # new_c = self.CoordinateCalculate(m)
            New_c = self.NewCoordinateCalculateForObj(m, obj)
            # print("Bear New C for MovingObj will be :", New_c)

            if self.IsMoveLegit(New_c) == 0:

                print(obj.previous_coordinates)
                # print("Bear debugger james")
                obj.previous_coordinates = obj.coordinates.copy()
                self.updateObjCoordinates(New_c, obj)

                updated_c = obj.coordinates
                # print("Bear Updated_c :", updated_c)

            else:
                print(" ")
                print("Bear tried to move to Wall ")

                return 0




        else:
                        print(" ---------Bear Moving Through the Wormhole ")

                        if self.active_Wormhole_Number == (len(self.wormsholes.coordinates) - 1):
                            next_worm_hole_coor = self.wormsholes.coordinates[0]
                            # print("Bear looped wormholes")
                        else:

                            next_worm_hole_coor = self.wormsholes.coordinates[self.active_Wormhole_Number + 1]
                            # print(" Bear Next_worm_hole_coor  ", next_worm_hole_coor)

                        obj.previous_coordinates = obj.coordinates.copy()
                        obj.CoordinateUpdate(next_worm_hole_coor)
                        updated_c = obj.coordinates
                        # print("Bear New c after Wh:", updated_c)

        # ----------------------------------------------------------------------------Check Collision
        import traceback
        wormhole_collision = 0

        # print(" Bear 2 debugger james")
        # print(" Bear id  : ", obj.id)
        if id == 1:
            # print("Bear  james 3")
            _, _, wormhole_collision, wormhole_number, _ = self.Collision_Status(
             self.bear,  self.treasure, self.door, self.wormsholes, self.player)

            self.Bear_active_Wormhole_Number = wormhole_number




        bypass = 0
        # if m != 9:
        # # if m != 9:
        #
        #     bypass = self.Islastcoordinatewaswormhole(obj, self.wormsholes)
        if m == 4:
            bypass = 1
        # print("bear bypass", bypass)
        # print("bear wormhole_collision", wormhole_collision)

        if wormhole_collision == 1:
            if bypass == 0:
                # print(" bear wormhole object collesion detected. Wormhole number: ", wormhole_number)

                self.updateMazeWithObj(obj)
                self.MoveTheObject(4,obj.id)

                self.updateMazeWithObj(obj)
        else:
            # print(" Bear enes: ")
            self.updateMazeWithObj(obj)

        if m != 4:
            self.lab_obj.printMaze()

        # if self.lastcommand ==9 or m!=4:
        #     self.lab_obj.printMaze()

        # self.lastcommand = m


        return 0






    def find_random_cell_coordinates(self ,n):

        # print("------------------------------find_random_cell_coordinates")
        empty_cell_index_list=[]
        random_cells=[]
        # [w,w,w,c], [w,c,c,c]
        # [0,1] , [1,1]

        for i,a in enumerate(self.maze):
            for ii,b in enumerate(a):
                # print("i :", i)
                # print("ii :", ii)
                if b=="c":
                    # print("ix :", i)
                    # print("iix :", ii)
                    # empty_cell_list.append([i,ii])
                    empty_cell_index_list.append([i,ii])

        x=random.sample(range(len(empty_cell_index_list)), n)
        # print("x:",x)
        # print("type x:",type(x))
        # x=randrange(len(empty_cell_index_list))
        for i in x:
            # print("i:", i)
            # print("empty_cell_index_list[i]:", empty_cell_index_list[i])

            random_cells.append(empty_cell_index_list[i])

        # print("random_cell:", random_cells)
        return tuple(random_cells)




    def gameBuilder(self):

        print("Gamebuilder is Working")
        n_of_w = 3

        self.player_life=2


        self.lab_obj.construct()
        rndm_w_c=self.find_random_cell_coordinates(3)
        self.wormsholes = PassiveGameObj(2, rndm_w_c, "h")
        # print("self.wormsholes c:", self.wormsholes.coordinates)
        self.updateMazeWithObj(self.wormsholes)

        rndm_c = self.find_random_cell_coordinates(1)
        self.door = PassiveGameObj(4, rndm_c[0], "d")
        self.updateMazeWithObj(self.door)


        rndm_c = self.find_random_cell_coordinates(1)

        self.treasure=PassiveGameObj( 3, rndm_c[0], "t")
        self.updateMazeWithObj(self.treasure)

        rndm_c = self.find_random_cell_coordinates(1)
        self.bear = MovingGameObj(15, rndm_c[0], "b")
        self.updateMazeWithObj(self.bear)

        rndm_c = self.find_random_cell_coordinates(1)
        self.player = MovingGameObj(1, rndm_c[0], "p")
        self.updateMazeWithObj(self.player)


        self.lab_obj.printMaze()

        Message="GAME BUILDED, YOU CAN MOVE THE PLAYER "
        return  0,Message


    def quit(self):
        pass


# maze genereator
# validater
# uml diagram
# extend

class cell(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self, id ,coordinates,designator):
        pass

    def CoordinateUpdate(self,c):
        pass















