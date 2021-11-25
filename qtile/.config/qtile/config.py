# QTILE CONFIG
#
# @Adri-md-1208
# adri.md.2001@gmail.com
# 2021


from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os
import subprocess

mod = "mod4"
terminal = "alacritty"
menu = "rofi -show drun -theme ~/dotfiles/rofi/.config/rofi/themes/apps.rasi"
browser = "firefox"
music_player = "spotify"
video_player = "vlc"
resources = "stacer"
network = "nm-connection-editor"
doc_reader = "zathura"
aur = "yay"
notes = "simplenote"
mail = "thunderbird"

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
    Key([mod], "f", lazy.spawn(browser)),
    Key([mod], "s", lazy.spawn(music_player)),
    Key([mod], "v", lazy.spawn(video_player)),
    Key([mod], "p", lazy.spawn(doc_reader)),
    Key([mod], "n", lazy.spawn(notes)),
    Key([mod, "shift"], "m", lazy.spawn(mail)),

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

group_list = ['DEV', 'WEB', 'MUS', 'VID', 'DOC', 'SYS']
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
    'Background':  '#282a36',
    'Foreground':  '#f8f8f2',
    'Inactive':    '#6272a4',
    'Blue':        '#8be9fd',
    'Green':       '#50fa7b',
    'Orange':      '#ffb86c',
    'Pink':        '#ff79c6',
    'Purple':      '#bd93f9',
    'Red':         '#ff5555',
    'Yellow':      '#f1fa8c',
    'Background2': '#44475a',
    'Salmon':      '#ff9580'
    }

gruvbox = {
    'Background':  '#282828',
    'Foreground':  '#ebdbb2',
    'Inactive':    '#a89984',
    'Blue':        '#458588',
    'Green':       '#98971a',
    'Orange':      '#fe8019',
    'Pink':        '#d3869b',
    'Purple':      '#b16286',
    'Red':         '#cc241d',
    'Yellow':      '#fabd2f',
    'Background2': '#504945',
    'Salmon':      '#8f3f71'
    }

gruvbox_bw = {
    'Background':  '#282828',
    'Foreground':  '#ebdbb2',
    'Inactive':    '#ebdbb2',
    'Blue':        '#ebdbb2',
    'Green':       '#ebdbb2',
    'Orange':      '#ebdbb2',
    'Pink':        '#ebdbb2',
    'Purple':      '#ebdbb2',
    'Red':         '#ebdbb2',
    'Yellow':      '#ebdbb2',
    'Background2': '#504945',
    'Salmon':      '#ebdbb2'
    }

gruvbox_wb = {
    'Background':  '#ebdbb2',
    'Foreground':  '#282828',
    'Inactive':    '#282828',
    'Blue':        '#282828',
    'Green':       '#282828',
    'Orange':      '#282828',
    'Pink':        '#282828',
    'Purple':      '#282828',
    'Red':         '#282828',
    'Yellow':      '#282828',
    'Background2': '#504945',
    'Salmon':      '#282828'
    }

colors = gruvbox_bw

#######################################
#   LAYOUTS                           #
#######################################

layouts_conf = {
    'border_focus': colors['Inactive'],
    'border_width': 2,
    'margin': 10
    }
layouts = [
      layout.MonadTall(**layouts_conf),
      layout.MonadWide(**layouts_conf),
      layout.Max(**layouts_conf),
      layout.Columns(
          border_width=0
          ),
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
        'foreground': colors[fg],
        'background': colors[bg]
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
                widget.GroupBox(
                    **base(),
                    margin_y=2,
                    margin_x=0,
                    active=colors['Foreground'],
                    inactive=colors['Inactive'],
                    highlight_method='block',
                    rounded=False,
                    highlight_color=colors['Background'],
                    this_current_screen_border=colors['Background2'],
                    borderwidth=2
                    ),
                widget.Spacer(
                    **base(),
                    ),
                widget.Cmus(
                    **base(),
                    ), icon(
                    text='  ',
                    fg='Inactive'
                    ),
                widget.CheckUpdates(
                    background=colors['Background'],
                    colour_have_updates=colors['Foreground'],
                    colour_no_updates=colors['Inactive'],
                    display_format='{updates}',
                    distro='Arch_checkupdates',
                    mouse_callbacks={'Button1': lambda:
                                     qtile.cmd_spawn(terminal + ' -e ' + aur)},
                    update_interval=60,
                    no_update_string='0'
                    ),
                pipe(),
                icon(
                    text='  ',
                    fg='Green'
                    ),
                widget.Memory(
                    **base(fg='Green'),
                    mouse_callbacks={'Button1': lambda:
                                     qtile.cmd_spawn(resources)},
                    padding=5
                    ),
                pipe(),
                icon(
                    text='  ',
                    fg='Orange'
                    ),
                widget.CPU(
                    **base(fg='Orange'),
                    format='{freq_current}GHz {load_percent}%',
                    mouse_callbacks={'Button1': lambda:
                                     qtile.cmd_spawn(resources)}
                    ),
                pipe(),
                icon(
                    text='  ',
                    fg='Red'
                    ),
                widget.Net(
                    **base(fg='Red'),
                    format='{down} ↓↑ {up}',
                    padding=5,
                    update_interval=1,
                    mouse_callbacks={'Button1': lambda:
                                     qtile.cmd_spawn(network)}
                    ),
                pipe(),
                icon(
                    text=' 盛 ',
                    fg='Pink'
                    ),
                widget.Backlight(
                    **base(fg='Pink'),
                    backlight_name='intel_backlight',
                    format='{percent:2.0%}',
                    ),
                pipe(),
                icon(
                    text=' 墳',
                    fg='Purple'
                    ),
                widget.Volume(
                    **base(fg='Purple'),
                    padding=5
                    ),
                pipe(),
                icon(
                    text=' ',
                    fg='Salmon'
                    ),
                widget.Battery(
                    **base(fg='Salmon'),
                    format='{percent:2.0%}'
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
                pipe(),
                widget.Clock(
                    **base(fg='Yellow'),
                    format='%d/%m %H:%M'
                    ),
                separator()
            ],
            28,

        ),
    ),
    Screen()
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
dgroups_app_rules = []
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
reconfigure_screens = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/dotfiles/qtile/.config/qtile/autostart.sh'])


wmname = "Qtile"
