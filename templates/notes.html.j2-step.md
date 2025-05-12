## a new form in the template

This is a typical example of a HTML `<form>` element. As the name suggests, it groups all the input fields that are needed for a specific API call, here a note creation.

Thanks to the JS code added in the same step, clicking the submit button - or hitting the enter key - will trigger the API call that will create a new note.

**note**: you could be tempted to create a new note in the UI upon completion of the API call. However we're not going to do it that way, because later on we will implement a broadcast system where the server will notify all clients of a new note. This way, all clients will be able to see the new note without having to refresh the page.  
And so in particular, the UI that has created the note will create the corresponding UI element just like any other UI.