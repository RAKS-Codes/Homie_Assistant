import wolframalpha
import wikipedia 
import os 
from os import environ


while True:
    a = input("Ask me anything: ")
    
    try:
        CONSUMER_KEY = environ["CONSUMER_KEY"]
        client = wolframalpha.Client('CONSUMER_KEY')
        res = client.query(a)
        answer = next(res.results).text
        
        print(answer)
    
    except:
        print(wikipedia.summary(a, sentences=3))
        
