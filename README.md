Testing patch: https://github.com/django/django/pull/17594

# Init

Clone Django

```
python -m venv venv
. ./venv/bin/activate
python -m pip install -r requirements.txt

# 1. Supporting Services
docker-compose up --build database pg_exporter prometheus grafana
# 2. Migrate
python server.py
# 3. Web Server
python -m uvicorn server:app --reload
# 4. Load Test
docker-compose up --build load_tests
```

Observe Grafana for postgres connections, P95, etc.:

http://localhost:3000/d/a1b733df-f5fc-46e7-b2cd-6030dcd483b6/webservice?orgId=1&refresh=5s

Run tests with stable/5.0.x branch
Run tests with patch branch

## Tests

Concurrent POST requests that CREATE records in the database

Use Psycopg Pool to limit number of connections to Postgres (not a new connection on every request)

Stable
- asgi
    - none
http_req_duration..............: avg=407.48ms min=95.49ms med=393.51ms max=767.85ms p(90)=527.87ms p(95)=569.82ms


Branch
- asgi
    - Pool: none
http_req_duration..............: avg=412.62ms min=94.88ms med=410.37ms max=834.19ms p(90)=504.37ms p(95)=535.28ms
    - Pool: min 2, max 5
http_req_duration..............: avg=111.22ms min=68.62ms med=105.86ms max=247.24ms p(90)=138.51ms p(95)=142.86ms
