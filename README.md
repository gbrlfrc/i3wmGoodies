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
In order to enable network interface just run: `python network.py arg`</br>
* __-n, --new__: scan for nerby wifi networks and connect to it (wifi network interface with: `ip link`)</br>
* __-c, --connect__: enable network interface and connect to a saved network<br>

About vim PlugIn you need to add VimPlug: <br>
`curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
 https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim`<br>
 <br>
 Once edited the __.vimrc__ file, from vim compile it with: `:source %` and install plugIn with `:PlugInstall`.<br>
 __YouCompleteMe__ extension require manual installation, from terminal just run:<br>
 `./~/.vim/plugged/YouCompleteMe/install.py`.
 <br><br>
 Finally to let __UndoTree__ plugIn loads buffer jsut run:<br>
 `mkdir ~/.vim/undodir`
 
## requirements
`pip install -r requirements.txt`
