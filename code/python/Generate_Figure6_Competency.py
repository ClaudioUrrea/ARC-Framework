#!/usr/bin/env python3
# ==============================================================================
# FIGURE 5: ARC Framework - Competency Progression Model
# ==============================================================================

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Configurar fuente Palatino Linotype
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['TeX Gyre Pagella', 'Palatino Linotype', 'Palatino', 'URW Palladio L', 'serif']
plt.rcParams['font.size'] = 16

# Definir niveles de competencia
competency_levels = {
    'Level 1': {
        'name': 'Novice',
        'description': 'Follows explicit instructions.\nLearns basic concepts.\nExplores robotics.',
        'tech_level': 'Educational Kits\n(LEGO Mindstorms)',
        'pedagogy': 'Direct instruction,\nDemonstrations,\nHands-on exploration',
        'color': '#f3effa'
    },
    'Level 2': {
        'name': 'Advanced Beginner',
        'description': 'Operates systems with guidance.\nRecognizes patterns.\nBegins programming.',
        'tech_level': 'Advanced Kits\n(LEGO EV3, Arduino)',
        'pedagogy': 'Guided inquiry,\nScaffolded activities,\nPeer collaboration',
        'color': '#d4ddf5'
    },
    'Level 3': {
        'name': 'Competent',
        'description': 'Plans and executes tasks\nwith industrial systems.\nApplies theory to practice.',
        'tech_level': 'Advanced Educational\n(Dobot, Niryo)',
        'pedagogy': 'Project-based learning,\nLab practicals,\nTeam challenges',
        'color': '#b5cbf0'
    },
    'Level 4': {
        'name': 'Proficient',
        'description': 'Integrated system operation,\ntroubleshooting complex issues.\nDevelops solutions.',
        'tech_level': 'Didactic Industrial\n(SCORBOT, UR3)',
        'pedagogy': 'Capstone projects,\nCase-based learning,\nInternships',
        'color': '#96b9ea'
    },
    'Level 5': {
        'name': 'Expert',
        'description': 'Autonomous problem-solving,\nsystem design, and optimization.\nMentors others.',
        'tech_level': 'Industrial-Grade\n(UR5e, KUKA)',
        'pedagogy': 'Self-directed projects,\nResearch & Development,\nIndustry partnerships',
        'color': '#77a7e5'
    }
}

# Crear figura
fig, ax = plt.subplots(figsize=(16, 11)) # (figsize=(14, 11))
#ax.set_xlim(0, 14)
#ax.set_ylim(0, 13)
ax.set_xlim(-0.2, 13.1) #(-0.2, 13.1)
ax.set_ylim(0.1, 12.4)    #(0, 12.4)

ax.axis('off')

# TÃ­tulo principal
ax.text(7, 12.4, 'ARC Framework: Competency Progression Model', 
        ha='center', va='top', fontsize=20, fontweight='bold')

# SubtÃ­tulo
ax.text(7, 11.9, 'Developmental Pathway from Novice to Expert in Industrial Robotics', 
        ha='center', va='top', fontsize=17, style='italic', color='black')

# Posiciones verticales para los 5 niveles (de arriba hacia abajo)
y_positions = [9.0, 7.2, 5.4, 3.6, 1.8]
box_height = 1.4

