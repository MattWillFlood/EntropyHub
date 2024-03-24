====================
Multiscale Entropies
====================

.. toctree::
   :maxdepth: 3


Functions for estimating the multiscale entropy of a univariate time series.
****************************************************************************

Multiscale entropy can be calculated using any of the :ref:`pyBase`: 
``ApEn``, ``AttnEn``, ``BubbEn``, ``CondEn``, ``CoSiEn``, ``DistEn``, 
``DispEn``, ``DivEn``, ``EnofEn``, ``FuzzEn``, ``GridEn``, ``IncrEn``, ``K2En``,
``PermEn``, ``PhasEn``, ``RangEn``, ``SampEn``, ``SlopEn``, ``SpecEn``, ``SyDyEn``.

.. important::

    Multiscale cross-entropy functions have two positional arguments:

    1. the data sequence, ``Sig`` (a vector > 10 elements),
    2. the multiscale entropy object, ``Mobj``.

..........................................................................

.. automodule:: EntropyHub
    :members: MSobject

..........................................................................

**The following functions use the multiscale entropy object shown above.**

..........................................................................

.. automodule:: EntropyHub
   :members: MSEn, cMSEn, rMSEn, hMSEn
