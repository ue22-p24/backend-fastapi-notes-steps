## the browser listens on the WS channel

in this new JS file, we program the browser: it will initialize a WebSocket
connection to the server and handle incoming messages; for now in this early
version, we simply assume incoming messages contain JSON data, so we docode it
and display it in the console

this new script is then simply included in the HTML template (we omit this diff here)

so at this point, our application has the basic WS infrastructure:

- each time a browser opens the notes page, it connects to the server on the `/ws/` endpoint
- the server knows the list of all connected clients
- also the server can detect when a client disconnects

we still need - see next step - to take advantage of that back channel, and to
have the server notify its clients of all the changes made to the notes
