FROM python:3.11 as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN pip install poetry


FROM base AS python-deps

# Install python dependencies in /.venv
COPY pyproject.toml poetry.lock /
RUN POETRY_VIRTUALENVS_IN_PROJECT=1 POETRY_VIRTUALENVS_OPTIONS_ALWAYS_COPY=1 poetry install --without dev --no-root


FROM python-deps AS runtime

WORKDIR /code
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"
RUN chown -R www-data:www-data /code
USER www-data

# Install application into container
COPY . /code/
