#!/bin/bash

# If you need to modify the envoronment before you launch pv_visualizer, do it here!

# Example:
# module purge
# module load Stages/2022
# module load GCC
# module load ParaStationMPI
# module load trame
# module load ParaView/5.10.1-EGL

python -c "from pv_visualizer.app.main import main; main(port=$1, no_http=True)"
