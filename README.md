# Virtual Environments and requirements.txt 

A virtual environment is an *isolated* environment for your Python project. Using virtual environments ensures that your projects are leveraging all necessary Python packages - and necessary versions of those packages - to keep your code function as designed. You should *always* create virtual environments for your projects. If you don't, all your projects will use the same packages and versions installed globally for your projects. 

Why is this important? Consider a scenario where you have two projects, both which depend on different versions of a Python package installed on your system. The first project relies on v1.0 of that package, which includes functions that have been deprecated in v2.0; the second project relies on v2.0, which includes functions not available in v1.0. If you update the globally installed package on your system from v1.0 to v2.0, you will break the first project. 

Using virtual environments allows you to run *both versions of a package in isolation from one another* to ensure both of your projects continue to function as designed. It's like having a walled garden for each project you create. 

In addition to using virtual environments to ensure your code continues to function as designed *for you*, you should create requirements.txt files to ensure that all the necessary Python packages - and necessary versions of those packages - are documented *for others* to ensure reproducibility. A requirements.txt file will keep track of all the Python packages and versions you have installed and used in your project (see example in this repo). 

If you include a requirements.txt file with your project code, someone can create a virtual environment, clone your project into it, install all the necessary packages and versions using the requirements.txt file, and reproduce your project as it was designed. If you ae using Git for version control, you can include an updated requirements.txt file with each commit to ensure that each version of your code functions as designed at the time. 

Ok. You're convinced. So how do you create a virtual environment and requirements.txt file?

### Creating a virtual environment





* Prior to each commit, you should 're-freeze' your requirements.txt file to ensure that it's updated to account for new packages that were loaded (or old packages that were removed) since the most recent commit. 

* Don't commit your virtual environment folder (env) to Github. If you use the command line for Github commits [create a .gitignore file](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files).
