// c언어 풀이 따라 했는데 틀림
function solution(n) {
  var answer = 0;

  const binN = n.toString(2);

  let cnt = 0;
  let z = n;

  for (let i = 0; i < 19; i++) {
    if ((z >> i) & 1) {
      cnt++;
    }
  }

  for (let i = n + 1; i <= 1000000; i++) {
    let c = 0;
    for (let k = 0; k <= 19; k++) {
      if ((i >> k) & 1) {
        c++;
      }
    }
    if (c == cnt) {
      return i;
    }
  }

  return answer;
}

// 2
// 1의 개수를 찾는 함수를 찾아서 복붙,,,
// 다 맞음
// https://stackoverflow.com/questions/43122082/efficiently-count-the-number-of-bits-in-an-integer-in-javascript
function solution(n) {
  let cnt = 0;

  // 1의 개수를 계산
  function bitCount(n) {
    n = n - ((n >> 1) & 0x55555555);
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333);
    return (((n + (n >> 4)) & 0xf0f0f0f) * 0x1010101) >> 24;
  }

  // 주어진 n의 1의 개수
  cnt = bitCount(n);

  // n ~ 1000000 중 n과 1의 개수가 같은 수 찾기
  for (let i = n + 1; i <= 1000000; i++) {
    const c = bitCount(i);
    if (c == cnt) {
      return i;
    }
  }
}
