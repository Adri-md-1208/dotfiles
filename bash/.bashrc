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
export PS1="\n\[\e[01;31m\][\[\e[0m\]\[\e[01;33m\]\u\[\e[0m\]\[\e[01;32m\]@\[\e[0m\]\[\e[01;34m\]\h\[\e[0m\] \[\e[01;35m\]\w\[\e[0m\]\[\e[01;31m\]]\[\e[0m\] " 
export ANDROID_HOME="$HOME/Android/Sdk"
export ANDROID_SDK_ROOT="$HOME/Android/Sdk"

# ALIAS
# Config files
alias cdd="cd ~/dotfiles"
alias cdw="cd ~/Downloads"
alias vv="vim ~/dotfiles/vim/.vimrc"
alias vz="vim ~/dotfiles/zsh/.zshrc"
alias vx="vim ~/dotfiles/.Xresources"
alias vq="vim ~/dotfiles/qtile/.config/qtile/config.py"
alias va="vim ~/dotfiles/alacritty/.config/alacritty/alacritty.toml"
alias vb="vim ~/.bashrc"
# Terminal 
alias files="ranger"
alias sd="sudo shutdown"
# Exa
alias ls='exa -la --icons --color=always --group-directories-first'
alias la='exa -a --color=always --group-directories-first'
alias ll='exa -l --color=always --group-directories-first'
alias l.='exa -a | egrep "^\."'
alias l='exa -la --icons --color=always --group-directories-first'
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
# Git
alias gss="git status --short"
alias gp="git push"
alias gcm="git commit -m"
alias ga="git add"
alias gd="git diff @{upstream}"

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
