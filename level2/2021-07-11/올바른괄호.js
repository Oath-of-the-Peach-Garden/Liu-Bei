function solution(s) {
  s = s.split(""); // s를 배열로

  let cnt = 0;
  while (s.length) {
    // pop 하면서 괄호를 확인
    if (s.pop() === "(") {
      cnt++; // 여는 괄호면 +
    } else {
      cnt--; // 닫는 괄호면 -
    }

    // cnt가 0보다 커지면
    //짝이 맞지 않게 여는 괄호가 들어왔다는 의미이므로 false
    if (cnt > 0) {
      return false;
    }
  }

  // 반복문이 끝나고 cnt가 0이면 올바른 괄호
  if (cnt === 0) {
    return true;
  }
  // cnt가 0이 아니면 올바른 괄호가 아님
  return false;
}
