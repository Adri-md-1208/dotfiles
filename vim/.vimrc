" VIM CONFIG
"
" @Adri-md-1208
" adri.md.2001@gmail.com
" 2021

set number
set mouse=a
set numberwidth=1
set clipboard=unnamedplus
set showcmd
set ruler
set encoding=utf-8
set showmatch 
set matchtime=3
set sw=2
set relativenumber
set laststatus=2
set noshowmode
set nohlsearch
syntax enable

call plug#begin('~/.vim/plugged')

" Themes
Plug 'dracula/vim',{'as':'dracula'}
Plug 'morhetz/gruvbox'

" Status bar
Plug 'itchyny/lightline.vim'
Plug 'shinchu/lightline-gruvbox.vim'

" Movement
Plug 'easymotion/vim-easymotion'
Plug 'christoomey/vim-tmux-navigator'

" Files
Plug 'scrooloose/nerdtree'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

" Autocompletion
Plug 'Valloric/YouCompleteMe'
Plug 'alvan/vim-closetag'

" Style
Plug 'ryanoasis/vim-devicons'
Plug 'ap/vim-css-color'

" Python
Plug 'nvie/vim-flake8'

" XML
Plug 'sukima/xmledit' 

" Markdown
Plug 'instant-markdown/vim-instant-markdown', {'for': 'markdown', 'do': 'yarn install'}

call plug#end()

" Themes
colorscheme gruvbox
set background=light
"let g:gruvbox_contrast_dark = 'hard'
hi Normal guibg=NONE ctermbg=NONE

" Pathogen
execute pathogen#infect()

" Airline
let g:lightline = {}
let g:lightline.colorscheme = 'gruvbox'

" NERDTree
let NERDTreeQuitOnOpen=1

" YCM
let g:ycm_autoclose_preview_window_after_completion=1

" Syntastic
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

" Web development
au BufNewFile,BufRead *.js, *.html, *.css, *.xml
    \ set tabstop=2 |
    \ set softtabstop=2 |
    \ set shiftwidth=2 |

" Keymaps
let mapleader=" "
nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>
nmap <leader>w :w<CR>
nmap <leader>q :q<CR>
nmap <leader>c ciw
nmap <leader>f :FZF<CR>
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
" Run Python code
autocmd FileType python map <buffer> <F9> :w<CR>:exec '!python3' shellescape(@%, 1)<CR>
autocmd FileType python imap <buffer> <F9> <esc>:w<CR>:exec '!python3' shellescape(@%, 1)<CR>
