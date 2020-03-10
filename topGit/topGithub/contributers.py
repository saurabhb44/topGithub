import requests

#Function which returns top contributers in a given repository
def top_m_contributers(orgname,repo_name,m):

    #Calling Github API
    url = 'https://api.github.com/repos/' + orgname + '/' + repo_name + '/stats/contributors?page=1&per_page=100'
    res = requests.get(url)
    repos = res.json()

    #If further pages exist in Github API
    while 'next' in res.links.keys():
        res=requests.get(res.links['next']['url'])
        repos.extend(res.json())

    count =[]

    #Fulling Data in return variable
    for i in repos:
        values = {
            'name' : i['author']['login'],
            'num' : i['total'],
            'url' : i['author']['html_url']
        }
        count.append(values)

    #Reversing the dictionary as results are in ascending order of Comit Counts by default
    count.reverse()
    length = len(count)
    
    #Check weather m is greater than Committers
    if m>length:
        m = length

    dict = []

    #Filling the data in return variable
    for j in range(m):
        dict+= [{
            'name': count[j]['name'],
            'num': count[j]['num'],
            'url': count[j]['url']
        }]
    
    return dict

    

