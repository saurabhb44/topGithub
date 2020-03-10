from django.http import HttpResponse
from django.shortcuts import render
from . import repos
from . import contributers


def index(request):
    username = request.GET.get('uname')
    n = request.GET.get('top_repos')
    m = request.GET.get('top_commiters')
    
    names = []
    contribute = []
    context = {'check':True}
    
    if n != None:
        lists = repos.top_n_repos(username,int(n))

        if lists == -1:
            context = {'check': False}

        else:
            for data in lists:
                name = {
                    'name': data['name'],
                    'forks': data['forks']
                }
                names.append(name)


            for i in range(int(n)):

                obj = {
                    'repoName': names[i]['name'],
                    'values': contributers.top_m_contributers(username,names[i]['name'],int(m))
                }
                contribute.append(obj)
            
            for buf in contribute:
                print(buf, end= "\n")
            
            context = {
                'check': True,
                'organisation': username,
                'data': names,
                'contribute': contribute
            }
        
        

    

    return render(request,'topGithub/index.html', context)
    