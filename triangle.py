import math
import pygame

class Triangle:
    def __init__(self):
        pass

    def find_third_point(self, x1, y1, x2, y2):
    
        # find slope for AB
        m_ab = (y2 - y1) / (x2 - x1)

        # find slope for perpendicular BC
        m_bc = - 1 / m_ab

        # find length of AB
        len_ab = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)

        # find delta_x and delta_y
        delta_x = math.sqrt(len_ab**2 / (1 + m_bc**2))
        delta_y = m_bc * delta_x

        # determine the sign for the direction of the perpendicular line
        if m_bc > 0:
            sign = 1
        else:
            sign = -1

        # calculate the coordinate for the third point (two possible solutions)
        x3_1 = x2 + sign * delta_x
        y3_1 = y2 + sign * delta_y

        x3_2 = x2 - sign * delta_x
        y3_2 = y2 - sign * delta_y

        return (x3_1, y3_1), (x3_2, y3_2)
    
    def find_line_midpoint(self, x1, y1, x2, y2):
    
        midpoint_x = (x1 + x2) / 2
        midpoint_y = (y1 + y2) / 2

        return (midpoint_x, midpoint_y)       
    
    def get_points(self, event):

        points = []

        if event.type == pygame.MOUSEBUTTONDOWN:

            position = event.pos
            points.append(position)

            if len(points) == 3:

                vertex_c, __ = self.find_third_point(points[0][0], points[0][1], points[1][0], points[1][1])
                __, vertex_d = self.find_third_point(points[0][0], points[0][1], points[2][0], points[2][1])
                vertex_g = self.find_line_midpoint(vertex_c[0], vertex_c[1], vertex_d[0], vertex_d[1])
                points.append(vertex_c)
                points.append(vertex_d)
                points.append(vertex_g)

            return points

    def draw(self, event, window, s, a, b, c, d, g):

        if event.type == pygame.KEYDOWN:
            # triangle 1
            pygame.draw.polygon(window, 
                                (200, 0, 0), 
                                [s, a, c],
                                3)
            # triangle 2
            pygame.draw.polygon(window, 
                                (0, 0, 200), 
                                [s, b, d],
                                3)
            # line of third points
            pygame.draw.line(window, 
                            (255, 255, 255), 
                            c, 
                            d, 
                            3)
            # third triangle
            pygame.draw.polygon(window, 
                                (0, 0, 0), 
                                [a, b, g],
                                3)

if __name__ == "__main__":

    pass
