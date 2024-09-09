#!/bin/sh

picom &
nitrogen --set-scaled --random &
xbindkeys
nm-applet &
xrandr --output HDMI1 --mode 1920x1080 --above eDP1
