## a broadcaster class

for starters, we define in `broadcaster.py` a class `WebSocketBroadcaster`, that will be in charge of

- registering all the connected clients (i.e. browsers)
- broadcasting messages to all the clients
- remove then ones that are disconnected

we will see in a bit how this is used in the application
