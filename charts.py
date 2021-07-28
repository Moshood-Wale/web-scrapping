# Modules imported 

from graph import *

from abc import ABC, abstractmethod

import matplotlib.pyplot as plt



class Interface(ABC):

    @abstractmethod
    
    def barchart(self):
        pass
    
    @abstractmethod
    
    def piechart(self):
        pass



class Chart(Interface, GraphValues) :

    def piechart(self):
        
        plt.xlabel("common words")
        plt.ylabel("frequency")
        plt.title("bar chart showing frequency of most used common words")
        plt.bar(self.x_axis(), self.y_axis()) 
        
        return plt.show()  
    
    def barchart(self):
        plt.pie(self.y_axis(), labels=self.x_axis(), autopct="%1.1f%%")

        return plt.show()