for i, (level_key, level_data) in enumerate(competency_levels.items()):
    y = y_positions[i]
    
    # Caja principal (nivel de competencia)
    main_box = FancyBboxPatch((0, y), 3.5, box_height,
                             boxstyle="round,pad=0.08",
                             facecolor=level_data['color'],
                             edgecolor='black',
                             linewidth=2.5,
                             alpha=0.85)
    ax.add_patch(main_box)
    
    # Texto del nivel
    ax.text(0.2, y + box_height - 0.2, level_key,
           fontsize=17, fontweight='bold', color='black')
    
    # Nombre de competencia
    ax.text(1.75, y + box_height - 0.2, level_data['name'],
           fontsize=16, fontweight='bold', color='black',
           ha='center')
    
    # DescripciÃ³n
    ax.text(1.75, y + 0.4, level_data['description'],
           fontsize=14, color='black', ha='center', va='center',
           multialignment='center')
    
    # Caja de tecnologÃ­a (derecha)
    tech_box = FancyBboxPatch((4.0, y), 3.2, box_height,
                             boxstyle="round,pad=0.08",
                             facecolor='#5b9bd5',
                             edgecolor='black',
                             linewidth=2,
                             alpha=0.8)
    ax.add_patch(tech_box)
    
    ax.text(5.6, y + box_height/2, level_data['tech_level'],
           fontsize=14, color='black', ha='center', va='center',
           multialignment='center', fontweight='bold')
    
    # Caja de pedagogÃ­a (extrema derecha)
    ped_box = FancyBboxPatch((7.7, y), 3.8, box_height,
                            boxstyle="round,pad=0.08",
                            facecolor='#70ad47',
                            edgecolor='black',
                            linewidth=2,
                            alpha=0.8)
    ax.add_patch(ped_box)
    
    ax.text(9.6, y + box_height/2, level_data['pedagogy'],
           fontsize=14, color='black', ha='center', va='center',
           multialignment='center')

# Flechas de progresiÃ³n entre niveles
for i in range(4):
    y_from = y_positions[i]
    y_to = y_positions[i+1] + box_height
    
    arrow = FancyArrowPatch((1.75, y_from), (1.75, y_to),
                           arrowstyle='->', mutation_scale=30,
                           linewidth=3.5, color='#e74c3c',
                           zorder=0)
    ax.add_patch(arrow)
    
    # Etiqueta de transiciÃ³n
    #mid_y = (y_from + y_to) / 2
    #ax.text(1.0, mid_y, 'Progress\nthrough\nlearning', 
    #       fontsize=13, ha='center', va='center',
    #       style='italic', color='#e74c3c', fontweight='bold')

# Headers para las columnas
ax.text(1.75, 10.8, 'Competency Level\n& Characteristics', 
       fontsize=16, fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#d4ddf5', 
                edgecolor='black', linewidth=2))

ax.text(5.6, 10.8, 'Technology\nLevel', 
       fontsize=16, fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#77B5FE', 
                edgecolor='black', linewidth=2))

ax.text(9.6, 10.8, 'Pedagogical\nApproaches', 
       fontsize=16, fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#3CB371', 
                edgecolor='black', linewidth=2))

# Indicador de tiempo estimado
time_labels = ['~3+ years', '~2 years', '~1.5 years', '~1 year', '~6 months']
for i, time_label in enumerate(time_labels):
    y = y_positions[i] + box_height/2
    ax.text(12.0, y, time_label,
           fontsize=14, ha='left', va='center',
           bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFD300', 
                    alpha=0.6, edgecolor='black'))

ax.text(12.0, 10.8, 'Typical\nDuration',
       fontsize=16, fontweight='bold', ha='left',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='#FED83A', 
                edgecolor='black', linewidth=1.5))

# Nota metodolÃ³gica
note_text = (
    "Progression Model based on Dreyfus Model of Skill Acquisition (Dreyfus & Dreyfus, 1980)\n"
    "adapted for industrial automation education. Advancement through levels requires\n"
    "demonstrated competency mastery and typically involves 200-300 hours of practice per level."
)
ax.text(6.5, 0.8, note_text,
       ha='center', va='center', fontsize=17, style='italic',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff4e6',
                edgecolor='#ff9900', linewidth=2, alpha=0.9))

plt.tight_layout()
plt.savefig('Figure6_Competency_Progression.png', dpi=300, bbox_inches='tight',
           facecolor='white')
print("Figure 6 saved: Figure6_Competency_Progression.png")
print("Resolution: 300 DPI")
plt.close()
plt.close()