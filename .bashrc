# BASH CONFIG
#
# @Adri-md-1208
# adri.md.2001@gmail.com
# 2021

# EXPORTS
export PATH=$HOME/bin:/usr/local/bin/:$PATH
export MANPATH="/usr/local/man:$MANPATH"
export LANG=en_US.UTF-8
export EDITOR='vim'
export MANPAGER='/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist norelativenumber nonu noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"'

# ALIAS
# Config files
alias cdd="cd ~/dotfiles"
alias vv="vim ~/dotfiles/.vimrc"
alias vz="vim ~/dotfiles/.zshrc"
alias vx="vim ~/dotfiles/.Xresources"
alias vq="vim ~/dotfiles/qtile/.config/qtile/config.py"
alias va="vim ~/dotfiles/alacritty/.config/alacritty/alacritty.yml"
alias vi3="vim ~/.config/i3/config"
alias vb="vim ~/.bashrc"
# Terminal 
alias e="exit"
alias c="clear"
alias files="ranger"
alias sd="shutdown"
# Exa
alias ls='exa -la --icons --color=always --group-directories-first'
alias la='exa -a --color=always --group-directories-first'
alias ll='exa -l --color=always --group-directories-first'
alias l.='exa -a | egrep "^\."'
alias l=ls
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
alias pcs="pokemon-colorscripts -r"

# HSTR configuration
alias hh=hstr                    # hh to be alias for hstr
export HSTR_CONFIG=hicolor       # get more colors
shopt -s histappend              # append new history items to .bash_history
export HISTCONTROL=ignorespace   # leading space hides commands from history
export HISTFILESIZE=10000        # increase history file size (default is 500)
export HISTSIZE=${HISTFILESIZE}  # increase history size (default is 500)
# ensure synchronization between bash memory and history file
export PROMPT_COMMAND="history -a; history -n; ${PROMPT_COMMAND}"
# if this is interactive shell, then bind hstr to Ctrl-r (for Vi mode check doc)
if [[ $- =~ .*i.* ]]; then bind '"\C-r": "\C-a hstr -- \C-j"'; fi
# if this is interactive shell, then bind 'kill last command' to Ctrl-x k
if [[ $- =~ .*i.* ]]; then bind '"\C-xk": "\C-a hstr -k \C-j"'; fi

# Start bash
pokemon-colorscripts -r 1-4


