.. image:: https://raw.githubusercontent.com/MattWillFlood/EntropyHub/main/metrics.entropyhub.svg
    :align: right
    :height: 80px
    :target: https://github.com/MattWillFlood/EntropyHub

**************
Latest Updates 
**************

.. toctree::
   :maxdepth: 3
   :titlesonly:

..............................................................


March 2024
############

Version 1.0 is here!
====================

| EntropyHub is continuously growing to incorporate the lastest developments in the scientific literature.
| This new major release (v1.0) reflects that with many new functions and features to provide you with a versatile environment that makes complex entropy methods easy to implement.
| The following list summarizes some of the main updates available in v1.0.

    **+ New entropy methods**      
        | Two new base entropy functions (and their multiscale versions) have been added:   
        | + `Diversity Entropy <https://ieeexplore.ieee.org/document/9194995>`_      
        | + `Range Entropy <https://www.mdpi.com/1099-4300/20/12/962>`_

    **+ New fuzzy membership functions**  
        | Several new fuzzy membership functions have been added to FuzzEn, XFuzzEn and FuzzEn2D to provide more options for mapping the degree of similarity between embedding vectors.
        | These include *trapezoidal*, *triangular* and *gaussian*, among others.
        | Further info on these membership functions can be found `here. <https://hal.science/hal-02267711/document>`_

    **+ Phase Permutation Entropy**
        | A new variant - '*phase*' permutation entropy - has been added to PermEn.   
        | This method employs a hilbert transformation of the data sequence, based on the methods outlined `here. <https://doi.org/10.1016/j.physa.2020.125686>`_

    **+ Cross-Entropy with different length sequences**
        | EntropyHub v1.0 now allows for cross-entropy (and multiscale cross-entropy) estimation with different length signals (*except XCondEn and XPermEn*).
        | As a result, the new cross-entropy functions require a separate input for each sequence (Sig1, Sig2).

    **+ Refined-Composite Multiscale Fuzzy Entropy**
        | In addition to the refined-composite multiscale sample entropy that was available in earlier versions, now one can estimate the refined-composite multiscale fuzzy entropy based on the method outlined `here. <https://link.springer.com/article/10.1007/s11517-017-1647-5>`_
        | What's more, refined-composite multicale cross-fuzzy entropy is also available, and both can be estimated using any of the fuzzy membership functions in FuzzEn or XFuzzEn.

    **+ Generalized Multiscale Entropy**
        | Generaized multiscale entropy and generalized multiscale cross-entropy can now be estimated. Just choose the '*generalized*' as the graining procedure in MSEn or XMSEn. 

    **+ Variance of sample entropy estimate**
        | Based on the `method outlined by Lake et al., <https://journals.physiology.org/doi/epdf/10.1152/ajpregu.00069.2002>`_ it is now possible to obtain a measure of the variance in the sample entropy estimate.
        | This is achieved by approximating the number of overlapping embedding vectors.
        | To do so, just set the parameter '*Vcp*'==true in SampEn and XSampEn, but note that doing so requires *a lot* of computer memory.

Several little bugs and inconsistencies have also been fixed in this release. We want to thank all of you who have identified and alerted us to these bugs. 
Most of these bugs have been noted via the `GitHub issues portal <https://github.com/MattWillFlood/EntropyHub/issues>`_.

    **Bug fixes**
        | - The DispEn2D function in python has now fixed `this issue <https://github.com/MattWillFlood/EntropyHub/issues/8>`_.
        | - The type hint for FuzzEn in python has been updated `as requested <https://github.com/MattWillFlood/EntropyHub/issues/1>`_.
        | - `Compatbility issues with EntropyHub.jl <https://github.com/MattWillFlood/EntropyHub.jl/issues/3>`_ are now resolved.
        | - A bug in the K2En python function led to incorrect entropy estimates for data sequences with many equal values. This has been corrected.
    
    **Other Changes**
        | - The *'equal'* method for discretizing data in DispEn and DispEn2D has been updated to be consistent across Python, MatLab and Julia.
        |   This is unlikely to have impacted any users previously.
        | - The zeroth dimension (m=0) estimate of ApEn and XApEn has been changed to -phi(1).
        | - The default radius threshold distance for XApEn, XSampEn and XK2En has been changed to use the *pooled* standard deviation [i.e. 0.2*SDpooled(X,Y)].
    

More to come!
=============

| We are currently adding several new elements to EntropyHub that we hope will benefit many users. However, this is a time-consuming effort.
| Keep checking in here to find out more in the future!
| Thanks for all your support so far :)

..............................................................


November 2022
#############

**EntropyHub is 1 year old!**

