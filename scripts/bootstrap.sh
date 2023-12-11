#!/bin/bash
#!/bin/bash
set -e

test -f .env.development || cp .env.example .env.development
test -f .env.test || cp .env.example .env.test

pipenv install --dev

! command -v pre-commit > /dev/null 2>&1 || pre-commit install

npm install
