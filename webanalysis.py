# Modules imported

from webscrape import *

from collections import Counter


class WebAnalysis(WebsiteText):

    def word_count(self):
        count = Counter(self.remove_common_words()).most_common(7)
        
        return count
    
    def top_words(self):
        most_count = Counter(self.remove_common_words()).most_common(1)
        best_count = [i[0] for i in most_count]
        
        new = print(f"The top word is {best_count[0]}")
        return new

