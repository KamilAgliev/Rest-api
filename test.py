from requests import get, post

# class work 3
print(get('http://localhost:5000/api/jobs').json())

print(get('http://localhost:5000/api/jobs/7').json())

print(get('http://localhost:5000/api/jobs/123').json())

print(get('http://localhost:5000/api/jobs/sffd').json())

# adding with open request
print(post('http://localhost:5000/api/jobs',
           json={'id': '1',
                 'team_leader': '1',
                 'job': 'jobs decription',
                 'work_size': 21,
                 'collaborators': '1,2,3',
                 'is_finished': False,
                 'start_date': 'now',
                 'end_date': 'next week',
                 'creator': 1,
                 },
           ).json())
# checking if job with same id exists
print(post('http://localhost:5000/api/jobs',
           json={'id': '6',
                 'team_leader': '1',
                 'job': 'jobs decription',
                 'work_size': 21,
                 'collaborators': '1,2,3',
                 'is_finished': False,
                 'start_date': 'now',
                 'end_date': 'next week',
                 'creator': 1,
                 },
           ).json())
# empty request
print(post('http://localhost:5000/api/jobs',
           json={},
           ).json())
