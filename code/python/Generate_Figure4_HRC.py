#!/usr/bin/env python3
# ==============================================================================
# FIGURE 4: HRC Performance Metrics (Real Data - Fanuc M-20iA) 
# ==============================================================================

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Configurar fuente Palatino Linotype
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Palatino Linotype', 'Palatino', 'URW Palladio L', 'serif']
plt.rcParams['font.size'] = 11

# Leer datos reales
df = pd.read_csv('HRC_Aggregated_Fanuc.csv')

# Convertir Workload y Safety a escala 0-100 para mejor visualizaciÃ³n
df['Workload_100'] = df['Workload'] * 100
df['Safety_100'] = df['Safety'] * 100

# Tomar primeros 200 episodios
df_plot = df.head(200).copy()

# Crear figura con 4 subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 11))

# Colores profesionales
color_throughput = '#2E86AB'
color_workload = '#A23B72'
color_safety = '#F18F01'

# ==============================================================================
# Panel (a): Throughput Evolution
# ==============================================================================
ax1.plot(df_plot['Episode'], df_plot['Throughput'], 
        linewidth=2.0, color=color_throughput, alpha=0.7)
ax1.fill_between(df_plot['Episode'], df_plot['Throughput'], 
                 alpha=0.25, color=color_throughput)

# Media mÃ³vil
window = 20
rolling_mean = df_plot['Throughput'].rolling(window=window).mean()
ax1.plot(df_plot['Episode'], rolling_mean, 'r--', 
        linewidth=2.5, label=f'{window}-Episode Moving Avg', alpha=0.9)

ax1.set_xlabel('Training Episode', fontsize=14, fontweight='bold')
ax1.set_ylabel('Throughput (tasks/hour)', fontsize=14, fontweight='bold')
ax1.set_title('(a) System Throughput Evolution', fontsize=15, fontweight='bold', pad=10)
ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
ax1.legend(loc='lower right', fontsize=12, framealpha=0.95, edgecolor='black')
ax1.tick_params(axis='both', labelsize=12)

# EstadÃ­stica - mean line
mean_throughput = df_plot['Throughput'].mean()
ax1.axhline(y=mean_throughput, color='green', linestyle=':', 
           linewidth=2.5, alpha=0.8, zorder=5)
ax1.text(5, mean_throughput - 0.15, f'Mean: {mean_throughput:.2f}', 
        fontsize=12, color='green', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                 edgecolor='green', alpha=0.9))

ax1.set_ylim([4.5, 7.0])

# ==============================================================================
# Panel (b): Human Workload (0-100 scale, lower is better)
# ==============================================================================
ax2.plot(df_plot['Episode'], df_plot['Workload_100'], 
        linewidth=2.0, color=color_workload, alpha=0.7)
ax2.fill_between(df_plot['Episode'], df_plot['Workload_100'], 
                 alpha=0.25, color=color_workload)

# Media mÃ³vil
rolling_mean_wl = df_plot['Workload_100'].rolling(window=window).mean()
ax2.plot(df_plot['Episode'], rolling_mean_wl, 'r--', 
        linewidth=2.5, label=f'{window}-Episode Moving Avg', alpha=0.9)

ax2.set_xlabel('Training Episode', fontsize=14, fontweight='bold')
ax2.set_ylabel('Human Workload (0-100)', fontsize=14, fontweight='bold')
ax2.set_title('(b) Human Workload Optimization', fontsize=15, fontweight='bold', pad=10)
ax2.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
ax2.legend(loc='upper right', fontsize=12, framealpha=0.95, edgecolor='black')
ax2.tick_params(axis='both', labelsize=12)

# EstadÃ­stica - mean line
mean_workload = df_plot['Workload_100'].mean()
ax2.axhline(y=mean_workload, color='blue', linestyle=':', 
           linewidth=2.5, alpha=0.8, zorder=5)
ax2.text(5, mean_workload + 1.5, f'Mean: {mean_workload:.2f}', 
        fontsize=12, color='blue', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                 edgecolor='blue', alpha=0.9))

ax2.set_ylim([60, 90])
ax2.invert_yaxis()  # Invertir porque menor es mejor

# ==============================================================================
# Panel (c): Safety Score (0-100 scale, higher is better)
# ==============================================================================
ax3.plot(df_plot['Episode'], df_plot['Safety_100'], 
        linewidth=2.0, color=color_safety, alpha=0.7)
