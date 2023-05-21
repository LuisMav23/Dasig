from job_rating import JobRating

rater =JobRating()
text = "Job Highlights Looking for experience Python Developer!Work with a team across APAC!Remote Work, competitive package and benefits.Job Description The Company At BCI we are driven by our vision to create transparency in the construction industry globally. We do so by providing qualified sales information on construction projects, networking session with industrial players, enabling our clients to showcase their product brand via digital marketing platforms, and many more. While the market braces itself for a global recession, BCI is experiencing exponential growth within both the APAC and American regions.The Role We are looking for a Digital Data Gatherer/Python developer to be based in Metro Manila, who will be responsible for building and maintaining an application to scrape the websites. An ideal candidate should be highly adept at writing clean, testable, and scalable. The developer must have a basic understanding of data scraping methodologies.Your day-to-day task will be: -Identify accurately and write scalable code for useful data using Python programming language.Operate web harvesting software in Python to scrape data from websites including in-house native harvester.Adhere to website-scraping targets Building/maintaining web scraping tools using Python (beautifulsoup/extractable API)Ability to integrate 3rd party packages and API libraries into web harvesting software Review and ensure that scraped data is correct Troubleshooting quality issues  Collaborate with developer teams for testing Responding to requests from the design team and management Monitoring bugs tracking and error reporting in Jira Requirements: -Bachelor's degree in Information Technology, Computer Science or relevant field.Experience in Python, Beautiful Soup and in-built modules Experience with Mozenda scraping software or other similar software.Knowledge of AWS (S3) and Apache Airflow coding for Orchestration will be added advantage.Good working knowledge of spreadsheet software, such as excel Good attitude, work ethic, self-motivated and fast learner. What's in it for you?An energetic team where people love their job and being challenged to perform at their best.Medical Insurance coverage.Starting with 12 days AL and up to 20 days per year.2 days paid leave for charity work Birthday & Work Anniversary Leave.New born baby bonus5 days working week (Monday to Friday)BCI Central values personal integrity, social and environmental responsibility as well as transparency, quality, and efficiency. Suitable candidates will share these values.(Only shortlisted candidates will be notified)Additional Information Career Level1-4 Years Experienced Employee Qualification Bachelor's/College Degree, Post Graduate Diploma/Master's Degree, Professional License (Passed Board/Bar/Professional License Exam)Years of Experience3 years Job Type Full-Time Job Specializations Computer/Information Technology, IT-Software Company Overview BCI Central Group  (Fka BCI Asia) of companies is a subsidiary of BYGGFAKTA GROUP, a leading software, and information company within the construction industry, with a proprietary cloud-based service and a fully integrated data and software platform. The Group is a major player at the center of the construction ecosystem.BCI Central established in 1998 and was founded to create efficiencies and enhance transparency in the intrinsically complex construction industry. Our software solutions and related services achieve this while simultaneously enabling our clients to identify sales opportunities, make informed decisions and connect with key target markets. We play a crucial role in empowering businesses around the world with construction-centric tools to succeed.Additional Company Information Company Size201 - 500 Employees Average Processing Time13 days Industry Consulting (Business & Management)Benefits & Others Dental, Miscellaneous allowance, Medical, Loans, Vision, Regular hours, Mondays - Fridays, Business (e.g. Shirts), HMO, Annual leaves, Birthday leave, Work Anniversary leave Company photos BCI Asia- Top 10 Awards 2015"
title = "Digital Data Gatherer/Python Developer"
skills = [
    'Python',
    'Machine Learning',
    'Data Analysis',
    'Natural Language Processing',
    'Deep Learning',
    'Computer Vision',
    'Front-end Development',
    'Back-end Development',
    'beautiful soup',
    'programming'
]
print(rater.filter_skills(skills=skills, listing_title=title, listing_desc=text))