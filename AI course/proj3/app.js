$(document).ready(function () {
  $(".headerPage").load("header.html");

  dataTable();

  loadDataTable();

  loadDataToJQData();
});

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

function dataTable() {
  var data = [
    [1, 2, 3],
    [3, 4, 3],
    [3, 4, 4],
    [3, 4, 4],
    [3, 4, 4],
    [3, 4, 4],
    [3, 4, 4],
    [3, 4, 4],
    [3, 4, 4],
    [3, 4, 4],
    [3, 4, 4],
    [3, 4, 4],
    [3, 4, 4],
  ];
  $("#myTable").DataTable({
    searching: true,
    pageLength: "10", // 預設為'10'，若需更改初始每頁顯示筆數，才需設定
    autoWidth: true, // 預設為true　設置是否要自動調整表格寬度(false代表不要自適應)
    data: data,
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
