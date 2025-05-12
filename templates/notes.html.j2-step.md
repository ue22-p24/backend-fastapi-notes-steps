## a Jinja template for notes

here's the Jinja template for the notes page;  
as you can see it's mostly HTML, with a few Jinja tags to insert the data from the FastAPI backend.

The Python code renders this template with a *context*, which is a dictionary of variables that are passed to the template.

In this template we see a few of the Jinja features in action:

### `{% for note in notes %}`

For example this template iterates over the `notes` variable, which is expected to be a list of dictionaries, each one representing a note.

Once rendered, this template will thus contain as many `<li>` elements as there are notes in the `notes` list.

### ` {{ note.title }}`

Using the `{{ ... }}` syntax, we can insert the value of a variable in the template.

### `{% if note.done %}`

We can also see in this example a use of a conditional statement.
