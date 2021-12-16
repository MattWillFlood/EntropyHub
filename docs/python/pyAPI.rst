=================
Python Functions: 
=================

.. toctree::
   :maxdepth: 3
   :titlesonly:
   :hidden:

    Base Entropies <./Functions/Base>
    Cross-Entropies <./Functions/Cross>
    Multiscale Entropies <./Functions/Multiscale>
    Multiscale Cross-Entropies <./Functions/MultiscaleCross>
    Bidimensional (2D) Entropies  <./Functions/Bidimensional>


EntropyHub functions fall into 5 categories:
############################################

    Base                
      functions for estimating the entropy of a single univariate time series.
    Cross   
      functions for estimating the entropy between two univariate time series.
    Bidimensional   
      functions for estimating the entropy of a two-dimensional univariate matrix.
    Multiscale     
      functions for estimating the multiscale entropy of a single univariate time series using any of the *Base* entropy functions.
    Multiscale Cross  
      functions for estimating the multiscale entropy between two univariate time series using any of the *Cross*-entropy functions.


.........................................................................................................................

**When new entropies are published in the scientific literature, efforts will be made to incorporate them in future releases.**

.........................................................................................................................

.. important:: 

    For concision, function commands written in the following sections using Python
    syntax exclude the module prefix which would otherwise be required,

    i.e. ``EntropyHub.SampEn()`` is written as ``SampEn()``.

.. note::

    Python functions in EntropyHub are based primarily on the `Numpy <https://numpy.org/doc/stable/user/whatisnumpy.html>`_ package.
    Arguments shown in python functions with the ``np.`` prefix refer to `numpy` functions.


Base Entropies:
***************

+------------------------------+----------------+
|Entropy Type                  | Function Name  |
+==============================+================+
|Approximate Entropy           | ApEn           |
+------------------------------+----------------+
|Sample Entropy                | SampEn         |
+------------------------------+----------------+
|Fuzzy Entropy                 | FuzzEn         |
+------------------------------+----------------+
|Kolmogorov Entropy            | K2En           |
+------------------------------+----------------+
|Permutation Entropy           | PermEn         |
+------------------------------+----------------+
|Conditional Entropy           | CondEn         |
+------------------------------+----------------+
|Distribution Entropy          | DistEn         |
+------------------------------+----------------+
|Spectral Entropy              | SpecEn         |
+------------------------------+----------------+
|Dispersion Entropy            | DispEn         |
+------------------------------+----------------+
|Symbolic Dynamic Entropy      | SyDyEn         |
+------------------------------+----------------+
|Increment Entropy             | IncrEn         |
+------------------------------+----------------+
|Cosine Similarity Entropy     | CoSiEn         |
+------------------------------+----------------+
|Phase Entropy                 | PhasEn         |
+------------------------------+----------------+
|Slope Entropy                 | SlopEn         |
+------------------------------+----------------+
|Bubble Entropy                | BubbEn         |
+------------------------------+----------------+
|Gridded Distribution Entropy  | GridEn         |
+------------------------------+----------------+
|Entropy of Entropy            | EnofEn         |
+------------------------------+----------------+
|Attention Entropy             | AttnEn         |
+------------------------------+----------------+


Cross Entropies:
****************

+------------------------------------+----------------+
|Entropy Type                        | Function Name  |
+====================================+================+
|Cross-Approximate Entropy           | XApEn          |
+------------------------------------+----------------+
|Cross-Sample Entropy                | XSampEn        |
+------------------------------------+----------------+
|Cross-Fuzzy Entropy                 | XFuzzEn        |
+------------------------------------+----------------+
|Cross-Kolmogorov Entropy            | XK2En          |
+------------------------------------+----------------+
|Cross-Permutation Entropy           | XPermEn        |
+------------------------------------+----------------+
|Cross-Conditional Entropy           | XCondEn        |
+------------------------------------+----------------+
|Cross-Distribution Entropy          | XDistEn        |
+------------------------------------+----------------+
|Cross-Spectral Entropy              | XSpecEn        |
+------------------------------------+----------------+


Bidimensional Entropies:
************************

+------------------------------------+----------------+
|Entropy Type                        | Function Name  |
+====================================+================+
|Bidimensional Sample Entropy        | SampEn2D       |
+------------------------------------+----------------+
|Bidimensional Fuzzy Entropy         | FuzzEn2D       |
+------------------------------------+----------------+
|Bidimensioanl Distribution Entropy  | DistEn2D       |
+------------------------------------+----------------+
|Bidimensioanl Dispersion Entropy    | DispEn2D       |
+------------------------------------+----------------+
|Bidimensioanl Permutation Entropy   | PermEn2D       |
+------------------------------------+----------------+
|Bidimensioanl Espinosa Entropy      | EspEn2D        |
+------------------------------------+----------------+


Multiscale  Entropies:
**********************

+------------------------------------------+----------------+
|Entropy Type                              | Function Name  |
+==========================================+================+
|Multiscale Entropy                        | MSEn           |
+------------------------------------------+----------------+
|Composite Multiscale Entropy              | cMSEn          |
|(+ Refined-Composite Multiscale Entropy)  |                |
+------------------------------------------+----------------+
|Refined Multiscale Entropy                | rMSEn          |
+------------------------------------------+----------------+
|Hierarchical Multiscale Entropy           | hMSEn          |
+------------------------------------------+----------------+


Multiscale Cross-Entropies:
***************************

+------------------------------------------------+----------------+
|Entropy Type                                    | Function Name  |
+================================================+================+
|Multiscale Cross-Entropy                        | XMSEn          |
+------------------------------------------------+----------------+
|Composite Multiscale Cross-Entropy              | cXMSEn         |
|(+ Refined-Composite Multiscale Cross-Entropy)  |                |
+------------------------------------------------+----------------+
|Refined Multiscale Cross-Entropy                | rXMSEn         |
+------------------------------------------------+----------------+
|Hierarchical Multiscale Cross-Entropy           | hXMSEn         |
+------------------------------------------------+----------------+

