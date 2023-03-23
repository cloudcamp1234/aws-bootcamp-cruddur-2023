# Week 4 — Postgres and RDS

## This week, the focus was on creating and setting up a connection to Amazon RDS using the Postgres database engine.

### The tasks completed this week were:
<ol>
  <li>Setup RDS database using the AWS CLI, as well as setting up security groups to allow access to RDS from the gitpod development environment</li>
  <li>Write bash scripts to create, setup, and connect to the database</li>
  <li>Setup and implement Psycopg (postgres database adapter for python)</li>
  <li>Setup a lambda handler function to manage cognito confirmation</li>
  <li>Use psycopg with home/activities/ and create/activity so a user can enter cruds and have it saved on the website</li>
</ol> 



### Create RDS DB instance!

![provisionrdsclli](https://user-images.githubusercontent.com/125153369/227349082-c2309bdc-8ece-4e2c-baf3-3e4feff8c175.PNG)

![rdsinstanceconsole](https://user-images.githubusercontent.com/125153369/227350007-152b6aeb-6a3d-4c43-aeb8-e89e24bcdd79.PNG)

### Bash Script - connect to RDS DB instance

![bashconnect](https://user-images.githubusercontent.com/125153369/227353761-dce2ec92-d94f-4b2a-9ade-da67cdc59bd4.PNG)


### Lambda function

![layeradded](https://user-images.githubusercontent.com/125153369/227350542-43404dbd-9a9c-46ae-afa7-7a7767deef60.PNG)

![lambdavpc](https://user-images.githubusercontent.com/125153369/227350580-5610562d-7fc6-41df-a183-60d2d8fcd097.PNG)


### Successfully post crud

#### Postgres environment

![crudworks](https://user-images.githubusercontent.com/125153369/227354422-5d1d5c8e-5f0f-47f4-a976-c0d8ec0a1d65.PNG)

#### Cruddur website 

![crudpost](https://user-images.githubusercontent.com/125153369/227355225-f5e550af-4647-426e-ad88-bc228c47dda1.PNG)
