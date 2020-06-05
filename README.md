# Research Paper and Motivation
This repository contains the code for implementing the algorithms and techniques in the research paper : 

Net2Text : https://www.usenix.org/conference/nsdi18/presentation/birkner

Website : NSDI'18 submission of the [Net2Text project](https://net2text.ethz.ch).

Bridging the semantic gaps that separate low-level forwarding rules distributed across the entire network and actionable 
high-level insights by network operators. Bridging this gap manually is slow. We replicate Net2Text, an interactive system 
which assists the network operator in reasoning about network-wide forwarding state. 

Out of the low-level forwarding state and a query expressed in natural language, Net2Text automatically produces succinct,
natural language descriptions, which efficiently capture network-wide behaviour. 

DEPENDENCIES
------------
Python Packages:
  Flask,
  Pandas,
  jsonify,
  make_response,
  json,
  
Software
--------
MySQL WorkBench

To run:
-------
1) Convert a network file using gml2csv.py.
2) Create a Database in MySql and add the converted file as a table.
3) Run python3 app.py
3) Open a web browser and go to 127.0.0.1:5000/
4) Run a query

Work By
-------
Tejas Arya(https://github.com/aryatejas2), Vaibhav Joshi(https://github.com/joshivaibhav), Ninad Godambe(https://github.com/NinadGodambe)
 

