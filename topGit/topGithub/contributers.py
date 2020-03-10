import requests

def top_m_contributers(orgname,repo_name,m):

    url = 'https://api.github.com/repos/' + orgname + '/' + repo_name + '/stats/contributors?page=1&per_page=100'
    res = requests.get(url)
    repos = res.json()

    while 'next' in res.links.keys():
        res=requests.get(res.links['next']['url'])
        repos.extend(res.json())

    count =[]

    for i in repos:
        values = {
            'name' : i['author']['login'],
            'num' : i['total'],
            'url' : i['author']['html_url']
        }
        count.append(values)

    count.reverse()
    length = len(count)
    
    if m>length:
        m = length

    dict = []

    for j in range(m):
        dict+= [{
            'name': count[j]['name'],
            'num': count[j]['num'],
            'url': count[j]['url']
        }]
    
    return dict

    

