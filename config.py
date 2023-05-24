from libqtile import hook
from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from libqtile import layout, bar
import os

# Definir variables de colores
colors = {
    'foreground': '#ffffff',
    'background': '#000000',
    'highlight': '#ff0000',
    'blue': '#0000ff',
    'green': '#00ff00',
}

# Definir teclas
keys = [
    # Moverse entre ventanas
    Key(['mod4'], 'k', lazy.layout.down()),
    Key(['mod4'], 'j', lazy.layout.up()),
    Key(['mod4'], 'h', lazy.layout.left()),
    Key(['mod4'], 'l', lazy.layout.right()),
    
    # Abrir terminal (Kitty)
    Key(['mod4'], 'Return', lazy.spawn('kitty')),
    
    # Abrir el menú Rofi
    Key(['mod4'], 'r', lazy.spawn('rofi -show drun')),
    
    # Cambiar el fondo de pantalla y transparencia
    Key(['mod4'], 'b', lazy.spawn('nitrogen --set-zoom-fill --random ~/Pictures/Wallpapers')),
    Key(['mod4'], 't', lazy.spawn('picom-trans -d 50')),
]

# Definir grupos de ventanas
groups = [
    Group('1', label='1'),
    Group('2', label='2'),
    Group('3', label='3'),
    Group('4', label='4'),
    Group('5', label='5'),
]

# Estilo de la barra y widgets
widget_defaults = dict(
    font='Arial',
    fontsize=12,
    padding=3,
    background=colors['background'],
    foreground=colors['foreground'],
)
widget_defaults_kitty = widget_defaults.copy()
widget_defaults_kitty.update(fontsize=14, foreground=colors['blue'])

extension_defaults = widget_defaults.copy()

# Configuración de la barra
screens = [
    bar.Bar(
        [
            # Botón para iniciar Rofi
            widget.TextBox(
                text='',
                foreground=colors['foreground'],
                background=colors['background'],
                fontsize=18,
                padding=0,
                mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('rofi -show drun')}
            ),
            widget.TextBox(text='Qtile', name='qtile-logo', fontsize=18, foreground=colors['green']),
        ],
        20,  # Tamaño de la barra
        background=colors['background'],
    ),
]

# Configuración de Qtile
@hook.subscribe.startup_once
def autostart():
    # Ejecutar comandos al iniciar Qtile
    os.system('nitrogen --restore')  # Restaurar fondo de pantalla
    os.system('picom &')  # Iniciar picom para transparencia

# Reglas de ventanas
def init_layout():
    return [
        Match(wm_class='kitty'),  # Aplicar regla a la terminal kitty
    ]

# Configuración de Qtile
config = {
    'keys': keys,
    'groups': groups,
    'widget_defaults': widget_defaults,
    'screens': screens,
    'mouse': [],
    'layouts': [],
    'floating_layout': layout.Floating(float_rules=init_layout()),
}

# Iniciar
from libqtile import manager

if __name__ == '__main__':
    manager.init(**config)
