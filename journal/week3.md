# Week 3 — Decentralized Authentication

## For this week, the goal was to implement authentication for users of Cruddur by using Amazon Cognito.

The following list shows the major steps taken, as well as highlighting issues found and resolved with troubleshooting.

1. Creating a Cognito user pool
2. Installing AWS Amplify and configuring env variables
3. Using Amplify Auth and Cognito to write functions that monitor user state and show components accordingly (i.e. user handle, username).
4. Using Amplify Auth and Cognito to authenticate users, confirm emails, and send password recovery codes.
5. Using logger.debug to track and fix issues with authentication using JSON web tokens.   
6. Modifying CORS to take the authorization header.
7. Implementing CSS style changes for better contrast and visibility

### Amplify installed

![amplifyinstall](https://user-images.githubusercontent.com/125153369/225106529-5438feec-a24d-4eab-88b2-18dd82d86cdf.PNG)

### Create Cognito user pool 

![userpool](https://user-images.githubusercontent.com/125153369/225109780-b72d2536-3c1b-40e9-bff3-e20d130c89b4.PNG)

![authenincorrect](https://user-images.githubusercontent.com/125153369/225106570-17cce9c2-03d5-40a9-a638-bc6e1abb775d.PNG)

### Successfull login with default handle/cognito user  

![successfull login](https://user-images.githubusercontent.com/125153369/225110156-c335be6e-7ba3-4bb9-af59-54efd1b67f53.PNG)

![successfullsigninafteremailconfirmation](https://user-images.githubusercontent.com/125153369/225110259-8094e3a8-f358-4cb0-8586-798978737af1.PNG)

### CSS Changes & Secret Message for authenticated user

![csschange](https://user-images.githubusercontent.com/125153369/225110473-f851ae1b-7c1c-4621-aa65-98215aeebe0d.PNG)

![css](https://user-images.githubusercontent.com/125153369/225110678-379ec4ef-a1c3-4d81-ba22-5955be968581.PNG)
