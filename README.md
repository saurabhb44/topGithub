# topGithub
Django Webapp, using GitHub API to display
1) Top N Repositories of a given Organisation based on their forks count and
2) For each resultant Repository, display top committers based on their commits count.

Test Cases:
GOOGLE, n:5, m:3

![Google](https://github.com/saurabhb44/topGithub/blob/master/topGit/Screenshots/Google.png)

MICROSOFT, n:6, m:4

![Microsoft](https://github.com/saurabhb44/topGithub/blob/master/topGit/Screenshots/Microsoft.png)

NOTE:
Github API limits the API calling to 60 calls/hour & for Search API 10 calls/Min
So make sure the total sum for Top Repositories (n) do not exceed 60, for that hour.

Usage:
1. Clone Repository
2. Make sure Django & Python is installed on your PC
3. In terminal, change directory to Local_Dictory/topGithub/topGit (manage.py file must be there).
4. Run command: python manage.py runserver
5. Open browser and search for in address bar http://localhost:8000/
6. Enter a Valid GitHub profile username and n,m.
7. Boom... Results Displayed

Thank You
