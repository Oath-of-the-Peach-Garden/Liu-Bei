function solution(lottos, win_nums) {
  // input
  // 일부가 지워진 로또 번호 숫자 배열 lottos
  // 1등 당첨 번호 숫자 배열 배열 win_nums

  // output
  // 구매한 로또의 최고 순위와 최저 순위

  // 최고 순위 - 지워진 번호가 모두 맞았을 경우
  // 최저 순위 - 지워진 번호가 모두 틀렸을 경우

  // win_nums의 값이 lottos에 들어있는지 확인해야 함
  // lottos에 담겨있는 숫자 중 지워진 번호(0)이 몇 개인지 확인함 -> unknown
  const unknown = lottos.reduce((cnt, num) => {
    if (num === 0) return cnt + 1;
    else return cnt;
  }, 0);

  // lottos 숫자중 win_nums 배열의 숫자와 일치하는 숫자가 몇 개 인지 확인함 -> checked
  const checked = lottos.reduce((cnt, num) => {
    if (win_nums.includes(num)) return cnt + 1;
    else return cnt;
  }, 0);

  // 최고 순위 = 7 - (unknown + checked)
  const high = 7 - (unknown + checked);
  // 최저 순위 = checked 가 1과 같거나 작으면 6등 아니면 7 - checked
  const low = 7 - checked;

  const score = (cnt) => (cnt === 7 ? 6 : cnt);

  return [score(high), score(low)];
}
