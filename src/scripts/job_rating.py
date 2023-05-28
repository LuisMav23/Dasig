import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokenizer import Tokenizer

class JobRating():
    nlp = spacy.load('en_core_web_sm')
    tokenizer = Tokenizer(nlp.vocab)
    
    def preprocess_text(self, text):
        doc = self.nlp(text)
        tokens = [token.text.lower() for token in doc if not token.is_stop]
        lemmatized_tokens = [token.lemma_ for token in self.nlp(" ".join(tokens))]
        return lemmatized_tokens
    
    def word_tokenize(self, text):
        doc = self.nlp(text)
        tokens = [token.text for token in doc if not token.is_space]
        return tokens
    
    def evaluate(self, locations, positions, skills, text):
        preprocessed_text = set(self.preprocess_text(text.lower()))
        skills_rating = self.filter_skills(skills, preprocessed_text)
        positions_rating = self.filter_positions(positions, preprocessed_text)
        locations_rating = self.filter_locations(locations, preprocessed_text)
        print(skills_rating)
        print(positions_rating)
        print(locations_rating)
        return (skills_rating * 0.70) + (positions_rating * 0.20) + (locations_rating * 0.10)
    
    def filter_locations(self, locations, preprocessed_text):
        matched_locations = []
        preprocessed_text_set = set(preprocessed_text)
        for location in locations:
            postition_tokens = self.word_tokenize(location.lower())
            if set(postition_tokens).issubset(preprocessed_text_set):
                matched_locations.append(location)
        return (len(matched_locations) / len(locations)) * 100
    
    def filter_positions(self, positions, preprocessed_text):
        matched_positions = []
        preprocessed_text_set = set(preprocessed_text)
        for position in positions:
            postition_tokens = self.word_tokenize(position.lower())
            if set(postition_tokens).issubset(preprocessed_text_set):
                matched_positions.append(position)
        return (len(matched_positions) / len(positions)) * 100
    
    def filter_skills(self, skills, preprocessed_text):
        matched_skills = []
        preprocessed_text_set = set(preprocessed_text)
        for skill in skills:
            skill_tokens = self.word_tokenize(skill.lower())
            if set(skill_tokens).issubset(preprocessed_text_set):
                matched_skills.append(skill)
        return (len(matched_skills) / len(skills)) * 100
