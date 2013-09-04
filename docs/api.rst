************
API reference
************

Arm class
---------

.. class:: Arm(**config)

    Create arm controlling instance.
    *config* - usb device configuration, by default:

    .. code-block:: python

        vendor = 0x1267
        bmRequestType = 0x40
        bRequest = 6
        wValue = 0x100
        wIndex = 0

    Usage:

    .. code-block:: python

        from roboarm import Arm


        arm = Arm()

Grips
-----

.. function:: arm.grips.open(timeout=1)

    Start opening device grips and stop after timeout. If *timeout=None* don't stop.

.. function:: arm.grips.close(timeout=1)

    Start closing device grips and stop after timeout. If *timeout=None* don't stop.

.. function:: arm.grips.stop()

    Stop current action.

Example usage:

.. code-block:: python

    from roboarm import Arm
    import time


    arm = Arm()

    # open grips for 2 seconds:
    arm.grips.open(2)

    # close grips, wait 2 seconds and stop:
    arm.grips.close(None)
    time.sleep(2)
    arm.grips.stop()

Wrist
-----

.. function:: arm.wrist.up(timeout=1)

    Start moving up device wrist and stop after timeout. If *timeout=None* don't stop.

.. function:: arm.wrist.down(timeout=1)

    Start moving down device wrist and stop after timeout. If *timeout=None* don't stop.

.. function:: arm.wrist.stop()

    Stop current action.
    
Example usage:

.. code-block:: python

    from roboarm import Arm
    import time


    arm = Arm()

    # up wrist for 2 seconds:
    arm.wrist.up(2)

    # down wrist, wait 2 seconds and stop:
    arm.wrist.down(None)
    time.sleep(2)
    arm.wrist.stop()

Elbow
-----

.. function:: arm.elbow.up(timeout=1)

    Start moving up device elbow and stop after timeout. If *timeout=None* don't stop.

.. function:: arm.elbow.down(timeout=1)

    Start moving down device elbow and stop after timeout. If *timeout=None* don't stop.

.. function:: arm.elbow.stop()

    Stop current action.
    
Example usage:

.. code-block:: python

    from roboarm import Arm
    import time


    arm = Arm()

    # up elbow for 2 seconds:
    arm.elbow.up(2)

    # down elbow, wait 2 seconds and stop:
    arm.elbow.down(None)
    time.sleep(2)
    arm.elbow.stop()

Shoulder
--------

.. function:: arm.shoulder.up(timeout=1)

    Start moving up device shoulder and stop after timeout. If *timeout=None* don't stop.

.. function:: arm.shoulder.down(timeout=1)

    Start moving down device shoulder and stop after timeout. If *timeout=None* don't stop.

.. function:: arm.shoulder.stop()

    Stop current action.
    
Example usage:

.. code-block:: python

    from roboarm import Arm
    import time


    arm = Arm()

    # up shoulder for 2 seconds:
    arm.shoulder.up(2)

    # down shoulder, wait 2 seconds and stop:
    arm.shoulder.down(None)
    time.sleep(2)
    arm.shoulder.stop()

Base
----

.. function:: arm.base.rotate_clock(timeout=1)

    Start rotating device clockwise and stop after timeout. If *timeout=None* don't stop.
    
.. function:: arm.base.rotate_counter(timeout=1)

    Start rotating device counterclockwise and stop after timeout. If *timeout=None* don't stop.

.. function:: arm.base.stop()

    Stop current action.

Example usage:

.. code-block:: python

    from roboarm import Arm
    import time


    arm = Arm()

    # rotate clockwise for 2 seconds:
    arm.base.rotate_clock(2)

    # rotate counterclockwise, wait 2 seconds and stop:
    arm.base.rotate_counter(None)
    time.sleep(2)
    arm.base.stop()

Led
----

.. function:: arm.led.on(timeout=None)

    Turn led on and stop after timeout. If *timeout=None* don't stop.

.. function:: arm.led.off(timeout=None)

    Turn led off and stop after timeout. If *timeout=None* don't stop.

.. function:: arm.led.stop()

    Stop current action.

Example usage:

.. code-block:: python

    from roboarm import Arm
    import time


    arm = Arm()

    # turn led on:
    arm.led.on()

    # turn led off:
    arm.led.off()

    #turn led on for 2 seconds:
    arm.led.on(2)
