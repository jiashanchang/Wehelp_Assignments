function search() {
  const username = document.getElementById("username").value;
  fetch("http://127.0.0.1:3000/api/member?username=" + username)
    .then(function (response) {
      return response.json();
    })
    .then(function (value) {
      document.getElementById("searchName").innerHTML =
        value.data.name + "(" + value.data.username + ")";
    })
    .catch(function (error) {
      document.getElementById("searchName").innerHTML = "查無此人";
    });
}

function update() {
  const update = document.getElementById("update").value;
  fetch("http://127.0.0.1:3000/api/member", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name: update }),
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (value) {
      document.getElementById("updateName").innerHTML = "更新成功";
    })
    .catch(function (error) {
      document.getElementById("updateName").innerHTML = "更新失敗";
    });
}
