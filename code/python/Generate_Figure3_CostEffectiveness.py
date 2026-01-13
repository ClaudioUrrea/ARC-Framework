#!/usr/bin/env python3
# ==============================================================================
# FIGURE 3: Cost-Effectiveness Analysis
# ==============================================================================

import matplotlib.pyplot as plt
import numpy as np

# Configurar fuente Palatino Linotype
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Palatino Linotype', 'Palatino', 'URW Palladio L', 'serif']
plt.rcParams['font.size'] = 14

# Datos de cost-effectiveness
technologies = ['Level 1:\nKits', 'Level 2:\nAdvanced', 'Level 3:\nDidactic',
                'Level 4:\nSemi-Ind', 'Level 5:\nIndustrial', 'Remote Lab\n(Level 5)']
costs = np.array([500, 800, 3500, 12000, 40000, 1500])
effect_sizes = np.array([0.59, 0.64, 0.68, 0.73, 0.94, 0.89])

# Calcular impacto por $1000
impact_per_1000 = (effect_sizes / costs) * 1000

# Crear figura
fig, ax = plt.subplots(figsize=(14, 9))

# Scatter plot con tamaÃ±o de burbujas proporcional al impacto
sizes = impact_per_1000 * 400  # Escalar para visualizaciÃ³n

scatter = ax.scatter(costs, effect_sizes, s=sizes, 
                    c=impact_per_1000, cmap='YlOrRd',
                    alpha=0.7, edgecolors='black', linewidth=2.5)

# Resaltar Remote Lab (punto Ã³ptimo)
optimal_idx = 5
ax.scatter(costs[optimal_idx], effect_sizes[optimal_idx], 
          s=sizes[optimal_idx], marker='*', c='gold',
          edgecolors='darkgoldenrod', linewidth=3.5, 
          zorder=10, label='Optimal: Remote Lab')

# Etiquetas para cada punto
for i in range(len(technologies)):
    offset_x = 0 if i != 4 else 3000  # Ajustar Level 5 para evitar overlap
    offset_y = 0.03 if i != 4 else -0.03
    
    ax.annotate(f'{technologies[i]}\n${costs[i]:,}\nd={effect_sizes[i]:.2f}',
               xy=(costs[i], effect_sizes[i]),
               xytext=(costs[i] + offset_x, effect_sizes[i] + offset_y),
               fontsize=11, ha='center', va='bottom' if i != 4 else 'top',
               bbox=dict(boxstyle='round,pad=0.4', 
                        facecolor='white', edgecolor='gray', alpha=0.85),
               fontweight='normal')

# LÃ­nea de tendencia (physical labs)
physical_indices = [0, 1, 2, 3, 4]  # Excluir remote lab
z = np.polyfit(costs[physical_indices], effect_sizes[physical_indices], 2)
p = np.poly1d(z)
x_line = np.linspace(costs[0], costs[4], 100)
ax.plot(x_line, p(x_line), 'r--', alpha=0.5, linewidth=2.5,
       label='Physical Labs Trend')

# Configurar ejes
ax.set_xlabel('Cost per Student (USD)', fontsize=15, fontweight='bold')
ax.set_ylabel("Effect Size (Hedges' d)", fontsize=15, fontweight='bold')
ax.set_title('Cost-Effectiveness Analysis: Technology Integration Models',
            fontsize=17, fontweight='bold', pad=20)

# Escala logarÃ­tmica en X para mejor visualizaciÃ³n
ax.set_xscale('log')
ax.set_xlim(200, 60000)
ax.set_ylim(0.50, 1.05)

# Grid
ax.grid(True, alpha=0.3, linestyle='--', linewidth=1)
ax.set_axisbelow(True)

# Colorbar para impacto
cbar = plt.colorbar(scatter, ax=ax, pad=0.02)
cbar.set_label('Impact per $1,000 Invested\n(Effect Size / Cost Ã— 1000)', 
              fontsize=13, fontweight='bold')
cbar.ax.tick_params(labelsize=11)

# Leyenda
legend = ax.legend(loc='upper left', fontsize=12, frameon=True, 
                  fancybox=True, shadow=True)
legend.get_frame().set_alpha(0.9)

# AnotaciÃ³n de insight clave
insight_text = (
    "Key Finding: Remote laboratories achieve 95% of industrial-grade\n"
    "effectiveness at 4% of the cost, representing optimal ROI."
)
ax.text(0.98, 0.05, insight_text, transform=ax.transAxes,
       fontsize=13, ha='right', va='bottom',
       bbox=dict(boxstyle='round,pad=0.6', facecolor='lightyellow',
                edgecolor='orange', linewidth=2, alpha=0.9))

# Ajustar tamaÃ±o de ticks
ax.tick_params(axis='both', which='major', labelsize=11)

plt.tight_layout()
plt.savefig('Figure3_Cost_Effectiveness.png', dpi=300, bbox_inches='tight',
           facecolor='white')
print("Figure 3 saved: Figure3_Cost_Effectiveness.png")
print("Resolution: 300 DPI")
plt.close()
