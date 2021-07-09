function solution(board) {
  let answer = 0;
  // 행, 열 길이
  const line = board.length;
  const row = board[0].length;

  // 행, 열 중 짧은 쪽이 최대 길이
  let length = line > row ? row : line;

  // 모두 1인 경우 판단
  const isOk = (item) => item === 1;
  // 정사각형 판단
  const isSquare = (i) => {
    const x = line - i;
    const y = row - i;
    // console.log(x, y, i)
    for (let l = 0; l <= x; l++) {
      for (let r = 0; r <= y; r++) {
        let cnt = 0;
        let flag = true;
        while (cnt < i) {
          // console.log(`l = ${l} r=${r} cnt=${cnt} ===`, cnt, board[l+cnt].slice(r, r + i))
          for (let idx = r; idx < r + i; idx++) {
            if (board[l + cnt][idx] === 0) {
              flag = false;
              break;
            }
          }
          // if (!board[l+cnt].slice(r, r + i)) {
          //   break;
          // }
          if (!flag) {
            break;
          }
          cnt++;
        }
        if (flag) {
          return true;
        }

        // console.log("===============================")
      }
    }
    return false;
  };

  // 최대 길이부터 1까지
  for (let i = length; i > 0; i--) {
    // console.log(i);
    if (isSquare(i)) {
      answer = i;
      break;
    }
  }

  return Math.pow(answer, 2);
}

// 2
// dp로 품
// board가 1일 때 dp의 dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] 중에 최소 값에 + 1 이 그 위치를 포함한 제일 큰 정사각형이 됨
function solution(board) {
  let answer = 0;

  let line = board.length;
  let row = board[0].length;
  // console.log(line, row)
  let dp = Array.from(Array(line), () => new Array(row));

  for (let i = 0; i < row; i++) {
    dp[0][i] = board[0][i];
    if (board[0][i] === 1 && answer === 0) {
      answer = 1;
    }
  }

  for (let i = 0; i < line; i++) {
    dp[i][0] = board[i][0];
    if (board[i][0] === 1 && answer === 0) {
      answer = 1;
    }
  }

  for (let i = 1; i < line; i++) {
    for (let j = 1; j < row; j++) {
      if (board[i][j] === 1) {
        dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1;
        answer = Math.max(dp[i][j], answer);
      } else {
        dp[i][j] = board[i][j];
      }
    }
  }

  // for (let d in dp) {
  //     console.log(d)
  // }
  // console.log(dp)

  return answer * answer;
}
