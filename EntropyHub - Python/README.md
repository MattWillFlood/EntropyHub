# EntropyHub: An open-source toolkit for entropic data analysis

__*Python Edition*__

<p align="center">
<img src="https://github.com/MattWillFlood/EntropyHub/blob/main/Graphics/EntropyHub_profiler.png" alt = "EntropyHub Git" width="250" height="250" />
</p>

## Installation

There are two ways to install EntropyHub for Python. Method 1 is strongly recommended.

#### Method 1:
   1. Using `pip` in your python IDE, type:
        `pip install EntropyHub`
	
#### Method 2:
   1. Download the folder above (EntropyHub.*x.x.x*.tar.gz) and unzip it.
   2. Open a command terminal (__*cmd*__ on Windows, __*terminal*__ on Mac) or __use the Anaconda prompt
      if you use Anaconda as your python package distribution__. 
   3. In the command prompt/terminal, navigate to the directory where you saved and extracted the .tar.gz folder.
   4. Enter the following in the command line:
         `python setup.py install`
       
### System Requirements & Dependencies
  There are several package dependencies which will be installed alongside EntropyHub:             
  Numpy, Scipy, Matplotlib, PyEMD
  
  EntropyHub was designed using Python 3 and thus is not intended for use with Python 2.
  Python versions > 3.6 are required for using EntropyHub. 
  


## Documentation & Help 

A key advantage of EntropyHub is the comprehensive documentation available to help users to make the most of the toolkit.
One can simply access the docstrings of a function (like any Python function) by typing `help FunctionName` in the command line, 
which will print the docstrings.

All information on the EntropyHub package is detailed in the *EntropyHub Guide*, a .pdf document available [here](https://github.com/MattWillFlood/EntropyHub/blob/main/EntropyHub%20Guide.pdf).
  
	
## Functions

EntropyHub functions fall into 5 categories: 

    * Base                functions for estimating the entropy of a single univariate time series.
    * Cross               functions for estimating the entropy between two univariate time series.
    * Bidimensional       functions for estimating the entropy of a two-dimensional univariate matrix.
    * Multiscale          functions for estimating the multiscale entropy of a single univariate time series using any of the Base entropy functions.
    * Multiscale Cross    functions for estimating the multiscale entropy between two univariate time series using any of the Cross-entropy functions.

#### The following tables outline the functions available in the EntropyHub package.

*When new entropies are published in the scientific literature, efforts will
be made to incorporate them in future releases.*

### Base Entropies:

Entropy Type   |  Function Name 
---|---
Approximate Entropy                               	  |	ApEn
Sample Entropy                                		  |	SampEn
Fuzzy Entropy                                 		  |	FuzzEn
Kolmogorov Entropy                            		  |	K2En
Permutation Entropy                           		  |	PermEn
Conditional Entropy                           		  |	CondEn
Distribution Entropy                          		  |	DistEn
Range Entropy                                             |     RangEn
Diversity Entropy                                         |     DivEn
Spectral Entropy                              		  |	SpecEn
Dispersion Entropy                            		  |	DispEn
Symbolic Dynamic Entropy                          	  |	SyDyEn
Increment Entropy                                 	  |	IncrEn
Cosine Similarity Entropy                         	  |	CoSiEn
Phase Entropy                                             |	PhasEn
Slope Entropy                                      	  |	SlopEn
Bubble Entropy                                		  |	BubbEn
Gridded Distribution Entropy                              |	GridEn
Entropy of Entropy                            	          |	EnofEn
Attention Entropy                                         |	AttnEn

_______________________________________________________________________

### Cross Entropies:

Entropy Type   |  Function Name 
---|---
Cross Sample Entropy                                  |	XSampEn
Cross Approximate Entropy                             |	XApEn
Cross Fuzzy Entropy                                   |	XFuzzEn
Cross Permutation Entropy                             |	XPermEn
Cross Conditional Entropy                             |	XCondEn
Cross Distribution Entropy                            |	XDistEn
Cross Spectral Entropy                          	  |	XSpecEn
Cross Kolmogorov Entropy                              |	XK2En
	
_______________________________________________________________________

### Bidimensional Entropies

Entropy Type   |  Function Name 
---|---
Bidimensional Sample Entropy                         |	SampEn2D
Bidimensional Fuzzy Entropy                          |	FuzzEn2D
Bidimensional Distribution Entropy                   |	DistEn2D
Bidimensional Dispersion Entropy                     |	DispEn2D
Bidimensional Permutation Entropy                    |	PermEn2D
Bidimensional Espinosa Entropy                       |	EspEn2D
	
_________________________________________________________________________

### Multiscale Entropy Functions

Entropy Type   |  Function Name 
---|---
Multiscale Entropy                                    | MSEn
Composite/Refined-Composite Multiscale Entropy        | cMSEn
Refined Multiscale Entropy                            | rMSEn
Hierarchical Multiscale Entropy                       | hMSEn
	
_________________________________________________________________________

### Multiscale Cross-Entropy Functions
Entropy Type   |  Function Name 
---|---
Multiscale Cross-Entropy                              |   XMSEn
Composite/Refined-Composite Multiscale Cross-Entropy  |   cXMSEn
Refined Multiscale Cross-Entropy                      |   rXMSEn
Hierarchical Multiscale Cross-Entropy                 |   hXMSEn



## License and Terms of Use
EntropyHub is licensed under the Apache License (Version 2.0) and is free to
use by all on condition that the following reference be included on any outputs
realized using the software:
 
        Matthew W. Flood (2021), 
        EntropyHub: An Open-Source Toolkit for Entropic Time Series Analysis,
        PLoS ONE 16(11):e0259448
        DOI: 10.1371/journal.pone.0259448
        www.EntropyHub.xyz

__________________________________________________________________


        © Copyright 2024 Matthew W. Flood, EntropyHub
        Licensed under the Apache License, Version 2.0 (the "License");
        you may not use this file except in compliance with the License.
        You may obtain a copy of the License at
        
                 http://www.apache.org/licenses/LICENSE-2.0
        
        Unless required by applicable law or agreed to in writing, software
        distributed under the License is distributed on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        See the License for the specific language governing permissions and
        limitations under the License.
        
        For Terms of Use see https://www.EntropyHub.xyz



## Contact

If you find this package useful, please consider starring it on GitHub, 
MatLab File Exchange, PyPI or Julia Packages as this helps us to gauge user 
satisfaction.

For general queries and information about EntropyHub, contact:    info@entropyhub.xyz
If you have any questions or need help using the package, please contact us at:    help@entropyhub.xyz
If you notice or identify any issues, please do not hesitate to contact us at:    fix@entropyhub.xyz

__Thank you__ for using EntropyHub.

Matt


<p  align="center">
	<img src="https://github.com/MattWillFlood/EntropyHub/blob/main/Graphics/EntropyHubLogo3.png" width="250" height="350"/>
</p>
        