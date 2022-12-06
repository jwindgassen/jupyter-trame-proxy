import os
import secrets
from tempfile import mkstemp
import logging


logger = logging.getLogger(__name__)
logger.setLevel("INFO")

HERE = os.path.dirname(os.path.abspath(__file__))


def _trame_mappath(path):
    # Append authKey to URL if we are at the base-url
    if path in ("/", "/index.html"):
        path += f"?secret={_auth_key}"

    return path


def setup_trame():
    # Generate authKey
    global _auth_key
    _auth_key = secrets.token_urlsafe(32)

    # Write authKey to tempfile
    tempfile, temppath = mkstemp()
    logger.info(f"Created tempfile with secure password for trame at {temppath}")

    with open(tempfile, "w") as file:
        file.write(_auth_key)

    # Create command
    cmd = [
        os.path.join(HERE, "share/launch_trame.sh"),
        "{port}",
        "--authKeyFile",
        temppath,
    ]

    logger.info(f"jupyter-trame-proxy command: {' '.join(cmd)}")

    return {
        "command": cmd,
        "mappath": _trame_mappath,
        "absolute_url": False,
        "timeout": 90,
        "new_browser_tab": True,
        "launcher_entry": {
            "enabled": True,
            "icon_path": os.path.join(HERE, "icons/logo.svg"),
            "title": "ParaView trame",
        },
    }
