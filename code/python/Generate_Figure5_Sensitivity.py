#!/usr/bin/env python3
# ==============================================================================
# FIGURE 4: Sensitivity Analysis 
# ==============================================================================

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Configurar fuente Palatino Linotype
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Palatino Linotype', 'Palatino', 'URW Palladio L', 'serif']
plt.rcParams['font.size'] = 12

# Leer datos reales
df = pd.read_csv('Sensitivity_Results_Fanuc_Shaded.csv')

# Convertir escalas
df['Workload_100'] = df['Workload'] / 100
df['Safety_100'] = df['Safety'] * 100

# Crear etiquetas descriptivas
labels = []
for idx, row in df.iterrows():
    param = row['Parameter']
    value = row['Value']
    
    if param == 'fatigueRate':
        if value == 0.9:
            labels.append('Fatigue Rate\n(-10%)')
        elif value == 1.0:
            labels.append('Fatigue Rate\n(Baseline)')
        else:
            labels.append('Fatigue Rate\n(+10%)')
    elif param == 'w1':
        if value == 0.9:
            labels.append('Reward wâ‚\n(-10%)')
        elif value == 1.0:
            labels.append('Reward wâ‚\n(Baseline)')
        else:
            labels.append('Reward wâ‚\n(+10%)')
    elif param == 'w3':
        if value == 0.9:
            labels.append('Reward wâ‚ƒ\n(-10%)')
        elif value == 1.0:
            labels.append('Reward wâ‚ƒ\n(Baseline)')
        else:
            labels.append('Reward wâ‚ƒ\n(+10%)')
    elif param == 'auctionFrequency':
        if value == 0.9:
            labels.append('Auction Freq.\n(-10%)')
        elif value == 1.0:
            labels.append('Auction Freq.\n(Baseline)')
        else:
            labels.append('Auction Freq.\n(+10%)')

df['Label'] = labels

# Crear figura
fig, ax = plt.subplots(figsize=(16, 10))

# ParÃ¡metros
n_params = len(df)
x_pos = np.arange(n_params)
width = 0.25

# Colores
colors = {
    'Throughput': '#b5cbf0',
    'Workload': '#A23B72',
    'Safety': '#F18F01'
}

# Barras agrupadas
bars1 = ax.bar(x_pos - width, df['Throughput'], width, 
              label='Throughput (tasks/hour)', 
              color=colors['Throughput'], alpha=0.85, 
              edgecolor='black', linewidth=1.5)

bars2 = ax.bar(x_pos, df['Workload_100'], width, 
              label='Human Workload (0-15)', 
              color=colors['Workload'], alpha=0.85, 
              edgecolor='black', linewidth=1.5)

bars3 = ax.bar(x_pos + width, df['Safety_100'], width, 
              label='Safety Score (0-100)', 
              color=colors['Safety'], alpha=0.85, 
              edgecolor='black', linewidth=1.5)

# Valores sobre barras baseline - CENTRADOS Y ABAJO
for i, (bar, val) in enumerate(zip(bars1, df['Throughput'])):
    if i % 3 == 1:  # Solo baseline
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height - 0.3,
               f'{val:.2f}',
               ha='center', va='top', fontsize=14, 
               fontweight='bold', color='black')

for i, (bar, val) in enumerate(zip(bars3, df['Safety_100'])):
    if i % 3 == 1:  # Solo baseline
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height - 2.0,
               f'{val:.2f}',
               ha='center', va='top', fontsize=14, 
               fontweight='bold', color='black')

# Error bars
ax.errorbar(x_pos - width, df['Throughput'], yerr=df['Std_Throughput'],
           fmt='none', ecolor='black', capsize=4, capthick=1.5, 
           alpha=0.6, linewidth=1.2)
ax.errorbar(x_pos, df['Workload_100'], yerr=df['Std_Workload']/100,
           fmt='none', ecolor='black', capsize=4, capthick=1.5, 
           alpha=0.6, linewidth=1.2)
ax.errorbar(x_pos + width, df['Safety_100'], yerr=df['Std_Safety']*100,
           fmt='none', ecolor='black', capsize=4, capthick=1.5, 
           alpha=0.6, linewidth=1.2)

