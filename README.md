# Virtual Environments and requirements.txt 

A virtual environment is an *isolated* environment for your Python project. Using virtual environments ensures that your projects are leveraging all necessary Python packages - and necessary versions of those packages - to keep your code function as designed. You should *always* create virtual environments for your projects. If you don't, all your projects will use the same packages and versions installed globally for your projects. 

Why is this important? Consider a scenario where you have two projects, both which depend on different versions of a Python package installed on your system. The first project relies on v1.0 of that package, which includes functions that have been deprecated in v2.0; the second project relies on v2.0, which includes functions not available in v1.0. If you update the globally installed package on your system from v1.0 to v2.0, you will break the first project. 

Using virtual environments allows you to run *both versions of a package in isolation from one another* to ensure both of your projects continue to function as designed. It's like having a walled garden for each project you create. 

In addition to using virtual environments to ensure your code continues to function as designed *for you*, you should create requirements.txt files to ensure that all the necessary Python packages - and necessary versions of those packages - are documented *for others* to ensure reproducibility. A requirements.txt file will keep track of all the Python packages and versions you have installed and used in your project (see example in this repo). 

If you include a requirements.txt file with your project code, someone can create a virtual environment, clone your project into it, install all the necessary packages and versions using the requirements.txt file, and reproduce your project as it was designed. If you ae using Git for version control, you can include an updated requirements.txt file with each commit to ensure that each version of your code functions as designed at the time. 

Ok. You're convinced. So how do you create a virtual environment and requirements.txt file?

### Creating a virtual environment

Open the command prompt (or terminal, if using a Mac) and create a new project directory called 'test-env' and change directories to work in it. 

> mkdir test-env && cd test-env

If you are using Python 3 (and you should be), the 'venv' package for creating virtual environments is included by default (Note: if you are using Python 2, you will need to [install, use and follow instructions for the 'virtualenv' package](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)). On the command prompt, enter:

> py -3 -m venv env 

(if you are using a Mac, in the terminal, enter: python3 -m venv env)

This creates a virtual environment named 'env' which you can activate for your project to install packages, write project code, etc. To activate 'env', on the command prompt, enter:

> env\Scripts\activate.bat

(if you are using a Mac, in the terminal, enter: source env/bin/activate) 

Once the environment has been activated, you should see (env) appear before the command prompt to denote that you are working in the virtual environment. 

Now you can begin installing your packages and writing code that depends on those packages, e.g. to install Pandas and NumPy: 

> (env) > pip3 install pandas numpy

These packages - and the dependencies on which they rely - will be stored in the env/Lib/site-packages path in your project directory for access in your project code.

You can now write a script (using whatever IDE you like, or a Jupyer Notebook) that leverages these packages and save it in your root project folder, e.g. the example.py script in this repository:

```
import pandas as pd
import numpy as np
data = {'Letter': ['A', 'B', 'C', 'D', 'E'], 'Number': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data) #this creates a dataframe using 'data' above containing 5 rows x 2 columns 
print(df.loc[np.random.choice(df.index, size=2)]) #randomly selects and prints 2 rows from the dataframe
```

You can now run this script on the command prompt to see that it works:

> (env) > python example.py

(Running this script should return two random rows from the dataframe in the command prompt)

### Creating a requirements.txt file

When you are ready to commit your project code to a Github repository, you can create a requirements.txt file with one simple command on the command prompt:

> (env) > pip3 freeze > requirements.txt

This will generate a requirements.txt file in the root folder of your project. 

If you open up the requirements.txt file, you will see the packages you installed - and packages on which they depend - along with the specific versions of the packages used in your project. 

Once you have created your requirements.txt file and are ready to commit your project code to Github, you can deactivate your virtual environment using the following command:

> deactivate

The (env) before the prompt should disappear to signify that you are no longer in the virtual environment. Now you can commit your project code to Github with the requirements.txt file. 

Two things to note: 

* Prior to each commit, you should 're-freeze' your requirements.txt file to ensure that it's updated to account for new packages that were loaded (or old packages that were removed) since the most recent commit. 

* Don't commit your virtual environment folder (env) to Github. If you use the command line to make Github commits [create a .gitignore file](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files) and ensure that your virtual environment is ignored when committing.

With the requirements.txt file in your Github repository, another user can now clone the repository you created, create and activate their own virtual environment, load the requirements.txt file to install the necessary packages and correct versions, and run the script to reproduce the results.

### Cloning a Repository, Creating a Virtual Environment and Loading requirements.txt

This repository contains a requirements.txt file with the packages needed (pandas, numpy and their dependencies) to run example.py file, which contains the code above in 'Creating a Virtual Environment'. Note: The steps below assume that you have Git and the Github Command Line Interface (CLI) installed on your system. If not, first download [Git](https://git-scm.com/downloads) and then [Github CLI](https://cli.github.com/) prior to executing the following commands.

To clone this repository and work in the project director, on the command prompt, enter:

> gh repo clone https://github.com/mbaldassaro/venv_requirements_demo.git && cd venv_requirements_demo

(note: the command above assumes you are using 'https' for cloning Github repositories. If you are using SSH, replace 'gh repo clone' with 'git clone')

Now create a virtual environment and activate it:

> py -3 -m venv env && env\Scripts\activate.bat

(if you are using a Mac: python3 -m venv env && source env/bin/activate)

Now install the necessary packages using the requirements.txt file:

> (env) > pip3 install -r requirements.txt

Finally, execute the example.py script to see the results:

> (env) > python example.py

If everything ran correctly, you should see two randomly selected rows from the dataframe.

That's it! Wasn't that easy? And now you know how to ensure your projects always function as you designed them using virtual environments and how others can reproduce your projects using requirements.txt files.



