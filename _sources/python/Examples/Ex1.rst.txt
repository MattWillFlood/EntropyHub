=========================
Example 1: Sample Entropy
=========================

Import a signal of normally distributed random numbers [mean = 0; SD = 1], and calculate the
sample entropy for each embedding dimension (``m``) from 0 to 4.

.. code-block:: python3

    X = EH.ExampleData("gaussian");
    Samp, _ = EH.SampEn(X, m = 4)

    >>> Samp = 
        array([2.1789, 2.1757, 2.1819, 2.2209, 2.1756])
    
Select the last value to get the sample entropy for ``m`` = 4.

.. code-block:: python3

    Samp[-1]
    >>> 2.1756

Calculate the sample entropy for each embedding dimension (``m``) from 0 to 4 with 
a time delay (``tau``) of 2 samples.

.. code-block:: python3

    Samp, Phi1, Phi2 = SampEn(X, m = 4, tau = 2)

    >>> Samp =
        array([2.1789 2.1833 2.1880 2.1892 2.1441])
