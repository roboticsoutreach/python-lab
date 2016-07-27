from __future__ import division

import pygame
from math import pi, sin, cos
from ..game_object import GameObject
from ..markers import Token

from arena import Arena, ARENA_MARKINGS_COLOR, ARENA_MARKINGS_WIDTH, \
                    CORNER_COLOURS, fade_to_white

import pypybox2d

class Podium(GameObject):
    @property
    def location(self):
        return self._body.position

    @location.setter
    def location(self, new_pos):
        if self._body is None:
            return  # Slight hack: deal with the initial setting from the constructor
        self._body.position = new_pos

    @property
    def heading(self):
        return self._body.angle

    @heading.setter
    def heading(self, _new_heading):
        if self._body is None:
            return  # Slight hack: deal with the initial setting from the constructor
        self._body.angle = _new_heading

    def __init__(self, arena):
        self._body = arena._physics_world.create_body(position=(0, 0),
                                                      angle=0,
                                                      type=pypybox2d.body.Body.STATIC)
        self._body.create_polygon_fixture([(-0.25, -0.25),
                                           ( 0.25, -0.25),
                                           ( 0.25,  0.25),
                                           (-0.25,  0.25)],
                                          restitution=0.2,
                                          friction=0.3)
        super(Podium, self).__init__(arena)

    surface_name = 'sr/podium.png'

class Smallpeice2016Arena(Arena):
    start_locations = [(-3.6, -3.6),
                       ( 3.6, -3.6),
                       ( 3.6,  3.6),
                       (-3.6,  3.6)]

    start_headings = [0.25*pi,
                      0.75*pi,
                      -0.75*pi,
                      -0.25*pi]

    corner_token_locations = [
        (3.75, 2.75),
        (3.75, 2.5),
        (3.75, 2.25),
        (3.75, 2)
    ]

    starting_zone_side = 1

    zone_size = 2  # Zones are specified as 2m

    @staticmethod
    def _rotateCoords(coords, theta):
        return [(x[0]*cos(theta)-x[1]*sin(theta), x[0]*sin(theta)+x[1]*cos(theta)) for x in coords]

    def _init_tokens(self):
        for i, pos in enumerate(self.corners):
            angle = pi / 2.0 * i
            for j, location in enumerate(self._rotateCoords(self.corner_token_locations, angle)):
                token = Token(self, 0, damping=2.15)
                token.location = (location[0], location[1])
                token.heading = 0
                self.objects.append(token)
        # poisonToken = Token(self, 1, damping=2.15)
        # poisonToken.location = (0, 0)
        # poisonToken.heading = 0
        # self.objects.append(poisonToken)

    def _init_podium(self):
        podium = Podium(self)
        podium.location = (0, 0)
        podium.heading = 0
        self.objects.append(podium)

    def __init__(self, objects=None, wall_markers=True):
        super(Smallpeice2016Arena, self).__init__(objects, wall_markers)

        self._init_tokens()
        self._init_podium()

    def draw_background(self, surface, display):
        # No super call, deliberate to hide motif.

        surface.fill((0x11, 0x18, 0x33))

        def get_coord(x, y):
            return display.to_pixel_coord((x, y), self)
        # Corners of the inside Diamond
        centre = get_coord(0, 0)
        top = get_coord(0, self.zone_size)
        bottom = display.to_pixel_coord((0, -self.zone_size))
        left = display.to_pixel_coord((-self.zone_size, 0))
        right = display.to_pixel_coord((self.zone_size, 0))

        # Lines separating zones
        def line(start, end):
            pygame.draw.line(surface, ARENA_MARKINGS_COLOR,
                             start, end, ARENA_MARKINGS_WIDTH)

        # draw the cross in the centre
        line(centre, top)
        line(centre, bottom)
        line(centre, left)
        line(centre, right)

        # Draw the starting zones



        def towards_zero(point, dist):
            if point < 0:
                return point + dist
            else:
                return point - dist


        def starting_zone(x, y):
            length = self.starting_zone_side
            a = get_coord(towards_zero(x, length), y)
            b = get_coord(x, towards_zero(y, length))
            c = (a[0], b[1])

            line(a, c)
            line(b, c)


        for i, pos in enumerate(self.corners):
            starting_zone(*pos)

        # Draw the diamond around the cross
        pygame.draw.polygon(surface, ARENA_MARKINGS_COLOR,
                            [top, right, bottom, left], 2)
