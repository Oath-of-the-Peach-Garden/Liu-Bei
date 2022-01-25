// 1
// 대체해야할 문자열을 인덱스 순서대로 배열로 만들어 놓고
// s의 처음부터 확인하면서 숫자이면 바로 answer에 추가하고
// s[idx]가 문자열이면 저장해놓은 다음에 다음 인덱스로 이동하면서 저장된 문자열이 배열에 있는지 확인함
// 배열에 있는게 확인되면 해당 인덱스를 answer에 이어 붙이고 저장된 문자열은 ""로 초기화함

function solution(s) {
  var answer = '';

  // 인덱스 - 숫자를 바꿀 때 사용할 배열
  const number = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
  ];

  // 인덱스에 문자가 있을 경우 저장할 변수
  let temp = '';
  for (let idx = 0; idx < s.length; idx++) {
    if (Number(s[idx]) || s[idx] === '0') {
      // idx에 숫자가 있을 경우 answer에 추가함
      answer += s[idx];
    } else {
      temp += s[idx]; // 문자를 temp에 추가하고 인덱스를 검색
      const index = number.indexOf(temp);
      if (index !== -1) {
        // 인덱스가 검색되면 answer에 인덱스를 추가하고 temp를 초기화함
        answer += index;
        temp = '';
      }
    }
  }
  return Number(answer);
}

// 2
// replaceAll을 사용해서 해결하려고 했는데, replaceAll은 나온지 얼마 안된 메소드라
// 모든 브라우저에서 사용되지 않는 것 같음
// RegExp로 정규표현식을 만들어서 replaceAll을 사용해봤는데도 오류로 인해 통과가 안됨
// 그래서 indexOf가 -1이 아닐 때까지 replace를 해주는 방법으로 풀이함

function solution(s) {
  var answer = s;

  // 인덱스 - 숫자를 바꿀 때 사용할 배열
  const number = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
  ];

  number.forEach((num, idx) => {
    while (answer.indexOf(num) !== -1) {
      answer = answer.replace(num, String(idx));
    }
  });

  return Number(answer);
}
