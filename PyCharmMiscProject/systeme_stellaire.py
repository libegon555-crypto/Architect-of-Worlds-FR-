from jets_de_des import random1d100, randomd6, chercher_tableau
import math

tableau_categories_masses = {(1, 4): "naine_brune", (4, 78): "faible_masse", (78, 91): "masse_intermediaire", (91, 101): "haute_masse"}

naine_brune = {(1, 11): 0.015, (11, 30): 0.02, (30, 46): 0.03, (46, 61): 0.04, (61, 75): 0.05, (75, 88): 0.06, (88, 101): 0.07}

faible_masse = {(1, 14): 0.08, (14, 24): 0.10, (24, 35): 0.12, (35, 44): 0.15, (44, 53): 0.18, (53, 60): 0.22, (60, 66): 0.26, (66, 71): 0.30, (71, 75): 0.34, (75, 78): 0.38, (78, 81): 0.42, (81, 84): 0.46, (84, 87): 0.50, (87, 90): 0.53, (90, 93): 0.56, (93, 96): 0.59, (96, 98): 0.62, (98, 100): 0.65, (100, 101): 0.68}

masse_intermediaire = {(1, 8): 0.70, (8, 14): 0.72, (14, 20): 0.74, (20, 25): 0.76, (25, 30): 0.78, (30, 35): 0.80, (35, 40): 0.82, (40, 44): 0.84, (44, 48): 0.86, (48, 52): 0.88, (52, 56): 0.90, (56, 60): 0.92, (60, 63): 0.94, (63, 66): 0.96, (66, 69): 0.98, (69, 72): 1.00, (72, 75): 1.02, (75, 79): 1.04, (79, 83): 1.07, (83, 86): 1.10, (86, 90): 1.13, (90, 93): 1.16, (93, 96): 1.19, (96, 98): 1.22, (98, 101): 1.25}

haute_masse = {(1, 4): 1.28, (4, 7): 1.31, (7, 10): 1.34, (10, 13): 1.37, (13, 17): 1.40, (17, 20): 1.44, (20, 24): 1.48, (24, 28): 1.53, (28, 32): 1.58, (32, 36): 1.64, (36, 39): 1.70, (39, 42): 1.76, (42, 46): 1.82, (46, 50): 1.90, (50, 54): 2.00, (54, 57): 2.10, (57, 60): 2.20, (60, 63): 2.30, (63, 68): 2.40, (68, 72): 2.60, (72, 76): 2.80, (76, 79): 3.00, (79, 83): 3.20, (83, 88): 3.50, (88, 92): 4.00, (92, 95): 4.50, (95, 97): 5.00, (97, 99): 5.50, (99, 101): 6.00}

tableau_temp_faible_masse = {(0.08, 0.09): (2500, 0.00047), (0.09, 0.11): (2710, 0.00087), (0.11, 0.135): (2930, 0.0016), (0.135, 0.165): (3090, 0.0029), (0.165, 0.20): (3210, 0.0044), (0.20, 0.24): (3370, 0.0070), (0.24, 0.28): (3480, 0.010), (0.28, 0.32): (3550, 0.013), (0.32, 0.36): (3600, 0.017), (0.36, 0.40): (3640, 0.020), (0.40, 0.44): (3680, 0.025), (0.44, 0.48): (3730, 0.031), (0.48, 0.52): (3780, 0.039)}

tableau_temp_sequence_principale = {(0.49, 0.545): (3820, 4410, 0.046, 1.012, 111.0), (0.545, 0.575): (3870, 4510, 0.054, 1.014, 94.1), (0.575, 0.605): (3920, 4610, 0.065, 1.016, 79.3), (0.605, 0.635): (4000, 4720, 0.079, 1.019, 66.8), (0.635, 0.665): (4090, 4810, 0.095, 1.022, 56.3), (0.665, 0.69): (4200, 4870, 0.12, 1.025, 47.4), (0.69, 0.71): (4290, 4930, 0.13, 1.028, 42.5), (0.71, 0.73): (4390, 5000, 0.15, 1.03, 38.1), (0.73, 0.75): (4490, 5060, 0.17, 1.032, 34.3), (0.75, 0.77): (4590, 5130, 0.2, 1.034, 30.9), (0.77, 0.79): (4690, 5190, 0.22, 1.037, 28.0), (0.79, 0.81): (4790, 5260, 0.25, 1.04, 25.4), (0.81, 0.83): (4880, 5320, 0.28, 1.043, 23.1), (0.83, 0.85): (4970, 5370, 0.32, 1.046, 20.9), (0.85, 0.87): (5070, 5420, 0.35, 1.05, 19.1), (0.87, 0.89): (5150, 5470, 0.39, 1.054, 17.5), (0.89, 0.91): (5240, 5520, 0.44, 1.056, 16.0), (0.91, 0.93): (5320, 5560, 0.48, 1.06, 14.7), (0.93, 0.95): (5390, 5590, 0.53, 1.064, 13.5), (0.95, 0.97): (5470, 5620, 0.59, 1.066, 12.4), (0.97, 0.99): (5540, 5650, 0.65, 1.073, 11.4), (0.99, 1.01): (5600, 5670, 0.71, 1.076, 10.5), (1.01, 1.03): (5660, 5690, 0.78, 1.083, 9.71), (1.03, 1.055): (5730, 5710, 0.85, 1.086, 8.94), (1.055, 1.085): (5810, 5730, 0.97, 1.096, 7.98), (1.085, 1.115): (5900, 5750, 1.1, 1.1, 7.12), (1.115, 1.145): (5970, 5760, 1.3, 1.104, 6.8), (1.145, 1.175): (6070, 5800, 1.5, 1.108, 6.12), (1.175, 1.205): (6140, 5810, 1.7, 1.11, 5.68), (1.205, 1.235): (6210, 5830, 1.9, 1.12, 5.16), (1.235, 1.265): (6300, 5850, 2.1, 1.136, 4.74), (1.265, 1.295): (6370, 5860, 2.4, 1.14, 4.65), (1.295, 1.325): (6470, 5890, 2.7, 1.145, 4.14), (1.325, 1.355): (6550, 5910, 3.0, 1.15, 3.96), (1.355, 1.385): (6630, 5930, 3.3, 1.167, 3.55), (1.385, 1.42): (6730, 5980, 3.5, 1.183, 3.29), (1.42, 1.46): (6880, 6040, 4.1, 1.204, 2.94), (1.46, 1.505): (7060, 6140, 4.7, 1.219, 2.69), (1.505, 1.555): (7290, 6260, 5.4, 1.223, 2.53), (1.555, 1.61): (7530, 6390, 6.3, 1.241, 2.4), (1.61, 1.67): (7800, 6540, 7.3, 1.296, 1.99), (1.67, 1.73): (8050, 6670, 8.6, 1.332, 1.84), (1.73, 1.79): (8300, 6800, 9.9, 1.395, 1.61), (1.79, 1.86): (8530, 6920, 11.0, 1.467, 1.45), (1.86, 1.95): (8840, 7090, 14.0, 1.496, 1.29), (1.95, 2.05): (9200, 7280, 17.0, 1.617, 1.12), (2.05, 2.15): (9550, 7480, 20.0, 1.785, 0.972), (2.15, 2.25): (9870, 7670, 24.0, 1.975, 0.851), (2.25, 2.35): (10200, 7880, 29.0, 2.156, 0.75), (2.35, 2.5): (10500, 8090, 34.0, 2.427, 0.669), (2.5, 2.7): (11100, 8510, 47.0, 3.114, 0.535), (2.7, 2.9): (11700, 8970, 62.0, 4.246, 0.436), (2.9, 3.1): (12200, 9430, 81.0, 5.943, 0.362), (3.1, 3.35): (12800, 9910, 100.0, 10.23, 0.305), (3.35, 3.75): (13500, 10600, 150.0, 15.7, 0.241), (3.75, 4.25): (14700, 11800, 240.0, 64.08, 0.171), (4.25, 4.75): (15800, 12900, 370.0, 263.5, 0.127), (4.75, 5.25): (16900, 13800, 540.0, 1620.0, 0.0987), (5.25, 5.75): (17800, 14500, 760.0, 15090.0, 0.0789), (5.75, 6.25): (18800, 15300, 1000.0, 185800.0, 0.0647)}

tableau_multiplicite_etoiles = {(1, 76): 1, (76, 96): 2, (96, 101): 3}

