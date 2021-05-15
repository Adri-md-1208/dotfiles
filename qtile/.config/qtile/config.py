# QTILE CONFIG
#
# @Adri-md-1208
# adri.md.2001@gmail.com
# 2021

from typing import List
from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os
import socket

mod = "mod4"
terminal = "alacritty"
menu = "rofi -show drun"

#######################################
#   KEYS                              #
#######################################

keys = [

    # Switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),

    # Move between windows
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows (Columns mode)
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),

    # Grow windows (XMonad mode)
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Spawn apps
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "r", lazy.spawn(menu)),

    # Toggle between layouts 
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    # Qtile options
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),

]

#######################################
#   GROUPS                            #
#######################################

group_list = ['DEV', 'WWW', 'MUS', 'VID', 'DOC', 'SYS', 'PY3', 'JAVA']
groups = [Group(name) for name in group_list]

for i, group in enumerate(groups):
    keys.extend([
        Key([mod], str(i+1), lazy.group[group.name].toscreen()),
        Key([mod, "shift"], str(i+1), lazy.window.togroup(group.name)),
    ])

#######################################
#   COLORS                            #
#######################################

dracula = {
    'Background': '#282a36',
    'Foreground': '#f8f8f2',
    'Inactive':   '#6272a4',
    'Cyan':       '#8be9fd',
    'Green':      '#50fa7b',
    'Orange':     '#ffb86c',
    'Pink':       '#ff79c6',
    'Purple':     '#bd93f9',
    'Red':        '#ff5555',
    'Yellow':     '#f1fa8c',
    'Background2':'#44475a'
    }


#######################################
#   LAYOUTS                           #
#######################################

layouts_conf = {
    'border_focus': dracula['Cyan'],
    'border_width': 2,
    'margin': 10
    }

layouts = [
      layout.MonadTall(**layouts_conf),
      layout.MonadWide(**layouts_conf),
      layout.Max(**layouts_conf),
    # layout.Columns(),
    # layout.Stack(),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    ]

#######################################
#   WIDGETS                           #
#######################################

widget_defaults = {
    'font': 'Caskaydia Cove Nerd Font',
    'fontsize': 15,
    'padding': 4
    }
extension_defaults = widget_defaults.copy()

def base(fg='Foreground', bg='Background'): 
    return {
        'foreground': dracula[fg],
        'background': dracula[bg]
        }

def separator():
    return widget.Sep(
            **base(),
            linewidth=0,
            padding=10
            )
    
def pipe():
    return widget.TextBox(
            **base(fg='Inactive'),
            text='|'
            )

def icon(fg='Foreground', bg='Background', fontsize=18, text="?"):
    return widget.TextBox(
         **base(fg, bg),
         fontsize=fontsize,
         text=text,
         )

#######################################
#   SCREENS                           #
#######################################

screens = [
    Screen(
        top=bar.Bar(
            [
                separator(),
                #icon(text='  ', fg='Cyan'),
                #separator(),
                widget.GroupBox(
                    **base(),
                    margin_y = 5,
                    margin_x = 0,
                    active=dracula['Cyan'],
                    inactive=dracula['Inactive'],
                    highlight_method='block',
                    rounded=False,
                    highlight_color=dracula['Background'],
                    this_current_screen_border=dracula['Background2'],
                    borderwidth=2
                    ),
                widget.Spacer(
                    **base(),
                    ),
                widget.Cmus(
                    **base(),
                    ),
                icon(
                    text='  ',
                    fg='Inactive'
                    ),
                widget.CheckUpdates(
                    background=dracula['Background'],
                    colour_have_updates=dracula['Cyan'],
                    colour_no_updates=dracula['Inactive'],
                    display_format='{updates}',
                    distro='Arch',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                    update_interval=1800,
                    no_update_string='0'
                    ),
                pipe(),
                icon(
                    text='  ',
                    fg='Green'
                    ),
                widget.Memory(
                    **base(fg='Green'),
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                    padding = 5
                    ),
                pipe(),
                icon(
                    text='  ',
                    fg='Orange'
                    ),
                widget.CPU(
                    **base(fg='Orange'),
                    format='{freq_current}GHz {load_percent}%',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
                    ),
                pipe(),
                icon(
                    text='  ',
                    fg='Red'
                    ),
                widget.Net(
                    **base(fg='Red'),
                    interface="enp0s20f0u3u4",
                    format='{interface}',
                    padding=5,
                    update_interval=1
                    ),
                pipe(),
                icon(
                    text=' 盛 ',
                    fg='Purple'
                    ),
                widget.Backlight(
                    **base(fg='Purple'),
                    backlight_name='intel_backlight',
                    format='{percent:2.0%}',
                    ),
                pipe(),
                icon(
                    text=' 墳',
                    fg='Pink'
                    ),
                widget.Volume(
                    **base(fg='Pink'),
                    padding=5
                    ),
                pipe(),
                widget.CurrentLayoutIcon(
                    **base(),
                    scale=0.5
                    ),
                pipe(),
                widget.Systray(
                    **base(), 
                    padding=5
                    ),
                separator(),
                widget.Clock(
                    **base(fg='Yellow'), 
                    format='[%d/%m - %H:%M]'
                    ),
                separator()
            ],
            28,
        ),
    ),
]

#######################################
#   MOUSE                             #
#######################################

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#######################################
#   OTHERS                            #
#######################################

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
