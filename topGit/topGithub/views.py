from django.http import HttpResponse
from django.shortcuts import render

#Importing Function Files
from . import repos
from . import contributers


def index(request):
    
    #Taking the inputs from HTML Form
    username = request.GET.get('uname')
    n = request.GET.get('top_repos')
    m = request.GET.get('top_commiters')
    
    names = []
    contribute = []
    context = {'check':True}
    
    #Type Conversion in Line 24 fails when n is None
    if n != None:
        
        #Computing the results from repos.py
        lists = repos.top_n_repos(username,int(n)) 

        #If Profile username is invalid
        if lists == -1:
            context = {'check': False}

        else:
            #Filling top Repositories data in names
            for data in lists:
                name = {
                    'name': data['name'],
                    'forks': data['forks']
                }
                names.append(name)

            #Filling top Committers data for each reposiroty
            for i in range(int(n)):
                obj = {
                    'repoName': names[i]['name'],
                    'values': contributers.top_m_contributers(username,names[i]['name'],int(m))
                }
                contribute.append(obj)
            #Sending data to HTML file through Context
            context = {
                'check': True,
                'organisation': username,
                'data': names,
                'contribute': contribute
            }
    #Rendering HTML Page    
    return render(request,'topGithub/index.html', context)
    