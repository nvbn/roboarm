from mock import MagicMock
from roboarm import roboarm, const, parts
from unittest import TestCase


class PartsCase(TestCase):
    """Test arm parts"""

    def setUp(self):
        roboarm.Arm._init_device = MagicMock()
        self.arm = roboarm.Arm()
        self.arm.perform = MagicMock()

    def test_init_parts(self):
        """Test parts init"""
        self.assertIsInstance(self.arm.grips, parts.Grips)

    def test_parts_call(self):
        """Test parts call"""
        self.arm.shoulder.up(None)
        self.arm.perform.assert_called_once_with(
            const.MOVEMENT_PART, const.SHOULDER_UP,
        )


class ConfigCase(TestCase):
    """Tests for config"""

    def setUp(self):
        roboarm.Arm._init_device = MagicMock()

    def test_stay_default(self):
        """Test stay default value"""
        arm = roboarm.Arm()
        self.assertEqual(
            arm.config['vendor'],
            roboarm.Arm.default_config['vendor'],
        )

    def test_override_value(self):
        """Test override config value"""
        vendor = 'test'
        arm = roboarm.Arm(vendor=vendor)
        self.assertEqual(arm.config['vendor'], vendor)