tableau_rapport_de_masses = {(1, 5): 0.05, (5, 9): 0.10, (9, 13): 0.15, (13, 17): 0.20, (17, 21): 0.25, (21, 25): 0.30, (25, 29): 0.35, (29, 32): 0.40, (32, 35): 0.45, (35, 39): 0.50, (39, 44): 0.55, (44, 49): 0.60, (49, 54): 0.65, (54, 59): 0.70, (59, 64): 0.75, (64, 70): 0.80, (70, 77): 0.85, (77, 87): 0.90, (87, 131): 0.95}

tableau_classe_spectrale = {(0, 536): 'Y0', (536, 606): 'T9', (606, 681): 'T8', (681, 761): 'T7', (761, 841): 'T6', (841, 921): 'T5', (921, 1001): 'T4', (1001, 1081): 'T3', (1081, 1156): 'T2', (1156, 1226): 'T1', (1226, 1311): 'T0', (1311, 1411): 'L9', (1411, 1511): 'L8', (1511, 1611): 'L7', (1611, 1716): 'L6', (1716, 1821): 'L5', (1821, 1921): 'L4', (1921, 2021): 'L3', (2021, 2121): 'L2', (2121, 2221): 'L1', (2221, 2346): 'L0', (2346, 2501): 'M9', (2501, 2661): 'M8', (2661, 2821): 'M7', (2821, 2981): 'M6', (2981, 3141): 'M5', (3141, 3301): 'M4', (3301, 3461): 'M3', (3461, 3621): 'M2', (3621, 3776): 'M1', (3776, 3921): 'M0', (3921, 4061): 'K9', (4061, 4201): 'K8', (4201, 4341): 'K7', (4341, 4486): 'K6', (4486, 4636): 'K5', (4636, 4781): 'K4', (4781, 4921): 'K3', (4921, 5061): 'K2', (5061, 5201): 'K1', (5201, 5301): 'K0', (5301, 5361): 'G9', (5361, 5421): 'G8', (5421, 5481): 'G7', (5481, 5541): 'G6', (5541, 5601): 'G5', (5601, 5666): 'G4', (5666, 5736): 'G3', (5736, 5811): 'G2', (5811, 5891): 'G1', (5891, 5976): 'G0', (5976, 6066): 'F9', (6066, 6176): 'F8', (6176, 6306): 'F7', (6306, 6436): 'F6', (6436, 6566): 'F5', (6566, 6696): 'F4', (6696, 6826): 'F3', (6826, 6991): 'F2', (6991, 7156): 'F1', (7156, 7341): 'F0', (7341, 7581): 'A9', (7581, 7826): 'A8', (7826, 8076): 'A7', (8076, 8326): 'A6', (8326, 8576): 'A5', (8576, 8826): 'A4', (8826, 9076): 'A3', (9076, 9326): 'A2', (9326, 9576): 'A1', (9576, 10251): 'A0', (10251, 11351): 'B9', (11351, 12451): 'B8', (12451, 13501): 'B7', (13501, 14501): 'B6', (14501, 15501): 'B5', (15501, 16501): 'B4', (16501, 1000001): 'B3'}

distance_etoile = {(0, 4): (0.015, -8), (4, 6): (0.15, -6), (6, 9): (1.5, -4), (9, 13): (15, -2), (13, 16): (150, 0), (16, 19): (1500, 0)}

excentricite_etoile = {(-10, 4): 0.0, (4, 5): 0.1, (5, 7): 0.2, (7, 9): 0.3, (9, 12): 0.4, (12, 14): 0.5, (14, 16): 0.6, (16, 17): 0.7, (17, 18): 0.8, (18, 19): 0.9}

tableau_densite_disque = {(3, 4): (0.25, -6), (4, 5): (0.32, -5), (5, 6): (0.4, -4), (6, 7): (0.5, -3), (7, 8): (0.6, -2), (8, 9): (0.7, -1), (9, 10): (0.8, 0), (10, 12): (1.0, 0), (12, 13): (1.2, 0), (13, 14): (1.4, 1), (14, 15): (1.7, 2), (15, 16): (2.0, 3), (16, 17): (2.5, 4), (17, 18): (3.2, 5), (18, 19): (4.0, 6)}

numeros_orbites = (0.6, 0.8, 1.2, 1.8, 2.7, 4.0, 6.0, 9.0, 13.5, 20.0, 30.0, 45.0, 68.0, 100.0, 150.0, 220.0)

tableau_planete_instabilite_disque = {(-5, 6): (13, 1), (6, 8): (12, 1), (8, 10): (11, 1), (10, 12): (9, 2), (12, 14): (8, 3), (14, 16): (8, 3), (16, 25): (7, 4)}

tableau_migration = {(3, 9): (6, 1.0), (9, 12): (5, 0.75), (12, 14): (4, 0.5), (14, 15): (3, 0.25), (15, 16): (2, 0.25), (16, 17): (1, 0.25), (17, 19): (0, 0.25)}

tableau_grand_tack = {(3, 9): 1, (9, 17): 2, (17, 19): 3}

tableau_espace_orbite = {(3, 6): -2, (6, 9): -1, (9, 13): 0, (13, 16): 1, (16, 19): 2}

tableau_ratio_orbite = {(3, 4): 0.71, (4, 5): 0.75, (5, 6): 0.78, (6, 7): 0.82, (7, 8): 0.86, (8, 9): 0.91, (9, 10): 0.95, (10, 11): 1, (11, 12): 1.05, (12, 13): 1.1, (13, 14): 1.16, (14, 15): 1.22, (15, 16): 1.28, (16, 17): 1.34, (17, 18): 1.41, (18, 19): 1.48}

tableau_resonance = {(1, 1.2211): (1.221, "4:3"), (1.227, 1.245): (1.237, "11:8"), (1.245, 1.261): (1.251, "7:5"), (1.261, 1.278): (1.268, "10:7"), (1.3, 1.321): (1.31, "3:2"), (1.342, 1.361): (1.352, "11:7"), (1.361, 1.376): (1.368, "8:5"), (1.376, 1.392): (1.382, "13:8"), (1.397, 1.416): (1.406, "5:3"), (1.422, 1.443): (1.432, "12:7"), (1.443, 1.462): (1.452, "7:4"), (1.47, 1.49): (1.48, "9:5"), (1.577, 1.597): (1.587, "2:1")}

tableau_excentricite = {(0, 3): 0.23, (3, 4): 0.15, (4, 5): 0.12, (5, 6): 0.1, (6, 7): 0.08, (7, 8): 0.07, (8, 10): 0.06, (10, 17): 0.05}

tableau_facteur_accretion1 = {(3, 5): 5, (5, 7): 6, (7, 9): 7.5, (9, 13): 10, (13, 15): 12, (15, 17): 15, (17, 19): 20}

tableau_facteur_accretion2 = {(3, 5): 2.5, (5, 7): 3, (7, 9): 4, (9, 13): 5, (13, 15): 6, (15, 17): 7.5, (17, 19): 10}

tableau_facteur_accretion3 = {(3, 5): 1.1, (5, 7): 1.1, (7, 9): 1.1, (9, 13): 1.2, (13, 15): 1.3, (15, 17): 1.5, (17, 19): 2}

ajustement_satellite = {(1, 2): -2, (2, 3): -1, (3, 5): 0, (5, 6): 1, (6, 7): 2}

tableau_ratio_satellites = {(3, 4): (1.406, "5:3"), (4, 5): (1.432, "12:7"), (5, 6): (1.452, "7:4"), (6, 7): (1.480, "9:5"), (7, 8): (1.50, "Aucun"), (8, 9): (1.55, "Aucun"), (9, 13): (1.587, "2:1"), (13, 14): (1.60, "Aucun"), (14, 15): (1.65, "Aucun"), (15, 16): (1.70, "Aucun"), (16, 17): (1.75, None), (17, 18): (1.80, "Aucun"), (18, 19): (1.85, "Aucun")}

tableau_anneau = {(3, 6): "Aucun", (6, 10): "Mince", (10, 14): "Moyen", (14, 19): "Épais"}

tableau_periode_rotation = {(3, 4): 4, (4, 5): 5, (5, 6): 6, (6, 7): 8, (7, 8): 10, (8, 9): 12, (9, 10): 16, (10, 11): 20, (11, 12): 24, (12, 13): 32, (13, 14): 40, (14, 15): 48, (15, 16): 64, (16, 17): 80, (17, 18): 96, (18, 19): 128, (19, 20): 160, (20, 21): 192, (21, 22): 256, (22, 23): 320, (23, 24): 384, (24, 101): "resonance"}

