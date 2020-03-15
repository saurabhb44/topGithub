# topGithub
Django Webapp, using GitHub API to display
1) Top N Repositories of a given Organisation based on their forks count and
2) For each resultant Repository, display top committers based on their commits count.

![Main](https://github.com/saurabhb44/topGithub/blob/master/Screenshots/SS1.PNG)

## Software Requirements

* Python `3.6`
* Git

## How to get started

* on **Ubuntu**:
  * Install the required packages using the following command :  
    `sudo apt install python3.6-dev python-virtualenv build-essential git`

* on **Windows**:
  * Get Python 3.6.8 from [here](https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe) for AMD64/x64 or [here](https://www.python.org/ftp/python/3.6.8/python-3.6.8.exe) for x86
  * Git from [here](https://git-scm.com/download/win)
  * Install both using the downloaded `exe` files  

  **Important:** Make sure to check the box that says **Add Python 3.x to PATH** to ensure that the interpreter will be placed in your execution path

### Downloading the Code

* Go to (<https://github.com/saurabhb44/topGithub>) and click on **Fork**
* You will be redirected to *your* fork, `https://github.com/<your_user_name>/topGithub`
* Open the terminal, change to the directory where you want to clone the **topGithub** repository
* Clone your repository using `git clone https://github.com/<your_user_name>/topGithub`
* Enter the cloned directory using `cd topGithub-master/topGit`

### Setting up environment

* Install Pip
  * on **Ubuntu**: `sudo apt install python-pip`
  * on **Windows Powershell**: Install from: `https://bootstrap.pypa.io/get-pip.py`

* Create a virtual environment  
  * on **Ubuntu**:
    *  `python3 -m pip install --user virtualenv`
    *  `python3 -m venv env`
  * on **Windows Powershell**:
    *  `python -m pip install --user virtualenv`
    *  `python -m venv env`

* Activate the *env*
  * on **Ubuntu**: `source env/bin/activate`  
  * on **Windows Powershell**: `.\env\scripts\activate`

* Install the requirements: `pip install -r requirements.txt`

### Running server

* Change directory to **topGithub**: In terminal, change directory to Local_Directory -> topGithub-master -> topGit (Check that manage.py file must be there). `cd topGit`
* Run the server `python manage.py runserver`

Usage:

* Open browser and search in address bar for <http://localhost:8000/>
* Enter a Valid GitHub profile username and n,m.
* Boom... Results Displayed

NOTE:<br>
Github API limits the API calling to 60 calls/hour for Core API & for 10 calls/Min for Search API. "Search" is called to find top repos & "Core" is called to find top Committers. So make sure the total sum for Top Repositories (n) do not exceed 60, for that hour.
For E.g, if we take "google", "n:5" & "m:4", then for top 5 repos search API will be called once (remaining search attempts 9/10 for that minute), but to find 4 top contributers of the resultant repos, the core API will be called 5 times, once for each repo (remaining core attempts 55/60 for that hour).

Test Cases:
GOOGLE, n:5, m:3

![Google](https://github.com/saurabhb44/topGithub/blob/master/Screenshots/Google.png)

MICROSOFT, n:6, m:4

![Microsoft](https://github.com/saurabhb44/topGithub/blob/master/Screenshots/Microsoft.png)

When Username Doesn't Exist
Ex: "wewefhgj"

![DNE](https://github.com/saurabhb44/topGithub/blob/master/Screenshots/DNE.png)


Thank You
