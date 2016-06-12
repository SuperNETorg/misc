#!/bin/bash
#####################################################
#Script to alert SLACK channel about a build failure#
#####################################################
#
#Generate Slack WebHook URL and paste the URL below
#
webhookURL="<webhookurl>"
#set -x

#
#BUILD INFORMATION 
# 
buildstatus=$1
jenkinInfo="*Job Name:* $JOB_NAME \n *Build Result:* $buildstatus \n *Build Number:* $BUILD_NUMBER \n *Build URL:* $BUILD_URL \n *Node Name:* $NODE_NAME \n *Git Commit:* $GIT_COMMIT "

#
#Alert Messge
#
alertText=$jenkinInfo;
if [[ -z $alertText ]]; then
    alertText="Build Failure"
fi
#
#CURL Binary Path
#
curl="/usr/bin/curl"

#
#Curl Command to call WebHook
#
$curl -X POST -H 'Content-type: application/json' --data "{\"text\": \"$alertText\", \"channel\": \"#jenkins-jobs\", \"username\": \"jenkins-bot\"}" $webhookURL
