const priorityNotes = document.getElementById("priority-notes");
const prioritySelect = document.getElementById("priority-select");

function getCookie(name) {
    return document.cookie
        .split("; ")
        .find((row) => row.startsWith(`${name}=`))
        ?.split("=")[1];
}


function fetchNotes() {
    console.log("Fetching notes from server.")
    const csrftoken = getCookie("csrftoken");
    const formData = new FormData();
    formData.set("csrfmiddlewaretoken", csrftoken);

    const priorityValue = prioritySelect.value;
    if (["L", "M", "H"].includes(priorityValue)) {
        formData.set("priority", priorityValue);
    }

    fetch(
        "",
        {
            "method": "POST",
            "body": formData,
        }
    ).then((response) => {
        response.json().then((data) => updateNotes(data)).catch(console.error);
    }).catch(console.error);
}

function updateNotes(notes) {
    if (!Array.isArray(notes)) {
        console.error("This is not an array", notes);
        return;
    }

    priorityNotes.innerHTML = ""
    if (notes.length === 0) {
        const p = document.createElement("p")
        p.innerText = "No notes found."
        priorityNotes.appendChild(p);
        return;
    }

    const fields = ["author", "priority", "note"];

    for (const header of fields) {
          let div = document.createElement("div");
          div.classList.add("header")
          div.innerText = header;
          priorityNotes.appendChild(div);
    }

    for (const note of notes) {
      for (const key of fields) {
          let div = document.createElement("div");
          div.innerText = note[key] ?? "Unknown";
          if (key === "priority") {
              div.classList.add(note[key]?.toLowerCase() ?? "");
          }
          priorityNotes.appendChild(div);
      }
    }
}

fetchNotes();
