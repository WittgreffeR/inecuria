#!/bin/bash
npm run build
python manage.py collectstatic --noinput
sed -i 's/static_build/static/g' static/webpack-stats.json