1. To create a project, do one of the following:
    - From the main menu, choose `File | New Project`
    - On the Welcome screen, click `New Project`
    - `New Project|Pure Python` dialog opens.
2. In the `New Project|Prue Python` dialog, specify the project `name` and its `location`. 
3. Next, click `>` Expand the node to expand the `Python Interpreter` node, and select the new environment or existing interpreter, by clicking the corresponding radio-button.
    - `New environment` using: if this option has been selected, choose the tool to be used to create a virtual environment. To do that, click the list and choose `Virtualenv, Pipenv, Poetry, or Conda`.
      - Next, specify the `Location` and `Base interpreter` of the new virtual environment.When configuring the `base interpreter`, you need to specify the path to the Python executable. If PyCharm detects no Python on your machine, it provides two options: to download the latest Python versions from python.org or to specify a path to the Python executable (in case of non-standard installation).
      - Select the `Inherit global site-packages` checkbox if you want that all packages installed in the global Python on your machine to be added to the virtual environment you're going to create. This checkbox corresponds to the `--system-site-packages` option of the virtualenv tool.
      - Select the `Make available to all projects` checkbox if you want to reuse this environment when creating Python interpreters in PyCharm.
   
    - `Previously configured interpreter`: if this option has been selected, choose the desired interpreter from the list, or (if the desired interpreter is not found), click Open and choose the interpreter. 

    - `Create a main.py welcome script`: keep this option selected if you want PyCharm to add the `main.py` file to your project. This file contains a very simple Python code sample and can be a starting point of your project.




