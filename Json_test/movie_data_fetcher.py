import json

import requests


def fetch_movie_data(api_key, total_pages):
    movie_data = []
    for page in range(1, total_pages+1):
        # API 엔드포인트와 필요한 매개변수 설정
        url = f'https://api.themoviedb.org/3/movie/now_playing?page={page}&language=ko-KR&api_key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            page_data = response.json()
            movie_data.extend(page_data['results'])
        else:
            print('Failed to fetch movie data.')
            return None
    return movie_data


def filter_movie_data(movie_data):
    filtered_data = []
    for movie in movie_data:
        if movie["overview"] == "":
            continue
        if movie["release_date"] == "":
            continue
        if movie["poster_path"] == "":
            continue
        if movie["genre_ids"] == "":
            continue

        filtered_movie = {
            "id": movie["id"],
            "model": "movies.movie",
            "fields": {
                "title": movie["title"],
                "release_date": movie["release_date"],
                "popularity": movie["popularity"],
                "vote_average": movie["vote_average"],
                "overview": movie["overview"],
                "poster_path": movie["poster_path"],
                "genre_ids": movie["genre_ids"],
                "backdrop_path": movie["backdrop_path"],
            }
        }
        filtered_data.append(filtered_movie)
    return filtered_data


def save_movie_data_to_json(movie_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(movie_data, file, indent=4, ensure_ascii=False)


api_key = 'c040cb7bd8b6353830e761a9f2364116'
total_pages = 86  # 전체 영화가 91page 지만 86 page부터 field 요소 자체가 없는경우가 있어서 오류가남 86이 최대치임
movies = fetch_movie_data(api_key, total_pages)
if movies:
    filtered_movies = filter_movie_data(movies)
    print(len(filtered_movies))
    save_movie_data_to_json(filtered_movies, 'movie_data1.json')