ax3.fill_between(df_plot['Episode'], df_plot['Safety_100'], 
                 alpha=0.25, color=color_safety)

# Media mÃ³vil
rolling_mean_sf = df_plot['Safety_100'].rolling(window=window).mean()
ax3.plot(df_plot['Episode'], rolling_mean_sf, 'r--', 
        linewidth=2.5, label=f'{window}-Episode Moving Avg', alpha=0.9)

ax3.set_xlabel('Training Episode', fontsize=14, fontweight='bold')
ax3.set_ylabel('Safety Score (0-100)', fontsize=14, fontweight='bold')
ax3.set_title('(c) Safety Score Progression', fontsize=15, fontweight='bold', pad=10)
ax3.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
ax3.legend(loc='lower right', fontsize=12, framealpha=0.95, edgecolor='black')
ax3.tick_params(axis='both', labelsize=12)

# EstadÃ­stica - mean line
mean_safety = df_plot['Safety_100'].mean()
ax3.axhline(y=mean_safety, color='darkgreen', linestyle=':', 
           linewidth=2.5, alpha=0.8, zorder=5)
ax3.text(5, mean_safety - 2.5, f'Mean: {mean_safety:.2f}', 
        fontsize=12, color='darkgreen', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                 edgecolor='darkgreen', alpha=0.9))

ax3.set_ylim([85, 101])

# ==============================================================================
# Panel (d): Multi-Objective Trade-off Space
# ==============================================================================
scatter = ax4.scatter(df_plot['Throughput'], df_plot['Workload_100'], 
                     c=df_plot['Safety_100'], cmap='RdYlGn', 
                     s=100, alpha=0.7, edgecolors='black', linewidth=1.2,
                     vmin=90, vmax=100)

ax4.set_xlabel('Throughput (tasks/hour)', fontsize=14, fontweight='bold')
ax4.set_ylabel('Human Workload (0-100)', fontsize=14, fontweight='bold')
ax4.set_title('(d) Multi-Objective Trade-off Space', fontsize=15, fontweight='bold', pad=10)
ax4.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
ax4.tick_params(axis='both', labelsize=12)
ax4.invert_yaxis()  # Invertir workload (menor es mejor)

# Colorbar para safety
cbar = plt.colorbar(scatter, ax=ax4, pad=0.02)
cbar.set_label('Safety Score', fontsize=13, fontweight='bold')
cbar.ax.tick_params(labelsize=12)

# Identificar regiÃ³n Pareto-optimal (alto throughput, bajo workload, alto safety)
pareto_threshold = {
    'throughput': df_plot['Throughput'].quantile(0.75),
    'workload': df_plot['Workload_100'].quantile(0.25),
    'safety': df_plot['Safety_100'].quantile(0.75)
}

pareto_points = df_plot[
    (df_plot['Throughput'] >= pareto_threshold['throughput']) &
    (df_plot['Workload_100'] <= pareto_threshold['workload']) &
    (df_plot['Safety_100'] >= pareto_threshold['safety'])
]

if len(pareto_points) > 0:
    ax4.scatter(pareto_points['Throughput'], pareto_points['Workload_100'],
               s=200, marker='*', c='gold', edgecolors='darkgoldenrod', 
               linewidth=2.5, label='Pareto-Optimal Region', zorder=10)
    ax4.legend(loc='lower left', fontsize=12, framealpha=0.95, edgecolor='black')

# Ajustar lÃ­mites
ax4.set_xlim([5.2, 7.0])
ax4.set_ylim([60, 85])

# TÃ­tulo general
fig.suptitle('Adaptive Multi-Objective Reinforcement Learning for Human-Robot Collaboration\n' +
             'Performance Metrics: Fanuc M-20iA Industrial Manipulator',
             fontsize=17, fontweight='bold', y=0.995)

plt.tight_layout(rect=[0, 0, 1, 0.99])
plt.savefig('Figure4_HRC_Performance.png', dpi=300, bbox_inches='tight',
           facecolor='white')

print("Figure 4 saved: Figure4_HRC_Performance.png")
print("Resolution: 300 DPI")
print("Data: Real Fanuc M-20iA metrics")
print(f"\nStatistics:")
print(f"  Throughput: Mean={mean_throughput:.3f} tasks/hour")
print(f"  Workload: Mean={mean_workload:.2f}% (lower is better)")
print(f"  Safety: Mean={mean_safety:.2f}% (higher is better)")
print(f"  Pareto-optimal points: {len(pareto_points)}")
plt.close()
