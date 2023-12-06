#import matplotlib
#print(matplotlib.__file__)


import matplotlib.font_manager

# Obtener la lista de fuentes disponibles
font_list = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='otf')

# Imprimir la lista de fuentes
for font in font_list:
    print(font)


#import matplotlib
#matplotlib.font_manager._rebuild()

#import  matplotlib.font_manager
#flist = matplotlib.font_manager.get_fontconfig_fonts()
#names = [matplotlib.font_manager.FontProperties(fname=fname).get_name() for fname in flist]
#print(names)
