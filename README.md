# P4 Tournament Results Project


## Introduction

This is the Project 4 Tournament Results project for Udacity Fullstack Nanodegree. This app covers the basics features such as...
- Data and Tables
- SQL queries


## Requirements

* python >= 2.7
* Oracle VM VirtualBox software
* Vagrant software
* Git software


## Installation

1. Clone or fork this repository
2. Download and Install Oracle VM software
3. Download and Install Vagrant software
4. Download and Install Git

##Usage

1. Open up Git Bash
2. Using Git command line. change directory through files until you're in the vagrant file. I.E. 'Root Folder/Vagrant/'
    * NOTE: You'll know if you're in the right directory when you see files like .vagrant, catalog, forum, tournament, Vagrantfile
3. Once in Vagrant directory, type 'vagrant up' into terminal to install files
4. Next, type 'vagrant ssh' to login
5. You're now logged into the virtual machine, type 'cd /vagrant/tournament'
6. Type 'psql -f tournament.sql'. To create new tournament database, players schema, and matches schema
7. Type 'python tournament_test.py' to run test file
8. Type '\exit' to logout


## Details

* This application allows the user to insert new SQL queries, new tables, and run the tournament_test.py file.
