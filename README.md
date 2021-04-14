<img  width="120" src="https://github.com/MattWillFlood/EntropyHub/blob/main/Graphics/EntropyHub_profiler2.png">

# EntropyHub: An open-source toolkit for entropic time-series analysis. 


### Welcome to EntropyHub.

EntropyHub is a software package providing a comprehensive set of functions to calculate information-theoretic entropy measures from time-series data.

Designed with all users in mind, EntropyHub is available in MatLab, Python and Julia, with a simple and consistent syntax across all three languages.
From relatively straightforward measures (e.g. sample entropy) to more advanced measures (e.g. composite multiscale corrected cross-conditional entropy), users can easily augment each entropy method at the command line by specifiying keyword arguments. 

Functions cover base/core entropies, cross-entropies and bidimensional [2D] entropies, all featuring time-delayed embedding. 
Multiscale variants of each base and cross-entropy function are also avaliable, including composite, refined and hierarchical multiscale approaches.
See the tables below for a full list of available functions.

EntropyHub aims to make the process of measuring the complex simple. 
As more methods of deriving approximating entropy emerge in the scientific literature, EntropyHub will be updated accordingly.

This package is open for use by all in accordance with the terms of the attached License agreement.

Any research outputs obtained using EntropyHub are required to include the following citation:

  **Matthew W. Flood and Bernd Grimm,   _EntropyHub: An open-source toolkit for entropic time series analysis_, 2021**


For any questions or issues, email _entropyhubproject@gmail.com_


We hope you find this software package useful.

Matt


 ---------------------------------------------------------- 
### _Guide_
The [EntropyHub Guide](https://github.com/MattWillFlood/EntropyHub/) is the primary source of information regarding all aspects of the package.
Users are encouraged to consult the guide prior to using EntropyHub.
The guide provides:
* an overview of the software,
* instructions for installation, 
* explanations of function arguments and outputs, 
* a tutorial with numerous examples 


## Installation

Here are the simplest ways to install EntropyHub.
For more specific information on installation in MatLab, Python or Julia, see the respective directories above or the EntropyHub guide.


### MatLab
[linktomatlab](https://www.mathworks.com)

### Python
[linktopypi](https://www.pypi.com)

### Julia
[linktojuliaobserver](https://www.julialang.com)

----------------------------------------------------------

**_EntropyHub functions belong to one of five main classes/categories:_**
* Base Entropies             >>  e.g. Approximate Entropy (ApEn), Sample Entropy (SampEn)
* Cross Entropies            >>  e.g. Cross-Approximate Entropy (XApEn), Cross-Sample Entropy (XSampEn)
* Bidimensional Entropies    >>  e.g. Bidimensional Sample Entropy (SampEn2D), Bidimensional Fuzzy Entropy (FuzzEn2D)
* Multiscale Entropies       >>  e.g. Multiscale Sample Entropy (MSEn),  Hierarchical Multiscale Sample Entropy (rMSEn)
* Multiscale Cross Entropies >>  e.g. Multiscale Cross-Sample Entropy (XMSEn),  Refined Multiscale Cross-Sample Entropy (rXMSEn)

----------------------------------------------------------



Base Entropies                                        |	Function Name	
------------------------------------------------------|------------------
Approximate Entropy                             	  |	ApEn
Sample Entropy                                		  |	SampEn
Fuzzy Entropy                                 		  |	FuzzEn
Kolmogorov Entropy                            		  |	K2En
Permutation Entropy                           		  |	PermEn
Conditional Entropy                            		  |	CondEn
Distribution Entropy                           		  |	DistEn
Spectral Entropy                               		  |	SpecEn
Dispersion Entropy                             		  |	DispEn
Symbolic Dynamic Entropy                           	  |	SyDyEn
Increment Entropy                                  	  |	IncrEn
Cosine Similarity Entropy                          	  |	CoSiEn
Phase Entropy                                         |	PhasEn
Slope Entropy                                      	  |	SlopEn
Bubble Entropy                                    		  |	BubbEn
Gridded Distribution Entropy                          |	GridEn
Entropy of Entropy                            	       |	EnofEn
Attention Entropy                                     |	AttnEn


Cross Entropies                                       |	Function Name
------------------------------------------------------|------------------
Cross Sample Entropy                                  |	XSampEn
Cross Approximate Entropy                             |	XApEn
Cross Fuzzy Entropy                                   |	XFuzzEn
Cross Permutation Entropy                             |	XPermEn
Cross Conditional Entropy                             |	XCondEn
Cross Distribution Entropy                            |	XDistEn
Cross Spectral Entropy                             	  |	XSpecEn
Cross Kolmogorov Entropy                              |	XK2En
	

Bidimensional Entropies                              |	Function Name
------------------------------------------------------|------------------
Bidimensional Sample Entropy                         |	SampEn2D
Bidimensional Fuzzy Entropy                          |	FuzzEn2D
Bidimensional Distribution Entropy                   |	DistEn2D
	

Multiscale Entropy Functions                          | Function Name
------------------------------------------------------|------------------
Multiscale Entropy                                    | MSEn
Composite Multiscale Entropy                          | cMSEn
+ Refined-Composite Multiscale Entropy                | 
Refined Multiscale Entropy                            | rMSEn
Hierarchical Multiscale Entropy Object                | hMSEn


Multiscale Entropies	MSEn                          |	
------------------------------------------------------|
Multiscale Sample Entropy                             |	
Multiscale Approximate Entropy                        |	
Multiscale Fuzzy Entropy                              |	
Multiscale Permutation Entropy                        |	
Multiscale Dispersion Entropy                         |	
Multiscale Cosine Similarity Entropy                  |	
Multiscale Symblic Dynamic Entropy                    |	
Multiscale Conditional Entropy                        |	    
Multiscale Entropy of Entropy                         | 
Multiscale Gridded Distribution Entropy               |	
Multiscale Slope Entropy                              |
Multiscale Phase Entropy                              |		
Multiscale Kolmogorov Entropy                         |	
Multiscale Distribution Entropy                       |		
Multiscale Bubble Entropy                             |	
Multiscale Increment Entropy                          |	
Multiscale Attention Entropy                          |	
	

Multiscale Cross-Entropy Functions                    | Function Name
------------------------------------------------------|------------------
Multiscale Cross-Entropy                              |   XMSEn
Composite Cross-Entropy                               |   cXMSEn
+ Refined-Composite Multiscale Cross-Entropy          |   
Refined Multiscale Entropy                            |   rXMSEn
Hierarchical Multiscale Entropy Object                |   hXMSEn


Multiscale Cross-Entropies                            |	
------------------------------------------------------|
Multiscale Cross-Sample Entropy                       |	
Multiscale Cross-Approximate Entropy                  |	
Multiscale Cross-Fuzzy Entropy                        |	
Multiscale Cross-Permutation Entropy                  |	    
Multiscale Cross-Distribution Entropy                 |	
Multiscale Cross-Kolmogorov Entropy                   | 
Multiscale Cross-Conditional Entropy                  |	

