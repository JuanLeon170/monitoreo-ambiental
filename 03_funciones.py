"""
Módulo: 03_funciones.py
Autor: Laura Sofia Bolivar Jimenez
Descripción: Modularización matemática, cálculo ponderado de IRCA (Resolución 2115 de 2007), 
balance de cargas contaminantes y estimación de dosificación química para desinfección en PTAP.
"""

def calcular_irca_res2115(ph, turbiedad_unt, cloro_residual, coliformes_totales):
    puntaje_total = 0.0
    if ph < 6.5 or ph > 9.0:
        puntaje_total += 1.5
    if turbiedad_unt > 2.0:
        puntaje_total += 15.0
    if cloro_residual < 0.3 or cloro_residual > 2.0:
        puntaje_total += 15.0
    if coliformes_totales > 0:
        puntaje_total += 15.0
    return puntaje_total

def calcular_carga_contaminante_dia(caudal_lps, concentracion_mg_l):
    carga_diaria = caudal_lps * concentracion_mg_l * 0.0864
    return round(carga_diaria, 4)

def estimar_demanda_cloro(volumen_tanque_m3, dosis_mg_l):
    masa_cloro_gramos = volumen_tanque_m3 * dosis_mg_l
    return round(masa_cloro_gramos, 2)

if __name__ == "__main__":
    print("=== PRUEBAS MODULARES - INTEGRANTE 3 ===")
    print(f"IRCA Calculado: {calcular_irca_res2115(7.2, 3.5, 0.2, 0)}%")
    print(f"Carga Contaminante: {calcular_carga_contaminante_dia(15.5, 45.0)} kg/día")
    print(f"Masa de cloro: {estimar_demanda_cloro(250.0, 2.5)} g")
