## CSR for note updates

this now is about client-side rendering of note updates; this is a tad more
tricky than pure creation, in particular we're using the fact that notes
&lt;li&gt; elements have their `id` based on the note DB id, so we can easily
find the corresponding DOM element to update

