https://builtwithdjango.com/blog/basic-django-setup


https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/


The first step in building a Phyton project s to create a virtual environement 

https://builtwithdjango.com/blog/basic-django-setup

This guide will help you through the process of installing poetry to manage python version in your system and to install python packages. Preferably, use Ubuntu WSL2 
this will alow you to more easily reporduce the environement and evitate conglicts.

You will first need to install pyen using pip.

Prerequisites

Pyenv
We are going to use brew to install Pyenv. If you don't have brew installed on your Mac, run the following command:

'''bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
'''

Then, install Pyenv:

'''bash
brew update
brew install pyenv
'''
to test if this was installed correctly try running this in your terminal:

'''bash
pyenv --version
'''

we are going to be using Python version 3.11.4 in our tutorial, so let's get that installed with the following command:

'''bash
pyenv install 3.9.9
'''
Your terminal will start giving you some outputs. Wait for a minute or two until the download and installation are complete. This is everything we are going to cover regarding pyenv, we don't need to know more for the purposes of this tutorial.

Poetry
If you have Poetry installed you can skip this step.

So, let's first install Poetry. You can do that by running the following command in your terminal:

'''bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
'''

The good news is that you have to do it once. To test that everything went smoothly, try running the following in your terminal:

'''bash
poetry --version
'''

Setting up the Environment
Alright, we are now ready to start. Here is what you want to do:

Open up your Ubuntu terminal, cd into the directory that you use to store all your code. For me it is:

cd ~/web

Then create a new directory for your project. I'm going to call mine "lukasScrapper":

mkdir lukasScrapper && cd basic_django

THen

code .

This will open up your VS Code in the current directory.

The most important part is to set the Python version for your project. You can do that by running the following command:

'''bash
pyenv local 3.11.4
'''
You can verify your local and global python isntalled verisons with the following commands:

'''bash 
pyenv versions
pyenv global
pyenv local
'''

Now, you can create a new virtual environment for your project by running the following command:

'''bash
poetry new .
'''
