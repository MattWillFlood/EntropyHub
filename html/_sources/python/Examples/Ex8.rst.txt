===========================================================
Example 8: Composite Multiscale Cross-[Approximate] Entropy
===========================================================

Import two signals of uniformly distributed pseudorandom integers in the range [1 8] and
create a multiscale entropy object with the following parameters:

EnType = ``XApEn()``, embedding dimension = 2, time delay = 2, radius distance threshold = 0.5.

.. code-block:: python3

    X = EH.ExampleData('randintegers2');

    Mobj = EH.MSobject('XApEn', m = 2, tau = 2, r = 0.5)

    Mobj.Func
    >>> <function EntropyHub._XApEn.XApEn(Sig, m=2, tau=1, r=None, Logx=2.71828)>
    
    Mobj.Kwargs
    >>> {'m': 2, 'tau': 2, 'r': 0.5}


Calculate the comsposite multiscale cross-approximate entropy over 3 temporal scales
where the radius distance threshold value (``r``) specified by ``Mobj`` becomes scaled by the
variance of the signal at each scale.

.. code-block:: python3

    MSx, _ = EH.cXMSEn(X, Mobj, Scales = 3, RadNew = 1)
    . . . . . . .

    >>> MSx =
        array([1.089, 1.4746, 1.2932])