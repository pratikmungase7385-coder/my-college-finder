from database import initialize_all, get_user_connection, get_college_connection

from flask import Flask, render_template,request, redirect, session, url_for,flash
import sqlite3
import os
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash





app = Flask(__name__)
app.secret_key = 'pratik12'
bcrypt = Bcrypt(app)



initialize_all()


# Dropdown data
maharashtra_universities = [
    "Select",
    "Un-Aided",
    "Autonomous",
    "Government",
    "Deemed University",
    "Savitribai Phule Pune University",
    "University of Mumbai",
    "SNDT Womens University",
    "Dr. Babasaheb Ambedkar Technological University, Lonere",
    "Shivaji University, Kolhapur",
    "Solapur University",
    "Nagpur University",
    "Yeshwantrao Chavan Maharashtra Open University, Nashik",
    "Tilak Maharashtra Vidyapeeth, Pune",
    "SNDT Women's University, Mumbai",
    " Dr. D.Y. Patil University, Pune",
    "Rajiv Gandhi Technical University, Mumbai",
    "Sant Gadge Baba Amravati University",
    "Swami Ramanand Teerth Marathwada University, Nanded"
]

maharashtra_cities = [
    "Select",
    "Ahilyanagar",
    "Akola",
    "Amravati",
    "Chhatrapati Sambhajinagar ",
    "Beed",
    "Bhandara",
    "Buldhana",
    "Chandrapur",
    "Dhule",
    "Gadchiroli",
    "Gondia",
    "Hingoli",
    "Jalgaon",
    "Jalna",
    "Kolhapur",
    "Latur",
    "Mumbai City",
    "Mumbai Suburban",
    "Nagpur",
    "Nanded",
    "Nandurbar",
    "osmanabad",
    "Palghar",
    "Parbhani",
    "Pune",
    "Raigad",
    "Ratnagiri",
    "Sangli",
    "Satara",
    "Sindhudurg",
    "Solapur",
    "Thane",
    "Wardha",
    "Washim",
    "Yavatmal"
]

maharashtra_branches = [
    "Select",
    "Computer Engineering",
    "Computer Science and Engineering",
    "Information Technology",
    "Mechanical Engineering",
    "Civil Engineering",
    "Electrical Engineering",
    "Electronics Engineering",
    "Electronics & Telecommunication",
    "Chemical Engineering",
    "Production Engineering",
    "Instrumentation Engineering",
    "Biomedical Engineering",
    "Aeronautical Engineering",
    "Automobile Engineering",
    "Agricultural Engineering",
    "Mining Engineering",
    "Petroleum Engineering",
    "Environmental Engineering",
    "Textile Engineering",
    "Marine Engineering",
    "Artificial Intelligence and Data Science",
    "Artificial Intelligence and Machine Learning",
    "Robotics and Automation",
    "Cybersecurity",
    "Mechatronics Engineering"
]





# DB_NAME = 'colleges0.db'

# # ------------------------ DB Setup ------------------------
# def init_db():
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()

   
#     cursor.executescript('''
#         CREATE TABLE IF NOT EXISTS colleges (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             university TEXT NOT NULL,
#             city TEXT NOT NULL,
#             branch TEXT NOT NULL,
#             cutoff_cet TEXT,
#             cutoff_jee TEXT
#         )
#     ''')
    

   
    # cursor.execute("DELETE FROM colleges;")
    # cursor.execute("DELETE FROM sqlite_sequence WHERE name='colleges';")

    





#     conn.commit()
#     conn.close()
#     print("Database initialized successfully!")





   

# conn = sqlite3.connect('users1.db')
# cur = conn.cursor()

# cur.executescript('''
# CREATE TABLE IF NOT EXISTS users1 (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT UNIQUE NOT NULL,
#     password TEXT NOT NULL
# )
# ''')

# conn.commit()
# conn.close()
# print("users table ready!")


# # Initialize DB
# init_db()

# # ------------------------ DB Connection ------------------------
# def get_db_connection():
#     conn = sqlite3.connect(DB_NAME)
#     conn.row_factory = sqlite3.Row
#     return conn

# ------------------------ Flask Routes ------------------------

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/filter', methods=['GET', 'POST'])
def filter_page():
    conn = get_college_connection()

    # Distinct dropdown data
    maharashtra_universities = [row['university'] for row in conn.execute("SELECT DISTINCT university FROM colleges")]
    maharashtra_cities = [row['city'] for row in conn.execute("SELECT DISTINCT city FROM colleges")]
    maharashtra_branches = [row['branch'] for row in conn.execute("SELECT DISTINCT branch FROM colleges")]

    colleges = []

    exam = request.args.get('exam', '').upper()

    if request.method == 'POST':
        exam = request.form['exam']
        caste = request.form['caste']
        score = float(request.form['score'])
        university = request.form['university']
        city = request.form['city']
        branch = request.form['branch']

        cutoff_column = "cutoff_cet" if exam == "CET" else "cutoff_jee"

        query = f"SELECT name, city, branch, {cutoff_column} as cutoff FROM colleges WHERE branch=?"
        params = [branch]

        if university and university != "Select":
            query += " AND university=?"
            params.append(university)
        if city and city != "Select":
            query += " AND city=?"
            params.append(city)

        print("[DEBUG] Query:", query)
        print("[DEBUG] Params:", params)

        rows = conn.execute(query, params).fetchall()
        print("[INFO] Colleges fetched from DB:", len(rows))

        for r in rows:
            # cutoff stored like: OPEN:89,OBC:85,SC:80,ST:74,NT:76,VJNT:78,EWS:83
            try:
                cutoff_dict = dict(item.split(":") for item in r['cutoff'].split(","))
                caste_cutoff = float(cutoff_dict.get(caste.upper(), 0))
                if score >= caste_cutoff:
                    colleges.append({
                        "name": r['name'],
                        "city": r['city'],
                        # "branch": r['branch'],
                        "caste_cutoff": caste_cutoff
                    })
            except Exception as e:
                print("[ERROR] Parsing cutoff for:", r['name'], "+", e)

        print("[INFO] Colleges Matched:", len(colleges))
        conn.close()
        return render_template('result.html', colleges=colleges)

    conn.close()
    return render_template(
        'filter.html',
        maharashtra_universities=maharashtra_universities,
        maharashtra_cities=maharashtra_cities,
        maharashtra_branches=maharashtra_branches,
          exam=exam
    )




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        conn.close()

        flash("✅ Account created! Please login.", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Connect to database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Find user by email
        cursor.execute("SELECT password, name FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        # Check user and verify password
        if user and bcrypt.check_password_hash(user[0], password):
            session['user_name'] = user[1]
            flash("✅ Login successful!", "success")
            return redirect(url_for('home'))
        else:
            flash("❌ Invalid email or password!", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/home',endpoint='home_page')
def home():
    if 'user_name' not in session:
        flash("⚠️ Please log in first!", "warning")
        return render_template('home.html', name=None)
    return render_template('home.html', name=session['user_name'])



@app.route('/logout')
def logout():
    session.clear()
    flash("👋 You been logged out successfully.", "info")
    return redirect(url_for('login'))


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


if __name__ == "__main__":
    app.run(debug=True)