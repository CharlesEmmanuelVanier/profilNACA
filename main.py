import numpy as np
import matplotlib.pyplot as plt

def creation_tableau_coord(profil, corde, precision, distribution):
    #Fonction qui crée 4 tableaux de coordonnées représentant l'extrados et l'intrados du profil d'ail selectionné
    #Set l'epaisseur max du profil choisi
    t = profil/100
    # Crée un tableau pour avoir une variation a pourcentage sur l'axe des X
    if distribution == 0:
        xc = 1/2*(1-np.cos(np.linspace(0, np.pi, precision)))
    else:
        xc = np.linspace(0, 1, precision, dtype=float)
    # Tableau de la distance en pourcentage entre la corde moyenne et le bord d'attaque ou le bord de fuite, assume profil symétrique
    yc = np.ones_like(xc) * 5 * t * (( (0.2969*np.sqrt(xc)) - (0.1260*xc) - (0.3516*(xc**2)) + 0.2843*(xc**2)) - (0.1036*xc**2))
    # Tableau de coordonnée de mon intrados et extrados


    # création des quatres tableaux des points de coordonnées
    x_up = xc * corde
    x_down = xc * corde
    y_up = yc * corde
    y_down = -1 * yc * corde

    return x_up, x_down, y_up, y_down

def indice_epaisseur_max(y_up, y_down):
    #Prend les tableaux en y pour trouver l'indice représentant l'épaisseur max et retourne l'indice trouvé
    return np.argmax(y_up - y_down)

def tracer_graph(x_up, x_down, y_up, y_down, profil):
    #Fonction qui utilise matplotlib pour tracer le profil d'ail
    plt.plot(x_up,y_up, label = 'Extrados')
    plt.plot(x_down, y_down, label = 'Intrados')
    plt.xlabel('Corde [en mètre]')
    plt.ylabel('Profil d''aile [en mètre]')
    plt.legend()
    plt.grid()
    plt.title(f"Profil d''Aile NACA00{profil}")
    plt.show()

def menu():
    #Fonction principale qui intéragie avec l'utilisateur et appelle les autres fonction

    #Intéraction avec l'utilisateur
    profil_naca = input("\nEntrez les 2 derniers chiffre du profil NACA00XX:")
    corde_naca = input("\nEntrez la corde du profil (en mètre): ")
    precision_naca = input("\nEntrez le nombre de point le long de la corde pour le tracé: ")
    type_point_naca = input("\nEntrez le type de distribution de point le long de la corde (Linéaire (1) ou Non-Linéaire (0): ")

    #On appelle la fonction pour recevoir nos tableaux de coordonnée représentant le profil d'ail selectionné
    x_up, x_down, y_up, y_down = creation_tableau_coord(int(profil_naca), int(corde_naca), int(precision_naca),type_point_naca)
    #On recoit la position dans les tableaux représentant l'épaisseur max du profil d'ail
    indice_max = indice_epaisseur_max(y_up, y_down)
    #On imprime les résultats demandé
    print(f"\nL'épaisseur max de notre profil d'aile est : {np.absolute(y_up[indice_max]) +  np.absolute(y_down[indice_max])} [m]")
    print(f"\nElle se retrouve à {x_up[indice_max]} [m]")
    #On trace une courbe avec Matplotlib
    tracer_graph(x_up, x_down, y_up, y_down, profil_naca)

#Main function
menu()