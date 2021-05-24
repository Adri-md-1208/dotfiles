# ZSH CONFIG
#
# @Adri-md-1208
# adri.md.2001@gmail.com
# 2021

# EXPORTS
export PATH=$HOME/bin:/usr/local/bin:$PATH
export ZSH="/home/adrian/.oh-my-zsh"
export MANPATH="/usr/local/man:$MANPATH"
export LANG=en_US.UTF-8
export EDITOR='vim'
export UPDATE_ZSH_DAYS=7

# THEME
ZSH_THEME="spaceship"

# PLUGINS
plugins=(git)

# SOURCE
source $ZSH/oh-my-zsh.sh

# ALIAS
#
# Config files
alias cdd="cd ~/dotfiles"
alias vv="vim ~/dotfiles/vim/.vimrc"
alias vz="vim ~/dotfiles/zsh/.zshrc"
alias vq="vim ~/dotfiles/qtile/.config/qtile/config.py"
alias va="vim ~/dotfiles/alacritty/.config/alacritty/alacritty.yml"
# Terminal 
alias e="exit"
alias c="clear"
# Python
alias p="python"
alias py="python"
alias py3="python3"
alias py2="python2"
