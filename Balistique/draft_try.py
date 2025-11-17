# -*- coding: utf-8 -*-
"""
L3 ME
Projet "balistique"

@author: C. Airiau
@date: 30/10/2023

Partie 1: apprentissage sur le modèle analytique: AnalyticalModelExample

"""
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
        self.time=np.linspace(0,100,80)
        self.x= np.zeros(len(self.time))
        self.z= np.zeros(len(self.time))
        self.v_x= np.zeros(len(self.time))
        self.v_z= np.zeros(len(self.time))
        self.v= np.zeros(len(self.time))
    

  
        




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

    ###############################################################################################################     Je complete le code par d'autres fonctons
    def set_trajectory (self,t_end,npt ):    # t_end is a nombers and npt is number
        self.time=np.linspace(0,t_end,npt)
        self.x= np.zeros(len(self.time))
        self.z= np.zeros(len(self.time))
        self.v_x= np.zeros(len(self.time))
        self.v_z= np.zeros(len(self.time))
        self.v= np.zeros(len(self.time))
        for i in (0,len(self.time)-1):
            self.x [i] = self.v_0*np.cos(self.alpha)*self.time[i]
            self.z [i]= -(g*0.5*(self.time[i])**2) + self.v_0 * self.time[i]*np.sin(self.alpha) + self.h
            self.v_x [i]= self.v_0*np.cos(self.alpha)
            self.v_z [i]= self.v_0 * np.sin(self.alpha) - g*self.time[i]
            self.v [i]= np.sqrt(self.v_x [i]**2 + self.v_z [i]**2)  
        
        return [ self.time ,  self.x , self.z, self.v_x , self.v_z , self.v ]
    

    
    def plot_trajectory(self,t_end,npt):
        liste= self.set_trajectory (t_end,npt ) 
        x1= liste[1]
        z1= liste[2]
        plt.plot(x1, z1, marker="+", color="red",linewidth=3)
        plt.xlabel("Position X")
        plt.ylabel("Position Z")
        plt.legend(["Position Z en fonction de la position z "], fontsize=12)
        plt.show ()

    def plot_component(self, t_end,npt):
        liste= self.set_trajectory (t_end,npt ) 
        time1= liste[0]
        v_z1= liste[4]
        v1= liste[5]
        plt.plot(time1, v_z1, marker="+",color="green",linewidth=3)
        plt.plot(time1, v1, marker="o",color="red",linewidth=3)
        plt.fill_between(time1, v_z1 , v1)
        plt.xlabel("Time")
        plt.ylabel("Position X and Z")
        plt.legend(["Position X en fonction du temps ","Position Z en fonction du temps "], fontsize=12)
        plt.show ()



############################################################################ 10.1 Graphiques de trajectoires
#############################################Not working part
"""""
   def set_trajectoryies(self, alpha):    # alpha est une liste
        x=np.zeros(len(alpha))
        z=np.zeros(len(alpha))

        for i in range (0,len (alpha)) :
            x[i]= self.v_0*np.cos(np.deg2rad(alpha[i])) *self.time
            z[i]= -(g*0.5*self.time**2) + self.v_0 * np.sin(np.deg2rad(alpha[i]))*self.time + self.h
        
        return [ x , z ]"""
##################################################################################################  Not working part



#################################################################### text part 



v_0=3
h=10
alpha=30

model= AnalyticalModelExample(h,v_0,alpha)

print(model.set_trajectory(2,50))     # en fonction de t temps et npt nombre de point 

#print(model.set_trajectoryies([20,40,60]))   # en fonction d'une liste d'angle alpha    
model.plot_trajectory(2,50)
model.plot_component(2,50)