function solution(brown, yellow) {
  const hap = (brown - 4) / 2;

  for (let i = 1; i < hap; i++) {
    if (yellow === i * (hap - i)) {
      return [hap - i + 2, i + 2];
    }
  }
}
