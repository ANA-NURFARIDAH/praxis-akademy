try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="nurfaridah12345")

    curs = conn.cursor()

    nama = "anaasy"
    query = f"delete from siswa where nama='{nama}'"

    curs.execute(query)
    conn.commit()
    print("data berhasil dihapus")
except Exception as e:
    print(e)