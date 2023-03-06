# Week 2 — Distributed Tracing

For this week, the focus was on distributed tracing, which is a way of tracking application requests (HTTP, POST, GET, etc.) in order to collect data and have better observability and performance monitoring.

## Honeycomb

Honeycomb is one of the distributed tracing software that will be used in this project.

For setting it up within our application, the following steps were taken:

1. Add the following llibraries to requirements.txt

```
opentelemetry-api 
opentelemetry-sdk 
opentelemetry-exporter-otlp-proto-http 
opentelemetry-instrumentation-flask 
opentelemetry-instrumentation-requests

```
Install dependencies
 
```
pip install -r requirements.txt
```

2.


