import random
import time
from colorama import init
from colorama import Fore, Back, Style


class labyrinth():
    def __init__(self,size):

        self.maze = []
        wall = 'w'
        cell = 'c'
        unvisited = 'u'
        if type(size)==str:
            size= int(size)
            print("....string argument changed to int")

        self.size = size
        self.height = size
        self.width = size

        maze = []

    def printMaze(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if (self.maze[i][j] == 'u'):
                    print(Fore.WHITE + str(self.maze[i][j]), end=" ")
                elif (self.maze[i][j] == 'c'):
                    print(Fore.GREEN + str(self.maze[i][j]), end=" ")
                elif (self.maze[i][j] == 'p'):
                    print(Fore.BLUE + str(self.maze[i][j]), end=" ")
                elif (self.maze[i][j] == 't'):
                    print(Fore.WHITE + str(self.maze[i][j]), end=" ")
                elif (self.maze[i][j] == 'h'):
                    print(Fore.YELLOW + str(self.maze[i][j]), end=" ")
                elif (self.maze[i][j] == 'd'):
                    print(Fore.LIGHTBLACK_EX + str(self.maze[i][j]), end=" ")
                elif (self.maze[i][j] == 'b'):
                    print(Fore.RED + str(self.maze[i][j]), end=" ")
                else:
                    print(Fore.WHITE + str(self.maze[i][j]), end=" ")

            print('\n')

    # Find number of surrounding cells
    def surroundingCells(self, rand_wall):
        s_cells = 0
        if (self.maze[rand_wall[0] - 1][rand_wall[1]] == 'c'):
            s_cells += 1
        if (self.maze[rand_wall[0] + 1][rand_wall[1]] == 'c'):
            s_cells += 1
        if (self.maze[rand_wall[0]][rand_wall[1] - 1] == 'c'):
            s_cells += 1
        if (self.maze[rand_wall[0]][rand_wall[1] + 1] == 'c'):
            s_cells += 1

        return s_cells

    def construct(self):
            wall = 'w'
            cell = 'c'
            unvisited = 'u'
            height = 5
            width = 5
            # maze = []
            # Initialize colorama
            init()
            z=self.height
            print(z)
            print(type(z))


            # Denote all cells as unvisited
            for i in range(0, self.height):
               line = []
               for j in range(0, self.width):
                    line.append(unvisited)
               self.maze.append(line)



            # Randomize starting point and set it a cell
            starting_height = int(random.random() * self.height)
            starting_width = int(random.random() * self.width)
            if (starting_height == 0):
                starting_height += 1
            if (starting_height == self.height - 1):
                starting_height -= 1
            if (starting_width == 0):
                starting_width += 1
            if (starting_width == self.width - 1):
                starting_width -= 1

            # Mark it as cell and add surrounding walls to the list
            self.maze[starting_height][starting_width] = cell
            walls = []
            walls.append([starting_height - 1, starting_width])
            walls.append([starting_height, starting_width - 1])
            walls.append([starting_height, starting_width + 1])
            walls.append([starting_height + 1, starting_width])

            # Denote walls in maze
            self.maze[starting_height - 1][starting_width] = 'w'
            self.maze[starting_height][starting_width - 1] = 'w'
            self.maze[starting_height][starting_width + 1] = 'w'
            self.maze[starting_height + 1][starting_width] = 'w'

            while (walls):
                # Pick a random wall
                rand_wall = walls[int(random.random() * len(walls)) - 1]

                # Check if it is a left wall
                if (rand_wall[1] != 0):
                    if (self.maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and self.maze[rand_wall[0]][rand_wall[1] + 1] == 'c'):
                        # Find the number of surrounding cells
                        s_cells = self.surroundingCells(rand_wall)

                        if (s_cells < 2):
                            # Denote the new path
                            self.maze[rand_wall[0]][rand_wall[1]] = 'c'

                            # Mark the new walls
                            # Upper cell
                            if (rand_wall[0] != 0):
                                if (self.maze[rand_wall[0] - 1][rand_wall[1]] != 'c'):
                                    self.maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
                                if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                                    walls.append([rand_wall[0] - 1, rand_wall[1]])

                            # Bottom cell
                            if (rand_wall[0] != self.height - 1):
                                if (self.maze[rand_wall[0] + 1][rand_wall[1]] != 'c'):
                                    self.maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
                                if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                                    walls.append([rand_wall[0] + 1, rand_wall[1]])

                            # Leftmost cell
                            if (rand_wall[1] != 0):
                                if (self.maze[rand_wall[0]][rand_wall[1] - 1] != 'c'):
                                    self.maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
                                if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                                    walls.append([rand_wall[0], rand_wall[1] - 1])

                        # Delete wall
                        for wall in walls:
                            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                                walls.remove(wall)

                        continue

                # Check if it is an upper wall
                if (rand_wall[0] != 0):
                    if (self.maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and self.maze[rand_wall[0] + 1][rand_wall[1]] == 'c'):

                        s_cells = self.surroundingCells(rand_wall)
                        if (s_cells < 2):
                            # Denote the new path
                            self.maze[rand_wall[0]][rand_wall[1]] = 'c'

                            # Mark the new walls
                            # Upper cell
                            if (rand_wall[0] != 0):
                                if (self.maze[rand_wall[0] - 1][rand_wall[1]] != 'c'):
                                    self.maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
                                if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                                    walls.append([rand_wall[0] - 1, rand_wall[1]])

                            # Leftmost cell
                            if (rand_wall[1] != 0):
                                if (self.maze[rand_wall[0]][rand_wall[1] - 1] != 'c'):
                                    self.maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
                                if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                                    walls.append([rand_wall[0], rand_wall[1] - 1])

                            # Rightmost cell
                            if (rand_wall[1] != self.width - 1):
                                if (self.maze[rand_wall[0]][rand_wall[1] + 1] != 'c'):
                                    self.maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
                                if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                                    walls.append([rand_wall[0], rand_wall[1] + 1])

                        # Delete wall
                        for wall in walls:
                            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                                walls.remove(wall)

                        continue

                # Check the bottom wall
                if (rand_wall[0] != self.height - 1):
                    if (self.maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and self.maze[rand_wall[0] - 1][rand_wall[1]] == 'c'):

                        s_cells = self.surroundingCells(rand_wall)
                        if (s_cells < 2):
                            # Denote the new path
                            self.maze[rand_wall[0]][rand_wall[1]] = 'c'

                            # Mark the new walls
                            if (rand_wall[0] != self.height - 1):
                                if (self.maze[rand_wall[0] + 1][rand_wall[1]] != 'c'):
                                    self.maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
                                if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                                    walls.append([rand_wall[0] + 1, rand_wall[1]])
                            if (rand_wall[1] != 0):
                                if (self.maze[rand_wall[0]][rand_wall[1] - 1] != 'c'):
                                    self.maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
                                if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                                    walls.append([rand_wall[0], rand_wall[1] - 1])
                            if (rand_wall[1] != self.width - 1):
                                if (self.maze[rand_wall[0]][rand_wall[1] + 1] != 'c'):
                                    self.maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
                                if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                                    walls.append([rand_wall[0], rand_wall[1] + 1])

                        # Delete wall
                        for wall in walls:
                            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                                walls.remove(wall)

                        continue

                # Check the right wall
                if (rand_wall[1] != self.width - 1):
                    if (self.maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and self.maze[rand_wall[0]][rand_wall[1] - 1] == 'c'):

                        s_cells = self.surroundingCells(rand_wall)
                        if (s_cells < 2):
                            # Denote the new path
                            self.maze[rand_wall[0]][rand_wall[1]] = 'c'

                            # Mark the new walls
                            if (rand_wall[1] != self.width - 1):
                                if (self.maze[rand_wall[0]][rand_wall[1] + 1] != 'c'):
                                    self.maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
                                if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                                    walls.append([rand_wall[0], rand_wall[1] + 1])
                            if (rand_wall[0] != self.height - 1):
                                if (self.maze[rand_wall[0] + 1][rand_wall[1]] != 'c'):
                                    self.maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
                                if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                                    walls.append([rand_wall[0] + 1, rand_wall[1]])
                            if (rand_wall[0] != 0):
                                if (self.maze[rand_wall[0] - 1][rand_wall[1]] != 'c'):
                                    self.maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
                                if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                                    walls.append([rand_wall[0] - 1, rand_wall[1]])

                        # Delete wall
                        for wall in walls:
                            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                                walls.remove(wall)

                        continue

                # Delete the wall from the list anyway
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

            # Mark the remaining unvisited cells as walls
            for i in range(0, self.height):
                for j in range(0, self.width):
                    if (self.maze[i][j] == 'u'):
                        self.maze[i][j] = 'w'

            # Set entrance and exit
            for i in range(0, self.width):
                if (self.maze[1][i] == 'c'):
                    self.maze[0][i] = 'c'
                    break

            for i in range(self.width - 1, 0, -1):
                if (self.maze[self.height - 2][i] == 'c'):
                    self.maze[self.height - 1][i] = 'c'
                    break






    # def construct(self):
    #         wall = 'w'
    #         cell = 'c'
    #         unvisited = 'u'
    #         height = 5
    #         width = 5
    #         # maze = []
    #
    #
    #
    #         # Initialize colorama
    #         init()
    #
    #
    #         # Denote all cells as unvisited
    #         for i in range(0, self.height):
    #             line = []
    #             for j in range(0, self.width):
    #                 line.append(unvisited)
    #             self.maze.append(line)
    #
    #         # Randomize starting point and set it a cell
    #         starting_height = int(random.random() * self.height)
    #         starting_width = int(random.random() * self.width)
    #         if (starting_height == 0):
    #             starting_height += 1
    #         if (starting_height == self.height - 1):
    #             starting_height -= 1
    #         if (starting_width == 0):
    #             starting_width += 1
    #         if (starting_width == self.width - 1):
    #             starting_width -= 1
    #
    #         # Mark it as cell and add surrounding walls to the list
    #         self.maze[starting_height][starting_width] = cell
    #         walls = []
    #         walls.append([starting_height - 1, starting_width])
    #         walls.append([starting_height, starting_width - 1])
    #         walls.append([starting_height, starting_width + 1])
    #         walls.append([starting_height + 1, starting_width])
    #
    #         # Denote walls in maze
    #         self.maze[starting_height - 1][starting_width] = 'w'
    #         self.maze[starting_height][starting_width - 1] = 'w'
    #         self.maze[starting_height][starting_width + 1] = 'w'
    #         self.maze[starting_height + 1][starting_width] = 'w'
    #
    #         while (walls):
    #             # Pick a random wall
    #             rand_wall = walls[int(random.random() * len(walls)) - 1]
    #
    #             # Check if it is a left wall
    #             if (rand_wall[1] != 0):
    #                 if (self.maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and self.maze[rand_wall[0]][rand_wall[1] + 1] == 'c'):
    #                     # Find the number of surrounding cells
    #                     s_cells = self.surroundingCells(rand_wall)
    #
    #                     if (s_cells < 2):
    #                         # Denote the new path
    #                         self.maze[rand_wall[0]][rand_wall[1]] = 'c'
    #
    #                         # Mark the new walls
    #                         # Upper cell
    #                         if (rand_wall[0] != 0):
    #                             if (self.maze[rand_wall[0] - 1][rand_wall[1]] != 'c'):
    #                                 self.maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
    #                             if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
    #                                 walls.append([rand_wall[0] - 1, rand_wall[1]])
    #
    #                         # Bottom cell
    #                         if (rand_wall[0] != self.height - 1):
    #                             if (self.maze[rand_wall[0] + 1][rand_wall[1]] != 'c'):
    #                                 self.maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
    #                             if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
    #                                 walls.append([rand_wall[0] + 1, rand_wall[1]])
    #
    #                         # Leftmost cell
    #                         if (rand_wall[1] != 0):
    #                             if (self.maze[rand_wall[0]][rand_wall[1] - 1] != 'c'):
    #                                 self.maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
    #                             if ([rand_wall[0], rand_wall[1] - 1] not in walls):
    #                                 walls.append([rand_wall[0], rand_wall[1] - 1])
    #
    #                     # Delete wall
    #                     for wall in walls:
    #                         if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
    #                             walls.remove(wall)
    #
    #                     continue
    #
    #             # Check if it is an upper wall
    #             if (rand_wall[0] != 0):
    #                 if (self.maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and self.maze[rand_wall[0] + 1][rand_wall[1]] == 'c'):
    #
    #                     s_cells = self.surroundingCells(rand_wall)
    #                     if (s_cells < 2):
    #                         # Denote the new path
    #                         self.maze[rand_wall[0]][rand_wall[1]] = 'c'
    #
    #                         # Mark the new walls
    #                         # Upper cell
    #                         if (rand_wall[0] != 0):
    #                             if (self.maze[rand_wall[0] - 1][rand_wall[1]] != 'c'):
    #                                 self.maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
    #                             if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
    #                                 walls.append([rand_wall[0] - 1, rand_wall[1]])
    #
    #                         # Leftmost cell
    #                         if (rand_wall[1] != 0):
    #                             if (self.maze[rand_wall[0]][rand_wall[1] - 1] != 'c'):
    #                                 self.maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
    #                             if ([rand_wall[0], rand_wall[1] - 1] not in walls):
    #                                 walls.append([rand_wall[0], rand_wall[1] - 1])
    #
    #                         # Rightmost cell
    #                         if (rand_wall[1] != self.width - 1):
    #                             if (self.maze[rand_wall[0]][rand_wall[1] + 1] != 'c'):
    #                                 self.maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
    #                             if ([rand_wall[0], rand_wall[1] + 1] not in walls):
    #                                 walls.append([rand_wall[0], rand_wall[1] + 1])
    #
    #                     # Delete wall
    #                     for wall in walls:
    #                         if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
    #                             walls.remove(wall)
    #
    #                     continue
    #
    #             # Check the bottom wall
    #             if (rand_wall[0] != self.height - 1):
    #                 if (self.maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and self.maze[rand_wall[0] - 1][rand_wall[1]] == 'c'):
    #
    #                     s_cells = self.surroundingCells(rand_wall)
    #                     if (s_cells < 2):
    #                         # Denote the new path
    #                         self.maze[rand_wall[0]][rand_wall[1]] = 'c'
    #
    #                         # Mark the new walls
    #                         if (rand_wall[0] != self.height - 1):
    #                             if (self.maze[rand_wall[0] + 1][rand_wall[1]] != 'c'):
    #                                 self.maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
    #                             if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
    #                                 walls.append([rand_wall[0] + 1, rand_wall[1]])
    #                         if (rand_wall[1] != 0):
    #                             if (self.maze[rand_wall[0]][rand_wall[1] - 1] != 'c'):
    #                                 self.maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
    #                             if ([rand_wall[0], rand_wall[1] - 1] not in walls):
    #                                 walls.append([rand_wall[0], rand_wall[1] - 1])
    #                         if (rand_wall[1] != self.width - 1):
    #                             if (self.maze[rand_wall[0]][rand_wall[1] + 1] != 'c'):
    #                                 self.maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
    #                             if ([rand_wall[0], rand_wall[1] + 1] not in walls):
    #                                 walls.append([rand_wall[0], rand_wall[1] + 1])
    #
    #                     # Delete wall
    #                     for wall in walls:
    #                         if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
    #                             walls.remove(wall)
    #
    #                     continue
    #
    #             # Check the right wall
    #             if (rand_wall[1] != self.width - 1):
    #                 if (self.maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and self.maze[rand_wall[0]][rand_wall[1] - 1] == 'c'):
    #
    #                     s_cells = self.surroundingCells(rand_wall)
    #                     if (s_cells < 2):
    #                         # Denote the new path
    #                         self.maze[rand_wall[0]][rand_wall[1]] = 'c'
    #
    #                         # Mark the new walls
    #                         if (rand_wall[1] != self.width - 1):
    #                             if (self.maze[rand_wall[0]][rand_wall[1] + 1] != 'c'):
    #                                 self.maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
    #                             if ([rand_wall[0], rand_wall[1] + 1] not in walls):
    #                                 walls.append([rand_wall[0], rand_wall[1] + 1])
    #                         if (rand_wall[0] != self.height - 1):
    #                             if (self.maze[rand_wall[0] + 1][rand_wall[1]] != 'c'):
    #                                 self.maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
    #                             if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
    #                                 walls.append([rand_wall[0] + 1, rand_wall[1]])
    #                         if (rand_wall[0] != 0):
    #                             if (self.maze[rand_wall[0] - 1][rand_wall[1]] != 'c'):
    #                                 self.maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
    #                             if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
    #                                 walls.append([rand_wall[0] - 1, rand_wall[1]])
    #
    #                     # Delete wall
    #                     for wall in walls:
    #                         if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
    #                             walls.remove(wall)
    #
    #                     continue
    #
    #             # Delete the wall from the list anyway
    #             for wall in walls:
    #                 if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
    #                     walls.remove(wall)
    #
    #         # Mark the remaining unvisited cells as walls
    #         for i in range(0, self.height):
    #             for j in range(0, self.width):
    #                 if (self.maze[i][j] == 'u'):
    #                     self.maze[i][j] = 'w'
    #
    #         # Set entrance and exit
    #         for i in range(0, self.width):
    #             if (self.maze[1][i] == 'c'):
    #                 self.maze[0][i] = 'c'
    #                 break
    #
    #         for i in range(self.width - 1, 0, -1):
    #             if (self.maze[self.height - 2][i] == 'c'):
    #                 self.maze[self.height - 1][i] = 'c'
    #                 break

            # Print final maze
            # self.printMaze()


# ikram=labyrinth(5)
# ikram.construct()
# print(ikram.maze)
# print(ikram.printMaze())