try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="nurfaridah12345")

    curs = conn.cursor()

    namaLama = "ana"

    namaBaru = "anaasy"
    umurBaru = 22
    query = f"update siswa set nama='{namaBaru}', umur={umurBaru} where nama='{namaLama}'"
    curs.execute(query)
    conn.commit()
    print("data berhasil diupdate")
except Exception as e:
    print(e)