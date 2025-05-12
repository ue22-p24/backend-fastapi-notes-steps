## expose /static/ folder with the CSS style

ok so at this point we want to expose a new endpoint, `/front/notes`, which will
return the HTML page to display, and later on interact with, the notes.

in order to do that, we need to expose some **static content**; for starters we have
a stylesheet, that we store in `static/style.css`; we're not going to detail the
CSS here, as we want to focus on the backend side of things

but it's important that the browser can access this file; and the way to do that
as shown here, by "mounting" the local `static` folder to the `/static` URL.
