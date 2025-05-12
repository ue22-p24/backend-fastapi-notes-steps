## allow callers to modify a note

It's cool to be able to create a note, but we also want to be able to modify it

it is the purpose of this new `PATCH` endpoint

Please note in this code:

- the use of the `Body` annotation; this means that the `payload` argument is
  expected to be in the body of the request, and not in the URL or headers
- again we use the `Note` class to define the type of the payload; this means that
  FastAPI will automatically check that the incoming data is consistent with the
  `Note` class, and will return a 422 error if it is not
- also interesting, this line  
  `db_note.sqlmodel_update(payload.model_dump(exclude_unset=True))`  
  which allow us to safely update the note with the new values;  
  compare this with a tedious code were we would consider each field one by one,
  checking of that field is provided or not by the caller, and update the object
  accordingly  
  clearly this one-liner is much more readable and maintainable !
