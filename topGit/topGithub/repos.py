import requests

#Function which Returns top n repos of a given organisation
def top_n_repos(username,n):
    
    #Calling Github API
    url = 'https://api.github.com/search/repositories?q=user:' + username + '+fork:true&sort=forks&order=desc&page=1&per_page=100'
    res=requests.get(url)
    repos=res.json()
    
    dict = []

    #Check if the User exists and returns if not
    if repos == {
        "message": "Validation Failed",
        "errors": [
            {
            "message": "The listed users and repositories cannot be searched either because the resources do not exist or you do not have permission to view them.",
            "resource": "Search",
            "field": "q",
            "code": "invalid"
            }
        ],
        "documentation_url": "https://developer.github.com/v3/search/"
        }:
        
        return -1

    

    results = 100

    #If total results exceed 100, next pages are demamded
    while 'next' in res.links.keys():
        
        #result may be greater than we require, so this if will only show us required amount results
        if results >= n:
            break
        res=requests.get(res.links['next']['url'])
        repos['items'].extend(res.json()['items'])
        results+=100
    
    #Append items in return variable
    for x in repos['items']:
        dict += [{
            'name': x['name'],
            'forks': x['forks']
        }]
        n-=1
        
        if n==0:
            break
    
    return dict

