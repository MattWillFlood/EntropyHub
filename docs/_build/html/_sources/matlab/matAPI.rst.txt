=================
MatLab Functions: 
=================

.. toctree::
   :maxdepth: 4
   :titlesonly:
   :hidden:

    Base Entropies <./Functions/matBase>
    Cross-Entropies <./Functions/matCross>
    Multivariate Entropies <./Functions/matMultivariate>
    Bidimensional (2D) Entropies  <./Functions/matBidimensional>
    Multiscale Entropies <./Functions/matMultiscale>
    Multiscale Cross-Entropies <./Functions/matMultiscaleCross>
    Multivariate Multiscale Entropies <./Functions/matMultivariateMultiscale>
    Other Functions <./Functions/matOther>


EntropyHub functions fall into 8 categories:
############################################

    Base                
      functions for estimating the entropy of a single univariate time series.
    Cross   
      functions for estimating the entropy between two univariate time series.
    Multivariate
      functions for estimating the entropy of a multivariate dataset.
    Bidimensional   
      functions for estimating the entropy of a two-dimensional univariate matrix.
    Multiscale     
      functions for estimating the multiscale entropy of a single univariate time series using any of the *Base* entropy functions.
    Multiscale Cross  
      functions for estimating the multiscale entropy between two univariate time series using any of the *Cross*-entropy functions.
    Multiscale Multivariate  
      functions for estimating the multivariate multiscale entropy of multivariate dataset using any of the *Multivariate*-entropy functions.
    Other
      Supplementary functions for various tasks related to EntropyHub and signal processing.


.........................................................................................................................

**When new entropies are published in the scientific literature, efforts will be made to incorporate them in future releases.**

.........................................................................................................................

Base Entropies:
***************
.. toggle::

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
  |Diversity Entropy             | DivEn          |
  +------------------------------+----------------+
  |Range Entropy                 | RangEn         |
  +------------------------------+----------------+

Cross Entropies:
****************
.. toggle::

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

Multivariate Entropies:
***********************
.. toggle::

  +----------------------------------------+----------------+
  | Entropy Type                           | Function Name  |
  +========================================+================+
  | Multivariate Sample Entropy            | MvSampEn       |
  +----------------------------------------+----------------+
  | Multivariate Fuzzy Entropy             | MvFuzzEn       |
  +----------------------------------------+----------------+
  | Multivariate Permutation Entropy       | MvPermEn       |
  +----------------------------------------+----------------+
  | Multivariate Dispersion Entropy        | MvDispEn       |
  +----------------------------------------+----------------+
  | Multivariate Cosine Similarity Entropy | MvCoSiEn       |
  +----------------------------------------+----------------+



Bidimensional Entropies:
************************
.. toggle::

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
.. toggle::

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
.. toggle::

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


Multivariate Multiscale  Entropies:
***********************************
.. toggle::

  +------------------------------------------+----------------+
  | Entropy Type                             | Function Name  |
  +==========================================+================+
  | Multivariate Multiscale Entropy          | MvMSEn         |
  +------------------------------------------+----------------+
  | Composite (+ Refined-Composite)          | cMvMSEn        |
  | Multivariate Multiscale Entropy          |                |
  +------------------------------------------+----------------+


Other Functions:
****************
.. toggle::

  +------------------------------------------+----------------+
  | Function  Description                    | Function Name  |
  +==========================================+================+
  | Example dataset import tool              | ExampleData    |
  +------------------------------------------+----------------+
  | Windowing tool                           |  WindowData    |
  | (for data segmentation)                  |                |
  +------------------------------------------+----------------+