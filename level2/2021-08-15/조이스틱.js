// 조이스틱
// https://programmers.co.kr/learn/courses/30/lessons/42860
// 3,4,7이 통과되지 않는데, 이유를 모르겠음
function solution(name) {
  let num = 0;
  // 바뀌어야하는 문자 개수 세기('A'가 아닌 문자 수)
  for (let i = 0; i < name.length; i++) {
    if (name[i] !== "A") {
      num += 1;
    }
  }
  // 바뀌어야하는 문자 수가 0이면 그냥 0리턴
  if (!num) {
    return 0;
  }

  let answer = 0;
  // 'A'에서 오른쪽이 빠른지 왼쪽이 빠른지 계산
  for (let ch of name) {
    answer += Math.min(
      ch.charCodeAt(0) - "A".charCodeAt(0),
      "Z".charCodeAt(0) - ch.charCodeAt(0) + 1
    );
  }

  name = name.split("");
  // 처음 시작 위치가 'A'가 아니면 반복문을 돌기전에 먼저 'A'로 만들어줌, 반복문은 현재 위치가 'A'라고 생각하고 시작
  if (name[0] !== "A") {
    num -= 1;
    name[0] = "A";
  }

  // 현재 위치
  let pos = 0;

  let cnt = num;
  while (cnt) {
    for (let i = 1; i < name.length; i++) {
      // 원형 리스트에서 오른쪽으로 i만큼 이동한 인덱스
      let r = (pos + i) % name.length;
      let l = (pos - i) % name.length;

      if (name[r] != "A") {
        answer += i;
        pos = r;
        name[pos] = "A";
        break;
      }

      if (name[l] != "A") {
        answer += i;
        pos = l;
        name[pos] = "A";
        break;
      }
    }
    cnt--;
  }

  return answer;
}
