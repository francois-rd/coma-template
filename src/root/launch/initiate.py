import logging

import coma

from ..io import logging as log


@coma.hooks.hook
def pre_config_hook(known_args):
    """This pre-config hook set the global default logging level."""
    log.DEFAULT_LEVEL = getattr(logging, known_args.log_level.upper())


@coma.hooks.hook
def pre_run_hook(known_args):
    """This pre-run hook exists early. Useful for debugging init hooks."""
    if known_args.dry_run:
        print("Dry run.")
        quit()


def init():
    """Initiate Coma with application-specific non-default hooks and configs."""
    # ===== 1. Create any additional hooks. =====

    # Parser hook for flagging a dry run.
    dry_run_hook = coma.hooks.parser_hook.factory(
        "--dry-run",
        action="store_true",
        help="exit during pre-run",
    )
    logging_level_hook = coma.hooks.parser_hook.factory(
        "--log-level",
        default="info",
        choices=["debug", "info", "warning", "error", "critical"],
        help="set the default global log level",
    )

    # ===== 2. Initialize. =====

    coma.initiate(
        # Add the dry run parser hook.
        parser_hook=coma.hooks.sequence(
            coma.hooks.parser_hook.default,
            dry_run_hook,
            logging_level_hook,
        ),
        # Add the logging level hook.
        pre_config_hook=pre_config_hook,
        # Add the dry run hook.
        pre_run_hook=pre_run_hook,
    )
