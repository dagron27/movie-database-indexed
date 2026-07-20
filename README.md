# Movie Database & Index Performance Demo

![CI](https://github.com/dagron27/movie-database-indexed/actions/workflows/ci.yml/badge.svg)

**Course:** `CSCI 411, Database Theory and Design, Fall 2025`

**Assignment:** `CSCI411-Project`

An iterative group project; this author's primary contribution was
the backend/database layer (schema, queries, and the indexing/generation
work described below). No commit history is preserved in this archive, so
the individual contribution breakdown across the team isn't visible here.

This repository holds two related but independent pieces of
coursework and is presented here as-is. It is early, student learning code:
functional for its original demo purposes, but not production-hardened, and
it has known gaps documented below.

## Assignment Intent

This was a two-part individual/group project built around the same movie
database. Every graded requirement below was checked directly against the
actual files, not assumed from the rubric text alone.

**Part 1 — ER model, schema, data, queries, indexing:**

- **ER model / table creation.** `query-toolkit/schema.sql` defines exactly the
  entities and relationships specified: `Movies`, `Genres`, `Directors`,
  `Actors`, plus the `MovieGenres` and `MovieActors` junction tables
  resolving the two many-to-many relationships, and a `DirectorID` foreign
  key on `Movies` for the one-to-many Directors/Movies relationship.
- **Data population.** `query-toolkit/populate_db.py` seeds the database with
  hardcoded real movie/genre/director/actor data (24 movies, comfortably
  over the assignment's 10-movie minimum) plus populated `MovieGenres` and
  `MovieActors` junction rows.
- **SQL queries (a-g).** All seven are present in `query-toolkit/queries/`, named
  closely enough to the rubric wording that the mapping is unambiguous:
  `retrieve_movie_titles.sql` (a), `movies_after_2010.sql` (b),
  `top_5_highest_rated_movies.sql` (c),
  `directors_with_at_least_3_movies.sql` (d),
  `average_rating_per_genre.sql` (e), `actors_in_genre.sql` (f),
  `movies_with_at_least_3_actors.sql` (g).
- **Index creation (5a/5b).** `src/search_movies.py`'s `create_index()` creates
  a single index, `idx_year` on `Movies(ReleaseYear)`. One index rather
  than two separate ones -- but a B-tree index on a single column
  accelerates both an equality lookup (`ReleaseYear = 1985`) and a range
  scan (`ReleaseYear BETWEEN 1900 AND 2024`) on that same column, so this
  one index is a legitimate answer to both 5a and 5b rather than a partial
  one.
- **Advanced queries (6a-6c).** All three are present in
  `query-toolkit/queries/advanced/`: `versatile_actor.sql` (6a, most diverse
  genres per actor), `director_highest_rated.sql` (6b -- this one
  literally does `CREATE VIEW DirectorHighestRatedMovies AS ...`, matching
  the "create a view" wording exactly), and `incomplete_data.sql` (6c,
  movies missing actors/genres).
- **Documentation/PDF report (part 7).** `docs/Report Part 1.pdf` is now
  present in this repository.

**Part 2 — generate movies at scale, benchmark search, add an index:**

- **Random genre/director/actor/movie generation.** `src/random_data.py`
  defines `generate_genre()` -- matching the assignment's example function
  almost exactly, including the name -- plus `generate_person()` (used for
  both directors and actors) and `generate_movie()`. Exposed via
  `src/app.py`'s `/add_genre`, `/add_director`, `/add_actor`, and
  `/add_movies` POST routes for bulk generation from the web UI.
- **Search by year, with timing.** `src/search_movies.py`'s
  `count_movies_by_year()` wraps the query in `time.time()` start/end
  calls and returns both the count and execution time, exposed via
  `src/app.py`'s `/search_by_year` route -- matching the assignment's expected
  "Number of movies found: X / Execution time: Y seconds" output.
- **Search by year range, with timing.** Same pattern:
  `count_movies_by_year_range()` and the `/search_by_year_range` route.
- **Before/after index comparison.** `src/search_movies.py`'s `create_index()`
  / `drop_index()`, exposed via `src/app.py`'s `/add_index` and `/drop_index`
  routes, so both search functions above can be timed with and without
  `idx_year` in place.
- **PDF report, ZIP submission, video demo (part 3 submission items).**
  `docs/Report Part 2.pdf` is now present in this repository; the ZIP
  submission and video demo are not.

One thing worth flagging: this Part 2 (root-level) app runs against its
own separate database (`data/new_movies.db`), independent of Part 1's
`query-toolkit/movies.db` -- see Overview below. `query-toolkit/main.py` additionally has
a pre-existing broken import (calls a `generate_movies` function that
doesn't exist in `src/db_utils.py`) unrelated to any of the above; see Known
Issues.

## Overview

**`query-toolkit/`** — A standalone movie/actor/director/genre schema for SQLite
(`query-toolkit/schema.sql`), a one-time data loader (`query-toolkit/populate_db.py`), and a
runner (`query-toolkit/main.py`) that executes a set of canned SQL queries from
`query-toolkit/queries/` (e.g. `movies_after_2010.sql`,
`top_5_highest_rated_movies.sql`, `directors_with_at_least_3_movies.sql`)
against `query-toolkit/movies.db` and prints the results.

**Project root** — A small Flask web app (`src/app.py`) backed by a second,
separate SQLite database (`data/new_movies.db`) with the same general shape. The
single page (`src/templates/index.html`) lets a user add random genres,
directors, actors, and movies (generated by `src/random_data.py` /
`src/db_utils.py`), then benchmark `COUNT(*)` queries filtered by release year
before and after creating an index on `Movies.ReleaseYear`
(`src/search_movies.py`, index management routes `/add_index` and
`/drop_index`).

The two halves do not share a database file or process — query-toolkit is a
query-demo script, the root app is the indexing-benchmark demo.

## Repository Organization

The original submission had the Part 2 Flask app's files (`app.py`,
`db_utils.py`, `random_data.py`, `search_movies.py`, `templates/`,
`static/`, `new_movies.db`) at the repository root, and the Part 1
folder was named `Part1/` rather than `query-toolkit/`. Both have been
reorganized for portfolio-wide consistency with sibling repositories:
the Part 2 app moved into `src/` (with `new_movies.db` renamed into
`data/`), and `Part1/` was renamed to `query-toolkit/` since `src/` was
already claimed by the other app and the old name only described a
submission milestone, not what the code does. `docs/Report Part 1.pdf`
and `docs/Report Part 2.pdf` were likewise moved into `docs/` from the
repository root. `.github/workflows/ci.yml` and this README were
updated to match throughout.

## Dependencies

A `requirements.txt` is now included (`pip install -r requirements.txt`).
Based on the imports actually used in the code:

- **Flask** — `src/app.py` (`from flask import Flask, request, render_template`).
  Not part of the Python standard library; must be installed separately
  (e.g. `pip install flask`).
- **Python standard library only** elsewhere: `sqlite3`, `random`, `os`,
  `time`, `datetime`.

No specific Python or Flask version is pinned anywhere in the repo.

## Environment Setup

These are the steps implied by the code as it exists today; there is no
setup script.

1. Install Python 3 and Flask (`pip install flask`).
2. **`query-toolkit/` query demo**: from `query-toolkit/`, ensure `movies.db` exists with the
   schema from `schema.sql` and run `python populate_db.py` to seed it, then
   `python main.py` to run the canned queries. Note: as written, `main.py`
   will fail before reaching the queries — see "Dead Code" below.
3. **Root Flask app**: from the repository root, run `python src/app.py`. This
   starts the Flask development server with debug mode disabled (see
   Security Findings — previously ran with the interactive debugger
   enabled). `data/new_movies.db` must already contain the expected tables
   (Genres, Directors, Actors, Movies, MovieGenres, MovieActors) for the
   app's routes to work — there is no schema-creation step invoked by
   `src/app.py` itself. The committed `data/new_movies.db` ships with
   exactly that schema (zero rows; use the "Add Random..." buttons to
   populate it), so a fresh clone works out of the box — see Known Issues
   for how this was confirmed.

## Known Issues

### Dead Code

- **`query-toolkit/main.py:3, 30`** — imports and calls `generate_movies` from
  `db_utils`: `from db_utils import generate_movies` and
  `generate_movies(cursor, num_movies)`. No `generate_movies` function
  exists in `src/db_utils.py` (its actual exports are `get_table_length`,
  `add_genre`, `add_director`, `add_actor`, `add_movie`, `add_movie_genre`,
  `add_movie_actor`). Running `query-toolkit/main.py` raises an `ImportError`
  immediately, before any of the canned queries execute.
  - *Fix-it plan (future work)*: either implement a `generate_movies`
    helper (bulk-insert version of `add_movie`) in `src/db_utils.py`, or remove
    the generation step from `query-toolkit/main.py` and let `populate_db.py` be
    the sole seeding path.

- **`src/random_data.py:170`** — a commented-out line,
  `#description = random.choice(genre_descriptions[genre_id])`, immediately
  followed by equivalent live code at lines 171-172
  (`option = random.randint(0, 2)` /
  `description = genre_descriptions[genre_id][option]`). The comment is a
  leftover from a refactor and serves no purpose.
  - *Fix-it plan (future work)*: delete the stale comment line.

- **`query-toolkit/populate_db.py:23`** — a leftover self-reminder comment,
  `# Add a comma here`, trailing the "Se7en" tuple in the `movies` list.
  The comma is already present; the comment no longer describes anything
  actionable.
  - *Fix-it plan (future work)*: delete the comment.

- **No route or page to list/view movies** — despite the "Movie Database"
  framing in `src/templates/index.html` (`<title>Movie Database</title>` at
  line 4, `<h1>Welcome to the Movie Database</h1>` at line 7), the app only
  exposes forms to add genres/directors/actors/movies and to search by
  year or year range. There is no `GET` route or template section that
  displays existing movie records.
  - *Fix-it plan (future work)*: add a `/movies` route that queries and
    renders the current contents of the `Movies` table, and link it from
    the index page.

- **`data/new_movies.db` tracking status -- resolved.** Earlier re-checking
  found `git ls-files` no longer showed this file tracked on `main`, despite
  an earlier claim that it was. Root cause found: a schema-only (all tables
  present, zero rows) version of the file existed on a different branch
  (`origin/branch1`) but had never been merged/brought into `main`. Since
  `src/app.py` has no schema-creation or init-on-missing step -- every
  route except `/` assumes the `Genres`, `Directors`, `Actors`, `Movies`,
  `MovieGenres`, and `MovieActors` tables already exist -- `main` was
  missing something it actually needs to function past the root route.
  Brought the schema-only database in from `branch1` and committed it
  directly (dropped from `.gitignore`, which previously listed it) rather
  than adding a schema-creation code path: it's premade infrastructure the
  app depends on, not something generated by this repository's own code,
  so tracking it directly is the more accurate fit. The file is seeded
  with schema only, zero rows -- populating it is what the "Add Random
  Genre/Director/Actor/Movie" buttons are for.

### Security Findings

- **`docs/Report Part 1.pdf` and `docs/Report Part 2.pdf` — PII
  exposure (Informational) -- Fixed**: both PDFs contained a PII
  exposure, found and remediated.
  - *Fixed*: true-redacted via PyMuPDF (search + black-fill annotation +
    apply-redactions), verified via re-extracted text showing zero
    remaining hits and an intact page count.

- **`src/app.py:204` — Flask debug mode enabled in the entrypoint (High)**:
  previously `app.run(debug=True)`. Debug mode turns on the Werkzeug
  interactive debugger, which allows arbitrary Python code execution from
  the browser for any request that raises an unhandled exception, and it
  prints full stack traces (including source code and local variables) to
  the client. If this app is ever reachable from an untrusted network, this
  is a remote code execution risk, not just an information leak.
  - *Fixed*: changed to `app.run(debug=False)`. There is no environment
    variable toggle; if local interactive debugging is needed again during
    development, re-enable it manually and revert before sharing/deploying.

- **`src/app.py` — unguarded `int()` conversions ahead of the `try` block
  (High)**: in `search_by_year`, `year = int(request.form['year'])`
  previously ran before the `try:`; in `search_by_year_range`,
  `start_year = int(...)` and `end_year = int(...)` previously ran before
  their `try:`. A non-numeric form value raised `ValueError` outside the
  surrounding `except Exception` handler, producing an unhandled exception
  (and, combined with debug mode, would have handed an attacker the
  interactive debugger simply by submitting a malformed year value).
  - *Fixed*: both `int()` conversions now happen inside the `try` block in
    `search_by_year` and `search_by_year_range` (`src/app.py`), with a
    dedicated `except ValueError` branch that returns a clean, user-facing
    error message ("Please enter a valid whole number for the year." /
    "...for the start and end years.") instead of raising unhandled.

- **`src/app.py` — no upper bound on `num_movies` (Medium, denial of
  service)**: `number_of_movies = int(request.form['num_movies'])` was used
  directly to drive `for _ in range(number_of_movies):`, with no maximum. A
  large submitted value could drive an unbounded insert loop against
  SQLite, with no authentication or CSRF protection on the route, so any
  client that could reach `/add_movies` could trigger a
  resource-exhausting insert loop.
  - *Fixed*: `add_movie_route` in `src/app.py` now clamps `number_of_movies` to
    a maximum of 1000 per request (values above that are silently capped;
    negative values are rejected with an error message), mirroring the
    existing 25-director / 50-actor caps elsewhere in the file. No request
    throttling or auth was added — the app is still intended for local,
    single-user use only.

- **`src/templates/index.html` — Jinja2 autoescaping disabled via `|safe`
  (Low)**: `{{ search_year_message|safe }}` and
  `{{ search_year_range_message|safe }}` rendered server-built strings
  without HTML escaping. These messages were built in `src/app.py` only from a
  query count (int) and an execution time (float) interpolated into an
  f-string, so there was no current injection path, but it was a latent
  XSS sink: if either message were ever built from user-controlled text, it
  would have rendered unescaped in the page.
  - *Fixed*: removed `|safe` from both template expressions in
    `src/templates/index.html`, so the values are auto-escaped regardless of
    future changes to what feeds them. The literal `<br>` line break that
    depended on `|safe` was replaced: `src/app.py` now separates the two lines
    of each message with `\n` instead of `<br>`, and the corresponding
    `<p>` tags in `src/templates/index.html` use `style="white-space:
    pre-line"` to render the line break visually without needing raw HTML.

- **`src/db_utils.py` — table name interpolated into an f-string SQL query
  (Informational)**: `get_table_length` builds its query as
  `cursor.execute(f"SELECT COUNT(*) FROM {table_name}")`. This is a
  classic SQL injection shape (unparameterized identifier interpolation).
  It is currently only ever called with hardcoded literals (`"Genres"`,
  `"Directors"`, `"Actors"`) from within `src/app.py`, so it was not reachable
  by user input, but the helper itself provided no protection against
  future misuse if a caller ever passed a table name derived from a
  request.
  - *Fixed*: `get_table_length` in `src/db_utils.py` now validates
    `table_name` against a fixed `ALLOWED_TABLES` whitelist (`Genres`,
    `Directors`, `Actors`, `Movies`, `MovieGenres`, `MovieActors`) and
    raises `ValueError` before interpolating anything outside that set,
    since SQLite does not support parameterized identifiers the way it
    does values.

## Status

This is coursework, not a maintained project. All items under "Security
Findings" above have been remediated (debug mode disabled, unguarded
`int()` conversions moved inside their `try` blocks with clean error
messages, an upper bound added to bulk movie generation, `|safe` removed
from the two templated messages, and the `src/db_utils.py` table-name
interpolation whitelisted). The "Dead Code" items remain open by design —
they are not security-relevant and were left as documented, including the
`data/new_movies.db` tracked-file question, which turned out to require an
actual code change (schema-creation logic) rather than a simple file
removal; see that entry for details. Treat both halves of the repo as
demonstration code: useful for illustrating SQL query patterns and
indexed-vs-unindexed query performance.
