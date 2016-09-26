# misc

- kickstart - Bash script to run any supported coin sychronization in Iguana, monitor it and include total sync time into kickstart.log. Usage: `./kickstart COIN` from `SuperNET/iguana` folder. `kickstart` is a more verbose, operator-attended version and `kickstart_jenkins` is prepared for automated jobs. The `_maxhelpers` script versions will maximize numhelpers parameter to equal the number of available CPU cores, while the plain version will use the numhelpers value in the reference gencoin.json versions.

- jenkins-auto.py - Trigger Jenkins build when last commit was made more than X hours ago.

- iguanaBTCloop.sh - Script to restart iguana + addcoin btc in case it crashed (ie. segfault error).  
Run it inside of a screen session, like
`./iguanaBTCloop.sh &`.

