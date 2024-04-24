# EntropyHub: An open-source toolkit for entropic data analysis

<p align="center">
<img src="https://github.com/MattWillFlood/EntropyHub/blob/main/Graphics/EntropyHub_profiler.png" alt = "EntropyHub Git" width="250" height="250" />
</p>

#### See full documentation at [www.EntropyHub.xyz](https://www.EntropyHub.xyz)

  
  Available in 
  [MatLab](https://www.mathworks.com/matlabcentral/fileexchange/94185-entropyhub "EH4MATLAB")  // 
  [Python](https://pypi.org/project/EntropyHub/ "EH4PYTHON")  // 
  [Julia](https://juliahub.com/ui/Packages/EntropyHub/npy5E/ "EH4JULIA") 


## Latest Update
### v2.0
__*----- New multivariate methods -----*__       
Five new multivariate entropy functions incorporating several method-specific variations        
        > [Multivariate Sample Entropy](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.84.061918)      
        > [Multivariate Fuzzy Entropy](https://www.mdpi.com/1099-4300/19/1/2) [++ many fuzzy functions]        
        > [Multivariate Dispersion Entropy](https://www.mdpi.com/1099-4300/21/9/913) [++ many symbolic sequence transforms]          
        > [Multivariate Cosine Similarity Entropy](https://www.mdpi.com/1099-4300/24/9/1287)        
        > Multivariate Permutation Entropy  [++ *amplitude-aware*, *edge*, *phase*, *weighted* and *modified* variants]       

__*----- New multivariate multiscale methods -----*__       
Two new multivariate multiscale entropy functions        
        > [Multivariate Multiscale Entropy](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.84.061918) [++ coarse, modified and generalized graining procedures]          
        > [Composite and Refined-composite Multivariate Multiscale Entropy](https://link.springer.com/article/10.1007/s11517-017-1647-5)      

__*----- Extra signal processing tools -----*__     
**WindowData()** is a new function that allows users to segment data (univariate or multivariate time series) into windows with/without overlapping samples! This allows users to calculate entropy on subsequences of their data to perform analyses with greater time resolution.        

*Other little fixes...*
   
__*----- Docs edits -----*__     
        - Examples in the www.EntropyHub.xyz documentation were updated to match the latest package syntax.     

    
### More to come!
We are currently adding several new elements to EntropyHub that we hope will benefit many users. However, this is a time-consuming effort.              
Keep checking in here to find out more in the future!           
Thanks for all your support so far :)           


## About

Information and uncertainty can be regarded as two sides of the same coin: 
the more uncertainty there is, the more information we gain by removing that 
uncertainty. In the context of information and probability theory, ***Entropy*** 
quantifies that uncertainty. 

Various measures have been derived to estimate entropy (uncertainty) from discrete 
data sequences, each seeking to best capture the uncertainty of the system under examination. 
This has resulted in many entropy statistics from approximate entropy and sample entropy, to
multiscale sample entropy and refined-composite multiscale cross-sample entropy.

The goal of EntropyHub is to provide a comprehensive set of functions with a simple and 
consistent syntax that allows the user to augment parameters at the command 
line, enabling a range from basic to advanced entropy methods to be implemented
with ease.

***It is important to clarify that the entropy functions herein described 
estimate entropy in the context of probability theory and information theory as
defined by Shannon, and not thermodynamic or other entropies from classical physics.***


.........................................................................................................


## Installation

To install EntropyHub with Matlab, Python or Julia, please follow the instructions given in the relevant folder above.

### Requirements
_________________________________________________________________________________________________________
#### MatLab
There are two additional MatLab toolboxes required to exploit the *full* functionality of the EntropyHub toolkit: 

__*Signal Processing Toolbox*__ and __*Statistics and Machine Learning Toolbox.*__

However, most functions will work without these toolboxes.

EntropyHub is intended for use with MatLab versions >= 2016a.  In some cases the toolkit may work on versions 2015a and 2015b, 
but it is not recommended to install on MatLab versions older than 2016.
_________________________________________________________________________________________________________

#### Python
There are several package dependencies which will be installed alongside EntropyHub: 
Numpy, Scipy, Matplotlib, PyEMD, Requests

EntropyHub was designed using Python 3 and thus is not intended for use with Python 2. Python versions > 3.6 are recommended for using EntropyHub.  
_________________________________________________________________________________________________________

#### Julia
There are several package dependencies which will be installed alongside EntropyHub (if not already installed):

__*DSP, FFTW, HTTP, Random, Plots, StatsBase, StatsFuns, GroupSlices, Statistics, DelimitedFiles, Combinatorics, LinearAlgebra, DataInterpolations, Clustering*__

EntropyHub was designed using Julia 1.5 and is intended for use with Julia versions >= 1.2.


.........................................................................................................

## Documentation & Help 

The EntropyHub Guide is a .pdf booklet written to help you use the toolkit effectively. 
(available [here](https://github.com/MattWillFlood/EntropyHub/blob/main/EntropyHub%20Guide.pdf))

In this guide you will find descriptions of function syntax, examples of function use, and references to the source literature of each function.

The MatLab version of the toolkit has a comprehensive help section which can be accessed through the help browser.


.........................................................................................................


## License and Terms of Use

EntropyHub is licensed under the Apache License (Version 2.0) and is free to
use by all on condition that the following reference be included on any outputs
realized using the software:
 
Matthew W. Flood (2021)     
[EntropyHub: An Open-Source Toolkit for Entropic Time Series Analysis,](https://doi.org/10.1371/journal.pone.0259448)     
PLoS ONE 16(11):e0259448      
DOI: 10.1371/journal.pone.0259448     
[www.EntropyHub.xyz](https://www.EntropyHub.xyz)   

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
        
        For Terms of Use see https://github.com/MattWillFlood/EntropyHub


.........................................................................................................


## Contact

If you find this package useful, please consider starring it on GitHub, 
MatLab File Exchange, PyPI or Julia Packages as this helps us to gauge user 
satisfaction.

If you have any questions about the package or identify any issues, 
please do not hesitate to contact us at:    info@entropyhub.xyz

***Thank you*** for using EntropyHub.

Matt

 
.........................................................................................................

## Functions

EntropyHub functions fall into 8 categories: 

    * Base                       functions for estimating the entropy of a single univariate time series.
    * Cross                      functions for estimating the entropy between two univariate time series.
    * Multivariate               functions for estimating the entropy of a multivariate dataset.
    * Bidimensional              functions for estimating the entropy of a two-dimensional univariate matrix.
    * Multiscale                 functions for estimating the multiscale entropy of a single univariate time series using any of the Base entropy functions.
    * Multiscale Cross           functions for estimating the multiscale entropy between two univariate time series using any of the Cross-entropy functions.
    * Multivariate Multiscale    functions for estimating the multivariate multiscale entropy of multivariate dataset using any of the Multivariate-entropy functions.
    * Other                      Supplementary functions for various tasks related to EntropyHub and signal processing.

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
Spectral Entropy                              		  |	SpecEn
Dispersion Entropy                            		  |	DispEn
Symbolic Dynamic Entropy                          	  |	SyDyEn
Increment Entropy                                 	  |	IncrEn
Cosine Similarity Entropy                         	  |	CoSiEn
Phase Entropy                                             |	PhasEn
Slope Entropy                                             |	SlopEn
Bubble Entropy                                		  |	BubbEn
Gridded Distribution Entropy                              |	GridEn
Entropy of Entropy                                        |	EnofEn
Attention Entropy                                         |	AttnEn
Range Entropy                                             |     RangEn
Diversity Entropy                                         |     DivEn

_______________________________________________________________________

### Cross Entropies:

Entropy Type   |  Function Name 
--|--
Cross Sample Entropy                                  |	XSampEn
Cross Approximate Entropy                             |	XApEn
Cross Fuzzy Entropy                                   |	XFuzzEn
Cross Permutation Entropy                             |	XPermEn
Cross Conditional Entropy                             |	XCondEn
Cross Distribution Entropy                            |	XDistEn
Cross Spectral Entropy                          	  |	XSpecEn
Cross Kolmogorov Entropy                              |	XK2En
	
_______________________________________________________________________

### Multivariate Entropies:

Entropy Type   |  Function Name 
--|--
Multivariate Sample Entropy                                  |	MvSampEn
Multivariate Fuzzy Entropy                                   |	MvFuzzEn
Multivariate Permutation Entropy                             |	MvPermEn
Multivariate Dispersion Entropy                              |	MvDispEn
Multivariate Cosine Similarity Entropy                       |	MvCoSiEn

_______________________________________________________________________

### Bidimensional Entropies

Entropy Type   |  Function Name 
--|--
Bidimensional Sample Entropy                         |	SampEn2D
Bidimensional Fuzzy Entropy                          |	FuzzEn2D
Bidimensional Distribution Entropy                   |	DistEn2D
Bidimensional Dispersion Entropy                     |	DispEn2D
Bidimensional Permutation Entropy                    |	PermEn2D
Bidimensional Espinosa Entropy	                     |	EspEn2D
	
_________________________________________________________________________

### Multiscale Entropy Functions

Entropy Type   |  Function Name 
--|--
Multiscale Entropy                                    | MSEn
Composite/Refined-Composite Multiscale Entropy        | cMSEn
Refined Multiscale Entropy                            | rMSEn
Hierarchical Multiscale Entropy                 | hMSEn
	
_________________________________________________________________________

### Multiscale Cross-Entropy Functions
Entropy Type   |  Function Name 
--|--
Multiscale Cross-Entropy                              |   XMSEn
Composite/Refined-Composite Multiscale Cross-Entropy  |   cXMSEn
Refined Multiscale Cross-Entropy                            |   rXMSEn
Hierarchical Multiscale Cross-Entropy                 |   hXMSEn

_________________________________________________________________________

### Multivariate Multiscale Entropy Functions

Entropy Type   |  Function Name 
--|--
Multivariate Multiscale Entropy                                    | MvMSEn
Composite/Refined-Composite Multivariate Multiscale Entropy        | cMvMSEn

_________________________________________________________________________

### Other Functions

Entropy Type   |  Function Name 
--|--
Example Data Import Tool            |  ExampleData
Window Data Tool                    |  WindowData
Multiscale Entropy Object           |  MSobject


        
        
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
        
        
<p  align="center">
	<img src="https://github.com/MattWillFlood/EntropyHub/blob/main/Graphics/EntropyHubLogo3.png" width="250" height="350"/>
</p>
