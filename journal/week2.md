# Week 2 — Distributed Tracing

For this week, the focus was on distributed tracing, which is a way of tracking application requests (HTTP, POST, GET, etc.) in order to collect data and have better observability and performance monitoring.

## Honeycomb

Honeycomb is one of the distributed tracing software that will be used in this project.

Honeycomb was set up within our application, and mock data was collected:

![app now](https://user-images.githubusercontent.com/125153369/223208520-9074298f-6709-482f-b074-613e9cfa636e.PNG)
![query](https://user-images.githubusercontent.com/125153369/223208529-e398b915-5d41-46e0-a160-3a55ff76871e.PNG)
![mulltiplespans](https://user-images.githubusercontent.com/125153369/223208537-b80251d0-6b63-4ea5-9803-b59fc032f434.PNG)
![spans](https://user-images.githubusercontent.com/125153369/223208545-4cd517bb-f0ba-40d4-a317-0e01a171f9ba.PNG)


## Rollbar

Rollbar, another distributed tracing software, was implemented as well.


![rollbar](https://user-images.githubusercontent.com/125153369/223208778-c76317c5-0eab-4b02-bd00-a2e1caa335b6.PNG)
![rollbar2](https://user-images.githubusercontent.com/125153369/223208780-2d879c2c-dd77-4740-afde-d4f84df95565.PNG)


## XRay

AWS XRay, which is the in-house distributed tracing system for Amazon Web Services, was also implemented. Of the three, this was the most challenging to implement.
 

![xray-sampling-rule](https://user-images.githubusercontent.com/125153369/223209181-646b67f8-1f93-4e24-92c7-65a5b2f10333.PNG)
![xraytraces](https://user-images.githubusercontent.com/125153369/223209196-6ef1fa34-ac7d-4e9c-b8c7-dda2eef7631a.PNG)
![xraytraces2](https://user-images.githubusercontent.com/125153369/223209208-c5fa346a-4746-4b40-958c-e06057926f8c.PNG)
![xrayworking](https://user-images.githubusercontent.com/125153369/223209217-144484a5-9f9e-4990-8399-d41daff8e2ea.PNG)


## CloudWatch Logs

We used CloudWatch Logs to monitor the traces sent from the application using XRay.


