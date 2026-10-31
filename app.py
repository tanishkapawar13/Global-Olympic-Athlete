import os
from flask import Flask, render_template

app = Flask(__name__)

# Published Tableau Public dashboard
DEFAULT_DASHBOARD_URL = (
    "https://public.tableau.com/views/GlobalOlympicsAthlete1/Dashboard1"
    "?:showVizHome=no&:embed=yes&:tabs=yes&:toolbar=yes"
)

# Published Tableau Public story supplied by the project owner
DEFAULT_STORY_URL = (
    "https://public.tableau.com/views/GlobalOlympicsAthlete1/Story1"
    "?:showVizHome=no&:embed=yes&:tabs=yes&:toolbar=yes"
)


def clean_tableau_url(url: str) -> str:
    """Return a Tableau URL without surrounding whitespace."""
    return (url or "").strip()


@app.route("/")
def index():
    dashboard_url = clean_tableau_url(
        os.environ.get("TABLEAU_DASHBOARD_URL", DEFAULT_DASHBOARD_URL)
    )
    story_url = clean_tableau_url(
        os.environ.get("TABLEAU_STORY_URL", DEFAULT_STORY_URL)
    )

    return render_template(
        "index.html",
        dashboard_url=dashboard_url,
        story_url=story_url,
    )


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    # Uses port 5000 by default; override locally with PORT=5001 python3 app.py.
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
