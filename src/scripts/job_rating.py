import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import re

class JobRating():
    
    # def __init__ (self):
    
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
    # 35% matched previous position
    # 25% matched location
    def evaluate(self, locations, positions, skills, listing_title, loc_list_listing, listing_desc):
        skills = skills.split('|')
        positions = positions.split('|')
        locations = locations.split('|')
        skills_rating = self.filter_skills(skills, listing_title, listing_desc)
        positions_rating = self.filyer_positions(positions, listing_title, listing_desc)
        locations_rating = self.filter_locations(locations, loc_list_listing)
        print(listing_title)
        print(skills_rating)
        print(positions_rating)
        print(locations_rating)
        return (skills_rating * 0.4) + (positions_rating * 0.35) + (locations_rating * 0.25)
    
    def filter_locations(self, locations, loc_list_listing):
        preprocessed_text = self.preprocess_text(loc_list_listing)
        matched_locations = []
        for location in locations:
            postition_tokens = word_tokenize(location.lower())
            if all(token in preprocessed_text for token in postition_tokens):
                matched_locations.append(location)
        return (len(matched_locations) / len(locations)) * 100
    
    def filyer_positions(self, positions, listing_title, listing_desc):
        preprocessed_text = self.preprocess_text(listing_title + " " + listing_desc)
        matched_positions = []
        for position in positions:
            postition_tokens = word_tokenize(position.lower())
            if all(token in preprocessed_text for token in postition_tokens):
                matched_positions.append(position)
        return (len(matched_positions) / len(positions)) * 100
    
    def filter_skills(self, skills, listing_title, listing_desc):
        text = listing_title + " " + listing_desc
        preprocessed_text = self.preprocess_text(text=text)
        matched_skills = []
        for skill in skills:
            skill_tokens = word_tokenize(skill.lower())
            if all(token in preprocessed_text for token in skill_tokens):
                matched_skills.append(skill)
        return (len(matched_skills) / len(skills)) * 100