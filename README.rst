Roboarm
=======

.. image:: https://travis-ci.org/nvbn/roboarm.png
   :alt: Build Status
   :target: https://travis-ci.org/nvbn/roboarm
.. image:: https://coveralls.io/repos/nvbn/roboarm/badge.png?branch=master
   :alt: Coverage Status
   :target: https://coveralls.io/r/nvbn/roboarm
.. image:: https://pypip.in/v/roboarm/badge.png
   :target: https://crate.io/packages/roboarm/
.. image:: https://pypip.in/d/roboarm/badge.png
   :target: https://crate.io/packages/roboarm/
.. image:: https://goo.gl/xnKADy
   :target: http://coviolations.io/projects/nvbn/roboarm/

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
