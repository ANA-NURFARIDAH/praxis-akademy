from flask import Flask, render_template, request, redirect
import psycopg2
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="data_santri_putri_programmer_ppqs",
        user="postgres",
        password="nurfaridah12345"
    )

    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        asal_kabupaten = request.form.get("asal_kabupaten")
        blok_kamar = request.form.get("blok_kamar")
        keterangan = request.form.get("keterangan")
        query = f"insert into projectku(nama, asal_kabupaten, blok_kamar, keterangan) values ('{nama}', '{asal_kabupaten}', '{blok_kamar}', '{keterangan}'"
        curs.execute(query)
        conn.commit()        
        
    print(request.method)
    query = f"select * from projectku"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("index.html", context=data)

    
# @app.route("/detail/<data_santri_putri_programmer_ppqs_id>")
# def detail(data_santri_putri_programmer_ppqs_id):
#     conn = psycopg2.connect(
#         host="localhost",
#         database="data_santri_putri_programmer_ppqs",
#         user="postgres",
#         password="nurfaridah12345"
#     )
#     curs = conn.cursor()
#     query = f"select * from projectku where id = {data_santri_putri_programmer_ppqs_id}"
#     curs.execute(query)
#     data = curs.fetchone()
#     conn.commit()        
#     curs.close()
#     conn.close()
#     print (data)
#     return render_template("detail.html", context=data)

# @app.route("/delete/<data_santri_putri_programmer_ppqs_id>")
# def delete(data_santri_putri_programmer_ppqs_id):
#     conn = psycopg2.connect(
#         host="localhost",
#         database="data_santri_putri_programmer_ppqs",
#         user="postgres",
#         password="nurfaridah12345"
#     )
#     curs = conn.cursor()
#     query = f"delete from projectku where id = {data_santri_putri_programmer_ppqs_id}"
#     curs.execute(query)
#     conn.commit()        
#     curs.close()
#     conn.close()
#     return redirect ("/")

# @app.route("/update/<data_santri_putri_programmer_ppqs_id>" ,methods=["GET", "POST"])
# def update(data_santri_putri_programmer_ppqs,_id):
#     conn = psycopg2.connect(
#         host="localhost",
#         database="data_santri_putri_programmer_ppqs",
#         user="postgres",
#         password="nurfaridah12345"
#     )
#     curs = conn.cursor()
#     if request.method == "POST":
#         nama = request.form.get("nama")
#         detail = request.form.get("detail")
#         query = f"update projectku set nama='{nama}', asal_kabupaten='{detail}', blok_kamar='{detail}', keterangan='{detail}' where nama ='{nama}'"
 

#         curs.execute(query)
#         conn.commit()
#         return redirect("/")

#     query = f"select * from projectku where id = {data_santri_putri_programmer_ppqs,_id}"
#     curs.execute(query)
#     data = curs.fetchone()
#     conn.close()
#     conn.close()
#     return render_template("update.html", context=data)

if __name__ == "__main__":
    app.run()