=================================================
Example 5: Multiscale Entropy Object [MSobject()]
=================================================

Create a multiscale entropy object (``Mobj``) for multiscale fuzzy entropy, 
calculated with an embedding dimension (``m``) of 5, a time delay (``tau``) of 2, 
using a sigmoidal fuzzy function with the ``r`` scaling parameters (3, 1.2).

.. code-block:: python3

    Mobj = EH.MSobject('FuzzEn', m = 5, tau = 2, Fx = 'sigmoid', r = (3, 1.2));
    Mobj.Func

    >>> <function EntropyHub._FuzzEn.FuzzEn(Sig, m=2, tau=1, r=(0.2, 2), Fx='default', Logx=2.71828)>
    
    Mobj.Kwargs

    >>> {'m': 5, 'tau': 2, 'Fx': 'sigmoid', 'r': (3, 1.2)}

Create a multiscale entropy object (``Mobj``) for multiscale corrected-cross-conditional 
entropy, calculated with an embedding dimension of 6 and using a 11-symbolic data transform.

.. code-block:: python3

    Mobj = EH.MSobject('XCondEn', m = 6, c = 11)
    
    Mobj.Func
    >>> <function EntropyHub._XCondEn.XCondEn(Sig, m=2, tau=1, c=6, Logx=2.71828, Norm=False)>
    
    Mobj.Kwargs
    >>> {'m': 6, 'c': 11}