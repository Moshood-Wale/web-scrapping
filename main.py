# Entry point of your application

# Modules Imported 

from webanalysis import *

from webscrape import WebsiteText

from charts import *

from graph import *


# The Program Output function

def program_output():
    
    while True:
        
        user_input = input('\nWould you like to scrape a website (y/n): ')

        if user_input =='n':
            print('\nThank you for the analysis. We hope to see you next time')
            exit()

        elif user_input =='y':
        
            website = input('\nEnter the website to analyze: \n')
            
            try:
                res=requests.get(website)
                res.raise_for_status()
            
            except requests.exceptions.RequestException as e:
                print('Connection error!')

            else: 
                word_counts=WebAnalysis(website)
                word_counts.remove_common_words()
                request = Chart(website)
                word_counts.top_words()
                print(request.piechart())
                print(request.barchart())
        
        
        else:
            print('Incorrect choice')
        
        

program_output()            

