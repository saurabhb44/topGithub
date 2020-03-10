# topGithub
Django Webapp, using GitHub API to display
1) Top N Repositories of a given Organisation based on their forks count and
2) For each resultant Repository, display top committers based on their commits count.

![Main](https://github.com/saurabhb44/topGithub/blob/master/Screenshots/SS1.PNG)

Usage:
1. Clone Repository
2. Make sure Django & Python is installed on your PC
3. In terminal, change directory to Local_Directory/topGithub/topGit (manage.py file must be there).
4. Run command: `
python manage.py runserver`
5. Open browser and search in address bar for http://localhost:8000/
6. Enter a Valid GitHub profile username and n,m.
7. Boom... Results Displayed

NOTE:
Github API limits the API calling to 60 calls/hour & for Search API 10 calls/Min
So make sure the total sum for Top Repositories (n) do not exceed 60, for that hour.

Test Cases:
GOOGLE, n:5, m:3

![Google](https://github.com/saurabhb44/topGithub/blob/master/Screenshots/Google.png)

MICROSOFT, n:6, m:4

![Microsoft](https://github.com/saurabhb44/topGithub/blob/master/Screenshots/Microsoft.png)

When Username Doesn't Exist
Ex: "wewefhgj"

![DNE](https://github.com/saurabhb44/topGithub/blob/master/Screenshots/DNE.png)


Thank You
