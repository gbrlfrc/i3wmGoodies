# i3wmGoodies
Standard configuration file for i3wm tiling window manager and vim configuration

# setup
The `config` file contains all shortcuts and hotkeys in order to manage i3wm wrkospaces and container navigations. Just add it in </br>
`~/.config/i3/` direcotry
</br></br>
`.xinit` file takes care of the i3wwm startup, managing wallpaper and keyboard language, will be automatically loaded after login. Add this file into your `/home/$USER` direcotry 
</br></br>
`network.py` is a simple python script to scan and connect to nearby network via wpa_supplicant module
<br><br>
`.vimrc` contain some setting to make vim a bit more usable

# usage
`python network.py arg`</br>
* __-n, --new__: scan for nerby wifi networks and connect to it (wifi network interface with: `ip link`)</br>
* __-c, --connect__: enable network interface and connect to a saved network

## requirements
`pip install -r requirements.txt`
