
# Modules Imported
from webanalysis import WebAnalysis

from webscrape import *



# This class inherits the class and methods of the webanalysis and webscrape module  
class GraphValues(WebAnalysis) :
    def x_axis(self):
        x_axis_values = [item[0] for item in self.word_count()]
        return x_axis_values
    
    def y_axis(self):
        y_axis_values = [item[1] for item in self.word_count()]
        return y_axis_values
