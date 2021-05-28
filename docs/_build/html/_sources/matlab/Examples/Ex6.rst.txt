=========================================
Example 6: Multiscale [Increment] Entropy
=========================================

Import a signal of uniformly distributed pseudorandom integers in the range [1,8] and
create a multiscale entropy object with the following parameters:

EnType = ``IncrEn()``, embedding dimension = 3, a quantifying resolution = 6, normalization = true.

.. code-block:: matlab

    X = ExampleData('randintegers');

    Mobj = MSobject('IncrEn', 'm', 3, 'R', 6, 'Norm', true)

    >>> Mobj = struct with fields:
        Func: @IncrEn
        m: 3
        R: 6
        Norm: 1

Calculate the multiscale increment entropy over 5 temporal scales using the modified
graining procedure where,

.. math::

     y_j^{(\tau)} =\frac{1}{\tau } \sum_{i=\left(j-1\right)\tau +1}^{j\tau }x{_i} ,  1 <= j <= \frac{N}{\tau}


.. code-block:: matlab

    MSx = MSEn(X, Mobj, 'Scales', 5, 'Methodx', 'modified')
    . . . . . .

    >>> MSx = 1×5
        4.2719 4.3059 4.2863 4.2494 4.2773