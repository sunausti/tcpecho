# tcpecho
This is a tcpsocket echo application on Bare metal ,Docker or Kubernetes
# Files
Dockerfile: used to build docker image
tcpsocket-echo.yaml: is used to create k8s app/svc. 'kubectl apply -f tcpsocket-echo.yaml'
socketserver.py: simply python server app
echo-client.py: python tcp client app
test_case.sh: test app( call echo-client many times)
# Usage
* python socketserver.py to start python socket server
  or kubectl apply -f tcpsocket-echo.yaml in k8s env
* python echo-client.py to echo 

