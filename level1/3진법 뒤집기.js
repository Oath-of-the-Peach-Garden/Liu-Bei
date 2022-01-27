function solution(n) {
  let answer = 0;
  // 10진법 n -> 3진법 n
  answer = toTernary(n);
  // 3진법 n -> reverse
  answer = String(answer).split('').reverse().join('');
  // reversed 3진법 n -> 10진법
  answer = ternayToDecimal(answer);

  return answer;
}

function toTernary(num) {
  let rest = num;
  let result = '';

  while (rest > 0) {
    console.log(rest % 3, parseInt(rest / 3));
    result = String(rest % 3) + result;
    rest = parseInt(rest / 3);
  }

  return Number(result);
}

function ternayToDecimal(num) {
  const numArray = num.split('').reverse();
  const result = numArray.reduce((sum, number, idx) => {
    return sum + Number(number) * 3 ** idx;
  }, 0);

  return result;
}