| There has been great interest in EntropyHub in the first year since its `original publication in Plos One <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0259448>`_.
| To date, 
| * there are about 11 `publications citing EntropyHub <./Publications.html>`_, covering a broad range of scientific disciplines including neuroscience, meteorology and mathematics.
| * the `EntropyHub <https://github.com/MattWillFlood/EntropyHub>`_ and `EntropyHub.jl <https://github.com/MattWillFlood/EntropyHub.jl>`_ GitHub repositories have over 50 stars (42 and 11 respectively).
| * the EntropyHub MatLab toolkit has been downloaded over 600 times from the `MatLab file exchange <https://www.mathworks.com/matlabcentral/fileexchange/94185-entropyhub>`_!

| We would like to extend our gratitude to all those who have used EntropyHub in their work, who have provided helpful feedback, and who starred the toolkit on GitHub and MatLab.
| We plan to expand EntropyHub in the coming years and we hope that you will continue to support us in this endeavour.
| Spread the word! ;)

..............................................................


July 2022
#########

**IEEE EMBC Symposium on Entropy Algorithms**

.. image:: ./_images/EMBC1.jpg
    :width: 500px
    :align: left
    :height: 400px

| At the 2022 IEEE EMBC conference in Glasgow, a symposium entitled *Recent Advances in Entropy Algorithms for Biomedical Signals: Beyond Univariate Time Series* 
| was organised by Prof. Javier Escudero and Prof. Anne Humeau-Huertier, introducing the latest methods in entropy analysis to the biomedical engineering community.
| As part of this symposium, Dr Matt Flood presented EntropyHub, introducing the audience to the advantages and benefits offered by the toolkit.
 
.. image:: ./_images/EMBC2.jpg
    :width: 500px
    :align: center
    :height: 400px

..............................................................


February 2022
#############

**EntropyHub Presentation at IEEE EMBC Glasgow 2022**

.. image:: ./_images/EMBC22.png
    :width: 500px
    :align: left
    :height: 150px

| The `2022 IEEE Engineering in Medicine and Biology Conference (EMBC) <https://embc.embs.org/2022/>`_ will take place in Glasgow from 11-15 July. As part of the conference, there will be a symposium titled *Recent Advances in Entropy Quantification Algorithms for Biomedical Signals: Beyond Univariate Time Series*, where novel appications of entropy in biomedicine will be discussed.
| Dr Matt Flood - founder and lead developer of EntropyHub - will give a presentation on *EntropyHub* as part of this symposium, introducing the toolkit, demonstrating its functionality, and revealing plans for future releases.

Read more about the conference programme `here <https://embc.embs.org/2022/wp-content/uploads/sites/80/2022/04/WS_MS_SS_program.pdf>`_          

Hope to meet you there!

..............................................................

December 2021
#############

**Version Update - EntropyHub v0.2**

EntropyHub v0.2 includes two new bidimensional entropy methods:      

| * `Bidimensional permutation entropy (PermEn2D) <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0040689>`_         
| * `Bidimensional Espinosa entropy (EspEn2D) <https://www.mdpi.com/1099-4300/23/10/1261>`_

..............................................................

November 2021
#############

**Publication of paper on EntropyHub in PLoS One.**

.. image:: ./_images/PLOS.png
    :width: 500px
    :align: left
    :height: 150px

| To bring EntropyHub to the attention of the wider scientific community, we are happy to announce that a paper describing the toolkit has been `published in PLoS One <https://www.doi.org/10.1371/journal.pone.0259448>`_.
| Users of the toolkit are **required** to cite this paper if they use EntropyHub in the work.

        | *Matthew W. Flood and Bernd Grimm,*     
        | *EntropyHub: An Open-Source Toolkit for Entropic Time Series Analysis,*    
        | *PLoS One 16(11):e0259448 (2021),*
        | *DOI: 10.1371/journal.pone.0259448*


**Version Update - EntropyHub v0.1.1**

EntropyHub v0.1.1 includes corrections to the entropy of entropy (EnofEn) function.
Following this update, users can specify the amplitude range (xmin, xmax) over which the number of slices (S1) are partitioned.
See the source literature for more info.

..............................................................

June 2021
#########

**First release of EntropyHub (v0.1).**

The initial release of the EntropyHub toolkit on all platforms including:

+ `GitHub <https://www.github.com/MattWillFlood/EntropyHub>`_,     
+ `Matlab File Exchange <https://www.mathworks.com/matlabcentral/fileexchange/94185-entropyhub>`_,    
+ `PyPI <https://pypi.org/project/EntropyHub/>`_ ,    
+ `Julia Packages <https://juliahub.com/ui/Packages/EntropyHub/npy5E/>`_

As with all initial releases, there may be some bugs, typo's or other small issues that will be ironed out in time.

..............................................................


.. image:: ./_images/EntropyHubLogo3.png
    :width: 250px
    :align: center
    :height: 350px



