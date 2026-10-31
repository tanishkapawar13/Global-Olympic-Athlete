# Olympic Tableau Portal (Flask + Render)

## Files
•⁠  ⁠⁠ app.py ⁠: Flask server.
•⁠  ⁠⁠ templates/index.html ⁠: dashboard/story page with two navigation tabs.
•⁠  ⁠⁠ requirements.txt ⁠: Python dependencies.
•⁠  ⁠⁠ Procfile ⁠: production start command.
•⁠  ⁠⁠ render.yaml ⁠: optional Render Blueprint configuration.

## Run locally
⁠ bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
python app.py
 ⁠
Open https://global-olympic-athlete.onrender.com/

## Deploy on Render
1.⁠ ⁠Upload these files to a GitHub repository.
2.⁠ ⁠In Render, choose New > Web Service and connect the repository.
3.⁠ ⁠Build command: ⁠ pip install -r requirements.txt ⁠
4.⁠ ⁠Start command: ⁠ gunicorn app:app ⁠
5.⁠ ⁠Deploy.

## Configure the Tableau Story
The dashboard URL was supplied. The exact Story URL is not yet known, so the Story tab shows instructions until you configure it.
In Render: open your service > Environment > Add Environment Variable:
•⁠  ⁠Key: ⁠ TABLEAU_STORY_URL ⁠
•⁠  ⁠Value: the published Tableau Story URL (get it from Tableau Public using Share > Copy Link)
Save changes and redeploy if prompted.

Optional environment variable:
•⁠  ⁠⁠ TABLEAU_DASHBOARD_URL ⁠: overrides the dashboard URL.

Note: Tableau Public views are public. Only publish data you are comfortable making publicly accessible.
