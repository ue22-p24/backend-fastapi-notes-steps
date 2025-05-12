// the callback attached to clicking the "done" checkbox
// it is used verbatim in the HTML template
async function note_done_changed(elt, nodeId) {
    const done = elt.checked
    const url = `/api/notes/${nodeId}`
    const data = { done: done }
    const response = await fetch(url, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
    if (response.ok) {
      const data = await response.json()
      console.log(`${url} returned`, data)
    } else {
      console.error("Error updating note done status:", response.statusText)
    }
  }
