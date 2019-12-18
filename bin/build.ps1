$base = $PSScriptRoot + "\..";
$venvdir = $base + '\venv';

$installcmd = "& '" + $venvdir + "\Scripts\pyinstaller.exe' -F -n normalizer " + $base + "\app\app.py --hidden-import=queue --paths=" + $base + "\app --onefile";
Invoke-Expression $installcmd;
