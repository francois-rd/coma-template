# coma-template

Simple template for [coma](https://github.com/francois-rd/coma/)-based programs.

*NOTE: This template is designed to speed up project creation based on
[my](https://github.com/francois-rd/) own workflow. I encourage others to find
use out of it, but the template has no allusions of being universal.*

## Features

Most of the features are design decisions driven by ``coma>=3.0.1``:

* Module structure enabling a fluid "command-from-components" design pattern.
* Simple [.bashrc](bashrc.bash) file template and directory structure for
  quick-launching commands using a ``launch`` command.
* Singleton for all path logic.

The remaining features include common utilities in my projects:

* Fairly comprehensive data loading and saving solution, including JSON, JSON-L, CSV,
  ``dataclasses``, and plain text.
* Basic utilities such as string scrubbing and instantiating ``Enum`` from strings.
* Simple [logging](https://docs.python.org/3/library/logging.html) factory.

## Usage

The repository isn't set up as a GitHub Template because it is meant to be
modified on a per-project basis. The recommended minimum modifications are:

* Rename [src/root](src/root) to ``src/<meaningful-name-for-your-project>``.
    * This also affects the ``import`` statement in [main.py](src/main.py).
* Use [@coma.command](https://coma.readthedocs.io/en/latest/tutorials/command.html) in
  submodules of the [commands](src/root/launch/commands) module. Any commands there
  will automagically be registered. Commands can be declared elsewhere, but you will
  need to import them manually.
* If encountering the PyCharm ``PYTHONPATH`` bug, uncomment the relevant line in
  [bashrc.bash](bashrc.bash).

Additional recommended (but not as strongly required) include:

* Add paths to all important files and directories in the
  [PathConfig](src/root/io/path.py) singleton.
* Whenever a new command is created, register it with Terminal auto-complete in
  [bashrc.bash](bashrc.bash).

*NOTE: Remember to run ``source bashrc.bash`` every time a new Terminal is open
and to re-run it in every open Terminal every time [bashrc.bash](bashrc.bash)
is modified.*

## Requirements

The included [requirements.txt](requirements.txt) is purposefully lightweight,
but includes a commented out reference to ``pandas`` which is required for the
``load_records_csv()`` function found [here](src/root/io/data.py).
