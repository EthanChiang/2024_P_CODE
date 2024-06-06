$(document).ready(function () {
  $(".headerPage").load("header.html");
  loadJsonData();
  TacTicTok();
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
    });
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
}

function TacTicTok() {
  let boxes = document.querySelectorAll(".box");
  let resetBtn = document.querySelector("#reset-btn");
  let newBtn = document.querySelector("#new-btn");
  let msgContainer = document.querySelector(".msg-container");
  let msg = document.querySelector("#msg");
  let turn0 = true; //playerX,player0

  const winPatterns = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [3, 4, 5],
    [6, 7, 8],
  ];

  boxes.forEach((box) => {
    box.addEventListener("click", () => {
      console.log("box was clicked");
      if (turn0) {
        box.innerText = "O";
        turn0 = false;
      } else {
        box.innerText = "X";
        turn0 = true;
      }
      box.disabled = true;
      checkWinner();
    });
  });
  const showWinner = (winner) => {
    msg.innerText = `恭喜, Winner is ${winner}`;
    msgContainer.classList.remove("hide");
    disableBoxes();
  };

  const resetGame = () => {
    turn0 = true;
    enableBoxes();
    msgContainer.classList.add("hide");
  };

  const disableBoxes = () => {
    for (let box of boxes) {
      box.disabled = true;
    }
  };

  const enableBoxes = () => {
    for (let box of boxes) {
      box.disabled = false;
      box.innerText = "";
    }
  };

  const checkWinner = () => {
    for (let pattern of winPatterns) {
      // console.log(pattern[0], pattern[1], pattern[2]);
      // console.log(
      //   boxes[pattern[0]].innerText,
      //   boxes[pattern[1]].innerText,
      //   boxes[pattern[2]].innerText
      // );
      let pos1Val = boxes[pattern[0]].innerText;
      let pos2Val = boxes[pattern[1]].innerText;
      let pos3Val = boxes[pattern[2]].innerText;
      if (pos1Val != "" && pos2Val != "" && pos3Val != "") {
        if (pos1Val == pos2Val && pos2Val == pos3Val) {
          console.log("winner", pos1Val);

          showWinner(pos1Val);
        }
      }
    }
  };

  newBtn.addEventListener("click", resetGame);
  resetBtn.addEventListener("click", resetGame);
}
