from flask import Flask, render_template, jsonify
app = Flask(__name__)

jobs = [{
    "id": 1,
    "title": "Software Engineer",
    "location": "Hydrabad",
    "salary": "20LPA",
    "mode": "Remote"
},
{
    "id": 2,
    "title": "UI/UX Designer",
    "location": "Pune",
    "mode": "Hybrid (On-site/Remote)"
},
{
    "id": 3,
    "title": "Database Administrator",
    "location": "Delhi",
    "salary": "32LPA",
    "mode": "On-site"
},
{
    "id": 4,
    "title": "DevOps Engineer",
    "location": "Mumbai",
    "salary": "20LPA",
    "mode": "Remote"
},
{
    "id": 5,
    "title": "FrontEnd Developer",
    "location": "Ahemdabad",
    "mode": "Hybrid (On-site/Remote)"
}]


@app.route("/")
def index():
    return render_template("index.html", jobs = jobs)

@app.route("/api/jobs")
def jobsList():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(debug = True)