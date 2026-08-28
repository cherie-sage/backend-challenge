# Backend Challenge

This is an empty Django project. There is no app code in it yet. That is on
purpose.

Before the interview, please set it up and check that it runs. You do **not**
need to write any code yet. We will give you the task on the day.

Please work in your own copy. You do not need to push anything back here.

---

## Step 1 — Get the code

Pick one. Both are fine.

**Option A — GitHub Codespaces (runs in your browser)**

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/cherie-sage/backend-challenge)

**Option B — Clone it and run it on your computer**

```bash
git clone https://github.com/cherie-sage/backend-challenge.git
cd backend-challenge
```

For Option B you need Docker Desktop installed.

## Step 2 — Add the container files

We sent you a folder called `.devcontainer` in a separate message.

Copy that folder into the top level of the project. When you are done, the
files should be here:

```
.devcontainer/devcontainer.json
.devcontainer/docker-compose.yml
```

**Do this before you start the container.** The project needs a Postgres
database, and these files are what set it up.

If you skipped this step and made a codespace already, that is fine. Add the
folder now, then open the command palette and run
**Dev Containers: Rebuild Container**.

## Step 3 — Start the container

**If you used Option A (Codespaces):** open the command palette
(`Ctrl/Cmd + Shift + P`) and run **Codespaces: Rebuild Container**.

**If you used Option B (your own computer):** open the folder in VS Code. It
will ask *"Reopen in Container"* — click it. If it does not ask, open the
command palette and run **Dev Containers: Reopen in Container**.

Either way, wait for it to finish. The first time takes a few minutes. It
installs the Python packages for you.

## Step 4 — Check that it works

Run these three commands, one at a time:

```bash
python manage.py check
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

This is what you should see:

| Command | What you should see |
| --- | --- |
| `check` | `System check identified no issues` |
| `migrate` | A list of migrations, each ending in `OK` |
| `runserver` | The server starts. Open `/admin/` and a login page loads. |

If all three work, you are ready. You can stop here.

## Step 5 — If something goes wrong

Tell us before the interview. Do not spend hours on it. A broken setup is our
problem, not part of the test.

Two common problems:

- **`could not connect to server`** — the database is not running. Check that
  you did Step 2 and that the container was rebuilt after that.
- **The server starts but `migrate` fails** — this usually means the container
  is running without the database. Same fix as above.

---

## After the interview: delete your codespace

Only if you used Option A.

Codespaces are paid for by **your own** GitHub account, not ours. A free account
has more than enough for this task. But a codespace you leave behind keeps using
your storage.

**Stopping a codespace is not the same as deleting it.** A stopped codespace
still uses storage.

To delete it:

1. Go to [github.com/codespaces](https://github.com/codespaces). This shows all
   your codespaces.
2. Click the `...` button next to this one.
3. Click **Delete**.

If you forget, GitHub deletes it for you after 30 days.

---

## About this project (for reference)

You do not need to read this to finish the setup.

**What is in the repo:**

```
config/           Django settings and URLs
manage.py         The Django command tool
requirements.txt  The Python packages
```

**Settings the container provides.** The project reads these from the
environment. They all have defaults, so you do not need to set them yourself:

| Name | Default |
| --- | --- |
| `POSTGRES_DB` | `challenge` |
| `POSTGRES_USER` | `challenge` |
| `POSTGRES_PASSWORD` | `challenge` |
| `POSTGRES_HOST` | `db` |
| `POSTGRES_PORT` | `5432` |
| `DJANGO_SECRET_KEY` | a test value |

**Login is already built.** The project uses Django REST Framework with token
login. You will not need to build sign-up or login during the task.
