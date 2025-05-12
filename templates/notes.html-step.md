## the HTML template

here w just do two things

- bind the `click` event of the checkbox button to the `note_done_changed` function
- and make sure to load the `update-backend.js`, since this is where that function is defined;  
  note how the `<script>` tag appears at the end of the page, this way it will
  be loaded after the HTML content is ready
