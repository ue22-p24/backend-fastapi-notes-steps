## create a broadcaster instance

our application needs to maintain a list of connected clients, so the main program creates one instance of the `WebSocketBroadcaster` class - this is known as a singleton pattern.

next we'll see how to take advantage of this instance for reacting on incoming websocket connections
