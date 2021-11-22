**********
EntropyHub 
**********

An open-source toolkit for entropic time series analysis
########################################################

.. image:: ./_images/EntropyHub_Profiler.png
    :width: 150px
    :align: center
    :height: 150px

.. centered:: Available in: 
.. centered:: `Matlab  <https://www.mathworks.com/matlabcentral/fileexchange/94185-entropyhub>`_ // `Python <https://pypi.org/project/EntropyHub/>`_  // `Julia <https://juliahub.com/ui/Packages/EntropyHub/npy5E/>`_

.. toctree::
   :maxdepth: 3
   :titlesonly:
   :hidden:

   EHupdates

* `Latest Updates <./EHupdates.html>`_
* `Take part in our user survey <https://forms.gle/QxwUQASUh3bVhpfN9>`_
    

Welcome
#######

Welcome to EntropyHub!

This toolkit provides a wide range of functions to calculate different entropy statistics.

There is an ever-growing range of information-theoretic and dynamical systems entropy measures presented in the scientific literature. 
Although many functions for estimating these entropies can be found in various corners of the internet, 
there is currently no toolkit to perform entropic time-series analysis in MatLab, Python and Julia, all with an extensive documentation and consistent syntax.

The goal of EntropyHub is to integrate the many established entropy methods in one open-source package.


About
#####

Information and uncertainty can be regarded as two sides of the same coin: 
the more uncertainty there is, the more information we gain by removing that uncertainty.
In the context of information and probability theory, **Entropy** quantifies that uncertainty. 

The concept of entropy has its origins in `classical physics <http://www.scholarpedia.org/article/Entropy>`_ under the second law of thermodynamics, 
a law `considered to underpin our fundamental understanding <https://www.penguin.co.uk/books/301539/the-order-of-time/9780141984964.html>`_
of `time in physics <https://en.wikipedia.org/wiki/Time_in_physics>`_. 
In the context of nonlinear dynamics, entropy is central in quantifying the degree of uncertainty or information gain, and is therefore widely used
to explain complex nonlinear behaviour in real-world systems.
Attempting to analyse the analog world around us requires that we measure time in discrete steps, but doing so compromises 
our ability to measure entropy accurately. Various measures have been derived to estimate entropy (uncertainty) from discrete time series, each seeking to 
best capture the uncertainty of the system under examination. This has resulted in many entropy statistics from approximate entropy and sample entropy, to
multiscale sample entropy and refined-composite multiscale cross-sample entropy.

As the number of statisitcal entropy measures grows, it becomes ever more difficult to identify, contrast and compare the performance of each measure. 
To overcome this, we have developed EntropyHub - an open-source toolkit designed to integrate the many established entropy methods into one package.
The goal of EntropyHub is to provide a comprehensive set of functions with a simple and consistent syntax that allows the user to augment parameters at the command 
line, enabling a range from basic to advanced entropy methods to be implemented with ease.

**It is important to clarify that the entropy functions herein described estimate entropy in the context of nonlinear dynamics, probability theory and information theory, and not thermodynamic or other entropies from classical physics.**

.........................................................................................................


Documentation & Help 
####################

The `EntropyHub Guide <https://github.com/MattWillFlood/EntropyHub/blob/main/EntropyHub%20Guide.pdf>`_ is a .pdf booklet written to help you use the toolkit effectively 
(available for :download:`download here <./_static/EntropyHubGuide.pdf>`).

In this guide you will find descriptions of function syntax, examples of function use, and references to the source literature of each function.

*The MatLab version of the toolkit has a comprehensive help section which can be accessed through the help browser.*


.........................................................................................................


Citation and Licensing
######################

EntropyHub is licensed under the Apache License (Version 2.0) and is free to
use by all on condition that the following reference be included on any scientific outputs
realized using the software:
 
        | **Matthew W. Flood and Bernd Grimm,**     
        | **EntropyHub: An Open-Source Toolkit for Entropic Time Series Analysis,**    
        | **PLoS One 16(11):e0259448 (2021),** 
        | **DOI: 10.1371/journal.pone.0259448**    

        | *www.EntropyHub.xyz*

__________________________________________________________________


        © Copyright 2021 Matthew W. Flood, EntropyHub

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


Contact
#######

If you find this package useful, please consider starring it on
`GitHub <https://www.github.com/MattWillFlood/EntropyHub>`_, `Matlab File Exchange <https://www.mathworks.com/matlabcentral/fileexchange/94185-entropyhub>`_, 
`PyPI <https://pypi.org/project/EntropyHub/>`_ , and `Julia Packages <https://juliahub.com/ui/Packages/EntropyHub/npy5E/>`_ as this helps us to gauge user satisfaction.

| If you have any questions about the package, please do not hesitate to contact us at:  ``info@entropyhub.xyz`` 
| If you identify any bugs, please contact us at:  ``fix@entropyhub.xyz``
| If you need any help installing or using the toolkit, please contact us at:  ``help@entropyhub.xyz`` 


**Thank you** for using EntropyHub.

Matt

.. image:: ./_images/EntropyHubLogo3.png
    :width: 250px
    :align: center
    :height: 350px