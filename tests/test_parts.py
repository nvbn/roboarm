from mock import MagicMock
from roboarm import parts, const
from unittest import TestCase


class ActionsCase(TestCase):
    """Test part actions"""

    def setUp(self):
        self.device = MagicMock()

    def test_actions_initialisation(self):
        """Test actions initialisation"""
        grips = parts.Grips(self.device)
        self.assertTrue(hasattr(grips.open, '__call__'))

    def test_actions_call(self):
        """Test actions call"""
        wrist = parts.Wrist(self.device)
        wrist.up(None)
        self.device.perform.assert_called_once_with(
            const.MOVEMENT_PART, const.WRIST_UP,
        )

    def test_actions_call_with_timeout(self):
        """Test actions call with timeout"""
        elbow = parts.Elbow(self.device)
        elbow.down(0)
        self.device.perform.assert_called_with(
            const.MOVEMENT_PART, const.STOP,
        )

    def test_stop(self):
        """Test stop"""
        shoulder = parts.Shoulder(self.device)
        shoulder.stop()
        self.device.perform.assert_called_once_with(
            const.MOVEMENT_PART, const.STOP,
        )


class LedCase(TestCase):
    """Test led"""

    def setUp(self):
        self.device = MagicMock()
        self.led = parts.Led(self.device)

    def test_on(self):
        """Test led on"""
        self.led.on()
        self.device.perform.assert_called_once_with(
            const.LED_PART, const.LED_ON,
        )

    def test_off(self):
        """Test led off"""
        self.led.off()
        self.device.perform.assert_called_once_with(
            const.LED_PART, const.LED_OFF,
        )
