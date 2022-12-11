# Server
## About:
This is my **prototype** implementation of a RESTFUL API for "Freecycle-Inc", a service designed for listing items that are no longer needed or to offer services to others. My implementation was made using Express and following [the OpenAPI specification](openapi.yml) provided.

## How to run the server:
This server is designed to be used in a containerized environment, which is done via the use of docker.

### Prerequisites:
Before trying to run this server, ensure docker has been installed and you have cloned the repository.

### Instructions:
Firstly start by moving to the correct directory:
```bash
cd server 
```
Once we are inside of the directory we need to build the container:
```bash
make build
```
After the container has been built we can run the container using:
```bash
make run
```
The server should now be running on port `8000`.

## How to interact with the server:
Due to this being a server implementation, there is no user interface. This being said you can still interact with the server using curl commands. To find out more about curl commands and how to use them, see [here](https://www.geeksforgeeks.org/curl-command-in-linux-with-examples/).

### Post:
To post to the server use the following curl command:
```bash
curl -v -X POST    http://localhost:8000/item/ -H "Content-Type: application/json" -d '{"user_id": "user1234", "keywords": ["hammer","nails","tools"],"description":"A hammer and nails set","image":"https://placekitten.com/200/300","lat":51.2798438,"lon":1.0830275}'
```
### Get:
To get all items on the server use the following command:
```bash
curl -v -X GET     http://localhost:8000/items/
```
Getting all items from the server isn't always convenient, so we can use the following command to get only the item with the id of 1:
```bash
curl -v -X GET  http://localhost:8000/item/1
```
### Delete:
We need to be able to remove items from the server when they aren't available anymore, this can be done with the delete curl command:
```bash
curl -v -X DELETE  http://localhost:8000/item/1
```
### Options:
to get options, use the following curl command:
```bash
curl -v -X OPTIONS http://localhost:8000/
```
## Refrences:
- https://github.com/calaldees
- https://github.com/KieranBest
- https://github.com/Reem-313
- https://expressjs.com/en/starter/installing.html
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
- https://stackoverflow.com/questions/2573521/how-do-i-output-an-iso-8601-formatted-string-in-javascript