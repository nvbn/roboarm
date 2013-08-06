Roboarm
=======

Python library for controlling owi robotic arm edge.
Docs available on `read the docs <https://roboarm.readthedocs.org>`_.

Installation
------------

You can install stable version from pypi:

.. code-block:: bash

    pip install roboarm

Or developer version from git:

.. code-block:: bash

    git clone git@github.com:nvbn/roboarm.git
    cd roboarm
    python setup.py develop

Basic usage
-----------

For rotate arm clockwise, move elbow up and open grips:

.. code-block:: python

    from roboarm import Arm


    arm = Arm()
    arm.base.rotate_clock(timeout=3)
    arm.elbow.up(timeout=1)
    arm.grips.open(timeout=2)

Examples
--------

- `examples/controller.py` - simple gui tool for working with arm(require pygame)
