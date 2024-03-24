# EntropyHub: An open-source toolkit for entropic data analysis

__*MatLab Edition*__

<p align="center">
<img src="https://github.com/MattWillFlood/EntropyHub/blob/main/Graphics/EntropyHub_profiler.png" alt = "EntropyHub Git" width="250" height="250" />
</p>


## Installation

There are two ways to install EntropyHub for MatLab.

#### Method 1:
   1. Download the MatLab toolbox file (**EntropyHub.mltbx**) above.
   2. Open matlab and change the current folder to the directory where the .mltbx file is saved.
	<img src="https://github.com/MattWillFlood/EntropyHub/blob/main/Graphics/MATLAB_README1.png" width="600" height="600"  />
	
   3. Double-click the .mltbx file to open it and click install.
	<img src="https://github.com/MattWillFlood/EntropyHub/blob/main/Graphics/MATLAB_README2.png" />
	
#### Method 2:
   1. In MatLab, open the Add-Ons browser under the home tab by clicking 'Get Add-Ons'.
  	<img src="https://github.com/MattWillFlood/EntropyHub/blob/main/Graphics/MATLAB_README3.png" width="1100" height="600"  />
   2. In the search bar, search for __*EntroypHub*__.
   3. Open the resulting link, and click '__*add*__' in the top-right corner.
   4. Follow the instructions to install the toolbox. __Note: You must be logged in to your MathWorks account__. 
	

### System Requirements 
  There are two additional toolboxes required to get the __*full*__ functionality of the EntropyHub toolkit:   
  *Signal Processing Toolbox* and *Statistics and Machine Learning Toolbox*.
  However, most functions will work without these toolboxes.
  
  EntropyHub is intended for use with MatLab versions >= 2016a, although some functions in v1.0 and later require >= 2022a and later.
  In some cases the toolkit may work on versions 2015a & 2015b. 
  However, it is not recommended to install on latest the MatLab version available.


## Documentation & Help 

A key advantage of EntropyHub is the comprehensive documentation available to help users to make the most of the toolkit.
In the supplemental software section of the MatLab help browser, you can find the custom EntropyHub documentation on each EntropyHub function, complete with several examples and references to relevant scientific sources. 
To learn more about a specific function, one can do so easily from the command line by typing: `doc FunctionName`, which will display the documentation in the help browser.
For example:

`doc SampEn`     Documentation on sample entropy function

`doc XSpecEn`    Documentation on cross-spectral entropy function

`doc hXMSEn`     Documentation on hierarchical multiscale cross-entropy function

Alternatively, one can simply access the docstrings of a function (like any MatLab function) by typing `help FunctionName` in the command line, which will display the docstrings in the command window.


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
Range Entropy                                  		  |	RangEn
Diversity Entropy                          		     |	DivEn
Spectral Entropy                              		  |	SpecEn
Dispersion Entropy                            		  |	DispEn
Symbolic Dynamic Entropy                          	  |	SyDyEn
Increment Entropy                                 	  |	IncrEn
Cosine Similarity Entropy                         	  |	CoSiEn
Phase Entropy                                        |	PhasEn
Slope Entropy                                     	  |	SlopEn
Bubble Entropy                                		  |	BubbEn
Gridded Distribution Entropy                         |	GridEn
Entropy of Entropy                                   |	EnofEn
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
Cross Spectral Entropy                            	   |	XSpecEn
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
Bidimensional Espinosa Entropy                       |	EspEn2D
	
_________________________________________________________________________

### Multiscale Entropy Functions

Entropy Type   |  Function Name 
--|--
Multiscale Entropy                                    | MSEn
Composite/Refined-Composite Multiscale Entropy        | cMSEn
Refined Multiscale Entropy                            | rMSEn
Hierarchical Multiscale Entropy                       | hMSEn
	
_________________________________________________________________________

### Multiscale Cross-Entropy Functions
Entropy Type   |  Function Name 
--|--
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
        
        For Terms of Use see https://github.com/MattWillFlood/EntropyHub



## Contact

If you find this package useful, please consider starring it on GitHub, 
MatLab File Exchange, PyPI or Julia Packages as this helps us to gauge user 
satisfaction.

If you have any questions about the package or identify any issues, 
please do not hesitate to contact us at:    info@entropyhub.xyz


***Thank you*** for using EntropyHub.

Matt

        
        
        
        
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
