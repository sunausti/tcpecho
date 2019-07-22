TEST_HOST=`kubectl get svc -n policy-demo | awk '/tcpsocket-echo/{print $3}'`
