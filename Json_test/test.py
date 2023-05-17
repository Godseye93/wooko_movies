def filter_movie_data(movie_data):
    filtered_data = []
    for movie in movie_data['results']:

        filtered_movie = {
            "model": "movies.movie",
            "fields": {
                "title": movie['title'],

            }
        }
        filtered_data.append(filtered_movie)
        print(filtered_data)
    return filtered_data
