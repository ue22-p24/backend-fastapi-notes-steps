## defining SessionDep for interacting with the DB

this is boilerplate code to expose a session object, which we'll need to
actually talk to the database

it's interesting to note: this pattern is called "dependency injection"; the
`SessionDep` object allows to reference a session object even though we **do not
explicitly create it**; by defining `get_session`, we just explain **how to
create it**, the framework will ensure its creation will happen before the first
use
