Script to Alert Jenkins build failiure to a slack Channel
---------------------------------------------------------

Pre-requisites:
----------------

1. curl needs to be installed in the host where Jenkins is running.
2. Get the WebHook URL from Slack. To generate it: 
   a. Go to slack.com. https://my.slack.com/services/new/incoming-webhook/
   b. Select the Channel and click "Add Incoming WebHook Integration" button
   c. Copy the Webhook URL and update it in slack-alert.sh
3. The slack-alert.sh needs to be installed at a path in the system. File permission should be in such a way that the "Jenkins" user is able to read and execute this script.
4. Test the slack-alert.sh by executing it manually. It should send a notification to the channel.


Script Installation & Jenkins Configuration Steps:
---------------------------------------------------

1. Login to Jenkins
2. Go to Manage Jenkins --> Manage Plugins --> Available
3. Search for "Hudson Post build task". Select the plugin and install it.
4. Open the build task from jenkins dashboad -> Configure 
5. Under "Post Build Action" add:  "Post Build Task"
6. Give the path of the shell script:  slack-alert.sh  eg: /tmp/slack-alert.sh
7. Under "Log text" area, add the proper build failure message from your build activity. Note that: trigger of the slack-alert.sh depends on this regex match
8. Save and Apply.

