$scriptpath = split-path -parent $MyInvocation.MyCommand.Definition
$venvpath = $scriptpath + '\..\venv'
$apppath = $scriptpath + '\..\app.py sampledata\sample.csv output1.csv'

$runapp = $venvpath + '\Scripts\python ' + $apppath
Invoke-Expression $runapp