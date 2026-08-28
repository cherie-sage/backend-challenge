# Backend Challenge

A bare Django + Django REST Framework project. There is no application code yet —
that's deliberate.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/cherie-sage/backend-challenge)

Work in a codespace or in a local clone — either is fine. Whichever you pick,
add the container configuration first; see below.

## Before the interview

Please get this project running inside the development container configuration
we've sent you separately. Add it to this repository, bring it up, and confirm
the checks below pass.

Doing this ahead of time means we can spend the session on the actual problem
rather than on environment setup. **You don't need to write any application code
yet** — the exercise itself is handed over at the start of the interview.

Please **clone this repository and work in your local copy** — there's no need
to push anything back to it.

If you get stuck on setup, tell us before the session rather than burning your
own time on it.

> **A note on Codespaces:** you're welcome to work in a codespace, but create it
> only *after* you've added the container configuration. A codespace made from
> this repository as-is falls back to a generic image with no database, and
> `migrate` will fail with a connection error — that's expected, not a broken
> repository.

## What the project expects

The database connection reads entirely from environment variables, which the
container is expected to supply:

| Variable | Default |
| --- | --- |
| `POSTGRES_DB` | `challenge` |
| `POSTGRES_USER` | `challenge` |
| `POSTGRES_PASSWORD` | `challenge` |
| `POSTGRES_HOST` | `db` |
| `POSTGRES_PORT` | `5432` |
| `DJANGO_SECRET_KEY` | a throwaway development value |

Every one has a default, so if your container runs Postgres on a host named `db`
with matching credentials, it will connect with no extra configuration.

Python dependencies are pinned in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Confirming it works

```bash
python manage.py check
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

You should see no issues from `check`, migrations applying cleanly against
Postgres, and the admin site responding at `/admin/`.

## What's here

```
config/           Django project settings, URLs, WSGI/ASGI entrypoints
manage.py         Django CLI entrypoint
requirements.txt  Pinned dependencies
```

DRF is installed and configured with token authentication and an
`IsAuthenticated` default permission class, so you won't need to build login or
registration during the exercise.

## If you used a codespace, delete it when we're done

Codespaces are billed to **your own** GitHub account, not ours. A personal
account includes a monthly allowance that comfortably covers an exercise this
size, but a codespace left lying around keeps consuming your storage quota until
it's removed.

**Stopping a codespace is not the same as deleting it** — a stopped codespace
still uses storage. To delete it properly:

1. Go to [github.com/codespaces](https://github.com/codespaces), which lists
   every codespace you own across all repositories.
2. Click the `...` menu next to this one and choose **Delete**.

You can also right-click it under **GitHub Codespaces** in the VS Code Remote
Explorer and choose *Delete Codespace*.

If you forget, GitHub deletes inactive codespaces automatically after 30 days by
default. You can shorten that at
[github.com/settings/codespaces](https://github.com/settings/codespaces).
