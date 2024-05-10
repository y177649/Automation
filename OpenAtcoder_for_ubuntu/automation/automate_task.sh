#!/bin/bash

# ステップ1：Seleniumスクリプトをバックグラウンドで実行
python3 ~/code/Automation/OpenAtcoder_for_ubuntu/automation/browser_automation.py &

# ステップ2：gnome-terminalで指定ディレクトリを開く
gnome-terminal --working-directory="$HOME/code/Atcoder/nabc"
