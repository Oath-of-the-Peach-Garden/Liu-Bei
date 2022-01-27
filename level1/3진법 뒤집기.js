function solution(n) {
  let answer = 0;
  // 10진법 n -> 3진법 n
  answer = toTernary(n);
  // answer = n.toString(3)
  // console.log(answer)
  // 3진법 n -> reverse
  // answer = String(answer).split('').reverse().join('');
  // reversed 3진법 n -> 10진법
  answer = ternayToDecimal(answer);

  return answer;
}

function toTernary(num) {
  let rest = num;
  let result = [];

  while (rest !== 0) {
    result.unshift(String(rest % 3));
    rest = parseInt(rest / 3);
  }

  return result;
}

function ternayToDecimal(numArray) {
  const result = numArray.reduce(
    (sum, number, idx) => sum + Number(number) * Math.pow(3, idx),
    0
  );

  return result;
}
