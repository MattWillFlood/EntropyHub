==============================================
Example 7: Refined Multiscale [Sample] Entropy
==============================================

Import a signal of uniformly distributed pseudorandom integers in the range [1, 8] and
create a multiscale entropy object with the following parameters:

EnType = ``SampEn()``, embedding dimension = 4, radius threshold = 1.25

.. code-block:: matlab 

    X = ExampleData('randintegers');

    Mobj = MSobject('SampEn', 'm', 4, 'r', 1.25)

    >>> Mobj = struct with fields:
        Func: @SampEn
        m: 4
        r: 1.2500

Calculate the refined multiscale sample entropy and the complexity index (``Ci``) over 5
temporal scales using a 3rd order Butterworth filter with a normalised corner frequency
of at each temporal scale, where the radius threshold value (``r``) specified by ``Mobj``
becomes scaled by the median absolute deviation of the filtered signal at each scale.

.. code-block:: matlab

    [MSx, Ci] = rMSEn(X, Mobj, 'Scales', 5, 'F_Order', 3, 'F_Num', 0.6, 'RadNew', 4)
    . . . . . .

    >>> MSx = 1×5
        0.5280 0.5734 0.5939 0.5908 0.5563
        
        Ci = 2.8424
