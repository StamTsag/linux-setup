from json import dumps
from typing import Dict

# Helpful apps many linux uses tend to use
utilities: Dict[str, str] = {

'Brave': {

'ubuntu': 
"""sudo apt install apt-transport-https curl
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install brave-browser"""},

'Wine': {

'ubuntu':
"""sudo apt install wine"""},

}

# Common bloatware
bloatware: Dict[str, str] = {

'ubuntu': {

# Gnome Mahjongg
'Gnome Mahjongg': 'gnome-mahjongg',
'Gnome Mines': 'gnome-mines',
'Gnome Sudoku': 'gnome-sudoku'

}}

def main():
    with open('pkgs.json', 'w') as f:
        f.write(dumps(dict(utilities=utilities, bloatware=bloatware), indent=4))

if __name__ == '__main__':
    main()
    