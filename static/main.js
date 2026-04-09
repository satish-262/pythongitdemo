async function addTask() {
  const input = document.getElementById("task-input");
  const text = input.value.trim();
  if (!text) return;
  await fetch("/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  input.value = "";
  location.reload();
}

async function toggleTask(id) {
  await fetch(`/toggle/${id}`, { method: "POST" });
  document.getElementById(`task-${id}`).classList.toggle("done");
}

async function deleteTask(id) {
  await fetch(`/delete/${id}`, { method: "DELETE" });
  document.getElementById(`task-${id}`).remove();
}

document.getElementById("task-input").addEventListener("keydown", (e) => {
  if (e.key === "Enter") addTask();
});
