from flask import Flask, render_template
import sqlite3
import ast
import json
import os

app = Flask(__name__)

DB_PATH = "/data/database.sqlite"
CONFIG_PATH = "/config/sites.json"
TITLE = "List of Porxies"

def get_data():
    urls = []
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT domain_names FROM proxy_host WHERE enabled = 1;")
        rows = cursor.fetchall()
        conn.close()
    except Exception as e:
        print(f"Error querying DB: {e}")
        # Exit out on that matter
        return []

    for row in rows:
        raw = row[0]
        try:
            parsed = ast.literal_eval(raw)
            print(parsed[0])
            if isinstance(parsed, list) and parsed:
                urls.append(parsed[0])
            elif isinstance(parsed, str):
                urls.append(parsed)
        except Exception:
            urls.append(raw)

    return urls

def load_site_meta():
    try:
        with open(CONFIG_PATH, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        return[]

@app.route('/')
def index():
    urls = get_data()
    site_meta = load_site_meta()
    url_meta = {site["url"]: site for site in site_meta}

    url_directory = []
    for url in urls:
        entry = url_meta.get(url)
        if entry and entry.get("hide") is True:
            continue
        label = entry.get("label") if entry else url
        url_directory.append((url, label))

    return render_template("index.html", TITLE=TITLE, url_directory=url_directory)


def main():
    app.run(host="0.0.0.0", port=5555)

if __name__ == '__main__':
    main()
    
