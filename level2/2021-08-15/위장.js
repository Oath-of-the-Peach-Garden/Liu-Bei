function solution(clothes) {
  var answer = 1;

  const closet = {};

  for (let i = 0; i < clothes.length; i++) {
    const [, key] = clothes[i];
    if (closet[key]) {
      closet[key] += 1;
    } else {
      closet[key] = 1;
    }
  }

  for (let key in closet) {
    answer *= closet[key] + 1;
  }

  return answer - 1;
}
