import pygame
from fn import _
from roboarm import Arm
from lib import Leap


Y_MID = 200
X_MIN = -200
X_MAX = 200
STEP = 0.2

W = 640
H = 480

ACTIVE_COLOR = (255, 0, 0)
INACTIVE_COLOR = (255, 255, 255)
BKG = (0, 0, 0)

BORDER = 2


class Deck(object):
    """Deck with separated rectangles"""

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._rect_x = (W - x * BORDER) / x
        self._rect_y = (H - y * BORDER) / y
        self._init_pygame()

    def _init_pygame(self):
        """Init pygame"""
        pygame.init()
        self.window = pygame.display.set_mode((W, H))
        self.window.fill(BKG)
        self._draw_rects()

    def _draw_rects(self, now_x=None, now_y=None):
        for x in range(self._x):
            for y in range(self._y):
                color = ACTIVE_COLOR if now_x == x and now_y == y\
                    else INACTIVE_COLOR
                self.window.fill(
                    color,
                    pygame.Rect(
                        x * self._rect_x + x * BORDER,
                        y * self._rect_y + y * BORDER,
                        self._rect_x,
                        self._rect_y,
                    ),
                )
        pygame.display.update()

    def highlight(self, x, y):
        """Highlight rectangel"""
        self._draw_rects(x, y)


class Listener(Leap.Listener):
    """Leap motion actions listner"""
    actions = (
        (_.base.rotate_clock, _.base.rotate_counter),
        (_.shoulder.up, _.shoulder.down),
        (_.elbow.up, _.elbow.down),
        (_.wrist.up, _.wrist.down),
        (_.grips.open, _.grips.close),
    )
    gestures = (
        (Leap.Gesture.TYPE_SCREEN_TAP, _.led.on, _.led.off),
    )

    def __init__(self, arm):
        super(Listener, self).__init__()
        self._arm = arm
        self._gesture_states = {
            gesture[0]: False for gesture in self.gestures
        }
        self._deck = Deck(len(self.actions), len(self.actions[0]))

    def on_connect(self, controller):
        """Init gestures"""
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)

    def on_frame(self, controller):
        """On new frame"""
        frame = controller.frame()
        self._do_gestures(frame)
        self._do_actions(frame)

    def _do_actions(self, frame):
        """Perform actions with frame"""
        for n, hand in enumerate(frame.hands):
            avg_pos = Leap.Vector()
            for finger in hand.fingers:
                avg_pos += finger.tip_position
            avg_pos /= len(hand.fingers)
            x_range = X_MAX - X_MIN
            try:
                action_n = int(avg_pos[0] - X_MIN) / (x_range / len(self.actions))
            except ValueError:
                continue
            action_y = avg_pos[1] < Y_MID
            action = self.actions[action_n][action_y]
            self._deck.highlight(action_n, action_y)
            action(self._arm)(STEP)
            print action

    def _do_gestures(self, frame):
        """Do actions for frame gestures"""
        for gesture in frame.gestures():
            for gesture_type, on, off in self.gestures:
                if gesture.type == gesture_type:
                    if self._gesture_states[gesture_type]:
                        on(self._arm)()
                    else:
                        off(self._arm)()
                    self._gesture_states[gesture_type] =\
                        not self._gesture_states[gesture_type]


if __name__ == '__main__':
    listener = Listener(Arm())
    controller = Leap.Controller()
    controller.add_listener(listener)
    raw_input()
