# Week 1 — App Containerization

## Required Homework/Tasks

In this week, we worked with containerizing the Cruddur application using Docker.

## Backend

1. Make sure flask is installed in gitpod
```pip install flask
```
2. Change directories to backend
    cd backend-flask
3. Set env variables for frontend and backend urls
    export FRONTEND_URL="*"
    export BACKEND_URL="*"
4. Run the flask application
    python3 -m flask run --host=0.0.0.0 --port=4567

## Create Dockerfile for Backend

The following script was used to containerize the backend

    FROM python:3.10-slim-buster

    WORKDIR /backend-flask

    COPY requirements.txt requirements.txt
    RUN pip3 install -r requirements.txt

    COPY . .

    ENV FLASK_ENV=development

    EXPOSE ${PORT}
    CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
    
    
The following commands were used to build and run the application:

    docker build -t  backend-flask ./backend-flask
    docker run --rm -p 4567:4567 -it backend-flask
    
    
## Frontend Dockerfile

Before building the Dockerfile for the frontend, npm install is required

    cd frontend-react-js
    npm i
    
We then create the Dockerfile:

    FROM node:16.18

    ENV PORT=3001

    COPY . /frontend-react-js
    WORKDIR /frontend-react-js
    RUN npm install
    EXPOSE ${PORT}
    CMD ["npm", "start"]
    
Build/Run Frontend Dockerfile

    docker build -t frontend-react-js ./frontend-react-js 
    docker run -p 3001:3001 -d frontend-react-js
    
## Docker Compose / Multiple Containers

In the root, we created a Dockerfile to run multiple containers simultaneously.
This file includes installation scripts for Postgres and AWS DynamoDB locally.

    version: "3.8"
    services:
      backend-flask:
        environment:
          FRONTEND_URL: "https://3001-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
          BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
        build: ./backend-flask
        ports:
          - "4567:4567"
        volumes:
          - ./backend-flask:/backend-flask
      frontend-react-js:
        environment:
          REACT_APP_BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
        build: ./frontend-react-js
        ports:
          - "3001:3001"
        volumes:
          - ./frontend-react-js:/frontend-react-js

      dynamodb-local:
        # https://stackoverflow.com/questions/67533058/persist-local-dynamodb-data-in-volumes-lack-permission-unable-to-open-databa
        # We needed to add user:root to get this working.
        user: root
        command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
        image: "amazon/dynamodb-local:latest"
        container_name: dynamodb-local
        ports:
          - "8000:8000"
        volumes:
          - "./docker/dynamodb:/home/dynamodblocal/data"
        working_dir: /home/dynamodblocal

      db:
        image: postgres:13-alpine
        restart: always
        environment:
          - POSTGRES_USER=postgres
          - POSTGRES_PASSWORD=password
        ports:
          - '5432:5432'
        volumes: 
          - db:/var/lib/postgresql/data
      # the name flag is a hack to change the default prepend folder
      # name when outputting the image names
      networks: 
        internal-network:
          driver: bridge
          name: cruddur

      volumes:
       db:
         driver: local
         
 Script for Postgres (added to gitpod.yml)
 
    - name: postgres
    init: |
      curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
      echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
      sudo apt update
      sudo apt install -y postgresql-client-13 libpq-dev
      

     
Postgres Installed  ![postgres](https://user-images.githubusercontent.com/125153369/221335377-38404b9e-cd83-47bb-b490-b49452e25a8c.PNG)

Docker Images ![docker images](https://user-images.githubusercontent.com/125153369/221335412-d559f66d-03f2-47a7-bfb3-1002fb309da0.PNG)


## Adding Notification Feature

![cruddurnotis](https://user-images.githubusercontent.com/125153369/221335417-d6548290-81b2-428f-915d-01f9c576ac4e.PNG)

![cruddurmessages](https://user-images.githubusercontent.com/125153369/221335418-9464efb6-2230-46f0-bd74-99c1c3cc3dc5.PNG)



    
    
    
    
    
    
