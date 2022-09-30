// 나머지가 1이 되는 수 찾기

function solution(n) {
  var answer = n - 1;
  for (let i = 2; i <= answer; i++) {
      if (answer % i === 0) return i;
  }
  return answer;
}

// n 에서 1을 뺀 수를 나누어떨어지게 하는 가장 작은 수를 구했다.