![](https://img.shields.io/badge/Python-3.8+-blue)
![](https://img.shields.io/badge/Django-3.2-blue)
![](https://img.shields.io/badge/djangorestframework-3.12-blue)

### About

A serialization layer for your Emby server's database, allowing information about movies, tv series and episodes to be
retrieved in `JSON` format via `GET` requests.

### Deploying the serializer

The easiest way to deploy the serializer is by creating a `docker-file.yml` inside the project's main folder, with the
following structure:

```yaml
version: '3'
services:
  serializer:
    container_name: emby-serializer
    build:
      context: .
    ports:
      - "8888:8888"
    volumes:
      - /path/to/emby/library/folder:/app/data/emby
```

Next you have to build the image:
```shell
docker-compose build
```

And start the container:
```shell
docker-compose up -d
```

### Available endpoints

Library data can be retrieved using the follwing endpoints:

* `/embymovies/`
* `/embyseries/`
* `/embyepisodes/`

### Ordering

Results are ordered by `id`, but passing `?ordering=name` at the end of every request will override this behavior.

### Filtering

It is possible to filter results by `IMDB`, `TVDB` or `TMDB` ids using the following query parameters:

* `?imdb=tt1234`
* `?tvdb=1234`
* `?tmdb=1234`

### Performance

Due to the fact that Emby server acccess its database in exclusive mode, the serializer must always work with a
temporary copy of the db file, which can impact performance and response times depending on the size of the database.