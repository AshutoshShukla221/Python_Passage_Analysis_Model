from transformers import pipeline

class API:
    def __init__(self):
        self.sentiment=pipeline("sentiment-analysis")
        self.ner=pipeline("ner",aggregation_strategy='simple')
        self.emotion=pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
    
    def sentiment_analysis(self,text):
        return self.sentiment(text)
    
    def ner_analysis(self,text):
        return self.ner(text)
    
    def emotion_analysis(self,text):
        return self.emotion(text)
    

# sentiment = pipeline("sentiment-analysis")
# ner = pipeline("ner")

# text = "Elon Musk founded Tesla"

# print(sentiment(text))
# print(ner(text))