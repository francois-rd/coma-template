import os

import coma

from .initiate import init


def register():
    """Registers any commands not decorated with '@coma.command' with Coma."""
    coma.register("test.launch", lambda: print("Successfully launched."))
    # Add additional calls to 'coma.register()' here.


def launch():
    """Launches the application with Coma."""
    init()
    register()
    try:
        coma.wake()
    except coma.WakeException as e:
        if any("command line" in arg for arg in e.args):
            os.chdir(os.environ["COMA_DEFAULT_CONFIG_DIR"])
            coma.wake(args=[os.environ["COMA_DEFAULT_COMMAND"]])
        else:
            raise
