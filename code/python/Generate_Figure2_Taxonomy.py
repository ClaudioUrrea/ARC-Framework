#!/usr/bin/env python3
# ==============================================================================
# FIGURE 2: Technology Complexity Taxonomy - ARC Framework
# ==============================================================================

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Configurar fuente Palatino Linotype
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['TeX Gyre Pagella', 'Palatino Linotype', 'Palatino', 'URW Palladio L', 'serif']
#plt.rcParams['font.serif'] = ['Palatino Linotype', 'Palatino', 'URW Palladio L', 'TeX Gyre Pagella', 'serif']
plt.rcParams['font.size'] = 16

# Datos del ARC Framework
levels = {
    'Level 1': {
        'name': 'Educational\nKits',
        'examples': 'LEGO Mindstorms,\nVEX IQ,\nMakeblock',
        'cost': r'\$300 ~ \$800',  # Escapa los $
        'effect_size': 'd = 0.59',
        'color': '#f3effa'
    },
    'Level 2': {
        'name': 'Advanced Kits',
        'examples': 'LEGO EV3,\nRaspberry Pi,\nArduino Mega',
        'cost': r'\$400 ~ \$1,200',  # Escapa los $
        'effect_size': 'd = 0.64',
        'color': '#d4ddf5'
    },
    'Level 3': {
        'name': 'Advanced\nEducational',
        'examples': 'Dobot Magician,\nEvoarm,\nNiryo One',
        'cost': r'\$2,000 ~ \$5,000',  # Escapa los $
        'effect_size': 'd = 0.68',
        'color': '#b5cbf0'
    },
    'Level 4': {
        'name': 'Didactic\nIndustrial',
        'examples': 'SCORBOT,\nKUKA youBot,\nUR3',
        'cost': r'\$8,000 ~ \$15,000',  # Escapa los $
        'effect_size': 'd = 0.73',
        'color': '#96b9ea'
    },
    'Level 5': {
        'name': 'Industrial-Grade\nSystems',
        'examples': 'UR5e, UR10e,\nKUKA LBR iiwa,\nABB IRB 1200',
        'cost': r'\$35,000 ~ \$150,000',  # Escapa los $
        'effect_size': 'd = 0.94',
        'color': '#77a7e5'
    }
}
# Crear figura
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0.28, 9.2)
ax.set_ylim(0, 11.3)
ax.axis('off')

# TÃƒÂ­tulo principal
ax.text(5, 11.3, 'ARC Framework: Technology Complexity Taxonomy', 
        ha='center', va='top', fontsize=20, fontweight='bold')

# Dibujar pirÃƒÂ¡mide (5 niveles)
y_positions = [2, 3.8, 5.6, 7.4, 9.2]
widths = [8, 7, 6, 5, 4]
heights = 1.6

for i, (level_key, level_data) in enumerate(levels.items()):
    y = y_positions[i]
    width = widths[i]
    x_center = 5
    x_left = x_center - width/2
    
    # Crear rectÃƒÂ¡ngulo con bordes redondeados
    box = FancyBboxPatch((x_left, y), width, heights,
                         boxstyle="round,pad=0.05",
                         facecolor=level_data['color'],
                         edgecolor='black',
                         linewidth=2.5,
                         alpha=0.85)
    ax.add_patch(box)
    
    # Ajustes especÃƒÂ­ficos para Level 5 para evitar superposiciÃƒÂ³n
    examples_fontsize = 14
    cost_fontsize = 14
    examples_x = x_left + 0.4
    if level_key == 'Level 5':
        examples_fontsize = 12
        cost_fontsize = 12
        examples_x = x_left + 0.3
    
    # Texto del nivel
    ax.text(x_left + 0.3, y + heights - 0.25, level_key,
           fontsize=17, fontweight='bold', color='black',
           va='top')
    
    # Nombre del nivel
    ax.text(x_center, y + heights/2 + 0.15, level_data['name'],
           ha='center', va='center', fontsize=16, 
           fontweight='bold', color='black')
    
    # Ejemplos (lado izquierdo)
    ax.text(examples_x, y + 0.15, level_data['examples'],
           fontsize=examples_fontsize, color='black', va='bottom', ha='left')
    
    # Costo (lado derecho, arriba)
    ax.text(x_left + width - 0.4, y + heights - 0.25, level_data['cost'],
           fontsize=cost_fontsize, color='black', va='top', ha='right',
           fontweight='normal')
    
    # Effect size (lado derecho, abajo)
    ax.text(x_left + width - 0.4, y + 0.15, level_data['effect_size'],
           fontsize=13, color='black', va='bottom', ha='right',
           fontweight='bold')

# Flechas indicando progresiÃƒÂ³n
for i in range(4):
    y_from = y_positions[i] + heights
    y_to = y_positions[i+1]
    ax.annotate('', xy=(5, y_to), xytext=(5, y_from),
               arrowprops=dict(arrowstyle='->', lw=3.5, color='red'))

# Etiquetas laterales
ax.text(0.5, 6, 'Increasing\nComplexity', rotation=90, 
       ha='center', va='center', fontsize=18, fontweight='bold',
       color='#333333')

ax.text(9.5, 6, 'Increasing\nEffect Size', rotation=270,
       ha='center', va='center', fontsize=18, fontweight='bold',
       color='#333333')

# Leyenda descriptiva abajo
legend_text = (
    "Effect sizes (Hedges' d) based on meta-analysis of 52 studies (2019-2025).\n"
    "Cost ranges represent typical per-student investment for educational institutions.\n"
    "Progression pathway: Students advance through levels as competency increases."
)
ax.text(5, 1.2, legend_text,
       ha='center', va='top', fontsize=17, style='italic',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff4e6', 
                edgecolor='#ff9900', alpha=0.7))

plt.tight_layout()
plt.savefig('Figure2_Technology_Taxonomy.png', dpi=300, bbox_inches='tight', 
           facecolor='white')
print("Figure 2 saved: Figure2_Technology_Taxonomy.png")
print("Resolution: 300 DPI")
plt.close()