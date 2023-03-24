# Jupyter-Notebook-Repo

This repository holds several examples of notebooks that are formatted so that the NSDF-Data-Portal can automatically serve them to the web.

## Notebook structure guidelines:
1. Visualizations must be created with Bokeh or Panel.

2. Add the following package install function to your code and use it to install all packages your code requires. Each notebook gets its own virtual environment so packages must be installed in this new environment.

def install(package_name):
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        subprocess.call(['pip3', 'install', package_name])

install('numpy')
install('bokeh')

3. Add the following code snippet to check if your notebook is being run for the web:

from bokeh.plotting import output_notebook, show, curdoc

def in_notebook():
    from IPython import get_ipython
    if get_ipython():
        return True
    else:
        return False 
    
ShowWebpage = True

if in_notebook():
    ShowWebpage = False

if ShowWebpage:
    pass
else:
    output_notebook()

4. Add the following code snippet at the end of your notebook. It determines if the notebook should serve the data visualization in line or in a web compatible way.

if ShowWebpage:
    modify_doc(curdoc())
else:
    show(modify_doc)
