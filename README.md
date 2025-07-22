# NPM Dashboard

A simple Flask-based dashboard that reads from your Nginx Proxy Manager (NPM) SQLite database and shows active proxy domains in a web UI.

## 🚀 Features

- Reads NPM’s live database (read-only) — no export/import required
- Supports optional JSON config to label or hide entries
- Runs inside Docker with minimal setup

## ❗️ Dependencies
- Nginx Proxy Manager

## 📁 Project Structure

.
├── app/                 # Python app source
│   ├── main.py          # Flask app entry point
│   ├── templates/       # Jinja2 HTML templates
│   └── requirements.txt # Python dependencies
├── tmp/                 # Template Files (Example sites.json)
│   └── sites.json       # Example json config file
├── Dockerfile
├── docker-compose.yml
├── TODO.md
└── README.md

## ⚙️ Setup

Make sure your Nginx Proxy Manager data is accessible to the container.

Either:
- Mount your NPM data directory (where `database.sqlite` lives) into `/data` inside the container
- Or update `docker-compose.yml` to point to wherever you store your NPM AppData folder

By default, this setup expects:
- NPM data at `/DATA/AppData/nginxproxymanager/data/` (this is a read-only mount)
- Config (e.g., `sites.json`) at `/DATA/AppData/npm_dash/` or wherever you keep your AppData

Make sure those paths exist and contain the expected files before launching the container.

### Example Config (`sites.json`)

[
  { "url": "internal.example.com", "label": "Internal Site", "hide": false },
  { "url": "test.example.com", "hide": true }
]

## 🐳 Running the App

docker compose up -d --build

Then visit:

http://<your-server-ip>:6565

⚠️ Use http:// — not https:// — unless you’ve added a reverse proxy.

## 🛠️ Notes

- The app listens on port `5555` inside the container, mapped to `6565` outside.
- Flask binds to `0.0.0.0` so it’s reachable on your LAN.
- Don’t hit it with https:// unless you're proxying through Nginx Proxy Manager with SSL.

## 📬 Future Ideas (PRs welcome)

- Filter by label/tag
- Search field
- Pagination
- Built-in theme or Tailwind CSS support
- "Active" Configuration (Renaming and Hiding entries in production)