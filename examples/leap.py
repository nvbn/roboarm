from fn import _
from roboarm import Arm
from lib import Leap


STEP = 0.3
LEFT = 0
RIGHT = 1
X = 0
Y = 1
Z = 2


class Listener(Leap.Listener):
    # (fingers, hands, dimension, action)
    actions = (
        ((1, 2), Y, _.shoulder.up, _.shoulder.down),
        ((1, 2), X, _.base.rotate_counter, _.base.rotate_clock),
        ((3, 4), Y, _.elbow.up, _.elbow.down),
        ((3, 4), X, _.wrist.up, _.wrist.down),
    )

    def __init__(self, arm):
        super(Listener, self).__init__()
        self._arm = arm
        self._skip = 0
        self._last_avg = [(0, 0, 0), (0, 0, 0)]
        self._last_events = [None, None]

    def on_connect(self, controller):
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

    def on_frame(self, controller):
        frame = controller.frame()
        for n, hand in enumerate(frame.hands):
            avg_pos = Leap.Vector()
            for finger in hand.fingers:
                avg_pos += finger.tip_position
            avg_pos /= len(hand.fingers)
            fingers = len(hand.fingers)
            for action in self.actions:
                if fingers in action[0]:
                    if avg_pos[action[1]] > self._last_avg[n][action[1]]:
                        action[2](self._arm)(STEP)
                    else:
                        action[3](self._arm)(STEP)
            print avg_pos, fingers
            self._last_avg[n] = avg_pos


    @property
    def allow(self):
        self._skip += 1
        if self._skip > 100:
            self._skip = 0
            return True
        else:
            return False



if __name__ == '__main__':
    listener = Listener(Arm())
    controller = Leap.Controller()
    controller.add_listener(listener)
    raw_input()
