from roboarm import Arm
from pygame import constants
import pygame
import time


HELP_TEXT = """
Open grips - a
Close grips - z
Up wrist - s
Down wrist - x
Up elbow - d
Down elbow - c
Up shoulder - f
Down shoulder - v
Rotate clockwise - g
Rotate counterclockwise - b
Led on - q
Led off - w
Exit - esc
"""


class Controller(object):
    """Basic arm controller"""

    def __init__(self):
        self._arm = Arm()
        self._init_pygame()
        self._init_actions()

    def _init_actions(self):
        """Init actions"""
        self.actions = {
            constants.KEYDOWN: {
                constants.K_a: self._arm.grips.open,
                constants.K_s: self._arm.wrist.up,
                constants.K_d: self._arm.elbow.up,
                constants.K_f: self._arm.shoulder.up,
                constants.K_g: self._arm.base.rotate_clock,

                constants.K_z: self._arm.grips.close,
                constants.K_x: self._arm.wrist.down,
                constants.K_c: self._arm.elbow.down,
                constants.K_v: self._arm.shoulder.down,
                constants.K_b: self._arm.base.rotate_counter,

                constants.K_q: self._arm.led.on,
                constants.K_w: self._arm.led.off,
            },
            constants.KEYUP: {
                constants.K_a: self._arm.grips.stop,
                constants.K_s: self._arm.wrist.stop,
                constants.K_d: self._arm.elbow.stop,
                constants.K_f: self._arm.shoulder.stop,
                constants.K_g: self._arm.base.stop,

                constants.K_z: self._arm.grips.stop,
                constants.K_x: self._arm.wrist.stop,
                constants.K_c: self._arm.elbow.stop,
                constants.K_v: self._arm.shoulder.stop,
                constants.K_b: self._arm.base.stop,
            },
        }

    def _init_pygame(self):
        """Init pygame"""
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        self.window.fill((0, 0, 0))
        pygame.display.set_caption('Roboarm controller')
        self._draw_help()

    def _draw_help(self):
        """Draw help"""
        font = pygame.font.SysFont(None, 30)
        for num, line in enumerate(HELP_TEXT.split('\n')[1:]):
            help_line = font.render(line, True, (255, 255, 255))
            self.window.blit(help_line, (30, 10 + num * 35))
        pygame.display.flip()

    def loop(self):
        """Main actions loop"""
        while True:
            for event in pygame.event.get():
                if event.type is constants.QUIT:
                    return

                if event.type is constants.KEYUP\
                        or event.type is constants.KEYDOWN:
                    if event.key == constants.K_ESCAPE:
                        return

                    if not self._process_event(event):
                        time.sleep(0.1)

    def _process_event(self, event):
        """Process pygame event"""
        action = self.actions.get(event.type, {}).get(event.key)

        if action:
            action(None)
            return True
        else:
            return False


if __name__ == '__main__':
    controller = Controller()
    controller.loop()
