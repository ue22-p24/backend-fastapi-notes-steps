## a simple redirect

generally, people will just type a URL with the domain name in their browser; i.e.  
`https://awesomenotes.io/`  
and not  
`https://awesomenotes.io/front/notes`  

so it's good practice that the `/` URL redirects to the `/front/notes` URL, which is what we do here

and in order to still get a way to see the current version of the API, we pass
another variable to the template context; this is used in the `.j2` template
(not shown here) to display the current version of the API
