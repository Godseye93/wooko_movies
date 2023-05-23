import json

import requests


def fetch_movie_data(api_key, total_pages):
    movie_data = []
    for page in range(1, total_pages + 1):
        url = f'https://api.themoviedb.org/3/trending/person/day?page={page}&language=ko-KR&api_key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            page_data = response.json()
            movie_data.extend(page_data['results'])
        else:
            print(f'Failed to fetch movie data for page {page}.')
    return movie_data


def filter_directors(movie_data):
    filtered_data = []
    for movie in movie_data:
        # if movie["known_for_department"] == "Directing":
        if 'known_for_department' in movie and movie["known_for_department"] == "Directing":
            filtered_data.append(movie)
    return filtered_data


def filter_director_fields(director_data):
    filtered_data = []
    for director in director_data:
        if "known_for" in director and director["known_for"] and all(
            "overview" in movie and movie["overview"]
            for movie in director["known_for"]
        ):
            filtered_director = {
                "id": director["id"],
                "name": director["name"],
                "profile_path": director["profile_path"],
                "known_for": [],
            }
            for movie in director["known_for"]:
                filtered_movie = {"id": movie["id"], "fields": {}}
                if "title" in movie:
                    filtered_movie["fields"]["title"] = movie["title"]
                if "release_date" in movie:
                    filtered_movie["fields"]["release_date"] = movie["release_date"]
                if "popularity" in movie:
                    filtered_movie["fields"]["popularity"] = movie["popularity"]
                if "vote_average" in movie:
                    filtered_movie["fields"]["vote_average"] = movie["vote_average"]
                if "overview" in movie and movie["overview"]:
                    filtered_movie["fields"]["overview"] = movie["overview"]
                if "poster_path" in movie:
                    filtered_movie["fields"]["poster_path"] = movie["poster_path"]
                if "genre_ids" in movie:
                    filtered_movie["fields"]["genre_ids"] = movie["genre_ids"]
                if "backdrop_path" in movie:
                    filtered_movie["fields"]["backdrop_path"] = movie["backdrop_path"]
                filtered_director["known_for"].append(filtered_movie)
            filtered_data.append(filtered_director)
    return filtered_data


def save_director_data_to_json(director_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(director_data, file, indent=4, ensure_ascii=False)


# 사용 예시
api_key = 'd39490e01fe62d2873cc30008341172d'
total_pages = 10
movies = fetch_movie_data(api_key, total_pages)
if movies:
    directors = filter_directors(movies)
    filtered_directors = filter_director_fields(directors)
    save_director_data_to_json(filtered_directors, 'director_data.json')
