#!/bin/bash
# DOTFILES INSTALLER
#
# @Adri-md-1208
# adri.md.2001@gmail.com
# 2022

if [ "$(id -u)" = 0 ]; then
  echo -e "\e[31mRuning this script as root may make adverse changes in your system\e[0m"
  echo -e "\e[31mPlease, run as non-root user\e[0m"
  exit 1
fi

function error_msg { 
  case "$1" in
    1)
      msg="Pacman error" 
      ;;
    *)
      msg="Unkown error"
      ;;
  esac
  printf "\e[31m\n[Error %d]\e[0m \e[33m%s\n\e[0m" "$1" "$msg" >&2
  exit 1
}

function success_msg {
  printf "\e[32m\n%s\n\e[0m" "$1"
}

function informative_msg {
  printf "\e[34m\n  %s\n\n\e[0m" "$1"
}

# UPGRADE AND SYNC PACMAN
informative_msg "Upgrading and syncing the repos of pacman"
sudo pacman --noconfirm --needed --noprogressbar --quiet -Syu 2> /dev/null ||
  error_msg 1

# INSTALL PACKAGES
sudo cat pkgs.txt | sudo pacman --needed -Sy - ||
  error_msg 1
[ -d ~/.config ] || mkdir ~/.config
