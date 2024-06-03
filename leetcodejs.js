grid = [
  [9, 9, 8, 1],
  [5, 6, 2, 6],
  [8, 2, 6, 4],
  [6, 2, 2, 2],
];
const largestLocal = function (grid) {
  let max = [
    [0, 0],
    [0, 0],
  ];

  for (let i = 0; i < grid.length - 1; i++) {
    for (let j = 0; j < grid.length - 1; j++) {
      if (grid[i][j] > max[0][0]) {
        max[0][0] = grid[i][j];
      }
      console.log("max1:" + max[0][0]);
    }
  }

  for (let i = 0; i < grid.length - 1; i++) {
    for (let j = 1; j < grid.length; j++) {
      if (grid[i][j] > max[0][1]) {
        max[0][1] = grid[i][j];
      }
      console.log("max2:" + max[0][1]);
    }
  }

  for (let i = 1; i < grid.length; i++) {
    for (let j = 0; j < grid.length - 1; j++) {
      if (grid[i][j] > max[1][0]) {
        max[1][0] = grid[i][j];
      }
      console.log("max3:" + max[1][0]);
    }
  }

  for (let i = 1; i < grid.length; i++) {
    for (let j = 1; j < grid.length; j++) {
      if (grid[i][j] > max[1][1]) {
        max[1][1] = grid[i][j];
      }
      console.log("max4:" + max[1][1]);
    }
  }

  console.log(max);
  return max;
};

largestLocal(grid);
