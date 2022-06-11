from flask import Flask, render_template, request, session, flash, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import os
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__) #webserver
Bootstrap(app) #css framework

'''
Define Configuration for the MySQL pipeline
'''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pusbangdisini26'
app.config['MYSQL_DB'] = 'uas_basdat'
# data get dict
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

# make connection
mysql = MySQL(app)
# handling cookies transfering
app.config['SECRET_KEY'] = os.urandom(24)


# ------------------------------------------------------------------------
'''
Backend Setting of the CRUD App
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email =='admin@gmail.com' and password == 'pass':
            session['email']=email
            return redirect(url_for('succes'))

        else:
            flash('Username atau Password Salah!!', 'danger')
    return render_template('index.html')

@app.route('/succes', methods=['GET', 'POST'])
def succes():
    if 'email' in session:
        return render_template('succes.html')
    else:
        return redirect(url_for('index'))

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if "email" in session:
        if request.method == 'POST':
            try:
                form = request.form
                Logistic_id = form['Logistic_id']
                Tanggal_Pengiriman = form['Tanggal_Pengiriman']
                Jenis_Pengiriman = form['Jenis_Pengiriman']
                Status = form['Status']
                Jalur_Pengiriman = form['Jalur_Pengiriman']
                Jenis_Barang = form['Jenis_Barang']
                Asal_Pengiriman = form['Asal_Pengiriman']
                Tujuan_Pengiriman = form['Tujuan_Pengiriman']

                cur = mysql.connection.cursor()
                sql = "INSERT INTO data_logistik(Logistic_id, Tanggal_Pengiriman, Jenis_Pengiriman, Status, Jalur_Pengiriman, Jenis_Barang, Asal_Pengiriman, Tujuan_Pengiriman) VALUES({},\'{}\',\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(Logistic_id, Tanggal_Pengiriman, Jenis_Pengiriman, Status, Jalur_Pengiriman, Jenis_Barang, Asal_Pengiriman, Tujuan_Pengiriman)
                cur.execute(sql)
                mysql.connection.commit()
                flash('Successfully inserted data', 'success')
            except Exception as e:
                flash(e, 'danger')
        return render_template('insert.html')
    else: 
     return redirect(url_for('index'))

@app.route('/cari', methods=['GET', 'POST'])
def cari():
    
    if "email" in session:
        search = " "
        result = " "
        if request.method == 'POST':
            form = request.form
            search = form['Logistic_id']
            try:
                cur = mysql.connection.cursor()
                sql = "SELECT * FROM data_logistik WHERE Logistic_id = {}".format(search)
                cur.execute(sql)
                result = cur.fetchall()
            except Exception as e:
                flash(e, 'danger')
        
        return render_template('search.html', search=search, result=result)
    else:
        return render_template('index.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        form = request.form
        Logistic_id = form['Logistic_id']
        Tanggal_Pengiriman = form['Tanggal_Pengiriman']
        Jenis_Pengiriman = form['Jenis_Pengiriman']
        Status = form['Status']
        Jalur_Pengiriman = form['Jalur_Pengiriman']
        Jenis_Barang = form['Jenis_Barang']
        Asal_Pengiriman = form['Asal_Pengiriman']
        Tujuan_Pengiriman = form['Tujuan_Pengiriman']

        cur = mysql.connection.cursor()
        sql = "UPDATE data_logistik SET(Logistic_id, Tanggal_Pengiriman, Jenis_Pengiriman, Status, Jalur_Pengiriman, Jenis_Barang, Asal_Pengiriman, Tujuan_Pengiriman) VALUES({},\'{}\',\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(Logistic_id, Tanggal_Pengiriman, Jenis_Pengiriman, Status, Jalur_Pengiriman, Jenis_Barang, Asal_Pengiriman, Tujuan_Pengiriman)
        cur.execute(sql)
        mysql.connection.commit()
        flash('Successfully updated data', 'success')
        return render_template('display.html')
    else:
        flash('Update Gagal', 'danger')


@app.route('/display')
def display():
    if "email" in session:
        cur = mysql.connection.cursor()
        result_value = cur.execute("SELECT * FROM data_logistik")
        if result_value > 0:
         display = cur.fetchall()
        return render_template('display.html', display=display)
    else:
        return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return 'This page was not found'

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True) # also define a port app.run(debug=True, port=50001)