---
title: 'distributedDirectedGraphAlgos: A Python package for distributed algorithms on directed graphs'
tags:
  - Python
  - directed graphs
  - distributed algorithms
authors:
  - name: Emily A. Reed
    orcid: 0000-0001-9598-5823
    equal-contrib: true
    corresponding: true # (This is how to denote the corresponding author)
    affiliation: 1 # (Multiple affiliations must be quoted)
  - name: Guilherme Ramos
    orcid: 0000-0001-6104-8444
    equal-contrib: true # (This is how you can denote equal contributions between multiple authors)
    affiliation: 2
  - name: Paul Bogdan
    orcid: 0000-0003-2118-0816
    affiliation: 1
  - name: Sérgio Pequito
    orcid: 0000-0002-5143-1543
    affiliation: 3
affiliations:
 - name: Ming Hsieh Department of Electrical and Computer Engineering, University of Southern California, Los Angeles, CA, USA
   index: 1
 - name: Dept. of Computer Science and Engineering, Instituto Superior Técnico, University of Lisbon, Portugal and Instituto de Telecomunicações, Lisbon, Portugal
   index: 2
 - name: Department of Information Technology, Division of Systems and Control, Uppsala University, Uppsala, Sweden
   index: 3
date: August 1, 2023
bibliography: paper.bib

---

# Summary

Many important computational problems need to be solved on large-scale directed graphs. Examples include partitioning graphs into clusters based on similar features, known as community detection, as well as identifying failures in communication across nodes, known as fault detection. Distributed computation is critical for solving these large-scale computational problems on multiple machines in an efficient manner. This package provides distributed functions in Python for solving computational problems on large-scale directed graphs. In particular, the package finds both the strongly connected components and finite diameter of directed graphs in a distributed manner. 

# Statement of need



`distributedDirectedGraphAlgos` is a Python package for computing properties of directed graphs in a distributed manner. The API for `distributedDirectedGraphAlgos` provides distributed implementations of important operations such as finding strongly connected components and the finite diameter of directed graphs. `distributedDirectedGraphAlgos` can be used for computation on large-scale graphs.

`distributedDirectedGraphAlgos` can be used by a large population of users, including researchers, scientists, and developers. 
The algorithms were previously developed and published in [@reedSCCs]. The distributed nature of these algorithms enable scalability thereby making `distributedDirectedGraphAlgos` accessible and useful for future scientific explorations.

# Mathematics

Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References