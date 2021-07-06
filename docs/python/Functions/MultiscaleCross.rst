==========================
Multiscale Cross-Entropies
==========================

.. toctree::
   :maxdepth: 3


Functions for estimating the multiscale cross-entropy between two univariate time series.
*****************************************************************************************

Just as one can calculate multiscale entropy using any Base entropy, the same functionality is possible with multiscale cross-entropy using any of the :ref:`pyCross`:
``XApEn``, ``XSampEn``, ``XK2En``, ``XCondEn``, ``XPermEn``, ``XSpecEn``, ``XDistEn``, ``XFuzzEn``

To do so, we again use the ``MSobject`` function to pass a multiscale object (``Mobj``) to the multiscale cross-entropy functions.

.. important::

    Multiscale cross-entropy functions have two positional arguments:

    1. the time series signals, ``Sig`` (an Nx2 matrix),
    2. the multiscale entropy object, ``Mobj``.

.. important::

    For cross-entropy and multiscale cross-entropy functions, the two time series signals are passed as a two-column or two-row matrix. 
    At present, it is not possible to pass signals of different lengths separately. 

..........................................................................


.. automodule:: EntropyHub
    :members: MSobject

..........................................................................

**The following functions use the multiscale entropy object shown above.**

..........................................................................

.. automodule:: EntropyHub
   :members: XMSEn, cXMSEn, rXMSEn, hXMSEn


