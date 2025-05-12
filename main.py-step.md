## a table to store notes, and an API endpoint to create them

this is typical code to create a table in a database; note the `table=True` passed to the `Note` class  
this is what defines the actual set of columns in the database table

as far as the API is concerned, we define a `POST` endpoint to create a note  
in particular, note how minimal the code is; we  don't need to make any check on
the incoming data, it will automatically be checked for consistency; and the
framework does that based on the `note: Note` argument type  
generally speaking, FastAPI will automatically check the types of the arguments,
based on such *type hints*, and will return a 422 error if the types do not
match  
similarly, having typed the return value of the function as `Note`, FastAPI will
automatically convert the returned object to JSON, and set the appropriate HTTP
status code (201)
