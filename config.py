from libqtile import hook, layout
from libqtile.config import Key, Group
from libqtile.command import lazy
from libqtile.widget import TextBox
from libqtile import bar
import os

# Definir variables de colores
colors = {
    'foreground': '#ffffff',
    'background': '#000000',
    'highlight': '#ff0000'
}

# Definir teclas
keys = [
    # Moverse entre ventanas
    Key(['mod4'], 'k', lazy.layout.down()),
    Key(['mod4'], 'j', lazy.layout.up()),
    Key(['mod4'], 'h', lazy.layout.left()),
    Key(['mod4'], 'l', lazy.layout.right()),
    
    # Abrir terminal
    Key(['mod4'], 'Return', lazy.spawn('kitty')),
    
    # Abrir el menú Rofi
    Key(['mod4'], 'm', lazy.spawn('rofi -show drun')),
    
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

# Estilo de la barra
widget_defaults = dict(
    font='Arial',
    fontsize=12,
    padding=3,
    background=colors['background'],
    foreground=colors['foreground'],
)

extension_defaults = widget_defaults.copy()

# Configuración de la barra
screens = [
    bar.Bar(
        [
            TextBox(text='Qtile', name='qtile-logo'),
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
        layout.Rule(
            Match(wm_class='kitty'),  # Aplicar regla a la terminal kitty
            float=True,
        ),
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

# Iniciar Qtile
def main(qtile):
    qtile.cmd_launch()
