******************
EntropyHub: Julia
******************

.. centered:: Links to installation files: `GitHub <https://github.com/MattWillFlood/EntropyHub/tree/main/EntropyHub%20-%20Julia>`_ || `Julia Registries <>`_

`EntropyHub.jl <https://mattwillflood.github.io/EntropyHub.jl/dev>`_ is the EntropyHub package for *Julia*.
The complete documentation for `EntropyHub.jl can be found here <https://mattwillflood.github.io/EntropyHub.jl/dev>`_

.. image:: ../_images/EntropyHubJuliaLogo.png
    :width: 250px
    :align: center
    :height: 350px
    :target: https://mattwillflood.github.io/EntropyHub.jl/dev

 
.. toctree::
   :maxdepth: 3
   :hidden:
   :titlesonly:

   EntropyHub.jl  <https://mattwillflood.github.io/EntropyHub.jl/dev>
   Examples <https://mattwillflood.github.io/EntropyHub.jl/dev/Examples/Examples>


Requirements & Installation:
############################

There are several package dependencies which will be installed alongside EntropyHub (if not already installed):
    - *DSP*, *FFTW*
    - *HTTP*, *DelimitedFiles*
    - *Random*
    - *Plots*
    - *StatsBase*, *StatsFuns*, *Statistics*
    - *GroupSlices*, *Combinatorics*, *Clustering*
    - *LinearAlgebra*, *Dierckx* 

EntropyHub was designed using Julia 1.5 and is intended for use with Julia versions >= 1.2.

......................................................................................................

There are two ways to install EntropyHub for Julia.

Method 1:
*********

   1. In Julia, open the package REPL by typing ``]``. The command line should appear as: 
   
      .. code-block:: julia
        
        julia > ]

        @vX.Y. pkg > 
      
      Where X and Y refer to your version of Julia.
  
   2. Type:

      .. code-block:: julia
   
        @vX.Y. pkg > add EntropyHub
	
      (Note: this is **case sensitive**)
      
   Alternatively, one can use the ``Pkg`` module to perform the same procedure:
   
      .. code-block:: julia 

        julia > using Pkg        
        julia > Pkg.add("EntropyHub")
    
Method 2:
*********

   1. In Julia, open the package REPL by typing ``]``. The command line should appear as: 
   
      .. code-block:: julia
        
        julia > ]

        @vX.Y. pkg > 
      
      Where X and Y refer to your version of Julia.
  
   2. Type:
   
       @vX.Y. pkg >  add https://github.com/MattWillFlood/EntropyHub.jl
	     
 

To use EntropyHub after installing, type:

.. code-block:: julia
   
   julia > using EntropyHub

To check that EntropyHub has been correctly installed and loaded, type:

.. code-block:: julia
   
   julia > EntropyHub.greet()

       ___  _   _  _____  _____  ____  ____  _     _          
      |  _|| \ | ||_   _||     \|    ||    || \   / |   ___________ 
      | \_ |  \| |  | |  |   __/|    ||  __| \ \_/ /   /  _______  \
      |  _|| \ \ |  | |  |   \  |    || |     \   /   |  /  ___  \  |
      | \_ | |\  |  | |  | |\ \ |    || |      | |    | |  /   \  | | 
      |___||_| \_|  |_|  |_| \_||____||_|      |_|   _|_|__\___/  | | 
      _   _  _   _  ____                           / |__\______\/  | 
      | | | || | | ||    \     An open-source      |  /\______\__|_/ 
      | |_| || | | ||    |     toolkit for         | |  /   \  | | 
      |  _  || | | ||    \     entropic time-      | |  \___/  | |          
      | | | || |_| ||     \    series analysis     |  \_______/  |
      |_| |_|\_____/|_____/                         \___________/

......................................................................................................

Documentation & Help:
#####################

A key advantage of EntropyHub is the comprehensive documentation available to help users to make the most of the toolkit.
 
To learn more about a specific function, one can do so easily from the command line by typing: **?**, 
which will open the julia help system, and then typing the function name.

For example:

.. code-block:: julia 

	julia> ?  
	help?> SampEn	  # Documentation on sample entropy function

	julia> ?  
	help?> XSpecEn    # Documentation on cross-spectral entropy function

	julia> ?
	help?> hXMSEn     # Documentation on hierarchical multiscale cross-entropy function

All information on the EntropyHub package is detailed in the *EntropyHub Guide*,
a .pdf document available to :download:`download here <../_static/EntropyHubGuide.pdf>`.

The EntropyHub Julia API can be found at https://MattWillFlood.github.io/EntropyHub.jl/stable.
