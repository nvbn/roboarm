class DeviceNotFound(Exception):
    """Device not found exception"""

    def __init__(self):
        super(DeviceNotFound, self).__init__("Device not found")
