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
export ZSH_THEME="spaceship"
export MANPAGER='/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist norelativenumber nonu noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"'

# PLUGINS
plugins=(git
  	 sudo
  	 zsh-autosuggestions)

# SOURCE
source $ZSH/oh-my-zsh.sh

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
setopt histignorespace           # skip cmds w/ leading space from history
export HSTR_CONFIG=hicolor       # get more colors
bindkey -s "\C-r" "\C-a hstr -- \C-j"     # bind hstr to Ctrl-r (for Vi mode check doc)


# Start zsh
pokemon-colorscripts -r 1-4


