
Get-ExecutionPolicy

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

$index = 'C:\Users\pylere\Programming\NC_CoalAshLocator\index.html'

$F = 'C:\Users\pylere\AppData\Local\atom\atom.exe'

echo $F

echo $index

& $F $index

echo 'working...'
