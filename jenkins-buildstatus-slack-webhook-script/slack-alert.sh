#!/bin/bash
#####################################################
#Script to alert SLACK channel about a build failure#
#####################################################
#
#Generate Slack WebHook URL and paste the URL below
#
webhookURL="<webhookurl>"

#
#Alert Messge
#
alertText="Build Failure"

#
#CURL Binary Path
#
curl="/usr/bin/curl"

#
#Curl Command to call WebHook
#

$curl -X POST -H 'Content-type: application/json' --data "{\"text\": \"$alertText\" }" $webhookURL
