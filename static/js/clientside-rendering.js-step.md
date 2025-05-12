## rendering new notes

so, to summarize; at this point:

- when the browser connects to the server, the page rendered by the server is
  obtained from the template; this is called SSR (Server Side Rendering)
- however when a new note gets created (either throught the API or by another
  browser), the server broadcasts the new note to all clients

and so at this point we still have to write the code for the browser to display
the new note; and this is called CSR (Client Side Rendering)

there is obviously some redundancy here; indeed it is important that the CSR
code creates a structure that is exactly similar to what is served by SSR in the
first place

for now, we simply duplicate - or rather, mimick - the SSR code into our `clientside-rendering.js` file

in this step, we address note creation
