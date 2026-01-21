from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            platform TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def add_game_to_db(title, platform, status):
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO games (title, platform, status) VALUES (?, ?, ?)",
        (title, platform, status)
    )

    conn.commit()
    conn.close()

    print("Saved:", title, platform, status)


def delete_game_from_db(game_id):
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM games WHERE id = ?",
        (game_id,)

    )

    conn.commit()
    conn.close()
    

def get_games():
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, platform, status FROM games ORDER BY id DESC")
    games = cursor.fetchall()

    conn.close()
    return games




@app.route("/")
def home():
    games = get_games()
    return render_template("index.html", games=games)

@app.route("/add", methods=["GET", "POST"])
def add_game():
    title = request.form.get("title")
    platform = request.form.get("platform")
    status = request.form.get("status")
    
    add_game_to_db(title, platform, status)
    return redirect(url_for("home"))


@app.route("/delete/<int:game_id>", methods=["POST"])
def delete_game(game_id):
    delete_game_from_db(game_id)
    return redirect(url_for("home"))

    
if __name__ == "__main__":
    init_db()            
    app.run(debug=True)

    