#==============================================================================
#  FOREST PLOT - Industrial Robotics Education (UPDATED: 52 studies)
#==============================================================================

library(metafor)

#==============================================================================
#  DATOS - 12 ESTUDIOS REPRESENTATIVOS (de n=52 total)
#==============================================================================
studies <- data.frame(
  Authors = c("Zamora", "Makulavicius", "Ouyang", "Antunes",
              "Zhang", "Alginahi", "Urrea", "Nomandela",
              "Tang", "Silva", "Dobot Platform", "UR Remote Lab"),
  Year = c(2025, 2025, 2024, 2023, 2025, 2025, 2025, 2025, 
           2025, 2025, 2024, 2024),
  g = c(0.94, 0.88, 0.71, 0.85, 0.92, 0.76, 0.94, 0.68, 
        0.73, 0.65, 0.68, 0.89),
  SE = c(0.12, 0.15, 0.08, 0.11, 0.13, 0.09, 0.11, 0.10, 
         0.08, 0.12, 0.14, 0.11),
  N = c(120, 85, 450, 95, 110, 200, 150, 78, 
        890, 145, 65, 180),
  Tech_Level = c("Industrial", "Industrial", "Educational", "Educational",
                 "Industrial", "Educational", "Industrial", "Industrial",
                 "Educational", "Educational", "Semi-Industrial", "Industrial")
)

# Calcular varianza
studies$Variance <- studies$SE^2

# Crear etiquetas de estudio
study_labels <- paste(studies$Authors, studies$Year, sep = ", ")

#==============================================================================
#  META-ANÃLISIS
#==============================================================================
ma <- rma(yi = g, vi = Variance, data = studies,
          method = "REML", slab = study_labels)

#==============================================================================
#  CREAR FIGURA CON COLORES INTENSOS Y VISIBLES (12 estudios)
#==============================================================================
png("Figure7_Forest_Plot.png", width = 1400, height = 1100, res = 150)

# Configurar mÃ¡rgenes optimizados
par(mar = c(5, 4, 1, 2), family = "serif")

# Crear forest plot base (sin anotaciones para evitar superposiciÃ³n)
forest(ma,
       xlab = "Hedges' g",
       slab = study_labels,
       ilab = studies$N,
       ilab.xpos = -0.4,
       ilab.pos = 4,
       textpos = c(-1.0, 2.3),
       cex = 0.88,
       cex.lab = 1.15,
       cex.axis = 0.88,
       header = c("Study", "Effect Size [95% CI]"),
       mlab = "Overall Effect (RE Model)",
       col = "navy",
       border = "navy",
       xlim = c(-1.0, 2.3),
       alim = c(-0.2, 1.4),
       at = seq(-0.2, 1.4, 0.2),
       psize = 2.0,
       refline = 0,
       digits = 3,
       annotate = FALSE)

# Header para columna N
text(-0.40, 14, "N", cex = 0.88, font = 2, pos = 4)

# AÃ±adir sombreado de colores por subgrupo - COLORES MÃS INTENSOS
for (i in 1:nrow(studies)) {
  y_pos <- nrow(studies) - i + 1
  
  if (studies$Tech_Level[i] == "Industrial") {
    # Azul intenso para Industrial-Grade Systems
    rect(-1.0, y_pos - 0.45, 2.3, y_pos + 0.45,
         col = rgb(0.6, 0.75, 1, 0.70), border = NA)
  } else if (studies$Tech_Level[i] == "Semi-Industrial") {
    # Gris para Semi-Industrial
    rect(-1.0, y_pos - 0.45, 2.3, y_pos + 0.45,
         col = rgb(0.8, 0.8, 0.8, 0.70), border = NA)
  } else {
    # Naranja intenso para Educational Kits
    rect(-1.0, y_pos - 0.45, 2.3, y_pos + 0.45,
         col = rgb(1, 0.80, 0.45, 0.70), border = NA)
  }
}

# Redibujar el forest plot ENCIMA del sombreado (con anotaciones)
par(new = TRUE)
par(mar = c(5, 4, 1, 2), family = "serif")

forest(ma,
       xlab = "Hedges' g",
       slab = study_labels,
       ilab = studies$N,
       ilab.xpos = -0.4,
       ilab.pos = 4,
       textpos = c(-1.0, 2.3),
       cex = 0.88,
       cex.lab = 1.15,
       cex.axis = 0.88,
       header = c("Study", "Effect Size [95% CI]"),
       mlab = "Overall Effect (RE Model)",
       col = "navy",
       border = "navy",
       xlim = c(-1.0, 2.3),
       alim = c(-0.2, 1.4),
       at = seq(-0.2, 1.4, 0.2),
       psize = 2.0,
       refline = 0,
       digits = 3,
       annotate = TRUE)

