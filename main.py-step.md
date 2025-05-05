## serve a HTML page from a Jinja template

this new `/front/notes/` endpoint will return a HTML page, which is rendered from a Jinja template

### templating

worth being noted here, is the way the data is passed from Python to the template, by setting the `context` parameter of the `render_template` function

### fetching data

another important point is this:  
for fetching the list of notes, we could have gotten it from the database directly, using this code

```python
def notes_page(request: Request, session: SessionDep):
    notes = session.exec(select(Note)).all()
    return templates.TemplateResponse(
        request=request,
        name="notes.html.j2",
        context={"notes": notes})
```

and that would have worked well  
however we choose to use the `/api/notes` endpoint instead, which is a bit more complex,
but allows for better flexibility in the long run, especially because the first step for scaling up will be to separate, on the one hand, the service that serves the frontend, and on the other hand the API service itself (and the DB service as well, for that matter)
