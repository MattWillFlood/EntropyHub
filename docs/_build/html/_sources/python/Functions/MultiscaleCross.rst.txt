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

    Multiscale cross-entropy functions have three positional arguments:

    1. the first data sequence, ``Sig1`` (a vector > 10 elements),
    2. the second data sequence, ``Sig2`` (a vector > 10 elements),
    3. the multiscale entropy object, ``Mobj``.

..........................................................................


.. automodule:: EntropyHub
    :members: MSobject

..........................................................................

**The following functions use the multiscale entropy object shown above.**

..........................................................................

.. automodule:: EntropyHub
   :members: XMSEn, cXMSEn, rXMSEn, hXMSEn


