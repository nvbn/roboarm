from functools import partial
from . import const
import time


class PartAction(int):
    """Shortcut for part action"""


class Part(object):
    """Device part"""
    PART = None

    def __init__(self, parent):
        self._parent = parent
        self._init_actions()

    def _init_actions(self):
        """Make device actions callable"""
        for attr, value in type(self).__dict__.items():
            if issubclass(type(value), PartAction):
                setattr(
                    self, attr, partial(self._perform, int(value)),
                )

    def _perform(self, action, timeout=1):
        """Perform device action"""
        self._parent.perform(self.PART, action)

        if timeout is not None:
            time.sleep(timeout)
            self._parent.perform(self.PART, const.STOP)

    def stop(self, timeout=None):
        """Stop current action"""
        self._perform(const.STOP, timeout)


class MovementPart(Part):
    """Base movement part"""
    PART = const.MOVEMENT_PART


class Grips(MovementPart):
    """Arm grips"""
    open = PartAction(const.GRIPS_OPEN)
    close = PartAction(const.GRIPS_CLOSE)


class Wrist(MovementPart):
    """Arm wrist"""
    up = PartAction(const.WRIST_UP)
    down = PartAction(const.WRIST_DOWN)


class Elbow(MovementPart):
    """Arm elbow"""
    up = PartAction(const.ELBOW_UP)
    down = PartAction(const.ELBOW_DOWN)


class Shoulder(MovementPart):
    """Arm shoulder"""
    up = PartAction(const.SHOULDER_UP)
    down = PartAction(const.SHOULDER_DOWN)


class Base(Part):
    """Arm base"""
    PART = const.ROTATE_PART

    rotate_clock = PartAction(const.BASE_CLOCK)
    rotate_counter = PartAction(const.BASE_COUNTER)


class Led(Part):
    """Arm led"""
    PART = const.LED_PART

    def on(self, timeout=None):
        """Turn led on"""
        self._perform(const.LED_ON, timeout)

    def off(self, timeout=None):
        """Turn led off"""
        self._perform(const.LED_OFF, timeout)
