#!/bin/bash

# ステップ1：xdg-openでWebサイトを開く
xdg-open "https://kenkoooo.com/atcoder/#/table/"

# ステップ2：Seleniumスクリプトをバックグラウンドで実行
python3 /path/to/project-root/automation/browser_automation.py &

# ステップ3：ディレクトリに移動してVS Codeで開く
code ~/code/Atcoder/nabc
