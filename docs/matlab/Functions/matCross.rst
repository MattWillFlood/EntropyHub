.. currentmodule:: EntropyHub
.. _matCross:

===============
Cross Entropies
===============

.. toctree::
   :maxdepth: 3
   

Functions for estimating the entropy between two univariate time series.
************************************************************************

*The following functions also form the cross-entropy method used by* **multiscale cross-entropy** *functions.*

.....................................................................................................

.. attention:: 

    For cross-entropy and multiscale cross-entropy functions, the two time series signals are passed as a two-column or two-row matrix. 
    At present, it is not possible  to pass signals of different lengths separately

.....................................................................................................

.. mat:automodule:: EntropyHub
   :members: XApEn, XCondEn, XDistEn, XFuzzEn, XK2En, XPermEn, XSampEn, XSpecEn