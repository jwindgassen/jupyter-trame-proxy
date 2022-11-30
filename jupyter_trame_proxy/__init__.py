import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

HERE = os.path.dirname(os.path.abspath(__file__))


def _trame_mappath(path):
    return path


def setup_trame():
    """ Setup commands and and return a dictionary compatible
        with jupyter-server-proxy.
    """

    # create command
    cmd = [
        os.path.join(HERE, 'share/launch_trame.sh'), "{port}"
    ]
    
    logger.info('Command: ' + ' '.join(cmd))

    return {
        'command': cmd,
        'mappath': _trame_mappath,
        'absolute_url': False,
        'timeout': 90,
        'new_browser_tab': True,
        'launcher_entry': {
            'enabled': True,
            'icon_path': os.path.join(HERE, 'icons/logo.svg'),
            'title': 'ParaView trame',
        },
    }
