import requests


def top_n_repos(username,n):
    
    url = 'https://api.github.com/search/repositories?q=user:' + username + '+fork:true&sort=forks&order=desc&page=1&per_page=100'
    res=requests.get(url)
    repos=res.json()

    dict = []

    results = 100

    while 'next' in res.links.keys():
        if results >= n:
            break
        res=requests.get(res.links['next']['url'])
        repos['items'].extend(res.json()['items'])
        results+=100
    
    for x in repos['items']:
        dict += [{
            'name': x['name'], 'forks': x['forks']
        }]
        # dict+=obj
        n-=1
        if n==0:
            break
    
    return dict

