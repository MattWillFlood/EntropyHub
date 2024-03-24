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
### v1.0
__*----- New entropy methods -----*__             
Two new base entropy functions (and their multiscale versions) have been added:         
        > [Diversity Entropy](https://ieeexplore.ieee.org/document/9194995)             
        > [Range Entropy](https://www.mdpi.com/1099-4300/20/12/962)             

__*----- New fuzzy membership functions -----*__          
Several new fuzzy membership functions have been added to FuzzEn, XFuzzEn and FuzzEn2D to provide more options for mapping the degree of similarity between embedding vectors.          
These include *trapezoidal*, *triangular* and *gaussian*, among others.                 
Further info on these membership functions can be found [here.](https://hal.science/hal-02267711/document)              

__*----- Phase Permutation Entropy -----*__               
A new variant - '*phase*' permutation entropy - has been added to PermEn.                  
This method employs a hilbert transformation of the data sequence, based on the methods outlined [here.](https://doi.org/10.1016/j.physa.2020.125686)           

__*----- Cross-Entropy with different length sequences -----*__           
EntropyHub v1.0 now allows for cross-entropy (and multiscale cross-entropy) estimation with different length signals (_except XCondEn and XPermEn_).            
As a result, the new cross-entropy functions require a separate input for each sequence (Sig1, Sig2).                   

__*----- Refined-Composite Multiscale Fuzzy Entropy -----*__              
In addition to the refined-composite multiscale sample entropy that was available in earlier versions, now one can estimate the refined-composite multiscale fuzzy entropy based on the method outlined [here.](https://link.springer.com/article/10.1007/s11517-017-1647-5)    
What's more, refined-composite multicale cross-fuzzy entropy is also available, and both can be estimated using any of the fuzzy membership functions in FuzzEn or XFuzzEn.             

__*----- Generalized Multiscale Entropy -----*__          
Generaized multiscale entropy and generalized multiscale cross-entropy can now be estimated. Just choose the '*generalized*' as the graining procedure in MSEn or XMSEn.        

__*----- Variance of sample entropy estimate -----*__             
Based on the [method outlined by Lake et al.,](https://journals.physiology.org/doi/epdf/10.1152/ajpregu.00069.2002) it is now possible to obtain a measure of the variance in the sample entropy estimate.              
This is achieved by approximating the number of overlapping embedding vectors.          
To do so, just set the parameter '*Vcp*'==true in SampEn and XSampEn, but note that doing so requires *a lot* of computer memory.              

*Several little bugs and inconsistencies have also been fixed in this release. We want to thank all of you who have identified and alerted us to these bugs.*       
*Most of these bugs have been noted via the [GitHub issues portal](https://github.com/MattWillFlood/EntropyHub/issues).*        

__*----- Bug fixes -----*__             
        - The DispEn2D function in python has now fixed [this issue](https://github.com/MattWillFlood/EntropyHub/issues/8).     
        - The type hint for FuzzEn in python has been updated [as requested](https://github.com/MattWillFlood/EntropyHub/issues/1).             
        - [Compatbility issues with EntropyHub.jl](https://github.com/MattWillFlood/EntropyHub.jl/issues/3) are now resolved.           
        - A bug in the K2En python function led to incorrect entropy estimates for data sequences with many equal values. This has been corrected.              
    
__*----- Other Changes -----*__             
        - The *'equal'* method for discretizing data in DispEn and DispEn2D has been updated to be consistent across Python, MatLab and Julia. This is unlikely to have impacted any users previously.          
        - The zeroth dimension (m=0) estimate of ApEn and XApEn has been changed to -phi(1).                    
        - The default radius threshold distance for XApEn, XSampEn and XK2En has been changed to use the *pooled* standard deviation [i.e. 0.2*SDpooled(X,Y)].          
    
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
Spectral Entropy                              		  |	SpecEn
Dispersion Entropy                            		  |	DispEn
Symbolic Dynamic Entropy                          	  |	SyDyEn
Increment Entropy                                 	  |	IncrEn
Cosine Similarity Entropy                         	  |	CoSiEn
Phase Entropy                                        |	PhasEn
Slope Entropy                                        |	SlopEn
Bubble Entropy                                		  |	BubbEn
Gridded Distribution Entropy                         |	GridEn
Entropy of Entropy                            	     |	EnofEn
Attention Entropy                                    |	AttnEn
Range Entropy                                        |   RangEn
Diversity Entropy                                    |   DivEn

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
