// ans = parseInt(prompt("input a number"));
// console.log(ans);
// console.log(typeof ans);
let ans = Math.floor(Math.random() * 100);
let n1 = 0;
let n2 = 99;
console.log(ans);
console.log(Math.random());
// input = parseInt(prompt("input a number between 0~100"));
while (true) {
  input = parseInt(prompt("input a number between " + n1 + " ~ " + n2));

  if (n2 < input || input < n1) {
    alert("無效猜測");
    continue;
  }

  if (ans == input) {
    alert("bingo");
    break;
  } else if (input > ans) {
    n2 = input;
  } else if (input < ans) {
    n1 = input;
  }
}
