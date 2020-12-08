#!/bin/sh
setxkbmap it
feh --bg-scale /home/gabriele/Immagini/wall/wall_main.jpg

dbus-update-activation-environment --systemd DISPLAY
eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
export SSH_AUTH_SOCK

exec i3
