![](https://img.shields.io/badge/Python-3.8+-blue)
![](https://img.shields.io/badge/Django-3.2-blue)
![](https://img.shields.io/badge/djangorestframework-3.12-blue)

### About

A serialization layer for your Emby server's database, allowing information about movies, tv series and episodes to be
retrieved in `JSON` format via `GET`requests.

### Deploying the serializer

To be written.

### Available endpoints

Library data can be retrieved using the follwing endpoints:

* `/embymovies/`
* `/embyseries/`
* `/embyepisodes/`

### Ordering

Results are ordered by `id`, but passing `?ordering=name` at the end of every request will override this behavior.

### Filtering

It is possible to filter content by `IMDB`, `TVDB` or `TMDB` ids using the following query parameters:

* `?imdb=tt1234`
* `?tvdb=1234`
* `?tmdb=1234`
