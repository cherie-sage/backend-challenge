# Backend Challenge

This is an empty Django project. There is no app code in it yet. That is on
purpose — we will give you the task on the day of the interview.

Before the interview, please open the project and check that it runs. You do
**not** need to write any code yet.

---

# Step 1 — Fork this repository

Click the **Fork** button at the top right of this page. That gives you your
own copy under your own GitHub account.

**Work in your fork, not in this one.** You do not have permission to push
here, and your fork is where your work lives.

---

# Step 2 — Choose how you want to work

There are two options. Both are fine. Pick whichever you prefer.

Either way, use **your fork**, not this repository.

---

## Option 1 — GitHub Codespaces (nothing to install)

Go to **your fork**, click the green **Code** button, open the
**Codespaces** tab, and click **Create codespace on main**.

That is the whole setup. It opens VS Code in your browser and prepares
everything for you: the database, the Python packages, and the migrations. The
first start takes a few minutes. After that, go to
[Check that it works](#check-that-it-works).

> **Make sure you are on your own fork before you click.** Starting a codespace
> from *this* repository works, but you will not be able to save your work,
> because you cannot push here. The page should show **your username**.

<details>
<summary>Just want a quick look without forking?</summary>

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/cherie-sage/backend-challenge)

This opens a codespace on our copy. Fine for a look around, but you cannot save
anything from it. Fork first if you are doing the setup properly.

</details>

**Things to know before you choose this option:**

- The editor runs in your browser, so typing can feel a little slower than an
  editor on your own machine.
- GitHub Copilot is already installed. You are welcome to use it.
- You will need to make port 8000 **public** once, the first time you start the
  server. This takes about five seconds — see below.
- **Please delete the codespace after the interview.** It is paid for by your
  own GitHub account. See [Delete your codespace](#delete-your-codespace-option-1-only)
  at the end.

---

## Option 2 — Run it on your own computer

### First, install these three things

1. **Docker Desktop** — install it, then **start it**. It has to be running.
2. **VS Code**
3. The **Dev Containers** extension for VS Code. This is the important one. It
   is made by Microsoft.

**How to install the extension:**

- Press `Ctrl + Shift + P` (Windows/Linux) or `Cmd + Shift + P` (Mac). A search
  box opens at the top of VS Code.
- Type `Extensions: Install Extensions` and press Enter.
- Search for **Dev Containers**.
- Click **Install** on the one published by Microsoft.

Without this extension, the next steps will not work.

### Then follow these steps

**Step 1.** Get the code:

Copy the URL from the green **Code** button on **your fork**, then:

```bash
git clone https://github.com/YOUR-USERNAME/backend-challenge.git
cd backend-challenge
```

Replace `YOUR-USERNAME` with your GitHub username.

**Step 2.** Open that folder in VS Code.

**Step 3.** Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on a Mac). In the
search box that opens, type:

```
Dev Containers: Reopen in Container
```

Press Enter.

*(VS Code sometimes shows a small popup in the corner asking "Reopen in
Container". Clicking that does exactly the same thing.)*

**Step 4.** Wait for it to finish. The first time takes a few minutes. It sets
up the database and installs the packages for you.

Then go to [Check that it works](#check-that-it-works).

---

# Using AI tools

**You can use AI. We do not mind which one.**

Copilot in the editor, ChatGPT or Claude in another browser tab, web search,
documentation — all of it is fine. Use whatever you normally use. You are not
limited to the tools inside the editor.

We only ask one thing: **be ready to explain your own code.** We will ask why
you did something and what happens in edge cases. That part matters more to us
than who or what wrote the first draft.

---

# Check that it works

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
| `migrate` | A list of migrations, each ending in `OK`, or `No migrations to apply` |
| `runserver` | The server starts. Open `/admin/` and a login page loads. |

### Codespaces only: make port 8000 public

When you start the server, Codespaces creates a web link for port 8000. **That
link is private by default, and you will get an error when you open it.** This
is expected. You only need to fix it once.

1. Click the **PORTS** tab. It is next to the **TERMINAL** tab, at the bottom.
2. Find the row for port **8000**.
3. Right-click that row.
4. Choose **Port Visibility**, then **Public**.

Now open the link again. It will work.

If you are running on your own computer (Option 2), ignore this. Use
`http://localhost:8000` as normal.

---

If all three commands work, you are ready. You can stop here.

---

# If something goes wrong

Tell us **before** the interview. Please do not spend hours on it. A broken
setup is our problem, not part of the test.

- **`could not connect to server`** — the database did not start. Wait a few
  seconds and try again. If it keeps happening, contact us.
- **The container will not build** — contact us. Do not try to fix it yourself.

---

# Delete your codespace (Option 1 only)

Skip this if you worked on your own computer.

Codespaces are paid for by **your own** GitHub account, not ours. A free account
has more than enough for this task. But a codespace you leave behind keeps using
your storage.

**Stopping a codespace is not the same as deleting it.** A stopped codespace
still uses storage.

To delete it:

1. Go to [github.com/codespaces](https://github.com/codespaces). This page shows
   all of your codespaces.
2. Click the `...` button next to this one.
3. Click **Delete**.

If you forget, GitHub deletes it for you after 30 days.

---

# About this project (for reference)

You do not need to read this to finish the setup.

**What is in the repository:**

```
config/           Django settings and URLs
manage.py         The Django command tool
requirements.txt  The Python packages
.devcontainer/    The container setup (database, Python)
```

**Database settings.** The container provides these. They all have defaults, so
you do not need to set anything yourself:

| Name | Default |
| --- | --- |
| `POSTGRES_DB` | `challenge` |
| `POSTGRES_USER` | `challenge` |
| `POSTGRES_PASSWORD` | `challenge` |
| `POSTGRES_HOST` | `db` |
| `POSTGRES_PORT` | `5432` |
| `DJANGO_SECRET_KEY` | a test value |

**Login is already built.** The project uses Django REST Framework with token
login, so you won't need to build sign-up or login during the task.

**Framework.** DRF is what's pre-wired, but you're not locked into it. Prefer
something else — Django Ninja, plain Django views returning JSON, whatever
you're comfortable with? That's fine. Just know that swapping frameworks means
you're also responsible for wiring up the token auth yourself, since the
pre-built login is a DRF piece.

**Django version.** `requirements.txt` pins a version so the setup works out
of the box. Feel free to use a different version of Django or DRF if you
prefer — just update `requirements.txt` and re-run the install step for
whichever setup option you picked.
