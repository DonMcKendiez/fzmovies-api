"""Vercel serverless entrypoint for the FZMovies API package."""

import json


def app(environ, start_response):
    """Minimal WSGI app so Vercel can deploy the package.

    The package CLI remains available from main.py; this endpoint exposes a
    lightweight health response for the Vercel deployment.
    """
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
