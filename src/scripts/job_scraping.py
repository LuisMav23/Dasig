from bs4 import BeautifulSoup
import requests
import re

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class JobSearch():
    
    def __init__ (self):
        nltk.download('stopwords')
        nltk.download('wordnet')

    def search(self, search, limit, locations, positions, skills):
        jobs = []
        url = f'https://www.jobstreet.com.ph/en/job-search/{search.replace(" ", "-")}-jobs/'
        with requests.Session() as session:
            response = session.get(url)
            soup_level1 = BeautifulSoup(response.content, 'html.parser')
            job_cards = soup_level1.select("div.z1s6m00._1hbhsw69y._1hbhsw68u._1hbhsw67e._1hbhsw67q")

            pages = int(soup_level1.select("option")[-1].text)
            print(pages)

            for page in range(1, min(pages + 1, limit // 20 + 1)):
                url = f'https://www.jobstreet.com.ph/en/job-search/{search.replace(" ", "-")}-jobs/{page}'
                response = session.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                job_cards = soup.select("div.z1s6m00._1hbhsw69y._1hbhsw68u._1hbhsw67e._1hbhsw67q")

                for job in job_cards:
                    loc_sal = job.select("span.z1s6m00._1hbhsw64y.y44q7i0.y44q7i3.y44q7i21.y44q7ih")
                    link = "https://www.jobstreet.com.ph" + job.select_one("a.jdlu994.jdlu996.jdlu999.y44q7i2.z1s6m00.z1s6m0f._1hbhsw6h")['href']
                    listing_html = session.get(link)
                    desc = BeautifulSoup(listing_html.content, 'html.parser')
                    job_desc = desc.select_one("div.z1s6m00._1hbhsw66y._1hbhsw673._1hbhsw674._1hbhsw682._1hbhsw687._1hbhsw688._1hbhsw69q._1hbhsw68m.y44q7i18.y44q7i1b._1hbhsw632._1hbhsw635")
                    if not job_desc:
                        continue
                    pattern = r'([a-z])([A-Z])'
                    cleaned_text = re.sub(pattern, r'\1 \2', job_desc.text).strip()
    
                    job_temp = {
                        'role': job.select_one("div.z1s6m00.l3gun70.l3gun74.l3gun72").text,
                        'company': job.select_one("span.z1s6m00.bev08l1._1hbhsw64y._1hbhsw60._1hbhsw6r").text,
                        'location': loc_sal[0].text,
                        'salary': loc_sal[1].text if len(loc_sal) > 1 else '',
                        'job_desc': cleaned_text,
                        'link': link
                    }
                    jobs.append(job_temp)
                    if len(jobs) >= limit:
                        break

                if len(jobs) >= limit:
                    break

        return jobs[:limit]
    
    def preprocess_text(text):
        # Tokenize the text into words
        tokens = word_tokenize(text)
        
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
        
        # Lemmatize the words
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
        
        return lemmatized_tokens
    
    # evaluates the compatibility of the job
    # 40% matched skills
    # 30% matched previous position
    # 30% matched location
    def evaluate(self, locations, positions, skills, title, loc, desc):
        k=[]
    
    def filter_locations(self, locations, text):
        
    
    def filyer_positions(self, positions, text):
        j=[]
        
    def filter_skills(self, skills, text):
        j= []