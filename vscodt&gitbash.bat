@echo off

:: Pythonスクリプトをバックグラウンドで実行
start /B python C:\code\automation\auto-atcoder.py

:: VS Codeで特定のフォルダを開く
start /B code C:\code\atcoder

:: Git Bashで特定のフォルダを開く
start /B "" "C:\Program Files\Git\git-bash.exe" -c "cd C:/code/atcoder && exec bash"

exit