from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)





































# MODELS #
class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	body = db.Column(db.Text)
	date = db.Column(db.DateTime)
	image = db.Column(db.Text)

	def __init__(self, name, body, image="image_not_found.jpg", date=None):
		self.name = name
		self.body = body
		if date == None:
			date = datetime.utcnow()
		self.date = date
		self.image = image

	def __repr__(self):
		return "<product %s>" % self.name

class Npc(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	background = db.Column(db.Text)
	location = db.Column(db.String(80))
	quests = db.Column(db.String(80))

	def __init__(self, name, background, location, quests):
		self.name = name
		self.background = background
		self.location = location
		self.quests = quests


	def __repr__(self):
		return "<npc {}>".format(self.name)

















































# VIEWS #
@app.errorhandler(404)
def page_not_found(e):
	return render_template("page_not_found.html")

@app.route("/")
def index():
	print(url_for('static', filename="fnatic_icon.png"))
	top_sellers = Product.query.all()[:3]
	return render_template("main.html", top_sellers=top_sellers)

@app.route("/admin", methods=["GET", "POST"])
def admin():
	if request.method == "POST":
		if request.form["submit"] == "npc-create":
			db.session.add(Npc(request.form["npc-name"], request.form["npc-background"], request.form["npc-location"], request.form["npc-quests"]))
			db.session.commit()
		elif request.form["submit"] == "delete":
			lista = []
			for item in request.form:
				try:
					lista.append(int(item[0]))
				except ValueError:
					continue
			for item in lista:
				del_prod = Npc.query.get(item)
				db.session.delete(del_prod)
			db.session.commit()


	npcs = Npc.query.all()
	return render_template("admin_panel.html", npcs=npcs)

@app.route("/product/<id>")
def product_detail(id):
	product = get_product(id)
	print(product)
	if product == None:
		abort(404)
	return render_template("product_detail.html", product=product)

@app.route("/classes")
def classes():
	return render_template("classes.html")

@app.route("/bestiary")
def bestiary():
	return render_template("bestiary.html")

@app.route("/npc")
def npc():
	npcs = Npc.query.all()
	return render_template("npc.html", npcs=npcs)

@app.route("/npc/<id>")
def npc_detail(id):
	npc = get_npc(id)
	if npc == None:
		abort(404)
	return render_template("npc_detail.html", npc=npc)

@app.route("/test")
def test():
	return render_template("test.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/projectdetail")
def project_detail():
	return render_template("project_details.html")

@app.route("/about/<project>")
def project(project):
	return render_template("project_details_{}.html".format(project))
















































# HELPER FUNCTIONS #

def get_product(id):
	return Product.query.get(id)

def get_npc(id):
	return Npc.query.get(id)





if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)