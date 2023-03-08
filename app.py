# print("Hello, repil")
from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Benglaru, India',
  'salary': 'Rs. 10,000,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Pune, India',
  'salary': 'Rs. 13,000,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Delhi, India',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Franciso, USA',
  'salary': '$120,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovain')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if (__name__ == '__main__'):
  app.run(host='0.0.0.0', debug=True)
