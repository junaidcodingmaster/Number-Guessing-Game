#      _                   _     _      _
#     | |_   _ _ __   __ _(_) __| |    / \   _ __  _ __  ___ 
#  _  | | | | | '_ \ / _` | |/ _` |   / _ \ | '_ \| '_ \/ __|
# | |_| | |_| | | | | (_| | | (_| |  / ___ \| |_) | |_) \__ \
#  \___/ \__,_|_| |_|\__,_|_|\__,_| /_/   \_\ .__/| .__/|___/
#                                           |_|   |_|
# By Junaid

clear

python logo.py

echo
echo "Installing Dependencies of this game ..."
echo

# Dependencies
pip install pyfiglet
pip install simple_chalk
pip install datetime


echo
echo "Dependencies are installed."
echo "You are ready to GO!"
echo

# deleting installation files 
rm -rf logo.py
rm -rf install.sh

echo -e "Default \e[33mThis Game will works best in CMD."
echo "To start game type : (In CMD only)"
echo "___________________________________"
echo
echo "==> python NumberGuessingGame.py"
echo "___________________________________"
start python NumberGuessingGame.py