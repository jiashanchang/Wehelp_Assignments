let src =
        "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
      fetch(src)
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          let newData = data.result.results;
          function show(start, end, divClass) {
            for (let i = start; i < end; i++) {
              let site = newData[i].file;
              let firstSite = site.toString().split("https:")[1];
              let newFirstSite = "https:" + firstSite;

              let mainElement = document.getElementById("main");

              let divElement = document.createElement("div");
              divElement.setAttribute("class", divClass);

              let imageElement = document.createElement("img");
              imageElement.setAttribute("src", newFirstSite);
              divElement.appendChild(imageElement);

              let placename = document.createElement("div");
              let textTitle = document.createTextNode(newData[i].stitle);
              placename.setAttribute("class", "placename");
              placename.appendChild(textTitle);
              divElement.appendChild(placename);
              mainElement.appendChild(divElement);
            }
          }
          show(0, 1, "promotion1");
          show(1, 2, "promotion2");
          show(2, 10, "picture");

          function loadMore(count) {
            let load = document.getElementsByClassName("placename").length;
            count = load;
            rest = newData.length - count;
            if (rest >= 8) {
              show(count, count + 8, "picture");
            } else {
              show(count, count + rest, "picture");
            }
          }
          let onClick = document.getElementsByTagName("button")[0];
          onClick.addEventListener("click", loadMore, false);
        });