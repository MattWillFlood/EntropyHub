=============================================
Example 2: (Fine-Grained) Permutation Entropy
=============================================

Import the x, y, and z components of the Lorenz system of equations.

.. code-block:: python3

    Data = EH.ExampleData('lorenz');
        
    from matplotlib.pyplot import fig, scatter, axis

    fig = figure(facecolor='k')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('k')
    ax.scatter(Data[:,0], Data[:,1], Data[:,2], c='g')
    ax.axis('off')

.. image:: https://github.com/MattWillFlood/EntropyHub/blob/main/Graphics/lorenz.png?raw=true

Calculate fine-grained permutation entropy of the z component in dits (logarithm base
10) with an embedding dimension of 3, time delay of 2, an alpha parameter of 1.234.
Return ``Pnorm`` normalised w.r.t the number of all possible permutations (``m!``) and the
condition permutation entropy (``cPE``) estimate.

.. code-block:: python3

    Z = Data[:,2];
    
    Perm, Pnorm, cPE = EH.PermEn(Z, m = 3, tau = 2, Typex = 'finegrain', 
                                    tpx = 1.234, Logx = 10, Norm = False)

    >>> Perm
        array([-0. , 0.8687, 0.9468])
    >>> Pnorm
        array([ nan, 0.8687, 0.4734])
    >>> cPE
        array([0.8687, 0.0781])





