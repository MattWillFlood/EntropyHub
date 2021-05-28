====================
Multiscale Entropies
====================

.. toctree::
   :maxdepth: 3


Functions for estimating the multiscale entropy between of a univariate time series.
************************************************************************************

Multiscale entropy can be calculated using any of the Base_ entropies: 
``ApEn``, ``AttnEn``, ``BubbEn``, ``CondEn``, ``CoSiEn``, ``DistEn``, 
``DispEn``, ``EnofEn``, ``FuzzEn``, ``GridEn``, ``IncrEn``, ``K2En``,
``PermEn``, ``PhasEn``, ``SampEn``, ``SlopEn``, ``SpecEn``, ``SyDyEn``.

.. important::

    Multiscale cross-entropy functions have two positional arguments:

    1. the time series signal, ``Sig`` (a vector > 10 elements),
    2. the multiscale entropy object, ``Mobj``.

..........................................................................

.. automodule:: EntropyHub
    :members: MSobject

..........................................................................

**The following functions use the multiscale entropy object shown above.**

..........................................................................

.. automodule:: EntropyHub
   :members: MSEn, cMSEn, rMSEn, hMSEn