tableau_verrouillage = {(0, 0.12): 1, (0.12, 0.25): 2/3, (0.25, 0.35): 0.5, (0.35, 0.45): 0.4, (0.45, 1): 1/3}

tableau_inclinaison = {(-5, 5): "Extreme", (5, 6): 48, (6, 7): 46, (7, 8): 44, (8, 9): 42, (9, 10): 40, (10, 11): 38, (11, 12): 36, (12, 13): 34, (13, 14): 32, (14, 15): 30, (15, 16): 28, (16, 17): 26, (17, 18): 24, (18, 19): 22, (19, 20): 20, (20, 21): 18, (21, 22): 16, (22, 23): 14, (23, 24): 12, (24, 25): 10, (25, 101): "Minimale"}

tableau_inclinaison_extreme = {(1, 3): 50, (3, 4): 60, (4, 5): 70, (5, 6): 80, (6, 7): 90}

tableau_prevalence_eau_initiale = {(-100, -4): ("Traces", 0.0), (-4, 0): ("Minimale", 0.0), (0, 1): ("Minimale", 0.01), (1, 2): ("Minimale", 0.02), (2, 3): ("Minimale", 0.03), (3, 4): ("Minimale", 0.05), (4, 5): ("Moderee", 0.075), (5, 6): ("Moderee", 0.1), (6, 7): ("Moderee", 0.2), (7, 8): ("Moderee", 0.3), (8, 9): ("Moderee", 0.4), (9, 10): ("Moderee", 0.5), (10, 11): ("Moderee", 0.55), (11, 12): ("Moderee", 0.6), (12, 13): ("Grande", 0.65), (13, 14): ("Grande", 0.7), (14, 15): ("Grande", 0.75), (15, 16): ("Grande", 0.8), (16, 17): ("Grande", 0.85), (17, 18): ("Grande", 0.9), (18, 19): ("Grande", 0.95), (19, 20): ("Grande", 0.975), (20, 101): ("Massive", 1.0)}

tableau_geologie = {(-100, 16): ("Fondue", 5, 6), (16, 24): ("Molle", 4, 4), (24, 32): ("Jeune", 3, 2), (32, 64): ("Mature", 2, 0), (64, 88): ("Ancienne", 1, -2), (88, 1000): ("Solide", 0, -4)}

tableau_champ_magnetique = {(0, 15): ("Aucun", -6), (15, 18): ("Faible", -4), (18, 20): ("Modere", -2), (20, 30): ("Fort", 0)}

tableau_albedo = {"Traces": 0.15, "Minimale": 0.16, "Moderee": 0.19, "Grande": 0.22, "Massive": 0.25}

tableau_albedo_classe_6 = {"Traces": 0.01, "Minimale": 0.02, "Moderee": 0.08, "Grande": 0.14, "Massive": 0.20}

tableau_photosynthese = {'B3': 0.09, 'B4': 0.09, 'B5': 0.09, 'B6': 0.09, 'B7': 0.09, 'B8': 0.09, 'B9': 0.09, 'A0': 0.1, 'A1': 0.1, 'A2': 0.1, 'A3': 0.1, 'A4': 0.1, 'A5': 0.1, 'A6': 0.1, 'A7': 0.1, 'A8': 0.1, 'A9': 0.1, 'F0': 0.1, 'F1': 0.1, 'F2': 0.1, 'F3': 0.1, 'F4': 0.1, 'F5': 0.1, 'F6': 0.1, 'F7': 0.1, 'F8': 0.1, 'F9': 0.1, 'G0': 0.1, 'G1': 0.1, 'G2': 0.1, 'G3': 0.1, 'G4': 0.1, 'G5': 0.1, 'G6': 0.1, 'G7': 0.1, 'G8': 0.105, 'G9': 0.105, 'K0': 0.11, 'K1': 0.115, 'K2': 0.12, 'K3': 0.13, 'K4': 0.145, 'K5': 0.16, 'K6': 0.18, 'K7': 0.21, 'K8': 0.24, 'K9': 0.27, 'M0': 0.3, 'M1': 0.3, 'M2': 0.3, 'M3': 0.3, 'M4': 0.3, 'M5': 0.3, 'M6': 0.3, 'M7': 0.3, 'M8': 0.3, 'M9': 0.3}

tableau_effet_de_serre_eau = {(0, 260): 0, (260, 261): 16, (261, 263): 17, (263, 266): 18, (266, 269): 19, (269, 271): 20, (271, 274): 21, (274, 277): 22, (277, 280): 23, (280, 283): 24, (283, 287): 25, (287, 290): 26, (290, 294): 27, (294, 297): 28, (297, 301): 29, (301, 305): 30, (305, 310): 31, (310, 314): 32, (314, 319): 33}

