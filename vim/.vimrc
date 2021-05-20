set number
set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax enable
set showcmd
set ruler
set encoding=utf-8
set showmatch 
set sw=2
set relativenumber
set laststatus=2
set noshowmode

call plug#begin('~/.vim/plugged')

" Themes
Plug 'dracula/vim',{'as':'dracula'}
Plug 'morhetz/gruvbox'

" Movement
Plug 'easymotion/vim-easymotion'
Plug 'christoomey/vim-tmux-navigator'

" Files
Plug 'scrooloose/nerdtree'

call plug#end()

" Themes
colorscheme gruvbox
set background=dark
let g:gruvbox_contrast_dark = 'hard'
hi Normal guibg=NONE ctermbg=NONE

" NERDTree
let NERDTreeQuitOnOpen=1

" Keymaps
let mapleader=" "
nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>
