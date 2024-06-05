$(document).ready(function () {
  $(".headerPage").load("header.html");
  loadJsonData();
  // dataTable();

  // loadDataTable();

  // loadDataToJQData();
});

function loadJsonData() {
  fetch("Banqiao.json")
    .then(async (response) => {
      return response.json();
    })
    .then((json) => {
      // console.log(typeof json);
      dataTable(json);
      print(json);
    });
}

function print(dataset) {
  dataset.foreach;
}

function loadDataToJQData() {
  document.querySelector(".test").innerHTML = "🌀資料載入中";
  let rows = "";
  fetch("Banqiao.json")
    .then(async (response) => {
      return response.json();
    })
    .then((json) => {
      console.log("jsonData:", json);
      json.forEach((json) => {
        rows += `<tr><td>${json.rps07}</td><td>${json.rps08}</td><td>${json.rps11}</td></tr>`;
      });
      document.querySelector(".test").innerHTML = rows;
    });
}

function dataTable(data) {
  // console.log("123:", data);
  // var data = [
  //   [1, 2, 3],
  //   [3, 4, 3],
  //   [3, 4, 4],
  //   [3, 4, 4],
  //   [3, 4, 4],
  //   [3, 4, 4],
  //   [3, 4, 4],
  //   [3, 4, 4],
  //   [3, 4, 4],
  //   [3, 4, 4],
  //   [3, 4, 4],
  //   [3, 4, 4],
  //   [3, 4, 4],
  // ];
  $("#myTable").DataTable({
    data: data,
    ordering: false,
    columns: [
      { data: "rps21" },
      { data: "rps01" },
      { data: "rps15" },
      { data: "rps11" },
      { data: "rps07" },
    ],
  });
}

function loadDataTable() {
  content.innerHTML = "🌀資料載入中";
  fetch("Banqiao.json")
    .then(async (response) => {
      return response.json();
    })
    .then((json) => {
      let rows = `<table id="content" class="table table-bordered"><tr><th scope="col">交易年月日</th>
      <th scope="col">單價元平方公尺</th>
      <th scope="col">車位總價元</th><tr>`;
      json.forEach((json) => {
        rows += `<tr><td>${json.rps07}</td><td>${json.rps08}</td><td>${json.rps09}</td></tr>`;
      });
      rows += "</table>";
      content.innerHTML = rows;
    });

  // .then((jsonObj) => {.....
  //   let rows = `
  //            <table border="1">
  //                <tr><th>縣市</th></tr>
  //        `;

  //   jsonObj.records
  //     .sort((a, b) => {
  //       return parseInt(a.aqi) - parseInt(b.aqi);
  //     })
  //     .forEach((record) => {
  //       rows += `<tr class="${record.status}">
  //                        <td>${record.county}</td>
  //                    </tr>`;
  //     });

  //   rows += "</table>";
  //   content.innerHTML = rows;
  // });
}
