import requests
from bs4 import BeautifulSoup

url = 'https://www.seek.co.nz/python-jobs?salaryrange=30000-40000&salarytype=annual'

if '__main__' == __name__:
    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')
 
    def get_data(tag: BeautifulSoup):
        return tag.has_attr('data-search-sol-meta')

    results = html.find_all(get_data(html))
    
    for job in results:
        try:
            titleEleemnt = job.find('a', attrs={"data-automation": "jobTitle"})
            title = titleEleemnt.get_text()
            company = job.find('a', attrs={'data-automation': 'jobCompany'}).get_text()
            jobLink = 'https://www.seek.co.nz' + titleEleemnt['href']
            salary = job.find('span', attrs={"data-automation": "jobSalary"})
            salary = salary.get_text() if salary else 'N/A'

            job = "Title {}\n Company {}\n Salary {}\n Link {}a\n"

            job = job.format(title, company, jobLink, salary)
            print(job)
        except Exception as e:
            print("Exception {} ".format(e))
            pass