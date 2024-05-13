#!/bin/bash

# ステップ1：Seleniumスクリプトをバックグラウンドで実行
python3 ~/code/Automation/OpenAtcoder_for_ubuntu/automation/browser_automation.py &

# ステップ2：gnome-terminalで指定ディレクトリを開く
gnome-terminal --working-directory="$HOME/code/Atcoder/nabc" &

# 少し待ってから配置を行う
sleep 5

# ディスプレイの解像度を取得
screen_width=$(xdpyinfo | awk '/dimensions/{print $2}' | cut -d 'x' -f 1)
screen_height=$(xdpyinfo | awk '/dimensions/{print $2}' | cut -d 'x' -f 2)
half_screen_width=$((screen_width / 2))

# ターミナルウィンドウを右半分に配置（特定のウィンドウIDを使用）
terminal_id=$(wmctrl -l | grep -i "Terminal" | awk '{print $1}')
wmctrl -i -r "$terminal_id" -e 0,$half_screen_width,0,$half_screen_width,$screen_height

# ブラウザウィンドウを特定
browser_id=$(wmctrl -l | grep "AtCoder" | awk '{print $1}')

# ブラウザウィンドウを左半分に配置し、縦も最大化
wmctrl -i -r "$browser_id" -e 0,0,0,$half_screen_width,$screen_height

# ユーザーの入力を待ってターミナルを閉じないようにする
echo "Press any key to continue..."
read -n 1 -s
