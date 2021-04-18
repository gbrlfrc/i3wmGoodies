#!/bin/sh
#this file is executed at login time

#set keybopard language
setxkbmap it
#use feh to set wallpaper
feh --bg-scale ~/Immagini/wall/wall_main.jpg

dbus-update-activation-environment --systemd DISPLAY
eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
export SSH_AUTH_SOCK

#run i3wm manager
exec i3