class Sys:
    def __init__(self, age, metallicite):
        self.age = age
        self.metallicite = metallicite
        self.etoiles = []
        self.planetes = []

    def generer_etoiles(self):
        liste_etoiles = []
        categorie_masse_primaire = chercher_tableau(random1d100(), tableau_categories_masses, True)
        if categorie_masse_primaire == "naine_brune":
            masse_primaire = chercher_tableau(random1d100(), naine_brune, True)
        elif categorie_masse_primaire == "faible_masse":
            masse_primaire = chercher_tableau(random1d100(), faible_masse, True)
        elif categorie_masse_primaire == "masse_intermediaire":
            masse_primaire = chercher_tableau(random1d100(), masse_intermediaire, True)
        else:
            masse_primaire = chercher_tableau(random1d100(), haute_masse, True)
        etoile_primaire = Etoile(self.age, masse_primaire)
        etoile_primaire.definir_caracteristiques(None, None, None, None, None, False, None, self.metallicite)
        liste_etoiles.append(etoile_primaire)
        chances_multiplicites = randomd6(3)
        if (chances_multiplicites >= 14) or (chances_multiplicites >= 13 and masse_primaire >= 0.08) or (chances_multiplicites >= 12 and masse_primaire >= 0.7) or (chances_multiplicites >= 11 and masse_primaire >= 1) or (chances_multiplicites >= 10 and masse_primaire >= 1.3):
            nombre_etoiles = chercher_tableau(random1d100(), tableau_multiplicite_etoiles, True)
            if nombre_etoiles == 1:
                configuration = (0, 0)
                mod_masse = (0, 0)
                mod_distance = (0, 0)
            elif nombre_etoiles == 2 and randomd6(1) < 4:
                configuration = (0, 1)
                mod_masse = (0, 30)
                mod_distance = (0, -3)
            elif nombre_etoiles == 2:
                configuration = (0, 0)
                mod_masse = (30, 0)
                mod_distance = (-3, 0)
            else:
                configuration = (0, 0, 2)
                mod_masse = (30, 0, 30)
                mod_distance = (-3, 0, -3)
            for etoile in range(nombre_etoiles):
                etoile_secondaire = Etoile(self.age, (liste_etoiles[configuration[etoile]].ancienne_masse*chercher_tableau(random1d100()+mod_masse[etoile], tableau_rapport_de_masses, True)))
                etoile_secondaire.centre_de_masse = configuration[etoile]
                etoile_secondaire.definir_caracteristiques(None, None, None,None, None, False, None, self.metallicite)
                separation = chercher_tableau(randomd6(3)+mod_distance[etoile], distance_etoile, True)
                etoile_secondaire.distance[1] = separation[0]*math.pow(10, (random1d100()*0.01))
                excentricite = chercher_tableau(randomd6(3)+separation[1], excentricite_etoile, True)
                etoile_secondaire.distance[0] = etoile_secondaire.distance[1]*(1-excentricite)
                etoile_secondaire.distance[2] = etoile_secondaire.distance[1]*(1+excentricite)
                liste_etoiles.append(etoile_secondaire)
        return liste_etoiles

    def generer_planetes(self):
        liste_planetes_finale = []
        deja_orbite_p = False
        etoile_orbite_p = None
        i = 0
        densite_disque = chercher_tableau(randomd6(3), tableau_densite_disque, True)
        masse_planetesimale = densite_disque[0]*self.etoiles[0].ancienne_masse*self.metallicite
        for etoile in self.etoiles:
            liste_planetes = []
            liste_orbites = {}
            zone_interdite = 9999999999999999999999
            vraie_orbite_0 = 0
            facteur_masse_planetesimale = 1
            bonus_bombardement_grand_tack = 0
            bonus_bombardement_kuiper = 0
            if (etoile.distance[1]-self.etoiles[etoile.centre_de_masse].distance[1]) <= 1.5 and i != 0:
                masse_etoile_effective = etoile.ancienne_masse + self.etoiles[etoile.centre_de_masse].ancienne_masse
                luminosite_effective = etoile.luminosite + self.etoiles[etoile.centre_de_masse].luminosite
                ancienne_luminosite_effective = etoile.ancienne_lum + self.etoiles[etoile.centre_de_masse].ancienne_lum
                for etoile2 in self.etoiles:
                    if self.etoiles[etoile2.centre_de_masse] == etoile and etoile2.distance[1] <= 1.5:
                        masse_etoile_effective += etoile2.ancienne_masse
                        luminosite_effective += etoile2.luminosite
                        ancienne_luminosite_effective += etoile2.ancienne_lum
                if etoile.centre_de_masse == 0 and deja_orbite_p:
                    masse_etoile_effective += etoile_orbite_p.ancienne_masse
                    luminosite_effective += etoile_orbite_p.luminosite
                    ancienne_luminosite_effective += etoile_orbite_p.ancienne_lum
                liste_orbites[0] = Orbite((etoile.distance[2]-self.etoiles[etoile.centre_de_masse].distance[0])*3.5)
                if etoile.centre_de_masse == 0:
                    deja_orbite_p = True
                    etoile_orbite_p = etoile
                n = 0
                for planete in liste_planetes_finale:
                    if planete.centre_de_masse == etoile.centre_de_masse or self.etoiles[planete.centre_de_masse] == etoile_orbite_p:
                        liste_planetes_finale.pop(n)
                    n += 1
                assert zone_interdite == 9999999999999999999999
            else:
                masse_etoile_effective = etoile.ancienne_masse
                luminosite_effective = etoile.luminosite
                ancienne_luminosite_effective = etoile.ancienne_lum
                liste_orbites[0] = Orbite(randomd6(2)*0.005*math.pow(etoile.ancienne_masse, 1/3))
            ligne_glace = 4 * math.pow(luminosite_effective, 0.5)
            ligne_accretion_lente = 20 * math.pow(masse_etoile_effective, 1/3)
            for etoile2 in self.etoiles:
                if etoile2.distance[1] > etoile.distance[1]:
                    if etoile2.distance[1]-etoile.distance[1] > 1.5 and (etoile2.distance[0]-etoile.distance[2])/3 < zone_interdite :
                        zone_interdite = (etoile2.distance[0]-etoile.distance[2])/3
                else:
                    if etoile.distance[1]-etoile2.distance[1] > 1.5 and (etoile.distance[0]-etoile2.distance[2])/3 < zone_interdite :
                        zone_interdite = (etoile.distance[0]-etoile2.distance[2])/3
            i_orbite = 0
            for orbite in numeros_orbites:
                nouvelle_orbite = Orbite(orbite * math.pow(ancienne_luminosite_effective, 0.5))
                if nouvelle_orbite.distance >= ligne_glace:
                    nouvelle_orbite.est_ligne_des_glaces = True
                if nouvelle_orbite.distance >= ligne_accretion_lente:
                    nouvelle_orbite.est_accretion_lente = True
                if nouvelle_orbite.distance >= zone_interdite:
                    nouvelle_orbite.est_interdite = True
                if nouvelle_orbite.distance < liste_orbites[0].distance:
                    nouvelle_orbite.distance = liste_orbites[0].distance
                    vraie_orbite_0 = i_orbite
                liste_orbites[i_orbite] = nouvelle_orbite
                i_orbite += 1
            if randomd6(3) >= 12:
                liste_planetes_instabilite = []
                instabilite = chercher_tableau(randomd6(3) + densite_disque[1], tableau_planete_instabilite_disque,True)
                for n in range(instabilite[1]):
                    planete = Planete(self.age, 0)
                    planete.centre_de_masse = i
                    planete.formation = "instabilite_disque"
                    planete.numero_orbite = instabilite[0] + n
                    planete.distance[1] = liste_orbites[planete.numero_orbite].distance
                    planete.categorie = "geante_gazeuse"
                    if masse_etoile_effective <= 0.5:
                        planete.masse = randomd6(3) * masse_etoile_effective * densite_disque[0]
                    else:
                        planete.masse = randomd6(3) * ((100 * masse_etoile_effective * densite_disque[0]) - 38)
                    if planete.distance[1] < zone_interdite and planete.masse >= 5:
                        liste_planetes_instabilite.append(planete)
                        liste_orbites[planete.numero_orbite].contient_planete = True
                liste_planetes += liste_planetes_instabilite
            if not liste_orbites[6].est_interdite:
                maximum_accretion = 4
                liste_planete_accretion = []
                orbite_accretion = 6
                nombre_planetes_accretion = 0
                if masse_planetesimale < 0.11:
                    maximum_accretion = 0
                elif masse_planetesimale < 0.17:
                    maximum_accretion = 1
                elif densite_disque[0] < 0.24:
                    maximum_accretion = 2
                while orbite_accretion < len(liste_orbites) and not liste_orbites[orbite_accretion].est_accretion_lente and not liste_orbites[orbite_accretion].contient_planete and not liste_orbites[orbite_accretion].est_interdite:
                    nombre_planetes_accretion += 1
                    orbite_accretion += 1
                nombre_planetes_accretion += chercher_tableau(randomd6(3), tableau_espace_orbite, True)
                if maximum_accretion < nombre_planetes_accretion:
                    nombre_planetes_accretion = maximum_accretion
                if nombre_planetes_accretion < 0:
                    nombre_planetes_accretion = 0
                if nombre_planetes_accretion > 0:
                    planete_premiere = Planete(self.age, 0)
                    planete_premiere.centre_de_masse = i
                    planete_premiere.formation = "accrétion"
                    planete_premiere.masse = (randomd6(3) + 20) * masse_planetesimale
                    if planete_premiere.masse >= 5:
                        planete_premiere.categorie = "geante_gazeuse"
                        planete_premiere.masse = planete_premiere.masse * chercher_tableau(randomd6(3), tableau_facteur_accretion1, True)
                    else:
                        planete_premiere.categorie = "planete_rocheuse"
                    migration_planetaire = list(chercher_tableau(randomd6(3), tableau_migration, True))
                    if migration_planetaire[0] < vraie_orbite_0:
                        migration_planetaire[0] = vraie_orbite_0
                    planete_premiere.numero_orbite = migration_planetaire[0]
                    facteur_masse_planetesimale = migration_planetaire[1]
                    for orbite in range(planete_premiere.numero_orbite, 7):
                        liste_orbites[orbite].mod_epuisement = 0.1
                    if nombre_planetes_accretion > 1 and randomd6(3) > 12:
                        bonus_bombardement_grand_tack = 6
                        n = 0
                        grand_tack = chercher_tableau(randomd6(3), tableau_grand_tack, True)
                        while n < grand_tack and not liste_orbites[planete_premiere.numero_orbite + 1].contient_planete and not liste_orbites[planete_premiere.numero_orbite + 1].est_interdite:
                            planete_premiere.numero_orbite += 1
                            n += 1
                    liste_orbites[planete_premiere.numero_orbite].contient_planete = True
                    planete_premiere.distance[1] = liste_orbites[planete_premiere.numero_orbite].distance
                    liste_planete_accretion.append(planete_premiere)
                    orbite_accretion = planete_premiere.numero_orbite+1
                    n = 1
                    while orbite_accretion < len(liste_orbites) and n < nombre_planetes_accretion and not liste_orbites[orbite_accretion].contient_planete:
                        planete = Planete(self.age, 0)
                        planete.centre_de_masse = i
                        planete.formation = "accretion"
                        planete.numero_orbite = orbite_accretion
                        planete.distance[1] = liste_orbites[planete.numero_orbite].distance
                        if n == 1:
                            planete.masse = (randomd6(3) + 10) * masse_planetesimale
                            if planete.masse >= 5:
                                planete.categorie = "geante_gazeuse"
                                planete.masse = planete.masse * chercher_tableau(randomd6(3), tableau_facteur_accretion2,True)
                            else:
                                planete.categorie = "planete_rocheuse"
                                planete.formation = "accretion_ratee"
                        else:
                            planete.masse = (randomd6(3) + 4) * masse_planetesimale
                            if planete.masse >= 5:
                                planete.categorie = "geante_gazeuse"
                                planete.masse = planete.masse * chercher_tableau(randomd6(3), tableau_facteur_accretion3, True)
                            else:
                                planete.categorie = "planete_rocheuse"
                        if planete.distance[1] < zone_interdite:
                            liste_planete_accretion.append(planete)
                            liste_orbites[planete.numero_orbite].contient_planete = True
                        n += 1
                        orbite_accretion += 1
                liste_planetes += liste_planete_accretion
                liste_planetes.sort(key=lambda x: x.numero_orbite)
            if (len(liste_planetes) == 0 or liste_planetes[0].numero_orbite > vraie_orbite_0+1) and not liste_orbites[vraie_orbite_0+1].est_interdite:
                liste_planetes_oligarches = []
                orbite_collision = vraie_orbite_0+1
                nombre_planetes_collision = 0
                while orbite_collision < 6 and not liste_orbites[orbite_collision].contient_planete and not liste_orbites[orbite_collision].est_interdite:
                    nombre_planetes_collision += 1
                    orbite_collision += 1
                espace_orbite = chercher_tableau(randomd6(3), tableau_espace_orbite, True)
                nombre_planetes_collision += espace_orbite
                if espace_orbite > 0:
                    orbite_collision = vraie_orbite_0
                else:
                    orbite_collision = vraie_orbite_0 + 1
                n = 0
                while orbite_collision < len(liste_orbites) and not liste_orbites[orbite_collision].contient_planete and n < nombre_planetes_collision:
                    planete = Planete(self.age, 0)
                    planete.centre_de_masse = i
                    planete.formation = "collision_oligarche"
                    planete.numero_orbite = orbite_collision
                    planete.distance[1] = liste_orbites[planete.numero_orbite].distance
                    if liste_orbites[planete.numero_orbite + 1].contient_planete:
                        planete.categorie = "ceinture_asteroide"
                    else:
                        planete.categorie = "planete_rocheuse"
                        planete.masse = randomd6(3)/5 * masse_planetesimale * facteur_masse_planetesimale * liste_orbites[orbite_collision].mod_epuisement
                    if planete.distance[1] < zone_interdite:
                        liste_planetes_oligarches.append(planete)
                        liste_orbites[planete.numero_orbite].contient_planete = True
                    n += 1
                    orbite_collision += 1
                liste_planetes += liste_planetes_oligarches
            liste_planetes.sort(key=lambda x: x.numero_orbite)
            if len(liste_planetes) > 0:
                if liste_planetes[0].numero_orbite > vraie_orbite_0:
                    liste_planetes[0].distance[1] *= (0.72 + randomd6(2)/25)
                liste_planetes[0].excentricite = chercher_tableau(len(liste_planetes), tableau_excentricite, True) + ((randomd6(2) - 7) * 0.01)
                liste_planetes[0].distance[0] = liste_planetes[0].distance[1] * (1 - liste_planetes[0].excentricite)
                liste_planetes[0].distance[2] = liste_planetes[0].distance[1] * (1 + liste_planetes[0].excentricite)
            if len(liste_planetes) > 1:
                if liste_planetes[-1].formation == "collision oligarche":
                    if ligne_glace < zone_interdite:
                        liste_planetes[-1].distance[1] = ligne_glace * (0.72 + randomd6(2) / 50)
                    else:
                        liste_planetes[-1].distance[1] = zone_interdite * (0.72 + randomd6(2) / 50)
                else:
                    liste_planetes[-1].distance[1] = liste_planetes[-1].distance[1] * (0.72 + randomd6(2)/25)
                liste_planetes[-1].excentricite = chercher_tableau(len(liste_planetes), tableau_excentricite, True) + ((randomd6(2) - 7) * 0.01)
                liste_planetes[-1].distance[0] = liste_planetes[-1].distance[1] * (1 - liste_planetes[-1].excentricite)
                liste_planetes[-1].distance[2] = liste_planetes[-1].distance[1] * (1 + liste_planetes[-1].excentricite)
            if len(liste_planetes) > 2:
                resonance_laplace = False
                ratio_orbite = math.pow(liste_planetes[-1].distance[1]/liste_planetes[0].distance[1], 1/(len(liste_planetes)-1))
                n = 1
                for planete in liste_planetes:
                    if planete != liste_planetes[0]:
                        if resonance_laplace:
                            planete.distance[1] = liste_planetes[n - 1].distance[1] * 1.587
                            planete.resonance = "2:1"
                            resonance_laplace = False
                        else :
                            ratio_corrige = ratio_orbite*chercher_tableau(randomd6(3), tableau_ratio_orbite, True)
                            if chercher_tableau(ratio_corrige, tableau_resonance, True) is not None:
                                planete.distance[1] = liste_planetes[n-1].distance[1]*chercher_tableau(ratio_corrige, tableau_resonance, True)[0]
                                planete.resonance = chercher_tableau(ratio_corrige, tableau_resonance, True)[1]
                                if planete.resonance == "2:1":
                                    if liste_planetes[n+1] == liste_planetes[-1]:
                                        planete.distance[1] *= 1.008
                                        planete.resonance = "Aucune"
                                    resonance_laplace = True
                            else:
                                planete.distance[1] = liste_planetes[n - 1].distance[1] * ratio_corrige
                        planete.excentricite = chercher_tableau(len(liste_planetes), tableau_excentricite, True) + ((randomd6(2) - 7) * 0.01)
                        planete.distance[0] = planete.distance[1]*(1-planete.excentricite)
                        planete.distance[2] = planete.distance[1]*(1+planete.excentricite)
                        if planete.distance[2] >= zone_interdite:
                            liste_planetes.pop(n)
                        elif planete.distance[2] >= ligne_accretion_lente:
                            bonus_bombardement_kuiper = 3
                        n += 1
            if len(liste_planetes) > 0 and liste_planetes[-1].distance[2] >= ligne_accretion_lente:
                bonus_bombardement_kuiper = 3
            bonus_bombardement = bonus_bombardement_grand_tack + bonus_bombardement_kuiper
            n = 0
            for planete in liste_planetes:
                if planete.categorie == "geante_gazeuse" and planete.masse <= 200:
                    planete.densite = 1 / math.pow(planete.masse, 0.5)
                elif planete.categorie == "geante_gazeuse":
                    planete.densite = math.pow(planete.masse, 1.27) / 11800
                elif planete.categorie == "planete_rocheuse":
                    planete.densite = math.pow(planete.masse, 0.2) + ((randomd6(3) - 10) * 0.01)
                    if planete.categorie == "reste_oligarche" and randomd6(1) > 4:
                        planete.densite += 0.4
                    elif planete.categorie == "accretion_ratee":
                        planete.densite -= 0.1
                    if planete.densite < 0.18:
                        planete.densite = 0.18
                    elif planete.densite > 1.43:
                        planete.densite = 1.43
                if not planete.categorie == "ceinture_asteroide":
                    planete.rayon = 6370 * math.pow(planete.masse / planete.densite, 1 / 3)
                    planete.gravite = math.pow(planete.masse * planete.densite * planete.densite, 1 / 3)
                    sphere_hill = 2.17 * math.pow(10, 6) * planete.distance[0] * math.pow(planete.masse / masse_etoile_effective, 1 / 3)
                    nombre_satellites = int(2 * math.pow(10, -15) * math.pow(sphere_hill, 2) / math.pow(planete.distance[1],0.5))
                    if nombre_satellites > 0:
                        planete.anneau = chercher_tableau(randomd6(3), tableau_anneau, True)
                        nombre_satellites += chercher_tableau(randomd6(1), ajustement_satellite, True)
                        if nombre_satellites < 0:
                            nombre_satellites = 0
                        if nombre_satellites > 8:
                            nombre_satellites = 8
                    resonance_laplace = False
                    liste_satellites = []
                    for satellite in range(nombre_satellites):
                        satellite = Planete(self.age, math.pow(10, -5) * randomd6(3) * planete.masse / nombre_satellites)
                        satellite.centre_de_masse = n
                        if len(liste_satellites) == 0:
                            satellite.distance[1] = planete.rayon * (randomd6(1) + 2)
                        elif resonance_laplace:
                            satellite.distance[1] = liste_satellites[-1].distance[1] * 1.587
                            satellite.resonance = "2:1"
                            resonance_laplace = False
                        else:
                            ratio = chercher_tableau(randomd6(3), tableau_ratio_satellites, True)
                            satellite.distance[1] = liste_satellites[-1].distance[1] * ratio[0]
                            satellite.resonance = ratio[1]
                            if satellite.resonance == "2:1":
                                resonance_laplace = True
                        liste_satellites.append(satellite)
                        n += 1
                    if (sphere_hill / planete.rayon) > 300 and randomd6(1) > 4:
                        satellite = Planete(self.age, math.pow(10, -3) * randomd6(3) * planete.masse)
                        satellite.distance[1] = (randomd6(3) + 7) * planete.rayon * 4
                        liste_satellites.append(satellite)
                    planete.satellites += liste_satellites
                    for satellite in planete.satellites:
                        satellite.categorie = "planete_rocheuse"
                        if planete.distance[1] < ligne_glace or (planete.masse > 200 and satellite.distance[1] < 600000):
                            satellite.formation = "satellite_rocheux"
                            satellite.densite = math.pow(satellite.masse, 0.2) + ((randomd6(3) + 10) * 0.01)
                        else:
                            satellite.formation = "satellite_glace"
                            satellite.densite = math.pow(satellite.masse, 0.2) + ((randomd6(3) - 20) * 0.01)
                        satellite.rayon = 6370 * math.pow(satellite.masse / satellite.densite, 1 / 3)
                        satellite.gravite = math.pow(satellite.masse * satellite.densite * satellite.densite, 1 / 3)
                        satellite.distance[0] = satellite.distance[1]
                        satellite.distance[2] = satellite.distance[1]
                if planete.categorie == "planete_rocheuse":
                    planete.definir_caracteristiques(masse_etoile_effective, luminosite_effective, ancienne_luminosite_effective, etoile, self.etoiles, False, bonus_bombardement, self.metallicite)
                elif planete.categorie == "geante_gazeuse" and len(planete.satellites) > 0:
                    for satellite in planete.satellites:
                        satellite.definir_caracteristiques(masse_etoile_effective, luminosite_effective, ancienne_luminosite_effective, planete, self.etoiles, True, bonus_bombardement, self.metallicite)
            if self.etoiles[-1] != etoile and self.etoiles[i+1].distance[1] <= 1.5:
                liste_planetes = []
            liste_planetes_finale += liste_planetes
            i += 1
        for planete in liste_planetes_finale:
            if planete.categorie == "planete_rocheuse":
                assert planete.temp > 0
        return liste_planetes_finale

