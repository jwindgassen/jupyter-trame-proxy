#!/bin/bash
# ================================================================
#  Launches ParaView trame after loading the required Modules
# 
#  Usage: launch_trame.sh PORT [args]
# ================================================================

# If you need to modify the envoronment before you launch pv_visualizer, do it here!
# Example:
# module purge
# module load Stages/2022
# module load GCC
# module load ParaStationMPI
# module load trame
# module load ParaView/5.10.1-EGL

# Pop Port from the Arguments
port=$1
shift

python -c "from pv_visualizer.app.main import main; main(port=$port, open_browser=False, timeout=0)" "$@"
