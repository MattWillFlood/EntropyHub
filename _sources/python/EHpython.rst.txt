******************
EntropyHub: Python
******************

.. toctree::
   :maxdepth: 3
   :hidden:
   :titlesonly:

   API <./pyAPI>
   Examples <./pyexamples>


.. centered:: Links to installation files:  `GitHub <https://github.com/MattWillFlood/EntropyHub/tree/main/EntropyHub%20-%20Python>`_ || `PyPi <https://pypi.org/project/EntropyHub/>`_

......................................................................................................

Requirements & Installation:
############################

There are several package dependencies which will be installed alongside EntropyHub (if not already installed):   
   - *Numpy*
   - *Scipy*
   - *Matplotlib*
   - *PyEMD* 
   - *Requests*

EntropyHub was designed using Python3 and thus is not intended for use with Python2. 
Python versions > 3.6 are required for using EntropyHub.

There are 2 ways to install EntropyHub for Python. **Method 1 is strongly recommended.**

Method 1:
*********
   1. Using ``pip`` in your python IDE, type:
        
        .. code-block:: python3
        
            pip install EntropyHub
    
	
Method 2:
*********
   1. Download the ``EntropyHub.x.x.x.tar.gz`` folder from the `EntropyHub PyPI repo <https://pypi.org/project/EntropyHub/>`_       
      (or the `EntropyHub GitHub repo <https://github.com/MattWillFlood/EntropyHub/tree/main/EntropyHub%20-%20Python>`_)  and unzip it.

      .. image:: ../_images/pyscreen1.png
         :width: 600px
         :align: center
         :height: 450px 

      __________________________________________________________________

      .. image:: ../_images/pyscreen2.png
         :width: 600px
         :align: center
         :height: 450px 

   2. Open a command terminal (*cmd* on Windows, *terminal* on Mac) 
      or use the Anaconda prompt if you use Anaconda as your python package distribution. 
   3. In the command prompt/terminal, navigate to the directory where you saved and extracted the ``.tar.gz`` folder.
   4. Enter the following in the command line:
        
        .. code-block:: python3
               
            python setup.py install

   - Ensure that an up-to-date version of setuptools is installed:
        
        .. code-block:: python3
        
            python -m pip install --upgrade setuptools


To use EntropyHub, import the module with the following command,

    .. code-block:: python3
        
        import EntropyHub

or in abbreviated form,

    .. code-block:: python3

        import EntropyHub as EH

To check that EntropyHub has imported correctly, type:

    .. code-block:: python3
        
        EntropyHub.greet()

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
One can simply access the docstrings of a function (like any Python function) by typing ``help FunctionName, e.g. help SampEn`` in the command line which will print the docstrings.

All information on the EntropyHub package is detailed in the *EntropyHub Guide*,
a .pdf document available to :download:`download here <../_static/EntropyHubGuide.pdf>`.
  
The Python API subsections outline the syntax for each base, cross-, multiscale, multiscale-cross, and bidimensional entropy Python function.
