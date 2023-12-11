FROM node:16-bullseye as asset_compiler
WORKDIR /code
COPY ./static_src /code/static_src
COPY ./package*.json /code/
COPY ./.eslintrc .
COPY ./.babelrc .
COPY ./.sasslintrc .
COPY ./postcss.config.js .
COPY ./config /code/config
COPY ./webpack.config.js .
RUN npm install
RUN npm run production

# syntax=docker/dockerfile:1
FROM python:3.11-slim
RUN apt-get update && apt-get -y install libpq-dev gcc git sed
RUN python -m pip install --upgrade pipenv
# Check .dockerignore if files are missing
WORKDIR /code
COPY . .
COPY --from=asset_compiler /code/static_build /code/static_build
RUN pipenv install --deploy --ignore-pipfile --system
RUN SECRET_KEY='something' \
    DATABASE_URL='postgres://user:pass@server:8000/db' \
    EMAIL_HOST='something' EMAIL_HOST_PASSWORD='something' \
    python manage.py collectstatic --noinput \
    && rm -rf /code/static_build \
    && rm -rf /code/static_src
RUN sed -i 's/static_build/static/g' static/webpack-stats.json
CMD ["gunicorn"]
