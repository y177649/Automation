@echo off

:: VS Codeで特定のフォルダを開く
start code C:\code\atcoder

:: Git Bashで特定のフォルダを開く
start "" "C:\Program Files\Git\git-bash.exe" -c "cd C:/code/atcoder && exec bash"

exit
