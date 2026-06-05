import json

from fzmovies_api.console import main


def app(environ, start_response):
    """Minimal WSGI app so Vercel can deploy this package."""
    payload = {
        "ok": True,
        "service": "fzmovies-api",
        "message": "FZMovies API package is deployed on Vercel.",
    }
    body = json.dumps(payload).encode("utf-8")
    headers = [
        ("Content-Type", "application/json; charset=utf-8"),
        ("Content-Length", str(len(body))),
    ]
    start_response("200 OK", headers)
    return [body]


if __name__ == "__main__":
    main()
