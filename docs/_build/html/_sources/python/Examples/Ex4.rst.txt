==================================================================
Example 4: Cross-Distribution Entropy w/ Different Binning Methods
==================================================================

Import a signal of pseudorandom integers in the range [1, 8] and calculate the cross-
distribution entropy with an embedding dimension (``m``) of 5, a time delay (``tau``) of 3,
and Sturges' bin selection method.

.. code-block:: python3

    X = EH.ExampleData('randintegers2');
    XDist, _ = EH.XDistEn(X[:,0], X[:,1], m = 5, tau = 3)

    >>> Note: 17/25 bins were empty
    >>> XDist =
        0.5248


Use Rice's method to determine the number of histogram bins and return the probability
of each bin (``Ppi``).

.. code-block:: python3

    XDist, Ppi = EH.XDistEn(X[:,0], X[:,1], m = 5, tau = 3, Bins = 'rice')

    >>> Note: 407/415 bins were empty
    >>> XDist =
        0.2802
    >>> Ppi =
        array([0.0000 0.0047 0.0368 0.1096 0.1978 0.2558 0.2421 0.1531])