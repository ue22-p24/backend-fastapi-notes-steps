## HTML forms with JSON

HTML forms can have an `action` attribute that points to a URL. When the form is submitted, the browser sends a request to that URL with the form data. The server can then process the data and return a response.

However, the default way for forms to do that relies on older technologies like `application/x-www-form-urlencoded` or `multipart/form-data`. These formats are not as flexible or powerful as JSON.

This script allows you to use JSON to send form data; it is generic and can be used with any form. It uses the `fetch` API to send the data as JSON to the server.

Note the use of the call to `event.preventDefault()` to prevent the default form submission behavior.
