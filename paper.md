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
link-citations: true
---

# Summary

Directed graphs are composed of a group of nodes that are connected by directed edges. Many important computational problems need to be solved on large-scale directed graphs. Examples include partitioning graphs into clusters based on similar features, known as community detection, as well as identifying failures in communication across nodes, known as fault detection. Distributed computation is critical for solving these large-scale computational problems on multiple machines in an efficient manner. This package provides distributed functions in Python for solving computational problems on large-scale directed graphs. 

# Statement of need


`distributedDirectedGraphAlgos` is a Python package for computing properties of directed graphs in a distributed manner. The API for `distributedDirectedGraphAlgos` provides distributed implementations of important operations including finding strongly connected components and the finite diameter of directed graphs. Strongly connected components are maximal subgraphs, where every node has a direct path from every other node in the subgraph. The finite diameter is the longest shortest path between any two nodes where such a path exists. Finding strongly connected components and the finite diameter of directed graphs have important implications in distributed control and in machine learning. For example, strongly connected components are important in designing controllable and observable networks and in solving community detection problems. Similarly, the finite diameter is important for fault detection in networks and speeding up search algorithms. In general, `distributedDirectedGraphAlgos` provides a foundation for distributed computation on large-scale directed graphs. 

`distributedDirectedGraphAlgos` can be used by a large population of users, including researchers, scientists, and developers. The algorithms were previously developed and published in [@reedSCCs]. The distributed nature of these algorithms enable scalability thereby making `distributedDirectedGraphAlgos` accessible and useful for future scientific explorations.


# Acknowledgements

E. Reed acknowledges the financial support from the National Science Foundation GRFP DGE-1842487, the University of Southern California Annenberg Fellowship, and a USC WiSE Top-Off Fellowship. E. Reed and P. Bogdan also acknowledge the financial support from the National Science Foundation under the Career Award CPS/CNS-1453860, the NSF award under Grant Numbers CCF-1837131, MCB-1936775, CMMI-1936624, and CNS-1932620, the U.S. Army Research Office (ARO) under Grant No. W911NF-17-1-0076 and W911NF-23-1-0111, and the DARPA Young Faculty Award and DARPA Director Award, under Grant Number N66001-17-1-4044, a 2021 USC Stevens Center Technology Advancement Grant (TAG) award, an Intel faculty award and a Northrop Grumman grant.

The financial supporters of this work had no role in the study design, data collection and analysis, decision to publish, or preparation of the manuscript. The views, opinions, and/or findings contained in this dissertation are those of the author and should not be interpreted as representing official views or policies, either expressed or implied by the Defense Advanced Research Projects Agency, the Department of Defense or the National Science Foundation.

# References