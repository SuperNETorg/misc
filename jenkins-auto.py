import sys
import os
#from git import *
import requests
import simplejson
import time
import datetime
import pytz

#How to install requirements
# apt-get install python-pip
#pip install requests
#pip install simplejson
#pip install pytz
#
#About the script:  This python script is used to poll a github repository and based on the 'delayHours' variable settings, it wil trigger the jenkins build request.
# Note:  script wil trigger build request only once after it notced a git repo update
# After the build request, it will not trigger a build until githup repo update + delayHours is over
# This script can be installed in a cron with 5 minutes to 1 hour interval schedule
#
#Configurations.  Change the values within "< >" with an appropriate value
#

#Github Repository Name
gitHubRepo="<REPONAME>"

#Github Repository user-id
gitHubUser="<GITHUBUSER>"

#GitHub Repository Password
gitHubPass="<GITHUBPASS>"

#Status file
StatusFle="/tmp/trigger-status.txt"

#Jenkins URL
JenkinsTriggerURL="<JENKINSBUILD URL>"   # eg: http://localhost:8080/job/test/build"

#Jenkins UserID
Jenkins_userid="<JENKINSUSER>"

#Jenkins Password
Jenkis_pass="<JENKINSPASS>"

#Build Wait Hours
delayHours=3

##
#  Settings End here
####

ts = time.time()


need_jenkins_trgger=1

oldTimeStamp=(datetime.datetime.fromtimestamp(ts,tz=pytz.utc)- datetime.timedelta(minutes=60*delayHours)).strftime('%Y-%m-%dT%H:%M:%SZ')

#print "OLD TME: " + oldTimeStamp

r = requests.get("https://api.github.com/repos/" + gitHubUser + "/" + gitHubRepo + "/commits?since=" + oldTimeStamp, auth=(gitHubUser, gitHubPass))
print r.status_code
c = r.content
j = simplejson.loads(c)

for item in j:
    need_jenkins_trgger=0
    #print "Latest Commit TS" + item['commit']['author']['date']

print need_jenkins_trgger
if( need_jenkins_trgger==1):
    if (os.path.exists(StatusFle)):
        print "No action"
    else:
    	print "Jenkins Trigger"
        r = requests.post(JenkinsTriggerURL,auth=(Jenkins_userid, Jenkis_pass))
    #touch status file
        open(StatusFle,"w")
    #Trigger Jenkins
else:
	#No Jenkins trigger. Remove the file
	if(os.path.exists(StatusFle)):
		os.remove(StatusFle)
    


