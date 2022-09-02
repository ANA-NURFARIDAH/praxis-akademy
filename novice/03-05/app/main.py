from flask import Flask, render_template, request
import psycopg2
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index(): 
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="nurfaridah12345"
        )
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        detail = request.form.get("detail")
        query = f"insert into buah(nama, detail) values('{nama}', '{detail}')"
        curs.execute(query)
        conn.commit()
        curs.close()
        conn.close()
    
    #     print(20*"=")
    #     print(nama)
    #     print(detail)
    #     print(20*"=")

    print(request.method)
    query = f"select * from buah"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    # data = ["apel", "pear", "anggur"]
    return render_template("index.html", contex=data)

if __name__ == "__main__":
    app.run()