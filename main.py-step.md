## create a database with sqlmodel using a lifespan

we import the `sqlmodel` module; and in order to create the database, we define the `lifespan` function.

FastAPI expects this function to be a generator function; this allows to define the application prolog and epilog
(the prolog is executed before the first `yield` statement, and the epilog is executed after that point)

Note how the `app` variable is created by passing the `lifespan` function to the `FastAPI` constructor.

With this version, the database is created and populated when the application starts (although at this point the database is empty)
