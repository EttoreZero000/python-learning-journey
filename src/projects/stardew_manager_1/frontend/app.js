const backendURL = "http://localhost:8000";

document.getElementById("test").addEventListener("click", async () => {
    const res = await fetch(`${backendURL}/ping`);
    const data = await res.json();
    document.getElementById("output").innerText = JSON.stringify(data);
});
