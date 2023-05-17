import json

import requests


def fetch_movie_data(api_key):
    # API 엔드포인트와 필요한 매개변수 설정
    url = f'https://api.themoviedb.org/3/movie/now_playing?page=9&language=ko-KR&api_key={api_key}'
    response = requests.get(url)
    # print(response)
    if response.status_code == 200:
        movie_data = response.json()
        return movie_data
    else:
        print('Failed to fetch movie data.')
        return None


def filter_movie_data(movie_data):
    filtered_data = []
    for movie in movie_data['results']:
        if movie["overview"] == "":
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


# 사용 예시
api_key = '44f7bac2823c6308d04f29254d02a914'
movies = fetch_movie_data(api_key)
if movies:
    filtered_movies = filter_movie_data(movies)
    save_movie_data_to_json(filtered_movies, 'movie_data9.json')
