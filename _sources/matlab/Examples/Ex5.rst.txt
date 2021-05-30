=================================================
Example 5: Multiscale Entropy Object [MSobject()]
=================================================

Create a multiscale entropy object (``Mobj``) for multiscale fuzzy entropy, 
calculated with an embedding dimension (``m``) of 5, a time delay (``tau``) of 2, 
using a sigmoidal fuzzy function with the ``r`` scaling parameters (3, 1.2).

.. code-block:: matlab

    Mobj = MSobject('FuzzEn', 'm', 5, 'tau', 2, 'Fx', 'sigmoid', 'r', [3, 1.2])

    >>> Mobj = struct with fields:
        Func: @FuzzEn
        m: 5
        tau: 2
        r: [3 1.2000]

Create a multiscale entropy object (``Mobj``) for multiscale corrected-cross-conditional 
entropy, calculated with an embedding dimension of 6 and using a 11-symbolic data transform.

.. code-block:: matlab

    Mobj = MSobject('XCondEn', 'm', 6, 'c', 11)

    >>> Mobj = struct with fields:
        Func: @XCondEn
        m: 6
        c: 11