class Astre:
    def __init__(self, age, masse):
        self.age = age
        self.masse = masse
        self.temp = 0
        self.rayon = 0
        self.ancienne_masse = masse
        self.centre_de_masse = 0
        self.distance = [0, 0, 0]
        self.categorie = ""

    def definir_caracteristiques(self, masse, luminosite, ancienne_lum, centre_de_masse, liste_etoiles, est_satellite, bonus_bomb, metallicite):
        pass

class Etoile(Astre):
    def __init__(self, age, masse):
        super().__init__(age, masse)
        self.luminosite = 0
        self.ancienne_lum = 0
        self.classe_spectrale = ""

    def definir_caracteristiques(self, masse, luminosite, ancienne_lum, centre_de_masse, liste_etoiles, est_satellite, bonus_bomb, metallicite):
        self.ancienne_masse = self.masse
        if self.masse < 0.08:
            self.temp = 18600*(math.pow(self.masse, 0.8))/math.pow(self.age, 0.3)
            if self.temp > 3000:
                self.temp = 3000
            self.rayon = 70000
            self.luminosite = math.pow(self.temp, 4)/(1.1*math.pow(10, 17))
            self.ancienne_lum = 0.00075
            self.categorie = "naine_brune"
        elif 0.08 <= self.masse <= 0.5:
            self.temp = chercher_tableau(self.masse, tableau_temp_faible_masse, True)[0]
            self.luminosite = chercher_tableau(self.masse, tableau_temp_faible_masse, True)[1]
            self.ancienne_lum = self.luminosite
            self.rayon = 2.315*math.pow(10, 13)*math.pow(self.luminosite, 0.5)/math.pow(self.temp, 2)
            self.categorie = "etoile_sequence_principale"
        else:
            evolution = chercher_tableau(self.masse, tableau_temp_sequence_principale, True)
            if self.age <= evolution[4]:
                self.temp = evolution[0] + (self.age/evolution[4])*(evolution[1]-evolution[0])
                if self.age <= evolution[4]*0.8:
                    self.luminosite = evolution[2]*math.pow(evolution[3], self.age)
                else:
                    self.luminosite = evolution[2]*math.pow(evolution[3], (3*self.age-1.6*evolution[4]))
                self.rayon = 2.315*math.pow(10, 13) * math.pow(self.luminosite, 0.5) / math.pow(self.temp, 2)
                self.ancienne_lum = self.luminosite
                self.categorie = "etoile_sequence_principale"
            elif self.age > evolution[4]*1.15:
                self.ancienne_lum = evolution[2]
                self.masse = (self.masse/10.4)+0.43
                self.temp = 13500*math.pow(self.masse, 0.25)/math.pow(self.age, 0.5)
                self.rayon = 5500/math.pow(self.masse, 3)
                self.luminosite = (math.pow(self.rayon, 2)*math.pow(self.temp, 4))/(5.4*math.pow(10, 26))
                self.categorie = "naine_blanche"
            else:
                stade_evolution = random1d100()
                if stade_evolution in range(1, 61):
                    self.temp = 5000
                    self.luminosite = evolution[2]*math.pow(evolution[3], 1.4*evolution[4])
                    self.categorie = "sous-geante"
                elif stade_evolution in range(61, 91):
                    branche_geante_rouge = random1d100()
                    self.temp = 5000 - (branche_geante_rouge*0.01*2000)
                    self.luminosite = math.pow(50, (1 + branche_geante_rouge))
                    self.categorie = "geante_rouge"
                else:
                    self.temp = 5000
                    self.luminosite = 50 + random1d100()*50*0.01
                    self.categorie = "geante_rouge"
                self.ancienne_lum = self.luminosite
                self.rayon = 2.315*math.pow(10, 13) * math.pow(self.luminosite, 0.5) / math.pow(self.temp, 2)
        if self.categorie == "naine_blanche":
            self.classe_spectrale = "D"
        else:
            self.classe_spectrale = chercher_tableau(self.temp, tableau_classe_spectrale, True)

