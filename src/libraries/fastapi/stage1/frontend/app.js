
fetch("http://127.0.0.1:8000/api/users")

  .then(res => res.json())
  .then(data => {
    const ul = document.getElementById("users");
    data.forEach(user => {
      ul.innerHTML += `<li>${user.name}</li>`;
    });
  });
