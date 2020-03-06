from requests import post, get

print(post('http://localhost:5000/api/jobs/change/6',
           json={'job': 'new jobs decription',
                 'work_size': 22,
                 'collaborators': '1,2,3',
                 'is_finished': False,
                 'start_date': 'now',
                 'end_date': 'next week',
                 'creator': 1,
                 },
           ).json())

print(post('http://localhost:5000/api/jobs/change/6',
           json={},
           ).json())

print(post('http://localhost:5000/api/jobs/change/6',
           json={'h': 21},
           ).json())

print(get('http://localhost:5000/api/jobs').json())
