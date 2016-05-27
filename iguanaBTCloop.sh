

#!/bin/bash

iguana_home="~/SuperNET/iguana"

while true; do

  if [ "$(pidof iguana)" ]; then

        sleep 30 # Iguana is running, waiting 30 seconds for next check

  else

        echo "Iguana Stopped Running. Waiting 10 seconds to restart ..."

        sleep 10

        cd "$iguana_home"

        $PWD/../agents/iguana &

        sleep 20

        curl --url "http://127.0.0.1:7778" --data "{\"agent\":\"iguana\",\"method\":\"addcoin\",\"newcoin\":\"BTC\",\"active\":1,\"services\":0}" &

  fi

done

