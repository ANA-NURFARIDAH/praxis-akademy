from app.controllers import buah
from app import app

app.route("/",                  methods=["GET", "POST"])    (buah.index)
app.route("/delete/<buah_id>",  methods=["GET"])            (buah.delete)
app.route("/update/<buah_id>",  methods=["GET", "POST"])    (buah.update)
app.route("/detail/<buah_id>",  methods=["GET"])            (buah.detail)