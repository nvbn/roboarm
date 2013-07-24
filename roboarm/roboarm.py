from . import parts, const
from .exceptions import DeviceNotFound
from copy import copy
import usb.core
import inspect


class Arm(object):
    """Arm object"""
    grips = parts.Grips
    wrist = parts.Wrist
    elbow = parts.Elbow
    shoulder = parts.Shoulder
    base = parts.Base
    led = parts.Led

    default_config = {
        'vendor': const.VENDOR,
        'bmRequestType': const.BM_REQUEST_TYPE,
        'bRequest': const.B_REQUEST,
        'wValue': const.W_VALUE,
        'wIndex': const.W_INDEX,
    }

    def __init__(self, **kwargs):
        self._state = [0, 0, 0]
        self._update_config(kwargs)
        self._init_device()
        self._init_parts()

    def _update_config(self, config):
        """Update configuration values"""
        self.config = copy(self.default_config)
        self.config.update(config)

    def _init_device(self):
        """Init device"""
        self.device = usb.core.find(idVendor=self.config['vendor'])
        if not self.device:
            raise DeviceNotFound()

        self.device.set_configuration()

    def _init_parts(self):
        """Init device parts"""
        for attr, value in type(self).__dict__.items():
            if inspect.isclass(value) and issubclass(value, parts.Part):
                setattr(self, attr, value(self))

    def _tell(self, msg):
        """Send message to devise"""
        self.device.ctrl_transfer(
            self.config['bmRequestType'],
            self.config['bRequest'],
            self.config['wValue'],
            self.config['wIndex'],
            msg,
        )

    def perform(self, part, state):
        """Perform action"""
        self._state[part] = state
        self.apply()

    def apply(self):
        """Apply current state"""
        self._tell(self._state)
