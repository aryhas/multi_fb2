#bin/bash
clear
echo
echo "Menginstall Semua Yang Dibutuhkan, Sabar Boss.....!"
echo
cd $HOME
pkg update && pkg upgrade
pkg install python -y
pkg install python
pkg install git 
pip install requests bs4
python3  -m pip install requests bs4
python3 upil.py
