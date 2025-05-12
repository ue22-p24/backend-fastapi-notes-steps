## a JS script to update the backend

here we define a (globally visible) function `note_done_changed`; its purpose is to be bound to the `done` checkbox of each note in the UI

and as you can see its job is simply to post a `PATCH` api request to the
backend, with the new value of the `done` checkbox