# Configurar ejes
ax.set_xlabel('Parameter Variation', fontsize=15, fontweight='bold', labelpad=10)
ax.set_ylabel('Performance Metrics (Normalized Scale)', fontsize=15, fontweight='bold')
ax.set_title('Sensitivity Analysis: Parameter Robustness in Industrial HRC Systems',
            fontsize=17, fontweight='bold', pad=15)

ax.set_xticks(x_pos)
ax.set_xticklabels(df['Label'], rotation=0, ha='center', fontsize=12)
ax.tick_params(axis='y', labelsize=12)

# Leyenda
legend = ax.legend(loc='center right', fontsize=13, frameon=True, 
                  fancybox=True, shadow=True, ncol=1)
legend.get_frame().set_alpha(0.95)
legend.get_frame().set_edgecolor('black')
legend.get_frame().set_linewidth(1.5)

# Grid
ax.grid(True, alpha=0.3, linestyle='--', axis='y', linewidth=1)
ax.set_axisbelow(True)

# Ajustar lÃ­mites ANTES de colocar etiquetas superiores
ax.set_ylim([0, 105])

# ==============================================================================
# ETIQUETAS SUPERIORES - CENTRADAS SOBRE BASELINE
# ==============================================================================

# Definir EXPLÃCITAMENTE las posiciones X de las barras Baseline
BASELINE_POSITIONS = {
    'Fatigue Rate': 1.25,         # Segunda barra del primer grupo
    'Reward Weight wâ‚': 4.25,     # Segunda barra del segundo grupo
    'Reward Weight wâ‚ƒ': 7.25,     # Segunda barra del tercer grupo
    'Auction Frequency': 10.25    # Segunda barra del cuarto grupo
}

# Definir grupos con sus caracterÃ­sticas
groups_info = [
    {'label': 'Fatigue Rate', 'start': 0, 'end': 3, 'color': 'lightgray'},
    {'label': 'Reward Weight wâ‚', 'start': 3, 'end': 6, 'color': 'lightgreen'},
    {'label': 'Reward Weight wâ‚ƒ', 'start': 6, 'end': 9, 'color': 'lightyellow'},
    {'label': 'Auction Frequency', 'start': 9, 'end': 12, 'color': 'lightcoral'}
]

# Aplicar sombreados y etiquetas
y_max = ax.get_ylim()[1]  # Obtener lÃ­mite superior actual

for group in groups_info:
    # Sombreado de fondo
    ax.axvspan(group['start'] - 0.5, group['end'] - 0.5, 
              alpha=0.08, color=group['color'], zorder=0)
    
    # ETIQUETA CENTRADA sobre posiciÃ³n de Baseline
    x_center = BASELINE_POSITIONS[group['label']]
    y_position = y_max * 0.988
    
    ax.text(x_center, y_position, group['label'], 
           ha='center', va='top', fontsize=13, fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.4', facecolor=group['color'], 
                    edgecolor='gray', alpha=0.7, linewidth=1.5))
    
# LÃ­neas verticales rojas en posiciones Baseline
for pos in BASELINE_POSITIONS.values():
    ax.axvline(x=pos, color='red', linestyle=':', linewidth=2, alpha=0.3)
   
# Insight box
insight_text = (
    "Robustness Analysis: System maintains stable performance across Â±10% parameter variations.\n"
    "Baseline values (100%) shown with vertical dotted lines. Fatigue rate and reward weights\n"
    "show greatest influence on multi-objective optimization. Error bars: Â±1 SD (n=10 trials).\n"
    "Workload scale normalized for visualization (actual range: 1200-1300)."
)
ax.text(0.4615, 0.3, insight_text, transform=ax.transAxes,
       fontsize=13, ha='left', va='bottom',
       bbox=dict(boxstyle='round,pad=0.6', facecolor='lightyellow',
                edgecolor='orange', linewidth=2.5, alpha=0.95))

plt.tight_layout()
plt.savefig('Figure5_Sensitivity_Analysis.png', dpi=300, bbox_inches='tight',
           facecolor='white')

print("\n" + "="*80)
print("Figure 5 saved: Figure5_Sensitivity_Analysis.png")
print("Resolution: 300 DPI")
print("="*80)
plt.close()
