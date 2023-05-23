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


def filter_actors(movie_data):
    filtered_data = []
    for movie in movie_data:
        if 'known_for_department' in movie and movie["known_for_department"] == "Acting":
            filtered_data.append(movie)
    return filtered_data


def filter_actor_fields(actor_data):
    filtered_data = []
    for actor in actor_data:
        if "known_for" in actor and actor["known_for"] and all(
            "overview" in movie and movie["overview"]
            for movie in actor["known_for"]
        ):
            filtered_actor = {
                "id": actor["id"],
                "fields": {
                    "name": actor["name"],
                    "profile_path": actor["profile_path"],
                    "known_for": [],
                },
            }
            for movie in actor["known_for"]:
                filtered_movie = {"id": movie["id"]}
                filtered_actor["fields"]["known_for"].append(filtered_movie)
            filtered_data.append(filtered_actor)
    return filtered_data


def save_data_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# 사용 예시
api_key = 'd39490e01fe62d2873cc30008341172d'
total_pages = 10

# 배우 데이터 필터링 및 저장
movies = fetch_movie_data(api_key, total_pages)
if movies:
    actors = filter_actors(movies)
    filtered_actors = filter_actor_fields(actors)
    save_data_to_json(filtered_actors, 'actor_data.json')