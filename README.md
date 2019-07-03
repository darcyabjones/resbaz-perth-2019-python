# resbaz-perth-2019-python

This repository contains Jupyter notebooks and resources for the 2019 Perth Research Bazaar, Python stream.

The lesson is adapted from the [Data Carpentry Ecology lesson](http://www.datacarpentry.org/python-ecology-lesson/) and the [CIC software carpentry training material](https://github.com/CurtinIC/cic-swc-material).

We'll be covering most of the content in the [Data Carpentry Ecology lesson](http://www.datacarpentry.org/python-ecology-lesson/), excluding the SQL and more advanced plotting content.

Additional Python learning resources for your future learning can be found at:
- <http://swcarpentry.github.io/python-novice-inflammation/>
- <http://swcarpentry.github.io/python-novice-gapminder/>
- <https://docs.python.org/3/tutorial/index.html>  # Suggest you read this piecemeal as you need it.
- <https://jakevdp.github.io/PythonDataScienceHandbook/>  # More complex but a good free resource for working with data.


## Setup

Please try to install a bash terminal, Python 3, and the required packages before coming.
If you're unable to get it running, don't stress!
We'll have people to help you on the day.

Instructions for installing a bash terminal are available at the [software carpentry shell lesson](http://swcarpentry.github.io/shell-novice/setup.html).
Instructions for installing Python 3 using [Anaconda](https://www.anaconda.com/distribution/) are available at the [software carpentry python lesson](http://swcarpentry.github.io/python-novice-gapminder/setup/).

**Windows users may need to perform a few extra steps to get Anaconda working with Git Bash.**
By default the Windows Anaconda installer doesn't add Anaconda to your `PATH` variable. This `PATH` variable is like an "address book" that terminals can go to look for software they can use.
[This article from DataCamp](https://www.datacamp.com/community/tutorials/installing-anaconda-windows) has a good tutorial for configuring the `PATH` variable and getting git bash to work with Anaconda with Windows 8 and 10.
Windows 7 users can follow most of those instructions, but the place to access and change the environment variables is different. [This blog post has the directions to set environment variables for Windows 7](http://geekswithblogs.net/renso/archive/2009/10/21/how-to-set-the-windows-path-in-windows-7.aspx).


The full Anaconda installation already installs all of the packages we will use.
If you install the "miniconda" version, you'll also need to install the python packages separately.

Open up Git Bash or your terminal and enter:

```bash
conda install -y numpy pandas matplotlib seaborn jupyter
```


## Download this repository!

We'll be working from this notebook and filling in the answers as we go.
To fetch the notebook and the example data we will be using you will need to download this repo.

If you have `git` installed you can `clone` it from the terminal at the location that you want to store it...

```bash
git clone https://github.com/darcyabjones/resbaz-perth-2019-python.git
```

If you don't have `git` installed, you can download a Zip archive of the repository from <https://github.com/darcyabjones/resbaz-perth-2019-python/archive/master.zip> and unzip it wherever you want :).

Note that you can find these urls yourself by clicking the green "Clone or download" button towards the top-right of the repository landing page.


To check that all of the required packages are installed, open a terminal in the repository directory and run the following command:

```bash
python3 scripts/check_packages.py
```

Windows users _may_ need to enter this command instead ...

```bash
Python scripts/check_packages.py
```

If any warnings come up, talk to us!


## Get started

You can start running the Jupyter notebook by opening Git Bash or your terminal and entering:

```bash
jupyter notebook
```

You should then see some text printed to screen, and a tab should open up in your web-browser.
