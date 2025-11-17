# -*- coding: utf-8 -*-
"""
L3 ME
Projet "balistique"

@author: C. Airiau
@date: 30/10/2023

Partie 1: Travail sur le modèle analytique

task :
    0 : graphiques: trajectoire, v_z et v, f(alpha)
        valeurs à l'impact
    1 : ajout fonction plot_trajectories, plot_maximun_distance, plot_maximum_height dans le script principal
        affichage de la portée maximale et de l'angle correspondant + valeur théorique
"""
import numpy as np
import matplotlib.pyplot as plt
from Ballistic.model_1 import Model_1
from Ballistic.colored_messages import *
from Ballistic.constantes import *

################################################################################################################################# CLASS 



import numpy as np  # module de math
import matplotlib.pyplot as plt  # module graphique
from scipy.constants import g    # constante en m/s^2.
from Ballistic.colored_messages import *
from Ballistic.constantes import *


class AnalyticalModelExample(object):
    """ Class of the analytical model (example to initiate to class)"""
    def __init__(self, h=10, v_0=10, alpha=30):
        """ Le constructeur de classe est lancé dès la création de la classe"""
        self.h = h
        self.v_0 = v_0
        self.alpha = np.deg2rad(alpha)  # on met alpha en radians directement
        self.initial_message()
        self.impact_values = None       # défini ici, utilisé plus tard

    @staticmethod
    def initial_message():
        set_title("Création d'une instance du modèle analytique (class initiation)")

    # SETTERS

    def update_parameters(self, params_dict):
        """ set new values for parameters from a dictionary"""
        if params_dict is None:
            params_dict = dict(v_0=10, h=20, alpha=30)
        else:
            for key in params_dict.keys():
                if key == "v_0":
                    self.v_0 = params_dict[key]
                elif key == "h":
                    self.h = params_dict[key]
                elif key == "alpha":
                    self.alpha = np.deg2rad(params_dict[key])
        self.get_parameters()

    def set_velocity(self, t):
        v_z = self.v_0 * np.sin(self.alpha) - g * t
        v_x = self.v_0 * np.cos(self.alpha)
        v = np.sqrt(v_x ** 2 + v_z ** 2)
        return v_x, v_z, v

    def set_impact_values(self):
        """
        retourne les valeurs temps, portée, vitesse et angle à l'impact
        """
        var = self.v_0 * np.sin(self.alpha)
        t_i = (var + np.sqrt(var ** 2 + 2 * g * self.h)) / g
        v_x, v_z, v = self.set_velocity(t_i)
        x_i = v_x * t_i  # ici des variables locales, pas de self devant
        theta_i = np.rad2deg(np.arctan(v_z / v_z))
        self.impact_values = {"t_i": t_i, "p": x_i, "angle": theta_i, "v": [v_x, v_z, v]}
        return self.impact_values

    # GETTERS
    def get_impact_values(self):
        """
        Joli affichage pour les valeurs d'impact
        """
        set_info("Impact:")
        print("time       : %.2f s" % self.impact_values["t_i"])
        print("length     : %.2f m" % self.impact_values["p"])
        print("angle      : %.2f °" % self.impact_values["angle"])
        print("|v|        : %.2f m/s" % self.impact_values["v"][2])

    def get_parameters(self):
        """
        Affichage formatté des paramètres
        """
        set_info("Parameters:")
        print("v_0        : %.2f m/s" % self.v_0)
        print("h          : %.2f m" % self.h)
        print("alpha      : %.2f °" % np.rad2deg(self.alpha))


 




########################################################################################################################################
















task = 0

if task == 0:

    

    # Pour tracer le graphe en fonction de alpha il faux avoir un tableau de v_z et v en fonction de alpha

    # declaration générales des variables 
    alphamin=20
    alphamax=70
    v_0=100
    h=10
    t=0.2

    alpha=np.linspace(alphamin, alphamax,5)
    model1=AnalyticalModelExample(h,v_0, alpha[0])
    v_z=np.zeros(len(alpha))
    v=np.zeros(len(alpha))

    for i in (0, len(alpha)-1) :    
                                               # Ici, je parcours les elements du tableau aplha contenant les angles
        dico={"v_0":v_0,   "h":h,  "alpha":alpha[i]}                                                           # update_parameters() prend en entrer un dictionaire donc je crée un dico
        model1.update_parameters(dico)                                                  # Ici, je crée differents model1 avec differentes valeur de l angle
        v_z[i] = model1.set_velocity(t) [1]                                                   # Ici je conserve dans le tableau v_z les differentes valeurs de v_z en fonction de l angle 
        v[i] = model1.set_velocity(t) [2]                                                       # Ici je conserve les différentes valeurs de v en fonction de l angle dans le tableau des v 

    # La c'est bon j'ai un tableau de v_z et de v en fonction de alpha qui change

    # On possede maintenant a l'affichage des courbes 
    print(v_z)
    plt.plot(alpha,v_z,color="red")
    plt.plot(alpha,v,marker="+",color="blue")
    plt.xlabel("alpha")
    plt.ylabel("$V_z$")
    plt.title("Vitesse ")
    plt.legend(["vitesse selon z et la norme de la vitesse "])
    plt.xlim(alphamin,alphamax)
    plt.ylim(0,100)
    plt.show()

    #
   
    pass

elif task == 1:
    pass
plt.show()
print("normal end of execution")
