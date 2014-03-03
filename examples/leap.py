from fn import _
from roboarm import Arm
from lib import Leap


Y_MID = 200
X_MIN = -200
X_MAX = 200
STEP = 0.2


class Listener(Leap.Listener):
    """Leap motion actions listner"""
    actions = (
        (_.base.rotate_clock, _.base.rotate_counter),
        (_.shoulder.up, _.shoulder.down),
        (_.elbow.up, _.elbow.down),
        (_.wrist.up, _.wrist.down),
        (_.grips.open, _.grips.close),
    )

    def __init__(self, arm):
        super(Listener, self).__init__()
        self._arm = arm

    def on_connect(self, controller):
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

    def on_frame(self, controller):
        frame = controller.frame()
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
            action = self.actions[action_n][avg_pos[1] < Y_MID]
            action(self._arm)(STEP)
            print action


if __name__ == '__main__':
    listener = Listener(Arm())
    controller = Leap.Controller()
    controller.add_listener(listener)
    raw_input()
