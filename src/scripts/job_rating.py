import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import re

class jobRating():
    
    def __init__ (self):
        nltk.download('stopwords')
        nltk.download('wordnet')
    
    def preprocess_text(self, text):
        # Tokenize the text into words
        tokens = word_tokenize(text.lower())
        
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
        
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens if word.isalnum()]
        
        return filtered_tokens

    
    # evaluates the compatibility of the job
    # 40% matched skills
    # 30% matched previous position
    # 30% matched location
    def evaluate(self, locations, positions, skills, listing_title, loc_list_listing, listing_desc):
        k=[]
    
    def filter_locations(self, locations, loc_list_listing):
        common_items = set(locations) & set(loc_list_listing)
        percentage = (len(common_items) / len(locations)) * 100
        return percentage
    
    def filyer_positions(self, positions, listing_title, listing_desc):
        preprocessed_text = self.preprocess_text(listing_title + " " + listing_desc)
        print(preprocessed_text)
        matched_positions = []
        for position in positions:
            postition_tokens = word_tokenize(position.lower())
            if all(token in preprocessed_text for token in postition_tokens):
                matched_positions.append(position)
        return matched_positions
    
    def filter_skills(self, skills, listing_title, listing_desc):
        preprocessed_text = self.preprocess_text(listing_title + " " + listing_desc)
        print(preprocessed_text)
        matched_skills = []
        for skill in skills:
            skill_tokens = word_tokenize(skill.lower())
            if all(token in preprocessed_text for token in skill_tokens):
                matched_skills.append(skill)
        return matched_skills