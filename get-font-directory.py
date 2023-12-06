#!/bin/python3

import matplotlib
import matplotlib.font_manager
from matplotlib.font_manager import findSystemFonts

# Imprimir todas las fuentes disponibles para Matplotlib
#print(matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf'))

# Obtener la configuración actual de la fuente
#print(matplotlib.rcParams['font.family'])


font_list = matplotlib.font_manager.findSystemFonts()
print(font_list)
