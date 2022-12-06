# jupyter-trame-proxy
Integrates [trame](https://github.com/Kitware/trame) in your Jupyter environment using [ParaView Visualizer](https://github.com/Kitware/paraview-visualizer).  

## Requirements
- Python **3.9+**
- ParaView **5.10+**
- Jupyter Notebook 6.0+
- JupyterLab 2.1+

This extension will start the `pv_visualizer` package. You must make sure it is on the PYTHONPATH! Adjust [launch_trame.sh](jupyter_trame_proxy/share/launch_trame.sh) to ensure this.

## Install 

#### Create and Activate Environment
```
virtualenv -p python3 venv
source venv/bin/activate
```

#### Install jupyter-trame-proxy
```
pip install git+https://github.com/jwindgassen/jupyter-trame-proxy.git
```

#### Enable jupyter-trame-proxy Extensions
For Jupyter Classic, activate the jupyter-server-proxy extension:
```
jupyter serverextension enable --sys-prefix jupyter_server_proxy
```

For Jupyter Lab, install the @jupyterlab/server-proxy extension:
```
jupyter labextension install @jupyterlab/server-proxy
jupyter lab build
```

## Starting
Click on the *ParaView trame* icon from the Jupyter Lab Launcher or the *ParaView trame* item from the new dropdown in Jupyter Classic.  

### Jupyter-Server-Proxy
[Jupyter-Server-Proxy](https://jupyter-server-proxy.readthedocs.io) lets you run arbitrary external processes alongside your notebook and provide web access to them. After installing this proxy, you can start trame using the *ParaView trame* entry in the launcher. It will start the server (which might take a few seconds) and open the website in a new tab.

## License
This software is provided under the BSD 3-Clause
