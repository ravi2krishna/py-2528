# External Modules 
import requests # ModuleNotFoundError: No module named 'requests'

r = requests.get('https://www.python.org/')
print(r.status_code)

r = requests.get('https://www.python.org/ravi')
print(r.status_code)

if r.status_code !=200:
    print("API Not Functional")
else:
    print("API Found")
    print("Further Processing Data With API")