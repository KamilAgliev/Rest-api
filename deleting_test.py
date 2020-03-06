from requests import get

print(get('http://localhost:5000/api/jobs/delete/120').json())

print(get('http://localhost:5000/api/jobs/delete/7').json())

print(get('http://localhost:5000/api/jobs').json())
