# Client
## About:
This is my **prototype** implementation of the client for the ["Freecycle-Inc" Restful API server](https://github.com/Joshua-Yuill/frameworks_and_languages_module/tree/main/server). This is a client facing application that will be used by the user to post, get and delete from the server. My implementation was done using the Vue Framework, with using bootstrap framework for css
## How to run the client:
This client is designed to be used in a containerized environment, which is done via the use of docker.

### Prerequisites:
Before trying to run this client, ensure docker has been installed and you have cloned the repository.

### Instructions:
Firstly start by moving to the correct directory:
```bash
cd client
```
Once we are inside of the directory we need to build the container:
```bash
make build
```
After the container has been built we can run the container using:
```bash
make run
```
The client should now be running on port `8001`.

## How to interact with the client:
Once the container has been run navigate to port `8001` then you will need to connect to the server.

### Connecting to the server
To connect to the server, on the end of the client url add `?api=` like can be seen bellow:
```
[clientURL]?api=[serverUrl]
```
For example:
```
http://localhost:8001?api=http://localhost:8000
```

## Refrences:
- https://github.com/calaldees
- https://github.com/KieranBest
- https://github.com/Reem-313
- https://getbootstrap.com/docs/5.2/getting-started/introduction/
- https://www.w3schools.com/bootstrap/
- https://vuejs.org/guide/introduction.html
- https://www.computerhope.com/issues/ch001704.htm#:~:text=Adding%20the%20%22list%2Dstyle%3A,removes%20any%20bullet%20or%20number.
- https://mdbootstrap.com/docs/b4/jquery/components/panels/