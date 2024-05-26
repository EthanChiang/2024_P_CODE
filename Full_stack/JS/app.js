// console.log("Hello World");
// // // window.alert("Wellcome");
// let user_name = window.prompt("請輸入");
// window.alert("Wellcome " + user_name);

// let x = 10; //X is a number(x is an object)
// let y = "10";
// let name = "ethan";
// // console.log(x + "10");
// // console.log(x + 10 + name + x + 50);
// // console.log(typeof x.toString());
// // console.log(x.toString); //toString 是一個function
// // 0.1 + 0.2 ===0.3  return false  因為2禁制 會有誤差

// let str = "ethan"; //若長度為x 長度為 x-1
// console.log(str.length); //length = property
// console.log(str[5]);
// console.log(str[str.length - 1]);
// str.slice(3);

// console.log(str.indexOf("the"));

// let sentece = "today is good day to die";

// console.log(sentece.split(" "));
// console.log(sentece.split("o"));

// let X
// let y = null
// console.log(typeof x)
// console.log()

// if ("好心情") {
//   console.log("HAHAHA");
// }

// const friends = ["Harry", "Ron", "Snap", "Mike", "Grace"];
// const reversed_friends = [];

// for (let i = 0; i < friends.length; i++) {
//   reversed_friends[i] = friends[friends.length - 1 - i];
//   console.log(reversed_friends[i]);
// }
// console.log(reversed_friends);

// function sayHelloToUser() {
//   alert("三秒過了");
// }

// let interval = window.setInterval(sayHelloToUser, 5000);
// window.clearInterval(interval);

// let Grace = {
//   name: "Grace",
//   age: 26,
// };

// let Wilson = {
//   name: "wilson",
//   age: 26,
//   spouse: Grace,
// };

// // console.log(Wilson.Grace.name);
// console.log(document.getElementById("myHeading1"));
// // let myHeading = document.getElementById("myHeading1");
// console.log(document.getElementsByClassName("myP"));

// let found_elements = document.querySelectorAll(".myP");
// console.log(found_elements);

// let hellos = document.getElementsByClassName("myP");
// let helloss = document.querySelectorAll(".myP");
// console.log(hellos.length);
// console.log(helloss.length);
// let body = document.querySelector("body");
// let p = document.createElement("p");
// p.innerText = "this is a new p";
// p.classList.add("myP");
// body.appendChild(p);

// console.log("改變後");
// console.log(hellos.length);  // 動態
// console.log(helloss.length);  // 靜態
// console.log(hellos);
// console.log(helloss);

// let WILSON = {
//   name: "Wilson",
//   walk: function () {
//     console.log(this.name + "正在走路");
//   },
// };

// WILSON.walk();

//addEvenListener 是一個higher order function
//react 是一個callback function
// window.addEventListener("click", react);

// window.addEventListener("click", function react() {
//   alert("點擊");
// });

//1.如果有許多callback function declararion,以後命名變數時,都需要避開
//function declaration
//2.callback function 名稱其實沒有意義
//3.程式碼變乾淨

// IIFE
// (function (a, b) {
//   console.log(a + b);
// })(10, 5);

// let hello = () => {
//   console.log("Hello World");
// };

// hello();

// let WILSON = {
//   name: "Wilson",
//   walk: () => {
//     console.log("正在走路");
//   },
// };

// WILSON.walk();

window.addEventListener("click", () => {
  alert("點擊2");
});

let addition = (a, b) => {
  return a + b;
};

addition(10, 15);

let num = () => 15;
console.log(num());
