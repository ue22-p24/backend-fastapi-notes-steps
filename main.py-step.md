## using the new types

we can now take advantage of these different types to annotate the various methods, and FastAPI will automatically adjust the allowed fields in each request body accordingly

in particular with the choice made above, it is no longer possible to pass a value for `done` at creation time - and this is by design
