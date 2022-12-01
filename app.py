from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
# from flask_mysqldb import MySQL


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] ='flask'

# mysql = MySQL(app)

# with app.app_context():
#     cur = mysql.connection.cursor()
#     cur.execute("select * from student");
#     data  = cur.fetchall()
#     print(data)
# cur = mysql.connection.cursor()


# print(name)
# installed mysql connection
# conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='crud',port='3000')
# xamp mysql
conn = mysql.connector.connect(
    user='root', password='', host='127.0.0.1', database='flask')
cur = conn.cursor()
app = Flask(__name__)
app.secret_key = 'secret key'


@app.route('/')
def home():

    cur = conn.cursor()
    cur.execute("SELECT * from student")
    data = cur.fetchall()

    # cur.close()
    # print(data)
    # return data;
    return render_template('index.html', students=data)


@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == "POST" or "GET":

        name = request.form['name']
        age = request.form['age']
        location = request.form['location']
        cur = conn.cursor()
        cur.execute(
            'insert into student(name,age,location) values(%s,%s,%s)', (name, age, location))
        conn.commit()
        # cur.commit();
    cur.close()
    flash("data inserted successfully")
    return redirect(url_for('home'))


@app.route('/edit/<string:id>', methods=['GET'])
def edit(id):
    cur = conn.cursor()
    cur.execute("SELECT * from student where id=%s", (id,))
    data = cur.fetchone()

    # cur.close()
    print(data)
    # return "hlo";
    return render_template('edit.html', students=data)


@app.route('/add', methods=['GET'])
def add():
    return render_template('add.html')


@app.route('/delete/<string:id>', methods=['GET'])
def delete(id):
    # id = request.body.id;
    cur = conn.cursor()
    cur.execute('delete from student where id = %s', (id,))
    conn.commit()
    cur.close()
    flash("data deleted successfully")
    return redirect(url_for('home'))


@app.route('/update/<string:id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        print("hi")
        name = request.form['name']
        age = request.form['age']
        location = request.form['location']
        cur = conn.cursor()
        cur.execute("update student set name=%s,age=%s,location=%s  where id = %s",
                    (name, age, location, id))
        conn.commit()
        cur.close()
        flash("data updated successfully")
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
