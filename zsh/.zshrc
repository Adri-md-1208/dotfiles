# ZSH CONFIG
#
# @Adri-md-1208
# adri.md.2001@gmail.com
# 2021

# EXPORTS
export DOTNET_ROOT=$HOME/dotnet
export PATH=$HOME/bin:/usr/local/bin/:$PATH:$DOTNET_ROOT
export ZSH="/home/adrian/.oh-my-zsh"
export SHELL="/usr/bin/zsh"
export MANPATH="/usr/local/man:$MANPATH"
export LANG=en_US.UTF-8
export EDITOR='vim'
export UPDATE_ZSH_DAYS=7

# THEME
ZSH_THEME="spaceship"

# PLUGINS
plugins=(git
  	 zsh-autosuggestions)

# SOURCE
source $ZSH/oh-my-zsh.sh

# ALIAS
# Config files
alias cdd="cd ~/dotfiles"
alias vv="vim ~/dotfiles/vim/.vimrc" alias vz="vim ~/dotfiles/zsh/.zshrc"
alias vq="vim ~/dotfiles/qtile/.config/qtile/config.py"
alias va="vim ~/dotfiles/alacritty/.config/alacritty/alacritty.yml"
# Terminal 
alias e="exit"
alias c="clear"
alias files="ranger"
alias sd="shutdown"
# Exa
alias ls='exa -la --color=always --group-directories-first'
alias la='exa -a --color=always --group-directories-first'
alias ll='exa -l --color=always --group-directories-first'
alias l.='exa -a | egrep "^\."'
# Python
alias p="python"
alias py="python"
alias py3="python3"
alias py2="python2"
# System
alias update="sudo pacman -Syu"
# Shell scripts
alias nf="neofetch"
alias pf="pfetch"
alias cs="colorscript random"

# Start zsh

