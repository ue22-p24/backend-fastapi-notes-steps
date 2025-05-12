## the /ws endpoint

so far our application has several endpoints that are all pure HTTP endpoints -
they react to GET, POST and similar verbs;  
when it comes to websockets, things are a bit different, there is no verb, and
the connection is kept open for a long time so the endpoint has a rather
different structure, primarily it describes the behaviour of the server **during
the whole connection lifetime**, rather than just the one request and one
response that we have seen so far

so here, we basically say this:  
each time a browser connects to this `/ws/` endpoint:
- first we register the client in our broadcaster instance
- then we keep the connection open indefinitely, and we wait for messages from the client

it turns out in our application, we use websockets **only** as a back channel to
send messages from the server to the client, so we don't need to do anything
with the messages that are sent by the client
