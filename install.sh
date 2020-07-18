#!/bin/bash
clear
echo
echo "\033[1;31mMenginstall Semua Yang Dibutuhkan,Sabar Bos..\033[0m"
echo
pkg update && pkg upgrade
pkg install python
pkg install git
pkg install figlet
pip install requests bs4
git clone https://github.com/aryhas/multi_mbf
cd multi_mbf
python3  -m pip install requests bs4
python3 upil.py
