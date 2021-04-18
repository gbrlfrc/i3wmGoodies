# i3wmGoodies
Standard configuration file for i3wm tiling window manager

# setup
The `config` file contains all shortcuts and hotkeys in order to manage i3wm wrkospaces and container navigations. Just add it in </br>
`~/.config/i3/` direcotry
</br></br>
`.xinit` file takes care of the i3wwm startup, managing wallpaper and keyboard language. Add it in your home directory.
</br></br>
`network.py` is a simple python script to scan and connect to nearby network via wpa_supplicant module

# usage
`# python network.py arg`</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-n, --new`: scan for nerby wifi networks and connect to it (wifi network interface with: `$ ip link`)</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-c, --connect`: enable network interface and connect to a saved network

## requirements
`pip install -r requirements.txt`
