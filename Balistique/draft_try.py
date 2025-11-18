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
        self.x = self.v_0*np.cos(self.alpha)*self.time
        self.z= -(g*0.5*(self.time)**2) + self.v_0 * self.time*np.sin(self.alpha) + self.h
        self.v_x= self.v_0*np.cos(self.alpha)*np.ones(len(self.time))
        self.v_z= self.v_0 * np.sin(self.alpha) - g*self.time
        self.v= np.sqrt(self.v_x**2 + self.v_z**2)
      
    
    

    
    def plot_trajectory(self):
        plt.plot(self.x, self.z, marker="+", color="red",linewidth=3)
        plt.xlabel("Position X")
        plt.ylabel("Position Z")
        plt.legend(["Position Z en fonction de la position z "], fontsize=12)
        plt.show ()

    def plot_component(self):

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)        
        
        ax1.plot(self.time, self.v_z, marker="+",color="green",linewidth=3)
        ax2.plot(self.time, self.v, marker="o",color="red",linewidth=3)
        plt.fill_between(self.time, self.v_z ,self.v)
        plt.xlabel("Time")
        plt.ylabel("Position X and Z")
        plt.legend(["Position X en fonction du temps ","Position Z en fonction du temps "], fontsize=12)
        plt.show ()




"""





##################################################################################################################################################""
    def set_trajectoryalpha(self,t_end,npt,alpha1 ):    # t_end is a nombers and npt is number
        self.time=np.linspace(0,t_end,npt)
        self.x= self.v_0*np.cos(alpha1)*self.time
        self.z= self.v_0 * np.sin(alpha1)*self.time - (g*0.5*(self.time)**2) + self.h
        self.v_x= self.v_0*np.cos(alpha1)*np.ones(len(self.time))
        self.v_z= self.v_0 * np.sin(alpha1) - g*self.time   
        self.v= np.sqrt(self.v_x**2 + self.v_z**2)
         for i in (0,len(self.time)-1):
            self.x [i] = self.v_0*np.cos(alpha1)*self.time[i]
            self.z [i]= -(g*0.5*(self.time[i])**2) + self.v_0 * self.time[i]*np.sin(alpha1) + self.h
            self.v_x [i]= self.v_0*np.cos(alpha1)
            self.v_z [i]= self.v_0 * np.sin(alpha1) - g*self.time[i]
            self.v [i]= np.sqrt(self.v_x [i]**2 + self.v_z [i]**2)  
            
        return [ self.time ,  self.x , self.z, self.v_x , self.v_z , self.v ]"""
                                                                                                                                                              

    def set_trajectories(self,alpha):    # alpha est une liste avec t_ent pour faire des trajectoires pour chaque alpha en focntion du temps 
        x=[]
        z=[]
        alpha=[]

        for i in range (20,70) :
            if i % 5 ==0 :
                alpha.append (i)

        for i in alpha :
            liste=self.set_trajectoryalpha (t_end,npt,i ) 
            x.append (liste[1])
            z.append(liste[2])  # derniere valeur de x                 
        return [ x , z ]      # x et z sont des listes de lsites x contient 11 listes pour xhaque valeur de alpha or on a 11 valeurs pour alpha car on a 5 multiples de 5 esntre 20 et 70

    def set_trajectories_plot(self,t_end,npt):
        liste= self.set_trajectories (t_end,npt ) 
        x1= liste[0]
        z1= liste[1]
        for i in range (len(x1)) :
            plt.plot(x1[i], z1[i], marker="+",linewidth=3)
        plt.xlabel("Position X")
        plt.ylabel("Position Z")
        plt.legend(["Position Z en fonction de la position z "], fontsize=12)
        plt.show ()


"""
############################################################################ 10.1 Graphiques de trajectoires
#############################################Not working part
J ai remplacé set_trajectoryalpha par set_trajectory pour simplifier, car le rôle de la fonction est déjà de travailler avec un angle
alpha J ai clarifié que la première fonction gère probablement une liste d'angles pour être cohérent avec l idée de tracer pour chaque angle alpha """



    
    

    

     
#"""
##################################################################################################  Not working part



#################################################################### text part 



v_0=3
h=10
alpha=30

model= AnalyticalModelExample(h,v_0,alpha)

print(model.set_trajectory(2,50))     # en fonction de t temps et npt nombre de point 
#print("le tableu des trajectoires en fonction de la variation de alpha", model.set_trajectories(5,100))

#print(model.set_trajectoryies([20,40,60]))   # en fonction d'une liste d'angle alpha    
model.plot_trajectory()
model.plot_component()
model.set_trajectories_plot(2,50)