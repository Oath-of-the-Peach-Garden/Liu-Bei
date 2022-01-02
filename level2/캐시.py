def solution(cacheSize, cities):
  # 캐시의 크기 cacheSize
  # 검색하는 도시 리스트 cities
  # 최근에 검색한 도시들을 우선으로 캐시에 저장하는 LRU 방식으로 캐시를 교체함
  # -> 캐시가 가득차면 제일 오래된 캐시를 지우고 최근 검색을 캐시에 저장
    answer = 0
    cache = []

    for city in cities:
        city = city.lower()

        # 캐시에 도시가 있다면 검색에 1초가 걸림
        # 캐시 리스트에서 최근 검색 도시를 제일 앞으로 올림
        if city in cache:
            idx = cache.index(city)
            answer += 1
            cache = cache[:idx] + cache[idx+1:] + [city]
        elif len(cache) < cacheSize:
          # 캐시에 도시가 없고(5초 소요), 캐시가 가득차지 않았으면
          # 캐시에 도시를 추가만 함
            cache.append(city)
            answer += 5
        else:
          # 캐시에 도시가 없고(5초 소요) 캐시가 가득 찼으면
          # 도시를 캐시에 넣고 가장 오래된 캐시를 리스트에서 제거함
            cache.append(city)
            cache.pop(0)
            answer += 5

    return answer
