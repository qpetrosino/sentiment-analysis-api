from textblob import TextBlob

def get_sentiment(string):
    #Input Error handling
    if not isinstance( string, str):
        return "Error: Input must be string."
    if not string.strip():
        return "error: Input cannot be empty."
   
    # Data logic 
    blob  = TextBlob(string)
    polarity = blob.sentiment.polarity 
    
    # Thresholds
    # Polarity range from -1 to 1
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

def run_test():
    test_cases = {
        "Positive": [
            "I love the weather today!",
            "The serive here was incredibly fast and friendly.",
            "Using TextBlob is such a cool tool."
            "This video was very informative and helpful."
        ],
        "Negative": [
            "The traffic was horrible today.",
            "My code is taking forever, this is dreadful.",
            "The food was bland and not presentable.",
            "I have so many tests coming up and barely have had time to study."
        ],
        "Neutral": [
            "My meeting is at 3 PM tomorrow.",
            "I am studying Computer Science.",
            "I am pursuing my Masters Degree next year.",
            "The knicks game is on tonight."
            
        ]
    }
    
    print(f"{'Actual':<12} | {'Predicted':<12} | {'Sentence'}")
    print("-" * 60)
    
    for actual, sentences in test_cases.items():
        for sentence in sentences:
            predicted = get_sentiment(sentence)
            print(f"{actual:<12} | {predicted:<12} | {sentence}")


if __name__ == "__main__":
    run_test()

'''
"The knicks game is on tonight." (Predicted: Negative)
Since "Knicks" usually appears with a negative connotation in social media like them losing it can shift the score slightly negative.

"I have so many tests coming up and barely have had time to study." (Predicted: Positive)
The issue with this is there is no real feeling words like love or hate. Since it is not explicit, I assume it was confused because of this.
'''

    
    
      

    
    
