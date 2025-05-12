## more elaborate typing

until now we had only one `Note` type; in practice it is often useful to define
several several types for the same entity, because you do not expect all the
fields to be present in all cases.

for example here what we choose to do is to define:

- `NoteCreate`, the type used for creating a note, that only has a `title` and a `description`;
  so notes are always created with their `done` field set to `False`;
- `NoteUpdate`, which contains the same 2 fields augmented with the `done` field; indeed we want it to be possible to change all 3 fields - at some point one will want to change `done` to `True`, and users can also change the title and description;
- `Note`, the full type that contains all 3 fields plus the `id` field
