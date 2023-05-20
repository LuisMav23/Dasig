from bs4 import BeautifulSoup
import requests

class JobSearch():

    def search(self, search, limit):
        jobs = []
        url = f'https://www.jobstreet.com.ph/en/job-search/{search.replace(" ", "-")}-jobs/'
        with requests.Session() as session:
            response = session.get(url)
            soup_level1 = BeautifulSoup(response.content, 'html.parser')
            job_cards = soup_level1.find_all("div", "z1s6m00 _1hbhsw69y _1hbhsw68u _1hbhsw67e _1hbhsw67q")

            pages = int(soup_level1.find_all("option")[-1].text)
            print(pages)

            for page in range(1, pages+1):
                url = f'https://www.jobstreet.com.ph/en/job-search/{search.replace(" ", "-")}-jobs/{page}'
                response = session.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                job_cards = soup.find_all("div", "z1s6m00 _1hbhsw69y _1hbhsw68u _1hbhsw67e _1hbhsw67q")

                jobs += [
                    {
                        'role': job.find("div", "z1s6m00 l3gun70 l3gun74 l3gun72").text,
                        'company': job.find("span", "z1s6m00 bev08l1 _1hbhsw64y _1hbhsw60 _1hbhsw6r").text,
                        'location': loc_sal[0].text,
                        'salary': loc_sal[1].text if len(loc_sal) > 1 else ''
                    }
                    for job in job_cards
                    for loc_sal in [job.find_all("span", "z1s6m00 _1hbhsw64y y44q7i0 y44q7i3 y44q7i21 y44q7ih")]
                ]
                if len(jobs) > limit:
                    break

        return jobs[:limit] if len(jobs) > limit else jobs
