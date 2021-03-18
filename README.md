# Paypr

## Auto create wallpapers from images that aren't 16:9

Built with Python

This repository uses Python 3.8.5 and [pytest](https://pytest.org) as the testing framework.

## Installing Locally outside of the virtual environment

If you wish to just use this package without changing the code, there are only a couple of steps.

**Requirement**: You must have Python 3.8^ installed, I have not tested on anything less

1. Clone git repo locally
2. In a terminal navigate to the root folder of the repo
3. Enter `pip install .` into the terminal and let the install complete
4. User `paypr` command anywhere

---

## Usage Instructions

This project was tested on Linux and macOS only (**_NOTE: On my MacBook, I had to use `$ python3` and `$ pip3` to get the correct versions as Python 2 is preinstalled_**), the process for virtualenv is [a little different for Windows](https://python.land/virtual-environments/virtualenv).

Open a terminal window and navigate to the root folder of this project

```bash
$ cd /path/to/root/paypr
```

Virtualenv is required with Python 3.6, if you do not have virtualenv installed, run this command:

```bash
$ pip install -U virtualenv
```

_Note: if you have Python 2 and Python 3 installed, you may need to use `pip3` instead or enter the command like `$ python3.8 -m pip install -U virtualenv`_

With virtualenv installed, create a virtualenv while remaining in the root folder:

```bash
$ virtualenv venv
```

Activate virtualenv:

```bash
$ source /venv/bin/activate
```

Then install needed packages:

```bash
(venv) $ pip install -r requirements.txt
(venv) $ pip install -e .
```

_The second command installs the local package, allowing use with the `paypr` CLI while in the virtualenv._

After that you should be able to run the main.py file `(venv) $ paypr` or run tests `(venv) $ pytest`.

> _Note: As of 1.0 release, testing is lacking. Pull Requests are encouraged, just use [black](https://pypi.org/project/black/) before submitting._

With the Paypr CLI, you can use the following flags:

- `--help` -- Will pull up a well formatted listing of all of the flags
- `-i`, `--input TEXT` - The input file, must be an image. [required]
- `-s`, `--size [HD|FHD|WUXGA|QHD|2K|UHD|4K|5K]` -- The output size for the wallpaper. Format options are HD, FHD, WUXGA, QHD, 2K, UHD, 4K, and 5K

Any of the two flags not accounted for will receive a prompt to enter the value.

When done, exit the virtualenv with:

```bash
(venv) $ deactivate
```
