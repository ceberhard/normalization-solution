# Normalization Problem Solution
A work sample solution to the Truss Software Engineering interview problem.

## Running Solution

### Compiled Distribution
I've included a compiled version of the utility (using the pyinstaller library) for running on Linux:
`normalizer\normalizer.tar.gz`

After extraction, go ahead and run the utility: `normalizer <input file path> <output file path>`

Running `normalizer -h` will get you some minor usage doc (included with the python argparse library).

### Development Mode - Windows
The solution was written using Python 3.6.4 on a dev box running Windows 10. It uses a couple external libraries (see [requirements.txt](requirements.txt)), so a virtual environment should be setup to run the solution in development mode.

Please run the following commands in Powershell (for Windows):
`.\bin\setup-venv.ps1`

This creates the virtual environment and `pip installs` the required libraries. Please make sure the PYTHON_PATH environment variable is set to your Python3 executable.

Running `.\bin\run-app.ps1` in Powershell will execute the application using the virtual environment. This is easier than remembering to activate the virtual env before running, though I haven't figured out how to interactively debug in VS Code using this shortcut script.

### Development Mode - Linux
I've included bash scripts for setting up a virtual environment and building the compiled normalizer utility:
`bin/setup-venv.sh`
`bin/build.sh`

## Regards
Thank you so much for taking the time to review my submission.

Chris Eberhard