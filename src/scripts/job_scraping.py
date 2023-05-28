from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import concurrent.futures


from job_rating import JobRating

class JobSearch():
    
    base_url = 'https://www.jobstreet.com.ph'
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                'Referer': base_url
            }
    
    search = ''
    limit = 0
    locations = []
    positions = []
    skills = []
    
    # list1 = []
    # list2 = []
    # list3 = []
    # list4 = []
    
    

    def search_jobs(self, pages_to_scan):
        jobs = []
        url = f'https://www.jobstreet.com.ph/en/job-search/{self.search.replace(" ", "-")}-jobs/'
        with requests.Session() as session:
            evaluator = JobRating()
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--log-level=3")
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--blink-settings=imagesEnabled=false')
            chrome_options.add_argument('--disable-animations')
            caps = DesiredCapabilities().CHROME
            caps["pageLoadStrategy"] = "eager"
            driver = webdriver.Chrome(desired_capabilities=caps, options=chrome_options)

            for page in pages_to_scan:
                print(page)
                url = f'https://www.jobstreet.com.ph/en/job-search/{self.search.replace(" ", "-")}-jobs/{page}'
                response = session.get(url, headers=self.headers)
                soup = BeautifulSoup(response.content, 'html.parser')
                job_cards = soup.select("div.z1s6m00._1hbhsw69y._1hbhsw68u._1hbhsw67e._1hbhsw67q")

                for job in job_cards:
                    loc_sal = job.select("span.z1s6m00._1hbhsw64y.y44q7i0.y44q7i3.y44q7i21.y44q7ih")
                    link = "https://www.jobstreet.com.ph" + job.select_one("a.jdlu994.jdlu996.jdlu999.y44q7i2.z1s6m00.z1s6m0f._1hbhsw6h")['href']
                    driver.get(link)
                    driver.implicitly_wait(5)
                    desc = BeautifulSoup(driver.page_source, 'html.parser')
                    job_desc = desc.select_one("div.z1s6m00._1hbhsw66y._1hbhsw673._1hbhsw674._1hbhsw682._1hbhsw687._1hbhsw688._1hbhsw69q._1hbhsw68m.y44q7i18.y44q7i1b._1hbhsw632._1hbhsw635") 
                    role = job.select_one("div.z1s6m00.l3gun70.l3gun74.l3gun72").text
                    if not job_desc:
                        print("skipped")
                        continue
                    pattern = r'([a-z])([A-Z])'
                    cleaned_text = re.sub(pattern, r'\1 \2', job_desc.text).strip()
                    
                    role = job.select_one("div.z1s6m00.l3gun70.l3gun74.l3gun72").text
                    company = job.select_one("span.z1s6m00.bev08l1._1hbhsw64y._1hbhsw60._1hbhsw6r").text
                    location = loc_sal[0].text
                    print(role)
                    rating = evaluator.evaluate(locations=self.locations, positions=self.positions, skills=self.skills, text=role + " " + location + " " + cleaned_text)
                    if rating < 15:
                        continue
                    # print(role)
                    # print(rating)
                    job_temp = {
                        'role': role,
                        'company': company,
                        'location': location,
                        'salary': loc_sal[1].text if len(loc_sal) > 1 else '',
                        'job_rating': rating,
                        'link': link
                    }
                    jobs.append(job_temp)
                    if len(jobs) >= self.limit:
                        break

                if len(jobs) >= self.limit:
                    break
            driver.close()
        return jobs[:self.limit]

    def search(self, search, limit, locations, positions, skills):
        self.search = search
        self.limit = limit
        self.locations = locations
        self.positions = positions
        self.skills = skills
        self.list1 = []
        self.list2 = []
        self.list3 = []
        self.list4 = []

        url = f'https://www.jobstreet.com.ph/en/job-search/{self.search.replace(" ", "-")}-jobs/'
        with requests.Session() as session:
            response = session.get(url, headers=self.headers)
            soup_level1 = BeautifulSoup(response.content, 'html.parser')
            pages = int(soup_level1.select("option")[-1].text)
            pages_to_scan = []
            for i in range(1, pages):
                pages_to_scan.append(i)
            return self.search_jobs(pages_to_scan)

    #     with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    #             # Submit tasks to the executor and collect the future objects
    #         futures = [
    #             executor.submit(self.thread1_func, pages),
    #             executor.submit(self.thread2_func, pages),
    #             executor.submit(self.thread3_func, pages),
    #             executor.submit(self.thread4_func, pages)
    #         ]

    #             # Wait for all tasks to complete
    #         concurrent.futures.wait(futures)

    #         # Extend the lists and return the combined result
    #     self.list2.extend(self.list3)
    #     self.list2.extend(self.list4)
    #     self.list1.extend(self.list2)

    #     return self.list1


    # def thread1_func(self, pages):
    #     pages_to_scan = []
    #     for i in range(1, pages):
    #         if i % 4 == 0:
    #             pages_to_scan.append(i)
    #     self.list1 = self.search_jobs(pages_to_scan)


    # def thread2_func(self,pages):
    #     pages_to_scan = []
    #     for i in range(1, pages):
    #         if i % 4 == 1:
    #             pages_to_scan.append(i)
    #     self.list2 =  self.search_jobs(pages_to_scan)


    # def thread3_func(self,pages):
    #     pages_to_scan = []
    #     for i in range(1, pages):
    #         if i % 4 == 2:
    #             pages_to_scan.append(i)
    #     self.list3 =  self.search_jobs(pages_to_scan)


    # def thread4_func(self,pages):
    #     pages_to_scan = []
    #     for i in range(1, pages):
    #         if i % 4 == 3:
    #             pages_to_scan.append(i)
    #     self.list4 =  self.search_jobs(pages_to_scan)

        