## Chosen Method & details

I have selected the Poll method.

I have created a new repository prog8860-Lab2 and added a python app.py which will print a statement, test_app.py file which will test if the statement is correct or not and Jenkinsfile to run the pipeline. 

In the Jenkinsfile, I have added the stages build, test and notification. 

I have created the pipeline and under the configuration selected Build Trigger -> Poll SCM and schedules as H/5 * * * * which means it will run after five minutes if there is any changes in the main branch. 
Also mentioned the git repository and the jenkinsfile path, branch name etc.

For notification, I have installed the Email Extension plugin and restarted Jenkins.
from manage jenkins-> configure system under the extended email notification section I have added below details

SMTP Server : smtp.gmail.com
smtp port: 587
use smtp auth : i have checked this box
username : email address
password : for this one i went to the link https://myaccount.google.com/apppasswords and under select app wrote Jenkins and generated the token and pasted teh password here.

In the jenkinsfile i am sending the notification which will contain the build status

After that, the pipeline got triggered after 5 mins and successfully ran.