from __future__ import division

import os
import threading, pygame

from arenas import PiratePlunderArena, CTFArena, SunnySideUpArena, Smallpeice2016Arena
from display import Display

DEFAULT_GAME = 'smallpeice-2016'

GAMES = {
    'pirate-plunder': PiratePlunderArena,
    'ctf': CTFArena,
    'sunny-side-up': SunnySideUpArena,
    'smallpeice-2016': Smallpeice2016Arena,
}


class Simulator(object):
    def __init__(self, config={}, frames_per_second=30, background=True):
        try:
            game_name = config['game']
            del config['game']
        except KeyError:
            game_name = DEFAULT_GAME
        game = GAMES[game_name]

        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.arena = game(**config)

        self.background = background
        self.frames_per_second = frames_per_second

        if self.background:
            self._loop_thread = threading.Thread(target=self._main_loop, args=(frames_per_second,))
            self._loop_thread.setDaemon(False)
            self._loop_thread.start()

    def run(self):
        if self.background:
            raise RuntimeError('Simulator runs in the background. Try passing background=False')
        self._main_loop(self.frames_per_second)

    def _main_loop(self, frames_per_second):
        self.display = Display(self.arena)
        clock = pygame.time.Clock()

        while True:
            if any(event.type == pygame.QUIT
                   or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
                   for event in pygame.event.get()):
                # KILL IT ALL WITH FIRE!!
                # must be _exit with an error code to force the other threads to die too.
                os._exit(0)

            self.display.tick(1 / frames_per_second)
            clock.tick(frames_per_second)

        pygame.quit()
