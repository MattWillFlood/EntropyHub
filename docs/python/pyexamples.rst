================
Python Examples:
================


.. toctree::
   :maxdepth: 3
   :titlesonly:

    Ex. 1 - Sample Entropy <./Examples/Ex1>
    Ex. 2 - [Fine-Grained] Permutation Entropy <./Examples/Ex2>
    Ex. 3 - Phase Entropy <./Examples/Ex3>
    Ex. 4 - Cross-Distribution Entropy <./Examples/Ex4>
    Ex. 5 - Multiscale Entropy Object <./Examples/Ex5>
    Ex. 6 - Multiscale [Increment] Entropy <./Examples/Ex6>
    Ex. 7 - Refined Multiscale [Sample] Entropy <./Examples/Ex7>
    Ex. 8 - Composite Multiscale Cross-[Approximate] Entropy <./Examples/Ex8>
    Ex. 9 - Hierarchical Multiscale corrected Cross-[Conditional] Entropy <./Examples/Ex9>
    Ex. 10 - Bidimensional Fuzzy Entropy <./Examples/Ex10>
    Ex. 11 - Multivariate Dispersion Entropy <./Examples/Ex11>
    Ex. 12 - [Generalized] Refined-composite Multivariate Multiscale Fuzzy Entropy <./Examples/Ex12>
    Ex. 13 - Windowing data with WindowData() <./Examples/Ex13>
    
.....................................................................................................

.. important:: 

    For concision, function commands written in the following example sections assume that the
    EntropyHub module has already been imported as EH.

    .. code-block:: python3
        
        import EntropyHub as EH
        EH.SampEn(...)

.....................................................................................................

**The following sections provide some basic examples of EntropyHub functions. 
These examples are merely a snippet of the full range of EntropyHub functionality.**

.. admonition:: ``ExampleData()``

    In the following examples, signals / data are imported into Python using the ``EntropyHub.ExampleData()`` function.
    To use this function as outlined in the examples below, **an internet connection is required**.

.....................................................................................................

``EntropyHub.ExampleData()`` accepts any of the following strings:

:``'uniform'``: vector of uniformly distributed random numbers in range [0 1]
:``'gaussian'``: vector of normally distributed random numbers with mean = 0; SD = 1
:``'randintegers'``: vector of uniformly distributed pseudorandom integers in range [1 8]
:``'chirp'``: vector of chirp signal with the following parameters,  f0 = .01; t1 = 4000; f1 = .025
:``'lorenz'``: 3-column matrix: X, Y, Z components of the Lorenz system,  (alpha = 10; beta = 8/3; rho = 28); [Xo = 10; Yo = 20; Zo = 10]
:``'henon'``: 2-column matrix: X, Y components of the Henon attractor (alpha = 1.4; beta = 0.3); [Xo = 0; Yo = 0]
:``'uniform2'``: 2-column matrix: uniformly distributed random numbers in range [0 1]
:``'gaussian2'``: 2-column matrix: normally distributed random numbers with mean = 0; SD = 1
:``'randintegers2'``: 2-column matrix: uniformly distributed pseudorandom integers in range [1 8]
:``'uniform_Mat'``: Matrix of uniformly distributed random numbers in range [0 1]
:``'gaussian_Mat'``: Matrix of normally distributed random numbers with mean = 0; SD = 1
:``'randintegers_Mat'``: Matrix of uniformly distributed pseudorandom integers in range [1 8]
:``'mandelbrot_Mat'``: Matrix of image of fractal generated from the mandelbrot set
:``'entropyhub_Mat'``: Matrix of image of the entropyhub logo


.. admonition::  THINGS TO REMEMBER

    Parameters of the *base*, *cross-* or *mulitvariate* entropy methods are passed to *multiscale*,
    *multiscale cross-*, *multivariate multiscale* entropy functions using the multiscale entropy object given by ``MSobject()``.
    *Base*, *cross-*, *multivariate* entropy methods are declared with ``MSobject()`` using a string of the function name.

    Each bidimensional entropy function (*SampEn2D*, *FuzzEn2D*, *DistEn2D*, *DispEn2D*, *EspEn2D*) has
    an important keyword argument - ``Lock``. *Bidimensional* entropy functions are
    "locked" by default (``Lock == True``) to only permit matrices with a maximum size of 128 x 128.

    In *hierarchical multiscale entropy* (``hMSEn()``) and *hierarchical multiscale cross-
    entropy* (``hXMSEn()``) functions, the length of the time series signal(s) is halved at each scale. 
    Thus, ``hMSEn()`` and ``hXMSEn()`` only use the first 2^N data points where 2^N <= the length of the original time series signal.
    i.e. For a signal of 5000 points, only the first 4096 are used. For a signal of 1500 points, only the first 1024 are used.


