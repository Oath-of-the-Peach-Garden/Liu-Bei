// 124 나라의 숫자

function solution(n) {
  let answer = "";

  const numbers = ["1", "2", "4"];

  while (n > 0) {
    // 0이 없기 때문에 자리를 계산할 때마다 1씩 빼줘야한다.
    n -= 1;
    // 3으로 나눈 나머지를 answer 앞에 붙여줌
    answer = String(numbers[n % 3]) + answer;
    // console.log(n%3, numbers[n%3])

    // 다음 반복문에는 3으로 나눈 몫
    n = parseInt(n / 3);
  }
  return answer;
}
