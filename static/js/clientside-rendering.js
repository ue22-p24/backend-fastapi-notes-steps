function createNoteElement(note) {
    const elt = document.createElement("li");
    elt.classList.add("note");
    elt.id = `note-${note.id}`;
    const html = `
    <div class="title">${note.title}
        <button class="delete-button" onclick="note_delete(this, ${note.id})">🗑</button>
    </div>
    <div class="line">
        <span>${note.description}</span>
        <input type="checkbox" ${note.done ? "checked" : ""}
        onchange="note_done_changed(this, ${note.id})" />
    </div>
`
    elt.innerHTML = html;
    document.querySelector("ul.notes").appendChild(elt);
}

function updateNoteElement(note) {
    console.log("Updating note:", note);
}

function deleteNoteElement(noteId) {
    console.log("Deleting note with ID:", noteId);
}
