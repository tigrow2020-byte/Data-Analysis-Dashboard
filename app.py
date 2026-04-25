from flask import Flask, render_template
from analysis import get_stats, create_graph

app = Flask(__name__)

@app.route("/")
def home():
    stats = get_stats()
    create_graph()
    html = "<h1>📊 Data Analysis Dashboard</h1>"
    html += f"<p>Total Students: {stats['total']}</p>"
    html += f"<p>Average Marks: {stats['average']}</p>"
    html += f"<p>Highest Marks: {stats['highest']}</p>"
    html += f"<p>Lowest Marks: {stats['lowest']}</p>"
    html += f"<p>Top Student: {stats['top_student']}</p>"
    html += "<br><img src='/static/graph.png'>"
    return html

if __name__ == "__main__":
    app.run(debug=True)
