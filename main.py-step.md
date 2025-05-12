## changes are broadcast to all clients

now that we have a back channel for the server to talk to clients, let 's use it
to broadcast changes to all clients

this now is a pretty straightforward change;
as you can see, the messages that are sent on the ws channel are all of the form

```json
{
  "action": "create",   # or "update" or "delete"
  "note": {
    ... the details of the note
  }
}
```