class Planete(Astre):
    def __init__(self, age, masse):
        super().__init__(age, masse)
        self.formation = ""
        self.numero_orbite = 0
        self.resonance = "Aucune"
        self.excentricite = 0
        self.densite = 0
        self.gravite = 0
        self.satellites = []
        self.anneau = "Aucun"
        self.periode_orbitale = 0
        self.periode_rotation = 0
        self.verrouillage = False
        self.inclinaison_axiale = 0
        self.instabilite = False
        self.temperature_corps_noir = 0
        self.nombre_m = 0
        self.quantite_eau = "Traces"
        self.hydrographie = 0
        self.a_subi_un_effet_de_serre = False
        self.type_effet_de_serre = "Aucun"
        self.geologie = ("Solide", 0, -4)
        self.tectonique_mobile = False
        self.champ_magnetique = ("Aucun", -6)
        self.atmosphere = {"Hydrogene": 0, "Helium": 0, "Azote": 0, "CO2": 0}
        self.albedo = 0
        self.cycle_silicate_carbone = False
        self.contient_vie = False
        self.profil_vie = {}
        self.contient_dioxygene = False

    def definir_caracteristiques(self, masse, luminosite, ancienne_lum, centre_de_masse, liste_etoiles, est_satellite, bonus_bomb, metallicite):
        if est_satellite:
            self.periode_orbitale = math.pow(10, -6)*math.pow(self.distance[1]/(centre_de_masse.masse + self.masse), 0.5)
            self.periode_rotation = self.periode_orbitale
            self.inclinaison_axiale = randomd6(3)-8
            if self.inclinaison_axiale < 0:
                self.inclinaison_axiale = 0
            if len(liste_etoiles) == 1:
                self.temperature_corps_noir = 278*math.pow(luminosite, 0.25)/math.pow(liste_etoiles[centre_de_masse.centre_de_masse].distance[1], 1/2)
            else:
                temperature_initiale = 0
                for etoile in liste_etoiles:
                    if etoile.distance[1] <= liste_etoiles[centre_de_masse.centre_de_masse].distance[1]:
                        temperature_initiale += math.pow(etoile.luminosite/math.pow(centre_de_masse.distance[1]+liste_etoiles[centre_de_masse.centre_de_masse].distance[1]-etoile.distance[1], 2), 0.25)
                    else:
                        temperature_initiale += math.pow(etoile.luminosite/math.pow(etoile.distance[1]-(centre_de_masse.distance[1]+liste_etoiles[centre_de_masse.centre_de_masse].distance[1]), 2), 0.25)
                self.temperature_corps_noir = temperature_initiale*278
        else:
            self.periode_orbitale = 8770/24*math.pow(math.pow(self.distance[1], 3)/self.masse, 0.5)
            if len(self.satellites) > 0:
                periode_estimee = math.pow(10, 25)*(self.age*math.pow(self.satellites[0].masse, 2)*math.pow(self.rayon, 3))/(self.masse*math.pow(self.satellites[0].distance[1], 6))
                if periode_estimee >= 2:
                    self.periode_rotation = self.satellites[0].periode_orbitale
                else:
                    self.periode_rotation = chercher_tableau(periode_estimee*12+randomd6(3), tableau_periode_rotation, True)
                    if self.periode_rotation == "resonance" or self.periode_rotation > self.satellites[0].periode_orbitale:
                        self.periode_rotation = self.satellites[0].periode_orbitale
                self.inclinaison_axiale = chercher_tableau(periode_estimee*12+randomd6(3), tableau_inclinaison, True)
            else:
                periode_estimee = 9.6*math.pow(10, -14) * (self.age * math.pow(masse, 2) * math.pow(self.rayon, 3)) / (self.masse * math.pow(self.distance[1], 6))
                if periode_estimee >= 2:
                    self.periode_rotation = self.periode_orbitale*chercher_tableau(self.excentricite, tableau_verrouillage, True)
                    self.verrouillage = True
                else:
                    self.periode_rotation = chercher_tableau((periode_estimee * 12 + randomd6(3)),tableau_periode_rotation, True)
                    if self.periode_rotation == "resonance":
                        self.periode_rotation = self.periode_orbitale * chercher_tableau(self.excentricite, tableau_verrouillage, True)
                        self.verrouillage = True
                    elif self.periode_rotation > self.periode_orbitale:
                        self.periode_rotation = self.periode_orbitale
                        self.verrouillage = True
                if self.verrouillage:
                    self.inclinaison_axiale = randomd6(3) - 8
                    if self.inclinaison_axiale < 0:
                        self.inclinaison_axiale = 0
                else:
                    instabilite = randomd6(3)
                    if instabilite < 8:
                        instabilite = -7
                    elif instabilite > 13:
                        instabilite = 7
                    else:
                        instabilite = 0
                    self.inclinaison_axiale = chercher_tableau(periode_estimee * 12 + randomd6(3) + instabilite, tableau_inclinaison,True)
            if self.inclinaison_axiale == "Extreme":
                self.inclinaison_axiale = chercher_tableau(randomd6(1), tableau_inclinaison_extreme, True)
            elif self.inclinaison_axiale == "Minimale":
                self.inclinaison_axiale = randomd6(3) - 8
                if self.inclinaison_axiale < 0:
                    self.inclinaison_axiale = 0
            if len(liste_etoiles) == 1:
                self.temperature_corps_noir = 278*math.pow(luminosite, 0.25)/math.pow(self.distance[1], 1/2)
            else:
                temperature_initiale = 0
                for etoile in liste_etoiles:
                    if etoile.distance[1] <= centre_de_masse.distance[1]:
                        temperature_initiale += math.pow(etoile.luminosite/math.pow(self.distance[1]+centre_de_masse.distance[1]-etoile.distance[1], 2), 0.25)
                    else:
                        temperature_initiale += math.pow(etoile.luminosite/math.pow(etoile.distance[1]-(self.distance[1]+centre_de_masse.distance[1]), 2), 0.25)
                self.temperature_corps_noir = temperature_initiale*278
        self.nombre_m = 700000 * self.temperature_corps_noir / (self.densite * math.pow(self.rayon, 2))
        if 1 < self.nombre_m < 4:
            self.nombre_m = 5
        if self.nombre_m < 2:
            self.quantite_eau = "Massive"
            self.hydrographie = 1.0
        elif self.nombre_m > 29:
            if self.temperature_corps_noir > 125 or self.formation == "satellite_rocheux":
                self.quantite_eau = "Traces"
                self.hydrographie = 0.0
            else:
                self.quantite_eau = "Massive"
                self.hydrographie = 1.0
        elif self.distance[1] > 4 * math.pow(ancienne_lum, 0.5):
            self.quantite_eau = "Massive"
            self.hydrographie = 1.0
        else:
            eau = chercher_tableau(randomd6(3) - self.nombre_m + bonus_bomb, tableau_prevalence_eau_initiale, True)
            self.quantite_eau = eau[0]
            self.hydrographie = eau[1]
        if self.temperature_corps_noir + randomd6(3) >= 318 and self.nombre_m > 2:
            if self.hydrographie >= 0.075:
                self.a_subi_un_effet_de_serre = True
                self.type_effet_de_serre = "Sec"
            self.quantite_eau = "Traces"
            self.hydrographie = 0.0
        if self.temperature_corps_noir + randomd6(3) >= 158 and self.nombre_m < 2:
            self.a_subi_un_effet_de_serre = True
            self.type_effet_de_serre = "Humide"
        mod_chaleur_primordiale = randomd6(3)+(self.age*8)-60*math.log(self.gravite, 10)-10*math.log(metallicite, 10)
        self.geologie = chercher_tableau(mod_chaleur_primordiale, tableau_geologie, True)
        if self.geologie[0] == "Jeune" or self.geologie[0] == "Mature" or self.geologie[0] == "Ancien":
            mod_tectonique = 0
            if self.hydrographie >= 0.65:
                mod_tectonique += 6
            if self.geologie[0] == "Jeune":
                mod_tectonique += 2
            if self.geologie[0] == "Ancien":
                mod_tectonique -= 2
            if self.hydrographie <= 0.05:
                mod_tectonique -= 6
            if randomd6(3) + mod_tectonique >= 11:
                self.tectonique_mobile = True
        if self.geologie[0] == "Fondue" and self.hydrographie < 1.0:
            self.quantite_eau = "Traces"
            self.hydrographie = 0.0
        elif self.quantite_eau == "Grande":
            if self.geologie[0] == "Solide" or self.geologie[0] == "Molle":
                self.hydrographie += (randomd6(3)+10)*0.01
            elif self.geologie[0] == "Jeune" or self.geologie[0] == "Ancien":
                self.hydrographie += randomd6(3)*0.01
            if self.hydrographie > 1.0:
                self.hydrographie = 1.0
        if self.geologie[1] == 4:
            mod_magnetique = 4
        elif (self.geologie[1] == 3 or self.geologie[1] == 1) and self.tectonique_mobile:
            mod_magnetique = 8
        elif self.geologie[1] == 2 and self.tectonique_mobile:
            mod_magnetique = 12
        else:
            mod_magnetique = 0
        self.champ_magnetique = chercher_tableau(randomd6(3)+mod_magnetique, tableau_champ_magnetique, True )
        cas_special = False
        type_atmo = None
        mod_retention_atmo = 0 + self.champ_magnetique[1] + self.geologie[2]
        if self.hydrographie == 1.0 or self.a_subi_un_effet_de_serre:
            mod_retention_atmo += 6
        retention_atmo = (randomd6(3)+mod_retention_atmo)*0.1
        if retention_atmo < 0:
            retention_atmo = 0
        if self.nombre_m <= 2:
            self.atmosphere["Hydrogene"] = 7.5*retention_atmo
        if self.nombre_m <= 4:
            self.atmosphere["Helium"] = 2.5 * retention_atmo
        if self.nombre_m <= 28 and self.temperature_corps_noir > 80:
            self.atmosphere["Azote"] = 0.7 * retention_atmo
            if self.hydrographie == 100 and self.temperature_corps_noir > 125:
                self.atmosphere["Azote"] *= 15
        if self.type_effet_de_serre == "Sec":
            self.albedo = 0.65 + (randomd6(3)*0.01)
            self.atmosphere["CO2"] = 100 * retention_atmo
            self.temp = (self.temperature_corps_noir * math.pow(1-self.albedo, 0.25))+(250*math.log(self.atmosphere["CO2"], 10))
        elif self.atmosphere["Hydrogene"] > 0:
            self.albedo = 0.2 + (randomd6(3)*0.01)
            if self.type_effet_de_serre == "Humide":
                self.temp = (self.temperature_corps_noir * math.pow(1-self.albedo, 0.25))+(500*math.log(self.atmosphere["Hydrogene"], 10))
            else:
                self.temp = (self.temperature_corps_noir * math.pow(1-self.albedo, 0.25))+(180*math.log(self.atmosphere["Hydrogene"], 10))
        elif self.atmosphere["Azote"] > 0 and (80 <= self.temperature_corps_noir <= 125):
            self.albedo = 0.1 + (randomd6(3)*0.01)
            cas_special = True
            type_atmo = 3
            self.temp = (self.temperature_corps_noir * math.pow(1 - self.albedo, 0.25))
        elif self.atmosphere["Azote"] > 0:
            self.albedo = chercher_tableau(self.quantite_eau, tableau_albedo, False) + (randomd6(3)*0.01)
            if self.nombre_m < 44 and self.temperature_corps_noir >= 195:
                self.atmosphere["CO2"] = retention_atmo
            self.temp = (self.temperature_corps_noir * math.pow(1 - self.albedo, 0.25))
            if self.atmosphere["CO2"] != 0 and (self.temp+(8*math.log(self.atmosphere["CO2"], 10)) + 36) > 260 and 0.075 <= self.hydrographie < 100:
                self.cycle_silicate_carbone = True
            cas_special = True
            type_atmo = 4
        elif self.atmosphere["Helium"] == 0 and self.nombre_m < 44 and self.temperature_corps_noir > 195:
            self.albedo = chercher_tableau(self.quantite_eau, tableau_albedo, False) + (randomd6(3)*0.01)
            if self.nombre_m < 44 and self.temperature_corps_noir >= 195:
                self.atmosphere["CO2"] = retention_atmo
            if retention_atmo == 0:
                self.atmosphere["CO2"] = randomd6(1)*0.01
            cas_special = True
            type_atmo = 5
            self.temp = (self.temperature_corps_noir * math.pow(1 - self.albedo, 0.25))
        else:
            self.albedo = chercher_tableau(self.quantite_eau, tableau_albedo_classe_6, False) + (randomd6(3)*0.01)
            if self.geologie[1] >= 4:
                self.albedo += 0.5
            elif self.geologie[1] >= 2 or (self.geologie == 1 and self.tectonique_mobile) or self.temperature_corps_noir < 80:
                self.albedo += 0.3
            self.temp = (self.temperature_corps_noir * math.pow(1 - self.albedo, 0.25))
        if self.albedo > 1:
            self.albedo = 1
        vie_hydrothermale = False
        vie_surface = False
        multicellularite = False
        if not self.a_subi_un_effet_de_serre and self.hydrographie >= 0.075 and (1 <= self.geologie[1] <= 4) and self.tectonique_mobile:
            temps_abiogenese_hydrothermale = randomd6(3)*0.03
            if self.age > temps_abiogenese_hydrothermale:
                self.contient_vie = True
                self.profil_vie["Apparition_hydrothermale"] = self.age - temps_abiogenese_hydrothermale
                vie_hydrothermale = True
        if self.cycle_silicate_carbone and (1 <= self.geologie[1] <= 4):
            if self.geologie[1] == 4 or self.tectonique_mobile:
                temps_abiogenese_surface = randomd6(3)*0.1
            else:
                temps_abiogenese_surface = randomd6(3) * 0.2
            if self.age > temps_abiogenese_surface:
                self.contient_vie = True
                vie_surface = True
                if vie_hydrothermale:
                    temps_alt = temps_abiogenese_hydrothermale + randomd6(3) * 0.075
                    if temps_alt < temps_abiogenese_surface:
                        temps_abiogenese_surface = temps_alt
                self.profil_vie["Apparition_surface"] = self.age - temps_abiogenese_surface
        if self.contient_vie:
            if vie_hydrothermale and vie_surface:
                if temps_abiogenese_hydrothermale < temps_abiogenese_surface:
                    temps_multicellularite = temps_abiogenese_hydrothermale + randomd6(3) * 0.075
                else:
                    temps_multicellularite = temps_abiogenese_surface + randomd6(3) * 0.075
            elif vie_surface:
                temps_multicellularite = temps_abiogenese_surface + randomd6(3) * 0.075
            else:
                temps_abiogenese_surface = temps_abiogenese_hydrothermale + randomd6(3) * 0.075
                temps_multicellularite = temps_abiogenese_surface + randomd6(3) * 0.075
            if self.age > temps_multicellularite:
                self.profil_vie["Multicellularite"] = self.age - temps_multicellularite
                multicellularite = True
            if est_satellite:
                if liste_etoiles[centre_de_masse.centre_de_masse].categorie != "naine_brune" and liste_etoiles[centre_de_masse.centre_de_masse].categorie != "naine_blanche":
                    temps_photosynthese = temps_abiogenese_surface + (chercher_tableau(liste_etoiles[centre_de_masse.centre_de_masse].classe_spectrale, tableau_photosynthese,False) * randomd6(3))
                    if self.age > temps_photosynthese:
                        self.profil_vie["Photosynthese"] = self.age - temps_photosynthese
                        temps_catastrophe_oxygene = randomd6(3)*1.5*chercher_tableau(liste_etoiles[centre_de_masse.centre_de_masse].classe_spectrale, tableau_photosynthese, False)
                        if temps_catastrophe_oxygene > self.age:
                            self.profil_vie["Catastrophe_oxygene"] = self.age - temps_catastrophe_oxygene
                            self.contient_dioxygene = True
            else:
                if centre_de_masse.categorie != "naine_brune" and centre_de_masse.categorie != "naine_blanche":
                    temps_photosynthese = temps_abiogenese_surface + (chercher_tableau(centre_de_masse.classe_spectrale, tableau_photosynthese, False)*randomd6(3))
                    if self.age > temps_photosynthese:
                        self.profil_vie["Photosynthese"] = self.age - temps_photosynthese
                        temps_catastrophe_oxygene = randomd6(3)*1.5*chercher_tableau(centre_de_masse.classe_spectrale, tableau_photosynthese, False)
                        if temps_catastrophe_oxygene > self.age:
                            self.profil_vie["Catastrophe_oxygene"] = self.age - temps_catastrophe_oxygene
                            self.contient_dioxygene = True
            if multicellularite:
                temps_animaux = temps_multicellularite + randomd6(3) * 0.3
                if self.contient_dioxygene:
                    if temps_animaux > temps_catastrophe_oxygene:
                        temps_animaux = temps_catastrophe_oxygene + (temps_animaux-temps_catastrophe_oxygene)/2
                if self.age > temps_animaux:
                    self.profil_vie["Animaux"] = self.age - temps_animaux
                    if self.hydrographie == 1.0:
                        temps_sapience = temps_animaux + randomd6(3) * 0.1
                    else:
                        temps_sapience = temps_animaux + randomd6(3) * 0.5
                    if self.age > temps_sapience:
                        self.profil_vie["Sapience"] = self.age - temps_sapience
        if cas_special:
            effet_de_serre_methane = 0
            effet_de_serre_ozone = 0
            if type_atmo == 3 or self.contient_vie:
                effet_de_serre_methane = 2.1 + (8 * math.log(retention_atmo, 10))
            if self.contient_dioxygene:
                effet_de_serre_ozone = 1.7 + (8 * math.log(retention_atmo, 10))
            self.temp = self.temp + effet_de_serre_methane + effet_de_serre_ozone
            if self.cycle_silicate_carbone:
                reste_co2 = 260 - self.temp
                if reste_co2 > 8:
                    self.atmosphere["CO2"] = (3.16 * math.pow(10, -5) * math.pow(1.333, reste_co2))
                    self.temp += reste_co2
                else:
                    self.atmosphere["CO2"] = (3.16 * math.pow(10, -5) * math.pow(1.333, reste_co2))
                    self.temp += 8
            elif self.atmosphere["CO2"] != 0:
                self.temp += 36 + (8 * math.log(self.atmosphere["CO2"], 10))
            if self.nombre_m < 18 and self.temperature_corps_noir >= 260 and self.hydrographie >= 0.075:
                effet_de_serre_eau = chercher_tableau(self.temperature_corps_noir, tableau_effet_de_serre_eau,
                                                      True) + 4 + 10 * math.log(self.hydrographie, 10)
                self.atmosphere["Eau"] = (1.78 * math.pow(10, -5) * math.pow(1.333, effet_de_serre_eau))
                self.temp += effet_de_serre_eau
        for satellite in self.satellites:
            satellite.definir_caracteristiques(masse, luminosite, ancienne_lum, centre_de_masse, liste_etoiles, est_satellite, bonus_bomb, metallicite)

class Orbite:
    def __init__(self, distance):
        self.distance = distance
        self.est_ligne_des_glaces = False
        self.est_accretion_lente = False
        self.est_interdite = False
        self.contient_planete = False
        self.mod_epuisement = 1