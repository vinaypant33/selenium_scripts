from bs4 import BeautifulSoup

# Your HTML snippet
html_content = """
<!-- Paste the HTML content here -->
"""

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the name
name = soup.find('a', class_='QKwVMNcugJZCSCraHfEjkhgrjQqBBdvPIrI')
name_text = name.get_text(strip=True) if name else "Name not found"

# Extract the job title and company
job_title_company = soup.find('div', class_='cesUrSERKWpafEWlNUJUYAicYwWVgbiQKwwU t-14 t-black t-normal')
job_title_company_text = job_title_company.get_text(strip=True) if job_title_company else "Job title or company not found"

# Extract the location
location = soup.find('div', class_='NUVcpIVwXOTmywJoLAacAoFgUrLkLSRAwWtJ t-14 t-normal')
location_text = location.get_text(strip=True) if location else "Location not found"

# Print extracted information
print(f"Name: {name_text}")
print(f"Job Title and Company: {job_title_company_text}")
print(f"Location: {location_text}")
