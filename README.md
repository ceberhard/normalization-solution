# Normalization Problem Solution
A work sample solution to the Truss Software Engineering interview problem.

## Running Solution

### Compiled Distribution


### Development Mode - Windows
The solution was written using Python 3.6.4 on a dev box running Windows 10. It uses a couple external libraries (see [requirements.txt](requirements.txt)), so a virtual environment should be setup to run the solution in development mode.

Please run the following commands in Powershell (for Windows):
`.\bin\setup-venv.ps1`

This creates the virtual environment and `pip installs` the required libraries. Please make sure the PYTHON_PATH environment variable is set to your Python3 executable.

Running `.\bin\run-app.ps1` in Powershell will execute the application using the virtual environment. This is easier than remembering to activate the virtual env before running, though I haven't figured out how to interactively debug in VS Code using this shortcut script.

### Development Mode - Linux
I haven't taken the time yet to port over the Bash equivalents of the utility scripts described above yet, though I have examples in other repos. If requested, I can include those scripts in this repo as well.

## Regards
Thank you so much for taking the time to review my submission.

Chris Eberhard