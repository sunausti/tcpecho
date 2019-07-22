#!/bin/bash
counter=1
HOST_IP=`kubectl get svc -n policy-demo | awk '/tcpsocket-echo/{print $3}'`
HOST_NAME='tcpsocket-echo.policy-demo.svc.cluster.local'
echo $HOST_IP
while [ $counter -le 100000 ]
do
  echo
  echo "Request: $counter"
  python3 echo-client.py $HOST_NAME
  rc=$?
  if [ $rc -ne 0 ]
  then
    echo $rc
    exit 1
  fi
  ((counter++))
  echo
done
echo "Done Done Done!!!"

