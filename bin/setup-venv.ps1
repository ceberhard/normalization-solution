$scriptpath = split-path -parent $MyInvocation.MyCommand.Definition
$venvpath = $scriptpath + '\..\venv'

if (test-path $venvpath) {
    remove-item $venvpath -recurse -force
}

$createpath = '& "' + $Env:PYTHON_PATH + '" -m venv "' + $venvpath + '"'
Invoke-Expression $createpath

$installreqs = $venvpath + '\Scripts\pip.exe --no-cache-dir install --upgrade -r .\requirements.txt'
Invoke-Expression $installreqs

echo ""
echo "---------------------------------------------------------------------------------"
echo "Virtual Environment installed... to activate the environment in your shell run:"
echo "---------------------------------------------------------------------------------"
echo ".\venv\Scripts\Activate.ps1"
echo ""