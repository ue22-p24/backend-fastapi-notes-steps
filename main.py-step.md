## how to get all the details on a specific note

as you can see, the code is as simple as it gets  
here again, FastAPI takes advantage of the type hints to automatically return a JSON-encoded dictionary,
and we control the actual set of fields exposed in the result by stating that the function returns a `Note` object