# Leyenda con colores mÃ¡s saturados e intensos (3 niveles)
legend(0.345, 14.95,
       legend = c("Industrial-Grade Systems", "Semi-Industrial", "Educational Kits"),
       fill = c(rgb(0.6, 0.75, 1, 0.85),    # Azul saturado
                rgb(0.8, 0.8, 0.8, 0.85),   # Gris
                rgb(1, 0.80, 0.45, 0.85)),  # Naranja saturado
       border = c(rgb(0.3, 0.5, 0.9, 1),    # Borde azul oscuro
                  rgb(0.5, 0.5, 0.5, 1),    # Borde gris oscuro
                  rgb(0.9, 0.6, 0.2, 1)),   # Borde naranja oscuro
       cex = 0.74,
       bty = "o",
       box.lwd = 1.2,
       box.col = "black",
       bg = "white",
       title = "Technology Level",
       title.cex = 0.78,
       pt.cex = 1.5,
       xpd = TRUE)

dev.off()

#==============================================================================
#  ESTADÃSTICAS
#==============================================================================
cat("\n", rep("=", 80), "\n", sep = "")
cat("META-ANALYSIS RESULTS - Forest Plot (12 representative studies from n=52)\n")
cat(rep("=", 80), "\n\n", sep = "")

cat("Overall Effect (Random-Effects Model):\n")
cat(sprintf("  Hedges' g = %.3f [95%% CI: %.3f, %.3f]\n",
            ma$beta, ma$ci.lb, ma$ci.ub))
cat(sprintf("  Z = %.3f, p = %.4f\n\n", ma$zval, ma$pval))

cat("Heterogeneity Statistics:\n")
cat(sprintf("  Q(df = %d) = %.3f, p = %.4f\n", ma$k - 1, ma$QE, ma$QEp))
cat(sprintf("  IÂ² = %.2f%%\n", ma$I2))
cat(sprintf("  Ï„Â² = %.4f\n\n", ma$tau2))

# AnÃ¡lisis por subgrupo
ind <- subset(studies, Tech_Level == "Industrial")
edu <- subset(studies, Tech_Level == "Educational")
semi <- subset(studies, Tech_Level == "Semi-Industrial")

ma_ind <- rma(yi = g, vi = Variance, data = ind, method = "REML")
ma_edu <- rma(yi = g, vi = Variance, data = edu, method = "REML")

cat("Subgroup Analysis by Technology Level:\n")
cat(sprintf("  Industrial-Grade Systems (n = %d, BLUE shading):\n", nrow(ind)))
cat(sprintf("    Pooled g = %.3f [95%% CI: %.3f, %.3f]\n",
            ma_ind$beta, ma_ind$ci.lb, ma_ind$ci.ub))
cat(sprintf("    Studies: %s\n\n", 
            paste(ind$Authors, collapse = ", ")))

cat(sprintf("  Educational Kits (n = %d, ORANGE shading):\n", nrow(edu)))
cat(sprintf("    Pooled g = %.3f [95%% CI: %.3f, %.3f]\n",
            ma_edu$beta, ma_edu$ci.lb, ma_edu$ci.ub))
cat(sprintf("    Studies: %s\n\n", 
            paste(edu$Authors, collapse = ", ")))

if (nrow(semi) > 0) {
  cat(sprintf("  Semi-Industrial (n = %d, GRAY shading):\n", nrow(semi)))
  cat(sprintf("    Studies: %s\n", paste(semi$Authors, collapse = ", ")))
  cat(sprintf("    Effect size: g = %.3f\n\n", semi$g[1]))
}

cat("Between-Group Comparison:\n")
diff_g <- ma_ind$beta - ma_edu$beta
cat(sprintf("  Difference: %.3f (Industrial > Educational)\n", diff_g))
cat(sprintf("  Relative improvement: %.1f%%\n\n",
            ((diff_g) / ma_edu$beta) * 100))

cat("Note: These 12 studies are representative of the full corpus of 52 studies\n")
cat("      analyzed in the systematic review (2019-2025).\n\n")

cat(rep("=", 80), "\n", sep = "")
