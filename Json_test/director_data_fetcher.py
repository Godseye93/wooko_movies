import json

import requests


def fetch_movie_data(api_key, total_pages):
    movie_data = []
    for page in range(1, total_pages+1):
        url = f'https://api.themoviedb.org/3/trending/person/day?page={page}&language=ko-KR&api_key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            page_data = response.json()
            movie_data.extend(page_data['results'])
        else:
            print('Failed to fetch movie data.')
            return None
    return movie_data


def filter_director_data(movie_data):
    filtered_data = []
    for movie in movie_data:
        if 'known_for_department' in movie and movie['known_for_department'] == 'Directing':
            if movie.get('known_for') and len(movie['known_for']) > 0:
                known_for = movie['known_for'][0]
                if known_for.get('title') and known_for.get('release_date') and known_for.get('poster_path') and known_for.get('genre_ids'):
                    filtered_movie = {
                        'id': movie['id'],
                        'model': 'movies.director',
                        'fields': {
                            'name': movie.get('name'),
                            'profile_path': movie.get('profile_path', None),  # None으로 설정
                            'title': known_for.get('title'),
                            'release_date': known_for.get('release_date'),
                            'popularity': known_for.get('popularity'),
                            'vote_average': known_for.get('vote_average'),
                            'overview': known_for.get('overview', None),
                            'poster_path': known_for.get('poster_path'),
                            'genre_ids': known_for.get('genre_ids'),
                            'backdrop_path': known_for.get('backdrop_path')
                        }
                    }
                    if None in filtered_movie['fields'].values():
                        continue
                    filtered_data.append(filtered_movie)
    return filtered_data


def save_movie_data_to_json(movie_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(movie_data, file, indent=4, ensure_ascii=False)


api_key = 'd39490e01fe62d2873cc30008341172d'
total_pages = 10

movies = fetch_movie_data(api_key, total_pages)
if movies:
    filtered_directors = filter_director_data(movies)
    print(len(filtered_directors))
    save_movie_data_to_json(filtered_directors, 'director_data.json')
