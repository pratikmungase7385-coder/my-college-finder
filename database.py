import sqlite3

# ---------- DATABASE NAMES ----------
USER_DB = 'users.db'
COLLEGE_DB = 'colleges0.db'


# ---------- USER DATABASE ----------
def init_user_db():
    conn = sqlite3.connect(USER_DB)
    cur = conn.cursor()
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()
    print("User database ready!")


# ---------- COLLEGE DATABASE ----------
def init_college_db():
    conn = sqlite3.connect(COLLEGE_DB)
    cur = conn.cursor()

    cur.executescript('''
    CREATE TABLE IF NOT EXISTS colleges (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
     
        university TEXT NOT NULL,
        city TEXT NOT NULL,
        branch TEXT NOT NULL,
        cutoff_cet TEXT,
        cutoff_jee TEXT
    );
    ''')

  

   
    cur.execute("DELETE FROM colleges;")
    cur.execute("DELETE FROM sqlite_sequence WHERE name='colleges';")


    cur.executescript('''

INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
('Keystone School of Engineering, Pune', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'Pune', 'Computer Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
('Keystone School of Engineering, Pune', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'Pune', 'Information Technology', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
('Keystone School of Engineering, Pune', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'Pune', 'Mechanical Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
('Keystone School of Engineering, Pune', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'Pune', 'Civil Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70'),
('Keystone School of Engineering, Pune', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'Pune', 'Electronics & Telecommunication', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
('Keystone School of Engineering, Pune', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'Pune', 'Artificial Intelligence & Machine Learning', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73');

     ''')                 
                      
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Sanjay Ghodawat Institute, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Computer Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Sanjay Ghodawat Institute, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Sanjay Ghodawat Institute, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Sanjay Ghodawat Institute, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Sanjay Ghodawat Institute, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Electronics & Telecommunication', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Sanjay Ghodawat Institute, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Artificial Intelligence & Machine Learning', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('COEP Technological University, Pune', 'CET,JEE', 'COEP Technological University, University, Autonomous', 'Pune', 'Computer Engineering', 'OPEN:99,OBC:96,SC:90,ST:85,NT:88,VJNT:89,EWS:97', 'OPEN:98,OBC:95,SC:89,ST:84,NT:87,VJNT:88,EWS:96'),
# ('COEP Technological University, Pune', 'CET,JEE', 'COEP Technological University, University, Autonomous', 'Pune', 'Information Technology', 'OPEN:98,OBC:95,SC:89,ST:84,NT:87,VJNT:88,EWS:96', 'OPEN:97,OBC:94,SC:88,ST:83,NT:86,VJNT:87,EWS:95'),
# ('COEP Technological University, Pune', 'CET,JEE', 'COEP Technological University, University, Autonomous', 'Pune', 'Mechanical Engineering', 'OPEN:96,OBC:93,SC:87,ST:82,NT:85,VJNT:86,EWS:94', 'OPEN:95,OBC:92,SC:86,ST:81,NT:84,VJNT:85,EWS:93'),
# ('COEP Technological University, Pune', 'CET,JEE', 'COEP Technological University, University, Autonomous', 'Pune', 'Civil Engineering', 'OPEN:95,OBC:92,SC:86,ST:81,NT:84,VJNT:85,EWS:93', 'OPEN:94,OBC:91,SC:85,ST:80,NT:83,VJNT:84,EWS:92'),
# ('COEP Technological University, Pune', 'CET,JEE', 'COEP Technological University, University, Autonomous', 'Pune', 'Electronics & Telecommunication', 'OPEN:97,OBC:94,SC:88,ST:83,NT:86,VJNT:87,EWS:95', 'OPEN:96,OBC:93,SC:87,ST:82,NT:85,VJNT:86,EWS:94'),
# ('COEP Technological University, Pune', 'CET,JEE', 'COEP Technological University, University, Autonomous', 'Pune', 'Artificial Intelligence & Machine Learning', 'OPEN:99,OBC:96,SC:90,ST:85,NT:88,VJNT:89,EWS:97', 'OPEN:98,OBC:95,SC:89,ST:84,NT:87,VJNT:88,EWS:96');



# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Dr. D.Y. Patil College of Engineering & Innovation, Talegaon', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'pune', 'Computer Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('Dr. D.Y. Patil College of Engineering & Innovation, Talegaon', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'pune', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Dr. D.Y. Patil College of Engineering & Innovation, Talegaon', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'pune', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Dr. D.Y. Patil College of Engineering & Innovation, Talegaon', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'pune', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Dr. D.Y. Patil College of Engineering & Innovation, Talegaon', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'pune', 'Electronics & Telecommunication', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Dr. D.Y. Patil College of Engineering & Innovation, Talegaon', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'pune', 'Artificial Intelligence & Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Dr. D.Y. Patil Pratishthans College of Engineering, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Computer Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Dr. D.Y. Patil Pratishthans College of Engineering, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Dr. D.Y. Patil Pratishthans College of Engineering, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Dr. D.Y. Patil Pratishthans College of Engineering, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Dr. D.Y. Patil Pratishthans College of Engineering, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Electronics & Telecommunication', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Dr. D.Y. Patil Pratishthans College of Engineering, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Artificial Intelligence & Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Dr. A. D. Shinde College of Engineering, Gadhinglaj, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Computer Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Dr. A. D. Shinde College of Engineering, Gadhinglaj, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Information Technology', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Dr. A. D. Shinde College of Engineering, Gadhinglaj, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Dr. A. D. Shinde College of Engineering, Gadhinglaj, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Civil Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Dr. A. D. Shinde College of Engineering, Gadhinglaj, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Artificial Intelligence & Machine Learning', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('MAEERs MIT College of Railway Engineering and Research, Jamgaon, Barshi', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Solapur', 'Computer Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('MAEERs MIT College of Railway Engineering and Research, Jamgaon, Barshi', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Solapur', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('MAEERs MIT College of Railway Engineering and Research, Jamgaon, Barshi', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Solapur', 'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Shree Siddheshwar Womens College of Engineering, Solapur', 'CET,JEE', 'Solapur University, Un-Aided', 'Solapur', 'Computer Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Shree Siddheshwar Womens College of Engineering, Solapur', 'CET,JEE', 'Solapur University, Un-Aided', 'Solapur', 'Information Technology', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Laxminarayan Innovation Technological University, Nagpur', 'CET,JEE', 'Laxminarayan Innovation Technological University, University, Autonomous', 'Nagpur', 'Computer Engineering', 'OPEN:95,OBC:91,SC:85,ST:80,NT:83,VJNT:84,EWS:92', 'OPEN:94,OBC:90,SC:84,ST:79,NT:82,VJNT:83,EWS:91'),
# ('Laxminarayan Innovation Technological University, Nagpur', 'CET,JEE', 'Laxminarayan Innovation Technological University, University, Autonomous', 'Nagpur', 'Mechanical Engineering', 'OPEN:93,OBC:89,SC:83,ST:78,NT:81,VJNT:82,EWS:90', 'OPEN:92,OBC:88,SC:82,ST:77,NT:80,VJNT:81,EWS:89');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Shri. Anandrao Abitkar College of Engineering, Pal', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Jalgaon', 'Computer Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Shri. Anandrao Abitkar College of Engineering, Pal', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Jalgaon', 'Mechanical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Tatyasaheb Kore Institute of Engineering and Technology, Yelur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided, Autonomous', 'Kolhapur', 'Computer Engineering', 'OPEN:86,OBC:82,SC:76,ST:71,NT:74,VJNT:75,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81'),
# ('Tatyasaheb Kore Institute of Engineering and Technology, Yelur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided, Autonomous', 'Kolhapur', 'Information Technology', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80'),
# ('Tatyasaheb Kore Institute of Engineering and Technology, Yelur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided, Autonomous', 'Kolhapur', 'Mechanical Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Tatyasaheb Kore Institute of Engineering and Technology, Yelur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided, Autonomous', 'Kolhapur', 'Civil Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('SVERIs College of Engineering, Pandharpur', 'CET,JEE', 'Solapur University, Solapur, Un-Aided, Autonomous', 'Solapur', 'Computer Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('SVERIs College of Engineering, Pandharpur', 'CET,JEE', 'Solapur University, Solapur, Un-Aided, Autonomous', 'Solapur', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('SVERIs College of Engineering, Pandharpur', 'CET,JEE', 'Solapur University, Solapur, Un-Aided, Autonomous', 'Solapur', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('SVERIs College of Engineering, Pandharpur', 'CET,JEE', 'Solapur University, Solapur, Un-Aided, Autonomous', 'Solapur', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Karmaveer Bhaurao Patil College of Engineering, Satara', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Satara', 'Computer Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Karmaveer Bhaurao Patil College of Engineering, Satara', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Satara', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Karmaveer Bhaurao Patil College of Engineering, Satara', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Satara', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Karmaveer Bhaurao Patil College of Engineering, Satara', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Satara', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Rajarambapu Institute of Technology, Islampur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided, Autonomous', 'Sangli', 'Computer Engineering', 'OPEN:88,OBC:84,SC:78,ST:73,NT:76,VJNT:77,EWS:85', 'OPEN:86,OBC:82,SC:76,ST:71,NT:74,VJNT:75,EWS:83'),
# ('Rajarambapu Institute of Technology, Islampur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided, Autonomous', 'Sangli', 'Information Technology', 'OPEN:87,OBC:83,SC:77,ST:72,NT:75,VJNT:76,EWS:84', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82'),
# ('Rajarambapu Institute of Technology, Islampur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided, Autonomous', 'Sangli', 'Mechanical Engineering', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80'),
# ('Rajarambapu Institute of Technology, Islampur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided, Autonomous', 'Sangli', 'Civil Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Sanjay Ghodawat Institute, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Computer Engineering', 'OPEN:86,OBC:82,SC:76,ST:71,NT:74,VJNT:75,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81'),
# ('Sanjay Ghodawat Institute, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Information Technology', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80'),
# ('Sanjay Ghodawat Institute, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Mechanical Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Sanjay Ghodawat Institute, Kolhapur', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Kolhapur', 'Civil Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('PVPIT Budhgaon, Sangli', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Sangli', 'Computer Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('PVPIT Budhgaon, Sangli', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Sangli', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('PVPIT Budhgaon, Sangli', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Sangli', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('PVPIT Budhgaon, Sangli', 'CET,JEE', 'Shivaji University, Kolhapur, Un-Aided', 'Sangli', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Government College of Engineering, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Government, Autonomous', 'Amravati', 'Computer Science and Engineering', 'OPEN:88,OBC:84,SC:78,ST:72,NT:75,VJNT:76,EWS:85', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83'),
# ('Government College of Engineering, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Government, Autonomous', 'Amravati', 'Information Technology', 'OPEN:87,OBC:83,SC:77,ST:71,NT:74,VJNT:75,EWS:84', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82'),
# ('Government College of Engineering, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Government, Autonomous', 'Amravati', 'Electronics and Telecommunication Engineering', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81'),
# ('Government College of Engineering, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Government, Autonomous', 'Amravati', 'Mechanical Engineering', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Government College of Engineering, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Government, Autonomous', 'Amravati', 'Civil Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Sant Gadge Baba Amravati University, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, University', 'Amravati', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('Sant Gadge Baba Amravati University, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, University ', 'Amravati', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Sant Gadge Baba Amravati University, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, University', 'Amravati', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Sant Gadge Baba Amravati University, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, University', 'Amravati', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Sant Gadge Baba Amravati University, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, University', 'Amravati', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Government College of Engineering, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Government', 'Yavatmal', 'Computer Science and Engineering', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81'),
# ('Government College of Engineering, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Government', 'Yavatmal', 'Information Technology', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Government College of Engineering, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Government', 'Yavatmal', 'Mechanical Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Government College of Engineering, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Government', 'Yavatmal', 'Civil Engineering', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Government College of Engineering, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Government', 'Yavatmal', 'Electrical Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Government College of Engineering, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Government', 'Yavatmal', 'Artificial Intelligence & Machine Learning', 'OPEN:87,OBC:83,SC:77,ST:71,NT:74,VJNT:75,EWS:84', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82'),
# ('Government College of Engineering, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Government', 'Yavatmal', 'Robotics and Automation', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Shri Sant Gajanan Maharaj College of Engineering, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('Shri Sant Gajanan Maharaj College of Engineering, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Shri Sant Gajanan Maharaj College of Engineering, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Shri Sant Gajanan Maharaj College of Engineering, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Shri Sant Gajanan Maharaj College of Engineering, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Shri Sant Gajanan Maharaj College of Engineering, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Electrical Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Shri Sant Gajanan Maharaj College of Engineering, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Artificial Intelligence & Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Shri Sant Gajanan Maharaj College of Engineering, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Robotics and Automation', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Prof. Ram Meghe Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Computer Science and Engineering', 'OPEN:87,OBC:83,SC:77,ST:71,NT:74,VJNT:75,EWS:84', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82'),
# ('Prof. Ram Meghe Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Information Technology', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81'),
# ('Prof. Ram Meghe Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Electronics and Telecommunication Engineering', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Prof. Ram Meghe Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Electrical Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Prof. Ram Meghe Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Mechanical Engineering', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Prof. Ram Meghe Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Civil Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Prof. Ram Meghe Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Artificial Intelligence & Machine Learning', 'OPEN:88,OBC:84,SC:78,ST:72,NT:75,VJNT:76,EWS:85', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83'),
# ('Prof. Ram Meghe Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Robotics and Automation', 'OPEN:87,OBC:83,SC:77,ST:71,NT:74,VJNT:75,EWS:84', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('P. R. Pote Patil College of Engineering & Management, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Computer Science and Engineering', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('P. R. Pote Patil College of Engineering & Management, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Information Technology', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('P. R. Pote Patil College of Engineering & Management, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Electronics and Telecommunication Engineering', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('P. R. Pote Patil College of Engineering & Management, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Electrical Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('P. R. Pote Patil College of Engineering & Management, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('P. R. Pote Patil College of Engineering & Management, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('P. R. Pote Patil College of Engineering & Management, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Artificial Intelligence & Machine Learning', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81'),
# ('P. R. Pote Patil College of Engineering & Management, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Robotics and Automation', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Sipna Shikshan Prasarak Mandal College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Sipna Shikshan Prasarak Mandal College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Sipna Shikshan Prasarak Mandal College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77'),
# ('Sipna Shikshan Prasarak Mandal College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Electrical Engineering', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:76'),
# ('Sipna Shikshan Prasarak Mandal College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:75'),
# ('Sipna Shikshan Prasarak Mandal College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:61,NT:64,VJNT:65,EWS:74'),
# ('Sipna Shikshan Prasarak Mandal College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Artificial Intelligence & Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Sipna Shikshan Prasarak Mandal College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Amravati', 'Robotics and Automation', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Shri Shivaji Education Society\s College of Engineering and Technology, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Computer Science and Engineering', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77'),
# ('Shri Shivaji Education Society\s College of Engineering and Technology, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:76'),
# ('Shri Shivaji Education Society\s College of Engineering and Technology, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Electronics and Telecommunication Engineering', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:75'),
# ('Shri Shivaji Education Society\s College of Engineering and Technology, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Electrical Engineering', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:61,NT:64,VJNT:65,EWS:74'),
# ('Shri Shivaji Education Society\s College of Engineering and Technology, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:60,NT:63,VJNT:64,EWS:73'),
# ('Shri Shivaji Education Society\s College of Engineering and Technology, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Civil Engineering', 'OPEN:77,OBC:73,SC:67,ST:61,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:59,NT:62,VJNT:63,EWS:72'),
# ('Shri Shivaji Education Society\s College of Engineering and Technology, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Artificial Intelligence & Machine Learning', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Shri Shivaji Education Society\s College of Engineering and Technology, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Robotics and Automation', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Jawaharlal Darda Institute of Engineering and Technology, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Linguistic Minority - Hindi', 'Yavatmal', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Jawaharlal Darda Institute of Engineering and Technology, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Linguistic Minority - Hindi', 'Yavatmal', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Jawaharlal Darda Institute of Engineering and Technology, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Linguistic Minority - Hindi', 'Yavatmal', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77'),
# ('Jawaharlal Darda Institute of Engineering and Technology, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Linguistic Minority - Hindi', 'Yavatmal', 'Electrical Engineering', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:76'),
# ('Jawaharlal Darda Institute of Engineering and Technology, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Linguistic Minority - Hindi', 'Yavatmal', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:75'),
# ('Jawaharlal Darda Institute of Engineering and Technology, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Linguistic Minority - Hindi', 'Yavatmal', 'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:61,NT:64,VJNT:65,EWS:74');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Shri Hanuman Vyayam Prasarak Mandal\s College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Computer Science and Engineering', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77'),
# ('Shri Hanuman Vyayam Prasarak Mandal\s College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:76'),
# ('Shri Hanuman Vyayam Prasarak Mandal\s College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Electronics and Telecommunication Engineering', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:75'),
# ('Shri Hanuman Vyayam Prasarak Mandal\s College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Electrical Engineering', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:61,NT:64,VJNT:65,EWS:74'),
# ('Shri Hanuman Vyayam Prasarak Mandal\s College of Engineering & Technology, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:60,NT:63,VJNT:64,EWS:73');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Janata Shikshan Prasarak Mandals Babasaheb Naik College Of Engineering, Pusad', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Yavatmal', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Janata Shikshan Prasarak Mandals Babasaheb Naik College Of Engineering, Pusad', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Yavatmal', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Janata Shikshan Prasarak Mandals Babasaheb Naik College Of Engineering, Pusad', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Yavatmal', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Janata Shikshan Prasarak Mandals Babasaheb Naik College Of Engineering, Pusad', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Yavatmal', 'Electrical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Janata Shikshan Prasarak Mandals Babasaheb Naik College Of Engineering, Pusad', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Yavatmal', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Janata Shikshan Prasarak Mandals Babasaheb Naik College Of Engineering, Pusad', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Yavatmal', 'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Janata Shikshan Prasarak Mandals Babasaheb Naik College Of Engineering, Pusad', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Yavatmal', 'Artificial Intelligence & Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Janata Shikshan Prasarak Mandals Babasaheb Naik College Of Engineering, Pusad', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Yavatmal', 'Robotics and Automation', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Dr. Rajendra Gode Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Dr. Rajendra Gode Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Dr. Rajendra Gode Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Dr. Rajendra Gode Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Electrical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Dr. Rajendra Gode Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Dr. Rajendra Gode Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Dr. Rajendra Gode Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Artificial Intelligence & Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Dr. Rajendra Gode Institute of Technology & Research, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Robotics and Automation', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Dwarka Bahu Uddeshiya Gramin Vikas Foundation, Rajarshi Shahu College of Engineering, Buldhana', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Computer Science and Engineering', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Dwarka Bahu Uddeshiya Gramin Vikas Foundation, Rajarshi Shahu College of Engineering, Buldhana', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Artificial Intelligence & Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Dwarka Bahu Uddeshiya Gramin Vikas Foundation, Rajarshi Shahu College of Engineering, Buldhana', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Electrical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Dwarka Bahu Uddeshiya Gramin Vikas Foundation, Rajarshi Shahu College of Engineering, Buldhana', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Dwarka Bahu Uddeshiya Gramin Vikas Foundation, Rajarshi Shahu College of Engineering, Buldhana', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Takshashila Institute of Engineering & Technology, Darapur, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Computer Science and Engineering', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Takshashila Institute of Engineering & Technology, Darapur, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Takshashila Institute of Engineering & Technology, Darapur, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Electrical Engineering', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:77,OBC:73,SC:67,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Takshashila Institute of Engineering & Technology, Darapur, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:76,OBC:72,SC:66,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Takshashila Institute of Engineering & Technology, Darapur, Amravati', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Civil Engineering', 'OPEN:77,OBC:73,SC:67,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:75,OBC:71,SC:65,ST:59,NT:62,VJNT:63,EWS:71');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Jagdambha College of Engineering and Technology, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Yavatmal', 'Computer Science and Engineering', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Jagdambha College of Engineering and Technology, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Yavatmal', 'Information Technology', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Jagdambha College of Engineering and Technology, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Yavatmal', 'Artificial Intelligence & Machine Learning', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81'),
# ('Jagdambha College of Engineering and Technology, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Yavatmal', 'Electrical Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Jagdambha College of Engineering and Technology, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Yavatmal', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Jagdambha College of Engineering and Technology, Yavatmal', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided, Autonomous', 'Yavatmal', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Prof. Ram Meghe College of Engineering and Management, Badnera', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Computer Science and Engineering', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81'),
# ('Prof. Ram Meghe College of Engineering and Management, Badnera', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Information Technology', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Prof. Ram Meghe College of Engineering and Management, Badnera', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Artificial Intelligence & Machine Learning', 'OPEN:87,OBC:83,SC:77,ST:71,NT:74,VJNT:75,EWS:84', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82'),
# ('Prof. Ram Meghe College of Engineering and Management, Badnera', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Electronics and Telecommunication Engineering', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Prof. Ram Meghe College of Engineering and Management, Badnera', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Electrical Engineering', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77'),
# ('Prof. Ram Meghe College of Engineering and Management, Badnera', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:76'),
# ('Prof. Ram Meghe College of Engineering and Management, Badnera', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Amravati', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:75');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Vision Buldhana Educational & Welfare Society\s Pankaj Laddhad Institute of Technology & Management Studies, Yelgaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Computer Science and Engineering', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Vision Buldhana Educational & Welfare Society\s Pankaj Laddhad Institute of Technology & Management Studies, Yelgaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77'),
# ('Vision Buldhana Educational & Welfare Society\s Pankaj Laddhad Institute of Technology & Management Studies, Yelgaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Electrical Engineering', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:77,OBC:73,SC:67,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Vision Buldhana Educational & Welfare Society\s Pankaj Laddhad Institute of Technology & Management Studies, Yelgaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:76,OBC:72,SC:66,ST:60,NT:63,VJNT:64,EWS:72');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Sanmati Engineering College, Sawargaon Barde, Washim', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Washim', 'Computer Science and Engineering', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Sanmati Engineering College, Sawargaon Barde, Washim', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Washim', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Sanmati Engineering College, Sawargaon Barde, Washim', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Washim', 'Electrical Engineering', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Sanmati Engineering College, Sawargaon Barde, Washim', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Washim', 'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:77,OBC:73,SC:67,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Sanmati Engineering College, Sawargaon Barde, Washim', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Washim', 'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:76,OBC:72,SC:66,ST:60,NT:63,VJNT:64,EWS:72');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Padmashri Dr. V. B. Kolte College of Engineering, Malkapur, Buldhana', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Padmashri Dr. V. B. Kolte College of Engineering, Malkapur, Buldhana', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Padmashri Dr. V. B. Kolte College of Engineering, Malkapur, Buldhana', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Electrical Engineering', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Padmashri Dr. V. B. Kolte College of Engineering, Malkapur, Buldhana', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:77,OBC:73,SC:67,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Padmashri Dr. V. B. Kolte College of Engineering, Malkapur, Buldhana', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:76,OBC:72,SC:66,ST:60,NT:63,VJNT:64,EWS:72');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Mauli Group of Institutions, College of Engineering and Technology, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Computer Science and Engineering', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Mauli Group of Institutions, College of Engineering and Technology, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Information Technology', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Mauli Group of Institutions, College of Engineering and Technology, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Electronics and Telecommunication Engineering', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Mauli Group of Institutions, College of Engineering and Technology, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Electrical Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Mauli Group of Institutions, College of Engineering and Technology, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Mauli Group of Institutions, College of Engineering and Technology, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Mauli Group of Institutions, College of Engineering and Technology, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Artificial Intelligence & Machine Learning', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81'),
# ('Mauli Group of Institutions, College of Engineering and Technology, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Artificial Intelligence & Data Science', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Mauli Group of Institutions, College of Engineering and Technology, Shegaon', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Robotics and Automation', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Siddhivinayak Technical Campus, School of Engineering & Research Technology, Shirasgon Nile', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Siddhivinayak Technical Campus, School of Engineering & Research Technology, Shirasgon Nile', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Siddhivinayak Technical Campus, School of Engineering & Research Technology, Shirasgon Nile', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Siddhivinayak Technical Campus, School of Engineering & Research Technology, Shirasgon Nile', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Electrical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Siddhivinayak Technical Campus, School of Engineering & Research Technology, Shirasgon Nile', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Siddhivinayak Technical Campus, School of Engineering & Research Technology, Shirasgon Nile', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Siddhivinayak Technical Campus, School of Engineering & Research Technology, Shirasgon Nile', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Artificial Intelligence & Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Siddhivinayak Technical Campus, School of Engineering & Research Technology, Shirasgon Nile', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Artificial Intelligence & Data Science', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Siddhivinayak Technical Campus, School of Engineering & Research Technology, Shirasgon Nile', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Buldhana', 'Robotics and Automation', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79');



# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Manav School of Engineering & Technology, Gut No. 1035 Nagpur Surat Highway, NH No. 6 Tal. Vyala, Balapur, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Manav School of Engineering & Technology, Gut No. 1035 Nagpur Surat Highway, NH No. 6 Tal. Vyala, Balapur, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Manav School of Engineering & Technology, Gut No. 1035 Nagpur Surat Highway, NH No. 6 Tal. Vyala, Balapur, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Manav School of Engineering & Technology, Gut No. 1035 Nagpur Surat Highway, NH No. 6 Tal. Vyala, Balapur, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Electrical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Manav School of Engineering & Technology, Gut No. 1035 Nagpur Surat Highway, NH No. 6 Tal. Vyala, Balapur, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Manav School of Engineering & Technology, Gut No. 1035 Nagpur Surat Highway, NH No. 6 Tal. Vyala, Balapur, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Manav School of Engineering & Technology, Gut No. 1035 Nagpur Surat Highway, NH No. 6 Tal. Vyala, Balapur, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Artificial Intelligence & Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Manav School of Engineering & Technology, Gut No. 1035 Nagpur Surat Highway, NH No. 6 Tal. Vyala, Balapur, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Artificial Intelligence & Data Science', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Manav School of Engineering & Technology, Gut No. 1035 Nagpur Surat Highway, NH No. 6 Tal. Vyala, Balapur, Akola', 'CET,JEE', 'Sant Gadge Baba Amravati University, Un-Aided', 'Akola', 'Robotics and Automation', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Government College of Engineering, Chhatrapati Sambhajinagar', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, Autonomous', 'Chhatrapati Sambhajinagar', 'Computer Science and Engineering', 'OPEN:88,OBC:84,SC:78,ST:72,NT:75,VJNT:76,EWS:85', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83'),
# ('Government College of Engineering, Chhatrapati Sambhajinagar', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, Autonomous', 'Chhatrapati Sambhajinagar', 'Information Technology', 'OPEN:87,OBC:83,SC:77,ST:71,NT:74,VJNT:75,EWS:84', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82'),
# ('Government College of Engineering, Chhatrapati Sambhajinagar', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, Autonomous', 'Chhatrapati Sambhajinagar', 'Electronics and Telecommunication Engineering', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81'),
# ('Government College of Engineering, Chhatrapati Sambhajinagar', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, Autonomous', 'Chhatrapati Sambhajinagar', 'Electrical Engineering', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Government College of Engineering, Chhatrapati Sambhajinagar', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, Autonomous', 'Chhatrapati Sambhajinagar', 'Mechanical Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Government College of Engineering, Chhatrapati Sambhajinagar', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, Autonomous', 'Chhatrapati Sambhajinagar', 'Civil Engineering', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Government College of Engineering, Chhatrapati Sambhajinagar', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, Autonomous', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Machine Learning', 'OPEN:89,OBC:85,SC:79,ST:73,NT:76,VJNT:77,EWS:86', 'OPEN:87,OBC:83,SC:77,ST:71,NT:74,VJNT:75,EWS:84'),
# ('Government College of Engineering, Chhatrapati Sambhajinagar', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, Autonomous', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Data Science', 'OPEN:89,OBC:85,SC:79,ST:73,NT:76,VJNT:77,EWS:86', 'OPEN:87,OBC:83,SC:77,ST:71,NT:74,VJNT:75,EWS:84'),
# ('Government College of Engineering, Chhatrapati Sambhajinagar', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, Autonomous', 'Chhatrapati Sambhajinagar', 'Robotics and Automation', 'OPEN:88,OBC:84,SC:78,ST:72,NT:75,VJNT:76,EWS:85', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83');



# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Shree Yash Pratishthan, Shreeyash College of Engineering and Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Computer Science and Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Shree Yash Pratishthan, Shreeyash College of Engineering and Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Shree Yash Pratishthan, Shreeyash College of Engineering and Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electronics and Telecommunication Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Shree Yash Pratishthan, Shreeyash College of Engineering and Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electrical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Shree Yash Pratishthan, Shreeyash College of Engineering and Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Shree Yash Pratishthan, Shreeyash College of Engineering and Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Shree Yash Pratishthan, Shreeyash College of Engineering and Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Shree Yash Pratishthan, Shreeyash College of Engineering and Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Shree Yash Pratishthan, Shreeyash College of Engineering and Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('G. S. Mandals Maharashtra Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided, Autonomous', 'Chhatrapati Sambhajinagar', 'Computer Science and Engineering', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81'),
# ('G. S. Mandals Maharashtra Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided, Autonomous', 'Chhatrapati Sambhajinagar', 'Information Technology', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('G. S. Mandals Maharashtra Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided, Autonomous', 'Chhatrapati Sambhajinagar', 'Electronics and Telecommunication Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('G. S. Mandals Maharashtra Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided, Autonomous', 'Chhatrapati Sambhajinagar', 'Mechanical Engineering', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('G. S. Mandals Maharashtra Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided, Autonomous', 'Chhatrapati Sambhajinagar', 'Civil Engineering', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:64,NT:67,VJNT:68,EWS:77'),
# ('G. S. Mandals Maharashtra Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided, Autonomous', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Machine Learning', 'OPEN:87,OBC:83,SC:77,ST:71,NT:74,VJNT:75,EWS:84', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82'),
# ('G. S. Mandals Maharashtra Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided, Autonomous', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Data Science', 'OPEN:87,OBC:83,SC:77,ST:71,NT:74,VJNT:75,EWS:84', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82'),
# ('G. S. Mandals Maharashtra Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided, Autonomous', 'Chhatrapati Sambhajinagar', 'Robotics and Automation', 'OPEN:86,OBC:82,SC:76,ST:70,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Deogiri Institute of Engineering and Management Studies, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79'),
# ('Deogiri Institute of Engineering and Management Studies, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:65,NT:68,VJNT:69,EWS:78'),
# ('Deogiri Institute of Engineering and Management Studies, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Deogiri Institute of Engineering and Management Studies, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Deogiri Institute of Engineering and Management Studies, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Deogiri Institute of Engineering and Management Studies, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Data Science', 'OPEN:85,OBC:81,SC:75,ST:69,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:67,NT:70,VJNT:71,EWS:80'),
# ('Deogiri Institute of Engineering and Management Studies, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Robotics and Automation', 'OPEN:84,OBC:80,SC:74,ST:68,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:66,NT:69,VJNT:70,EWS:79');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Matoshri Pratishans Group of Institutions (Integrated Campus), Kupsarwadi, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Computer Science and Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Matoshri Pratishans Group of Institutions (Integrated Campus), Kupsarwadi, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Matoshri Pratishans Group of Institutions (Integrated Campus), Kupsarwadi, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Matoshri Pratishans Group of Institutions (Integrated Campus), Kupsarwadi, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Matoshri Pratishans Group of Institutions (Integrated Campus), Kupsarwadi, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Artificial Intelligence & Machine Learning', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Matoshri Pratishans Group of Institutions (Integrated Campus), Kupsarwadi, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Artificial Intelligence & Data Science', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Matoshri Pratishans Group of Institutions (Integrated Campus), Kupsarwadi, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Robotics and Automation', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Mahatma Gandhi Missions College of Engineering, Hingoli Rd, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Mahatma Gandhi Missions College of Engineering, Hingoli Rd, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Mahatma Gandhi Missions College of Engineering, Hingoli Rd, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Mahatma Gandhi Missions College of Engineering, Hingoli Rd, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Electrical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Mahatma Gandhi Missions College of Engineering, Hingoli Rd, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Mahatma Gandhi Missions College of Engineering, Hingoli Rd, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Mahatma Gandhi Missions College of Engineering, Hingoli Rd, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Artificial Intelligence & Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80'),
# ('Mahatma Gandhi Missions College of Engineering, Hingoli Rd, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Artificial Intelligence & Data Science', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80'),
# ('Mahatma Gandhi Missions College of Engineering, Hingoli Rd, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Robotics and Automation', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('M.S. Bidve Engineering College, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Computer Science and Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('M.S. Bidve Engineering College, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('M.S. Bidve Engineering College, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Electronics and Telecommunication Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('M.S. Bidve Engineering College, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Electrical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('M.S. Bidve Engineering College, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('M.S. Bidve Engineering College, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('M.S. Bidve Engineering College, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Artificial Intelligence & Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('M.S. Bidve Engineering College, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Artificial Intelligence & Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('M.S. Bidve Engineering College, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Terna Public Charitable Trust\s College of Engineering, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Terna Public Charitable Trust\s College of Engineering, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Terna Public Charitable Trust\s College of Engineering, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Terna Public Charitable Trust\s College of Engineering, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Electrical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Terna Public Charitable Trust\s College of Engineering, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Terna Public Charitable Trust\s College of Engineering, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Terna Public Charitable Trust\s College of Engineering, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Artificial Intelligence & Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80'),
# ('Terna Public Charitable Trust\s College of Engineering, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Artificial Intelligence & Data Science', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80'),
# ('Terna Public Charitable Trust\s College of Engineering, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Robotics and Automation', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Shree Tuljabhavani College of Engineering, Tuljapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Computer Science and Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Shree Tuljabhavani College of Engineering, Tuljapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Shree Tuljabhavani College of Engineering, Tuljapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Electronics and Telecommunication Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Shree Tuljabhavani College of Engineering, Tuljapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Electrical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Shree Tuljabhavani College of Engineering, Tuljapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Shree Tuljabhavani College of Engineering, Tuljapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Shree Tuljabhavani College of Engineering, Tuljapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Artificial Intelligence & Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Shree Tuljabhavani College of Engineering, Tuljapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Artificial Intelligence & Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Shree Tuljabhavani College of Engineering, Tuljapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere', 'Osmanabad', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Mahatma Basaweshwar Education Societys College of Engineering, Ambejogai', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Computer Science and Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Mahatma Basaweshwar Education Societys College of Engineering, Ambejogai', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Mahatma Basaweshwar Education Societys College of Engineering, Ambejogai', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Electronics and Telecommunication Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Mahatma Basaweshwar Education Societys College of Engineering, Ambejogai', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Electrical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Mahatma Basaweshwar Education Societys College of Engineering, Ambejogai', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Mahatma Basaweshwar Education Societys College of Engineering, Ambejogai', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Civil Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('Mahatma Basaweshwar Education Societys College of Engineering, Ambejogai', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Artificial Intelligence & Machine Learning', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Mahatma Basaweshwar Education Societys College of Engineering, Ambejogai', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Artificial Intelligence & Data Science', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Mahatma Basaweshwar Education Societys College of Engineering, Ambejogai', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Robotics and Automation', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Peoples Education Societys College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Computer Science and Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Peoples Education Societys College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Peoples Education Societys College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electronics and Telecommunication Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Peoples Education Societys College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electrical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Peoples Education Societys College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Peoples Education Societys College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Peoples Education Societys College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Peoples Education Societys College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Peoples Education Societys College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Hi-Tech Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Hi-Tech Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Hi-Tech Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Hi-Tech Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electrical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Hi-Tech Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Hi-Tech Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Hi-Tech Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80'),
# ('Hi-Tech Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Data Science', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80'),
# ('Hi-Tech Institute of Technology, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Robotics and Automation', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Aditya Engineering College, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Computer Science and Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Aditya Engineering College, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Aditya Engineering College, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Electronics and Telecommunication Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Aditya Engineering College, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Electrical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Aditya Engineering College, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Aditya Engineering College, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Civil Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('Aditya Engineering College, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Artificial Intelligence & Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Aditya Engineering College, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Artificial Intelligence & Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Aditya Engineering College, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Nagnathappa Halge Engineering College, Parli, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Computer Science and Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Nagnathappa Halge Engineering College, Parli, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Nagnathappa Halge Engineering College, Parli, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Electronics and Telecommunication Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Nagnathappa Halge Engineering College, Parli, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Electrical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Nagnathappa Halge Engineering College, Parli, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Mechanical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('Nagnathappa Halge Engineering College, Parli, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Civil Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:61,VJNT:62,EWS:71'),
# ('Nagnathappa Halge Engineering College, Parli, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Artificial Intelligence & Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Nagnathappa Halge Engineering College, Parli, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Artificial Intelligence & Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Nagnathappa Halge Engineering College, Parli, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Matsyodari Shikshan Sansatha College of Engineering and Technology, Jalna', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Jalna', 'Computer Science and Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Matsyodari Shikshan Sansatha College of Engineering and Technology, Jalna', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Jalna', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Matsyodari Shikshan Sansatha College of Engineering and Technology, Jalna', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Jalna', 'Electronics and Telecommunication Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Matsyodari Shikshan Sansatha College of Engineering and Technology, Jalna', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Jalna', 'Electrical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Matsyodari Shikshan Sansatha College of Engineering and Technology, Jalna', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Jalna', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Matsyodari Shikshan Sansatha College of Engineering and Technology, Jalna', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Jalna', 'Civil Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('Matsyodari Shikshan Sansatha College of Engineering and Technology, Jalna', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Jalna', 'Artificial Intelligence & Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Matsyodari Shikshan Sansatha College of Engineering and Technology, Jalna', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Jalna', 'Artificial Intelligence & Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Matsyodari Shikshan Sansatha College of Engineering and Technology, Jalna', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Jalna', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Adarsh Shikshan Prasarak Mandals K. T. Patil College of Engineering and Technology, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Osmanabad', 'Computer Science and Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Adarsh Shikshan Prasarak Mandals K. T. Patil College of Engineering and Technology, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Osmanabad', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Adarsh Shikshan Prasarak Mandals K. T. Patil College of Engineering and Technology, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Osmanabad', 'Electronics and Telecommunication Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Adarsh Shikshan Prasarak Mandals K. T. Patil College of Engineering and Technology, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Osmanabad', 'Electrical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Adarsh Shikshan Prasarak Mandals K. T. Patil College of Engineering and Technology, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Osmanabad', 'Mechanical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('Adarsh Shikshan Prasarak Mandals K. T. Patil College of Engineering and Technology, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Osmanabad', 'Civil Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:61,VJNT:62,EWS:71'),
# ('Adarsh Shikshan Prasarak Mandals K. T. Patil College of Engineering and Technology, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Osmanabad', 'Artificial Intelligence & Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Adarsh Shikshan Prasarak Mandals K. T. Patil College of Engineering and Technology, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Osmanabad', 'Artificial Intelligence & Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Adarsh Shikshan Prasarak Mandals K. T. Patil College of Engineering and Technology, Osmanabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Osmanabad', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Aurangabad College of Engineering, Naygaon Savangi, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Computer Science and Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Aurangabad College of Engineering, Naygaon Savangi, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Aurangabad College of Engineering, Naygaon Savangi, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electronics and Telecommunication Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Aurangabad College of Engineering, Naygaon Savangi, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electrical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Aurangabad College of Engineering, Naygaon Savangi, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Aurangabad College of Engineering, Naygaon Savangi, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Civil Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('Aurangabad College of Engineering, Naygaon Savangi, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Aurangabad College of Engineering, Naygaon Savangi, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Aurangabad College of Engineering, Naygaon Savangi, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Marathwada Shikshan Prasarak Mandals Shri Shivaji Institute of Engineering and Management Studies, Parbhani', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Parbhani', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Marathwada Shikshan Prasarak Mandals Shri Shivaji Institute of Engineering and Management Studies, Parbhani', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Parbhani', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Marathwada Shikshan Prasarak Mandals Shri Shivaji Institute of Engineering and Management Studies, Parbhani', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Parbhani', 'Electronics and Telecommunication Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Marathwada Shikshan Prasarak Mandals Shri Shivaji Institute of Engineering and Management Studies, Parbhani', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Parbhani', 'Electrical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Marathwada Shikshan Prasarak Mandals Shri Shivaji Institute of Engineering and Management Studies, Parbhani', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Parbhani', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Marathwada Shikshan Prasarak Mandals Shri Shivaji Institute of Engineering and Management Studies, Parbhani', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Parbhani', 'Civil Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('Marathwada Shikshan Prasarak Mandals Shri Shivaji Institute of Engineering and Management Studies, Parbhani', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Parbhani', 'Artificial Intelligence and Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80'),
# ('Marathwada Shikshan Prasarak Mandals Shri Shivaji Institute of Engineering and Management Studies, Parbhani', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Parbhani', 'Artificial Intelligence and Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Marathwada Shikshan Prasarak Mandals Shri Shivaji Institute of Engineering and Management Studies, Parbhani', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Parbhani', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Vilasrao Deshmukh Foundation Group of Institutions, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Computer Science and Engineering', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80'),
# ('Vilasrao Deshmukh Foundation Group of Institutions, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Information Technology', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Vilasrao Deshmukh Foundation Group of Institutions, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Vilasrao Deshmukh Foundation Group of Institutions, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Electrical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Vilasrao Deshmukh Foundation Group of Institutions, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Vilasrao Deshmukh Foundation Group of Institutions, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Vilasrao Deshmukh Foundation Group of Institutions, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Artificial Intelligence and Machine Learning', 'OPEN:86,OBC:82,SC:76,ST:71,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81'),
# ('Vilasrao Deshmukh Foundation Group of Institutions, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Artificial Intelligence and Data Science', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80'),
# ('Vilasrao Deshmukh Foundation Group of Institutions, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Robotics and Automation', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79');
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Aditya Education Trusts Mitthulalji Sarada Polytechnic, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Computer Science and Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Aditya Education Trusts Mitthulalji Sarada Polytechnic, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Aditya Education Trusts Mitthulalji Sarada Polytechnic, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Electronics and Telecommunication Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Aditya Education Trusts Mitthulalji Sarada Polytechnic, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Electrical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Aditya Education Trusts Mitthulalji Sarada Polytechnic, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Aditya Education Trusts Mitthulalji Sarada Polytechnic, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Civil Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('Aditya Education Trusts Mitthulalji Sarada Polytechnic, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Artificial Intelligence and Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Aditya Education Trusts Mitthulalji Sarada Polytechnic, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Artificial Intelligence and Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Aditya Education Trusts Mitthulalji Sarada Polytechnic, Beed', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Un-Aided', 'Beed', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');

                      
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('GRAMIN Technical and Management Campus, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Computer Science and Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('GRAMIN Technical and Management Campus, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('GRAMIN Technical and Management Campus, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Electronics and Telecommunication Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('GRAMIN Technical and Management Campus, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Electrical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('GRAMIN Technical and Management Campus, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('GRAMIN Technical and Management Campus, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('GRAMIN Technical and Management Campus, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Artificial Intelligence and Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80'),
# ('GRAMIN Technical and Management Campus, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Artificial Intelligence and Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('GRAMIN Technical and Management Campus, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('International Centre Of Excellence In Engineering and Management (ICEEM), Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Computer Science and Engineering', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80'),
# ('International Centre Of Excellence In Engineering and Management (ICEEM), Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Information Technology', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('International Centre Of Excellence In Engineering and Management (ICEEM), Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electronics and Telecommunication Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('International Centre Of Excellence In Engineering and Management (ICEEM), Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electrical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('International Centre Of Excellence In Engineering and Management (ICEEM), Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('International Centre Of Excellence In Engineering and Management (ICEEM), Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('International Centre Of Excellence In Engineering and Management (ICEEM), Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Machine Learning', 'OPEN:86,OBC:82,SC:76,ST:71,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81'),
# ('International Centre Of Excellence In Engineering and Management (ICEEM), Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Data Science', 'OPEN:86,OBC:82,SC:76,ST:71,NT:73,VJNT:74,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81'),
# ('International Centre Of Excellence In Engineering and Management (ICEEM), Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Robotics and Automation', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('STMEIs Sandipani Technical Campus - Faculty of Engineering, Latur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Latur', 'Computer Science and Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('STMEIs Sandipani Technical Campus - Faculty of Engineering, Latur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Latur', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('STMEIs Sandipani Technical Campus - Faculty of Engineering, Latur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Latur', 'Electronics and Telecommunication Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('STMEIs Sandipani Technical Campus - Faculty of Engineering, Latur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Latur', 'Electrical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('STMEIs Sandipani Technical Campus - Faculty of Engineering, Latur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Latur', 'Mechanical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('STMEIs Sandipani Technical Campus - Faculty of Engineering, Latur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Latur', 'Civil Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:61,VJNT:62,EWS:71'),
# ('STMEIs Sandipani Technical Campus - Faculty of Engineering, Latur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Latur', 'Artificial Intelligence & Machine Learning', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('STMEIs Sandipani Technical Campus - Faculty of Engineering, Latur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Latur', 'Artificial Intelligence & Data Science', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('STMEIs Sandipani Technical Campus - Faculty of Engineering, Latur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Latur', 'Robotics and Automation', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('CSMSS Chhatrapati Shahu College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Computer Science and Engineering', 'OPEN:88,OBC:84,SC:78,ST:73,NT:75,VJNT:76,EWS:85', 'OPEN:86,OBC:82,SC:76,ST:71,NT:73,VJNT:74,EWS:83'),
# ('CSMSS Chhatrapati Shahu College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Information Technology', 'OPEN:87,OBC:83,SC:77,ST:72,NT:74,VJNT:75,EWS:84', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82'),
# ('CSMSS Chhatrapati Shahu College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electronics and Telecommunication Engineering', 'OPEN:85,OBC:81,SC:75,ST:70,NT:72,VJNT:73,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80'),
# ('CSMSS Chhatrapati Shahu College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electrical Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('CSMSS Chhatrapati Shahu College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Mechanical Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('CSMSS Chhatrapati Shahu College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Civil Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('CSMSS Chhatrapati Shahu College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Machine Learning', 'OPEN:89,OBC:85,SC:79,ST:74,NT:76,VJNT:77,EWS:86', 'OPEN:87,OBC:83,SC:77,ST:72,NT:74,VJNT:75,EWS:84'),
# ('CSMSS Chhatrapati Shahu College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Data Science', 'OPEN:89,OBC:85,SC:79,ST:74,NT:76,VJNT:77,EWS:86', 'OPEN:87,OBC:83,SC:77,ST:72,NT:74,VJNT:75,EWS:84'),
# ('CSMSS Chhatrapati Shahu College of Engineering, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Robotics and Automation', 'OPEN:88,OBC:84,SC:78,ST:73,NT:75,VJNT:76,EWS:85', 'OPEN:86,OBC:82,SC:76,ST:71,NT:73,VJNT:74,EWS:83');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Jijau Institute of Engineering Technology and Management, Naigaon, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Computer Science and Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Jijau Institute of Engineering Technology and Management, Naigaon, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Information Technology', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Jijau Institute of Engineering Technology and Management, Naigaon, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Electronics and Telecommunication Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Jijau Institute of Engineering Technology and Management, Naigaon, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Electrical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Jijau Institute of Engineering Technology and Management, Naigaon, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Mechanical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('Jijau Institute of Engineering Technology and Management, Naigaon, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Civil Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:61,VJNT:62,EWS:71'),
# ('Jijau Institute of Engineering Technology and Management, Naigaon, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Artificial Intelligence & Machine Learning', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Jijau Institute of Engineering Technology and Management, Naigaon, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Artificial Intelligence & Data Science', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Jijau Institute of Engineering Technology and Management, Naigaon, Nanded', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Nanded', 'Robotics and Automation', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76');



# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Dr. V.K. Patil College of Engineering & Technology, Udgir', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Computer Science and Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Dr. V.K. Patil College of Engineering & Technology, Udgir', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Dr. V.K. Patil College of Engineering & Technology, Udgir', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Electronics and Telecommunication Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Dr. V.K. Patil College of Engineering & Technology, Udgir', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Electrical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Dr. V.K. Patil College of Engineering & Technology, Udgir', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Dr. V.K. Patil College of Engineering & Technology, Udgir', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Civil Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('Dr. V.K. Patil College of Engineering & Technology, Udgir', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Artificial Intelligence & Machine Learning', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Dr. V.K. Patil College of Engineering & Technology, Udgir', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Artificial Intelligence & Data Science', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Dr. V.K. Patil College of Engineering & Technology, Udgir', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Robotics and Automation', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Mangaldeep College of Engineering, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Computer Science and Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75'),
# ('Mangaldeep College of Engineering, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Information Technology', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Mangaldeep College of Engineering, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Electronics and Telecommunication Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Mangaldeep College of Engineering, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Electrical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('Mangaldeep College of Engineering, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Mechanical Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:61,VJNT:62,EWS:71'),
# ('Mangaldeep College of Engineering, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Civil Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:60,VJNT:61,EWS:70'),
# ('Mangaldeep College of Engineering, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Artificial Intelligence & Machine Learning', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Mangaldeep College of Engineering, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Artificial Intelligence & Data Science', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Mangaldeep College of Engineering, Latur', 'CET,JEE', 'Swami Ramanand Teerth Marathwada University, Un-Aided', 'Latur', 'Robotics and Automation', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Sant Eknath College of Engineering, Paithan, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Computer Science and Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78'),
# ('Sant Eknath College of Engineering, Paithan, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:67,VJNT:68,EWS:77'),
# ('Sant Eknath College of Engineering, Paithan, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electronics and Telecommunication Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76'),
# ('Sant Eknath College of Engineering, Paithan, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Electrical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:66,VJNT:67,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74'),
# ('Sant Eknath College of Engineering, Paithan, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:65,VJNT:66,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:63,VJNT:64,EWS:73'),
# ('Sant Eknath College of Engineering, Paithan, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Civil Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:64,VJNT:65,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:62,VJNT:63,EWS:72'),
# ('Sant Eknath College of Engineering, Paithan, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Machine Learning', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Sant Eknath College of Engineering, Paithan, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Artificial Intelligence & Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:71,VJNT:72,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:69,VJNT:70,EWS:79'),
# ('Sant Eknath College of Engineering, Paithan, Aurangabad', 'CET,JEE', 'Dr. Babasaheb Ambedkar Marathwada University, Un-Aided', 'Chhatrapati Sambhajinagar', 'Robotics and Automation', 'OPEN:83,OBC:79,SC:73,ST:68,NT:70,VJNT:71,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:68,VJNT:69,EWS:78');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Veermata Jijabai Technological Institute (VJTI), Matunga, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous', 'Mumbai', 'Computer Engineering', 'OPEN:99.40,OBC:98.80,SC:97.10,ST:94.60,NT:95.50,VJNT:96.00,EWS:98.50', 'OPEN:99.30,OBC:98.70,SC:97.00,ST:94.40,NT:95.30,VJNT:95.90,EWS:98.40'),
# ('Veermata Jijabai Technological Institute (VJTI), Matunga, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous', 'Mumbai', 'Information Technology', 'OPEN:99.20,OBC:98.50,SC:96.80,ST:94.10,NT:95.00,VJNT:95.60,EWS:98.20', 'OPEN:99.10,OBC:98.40,SC:96.70,ST:93.90,NT:94.90,VJNT:95.50,EWS:98.10'),
# ('Veermata Jijabai Technological Institute (VJTI), Matunga, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous', 'Mumbai', 'Electronics and Telecommunication Engineering', 'OPEN:98.90,OBC:98.20,SC:96.40,ST:93.70,NT:94.60,VJNT:95.20,EWS:97.80', 'OPEN:98.80,OBC:98.10,SC:96.30,ST:93.50,NT:94.40,VJNT:95.10,EWS:97.70'),
# ('Veermata Jijabai Technological Institute (VJTI), Matunga, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous', 'Mumbai', 'Electrical Engineering', 'OPEN:98.50,OBC:97.80,SC:95.90,ST:93.30,NT:94.00,VJNT:94.70,EWS:97.40', 'OPEN:98.40,OBC:97.70,SC:95.80,ST:93.10,NT:93.90,VJNT:94.60,EWS:97.30'),
# ('Veermata Jijabai Technological Institute (VJTI), Matunga, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous', 'Mumbai', 'Mechanical Engineering', 'OPEN:98.30,OBC:97.60,SC:95.60,ST:92.90,NT:93.70,VJNT:94.40,EWS:97.10', 'OPEN:98.20,OBC:97.50,SC:95.50,ST:92.70,NT:93.60,VJNT:94.30,EWS:97.00'),
# ('Veermata Jijabai Technological Institute (VJTI), Matunga, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous', 'Mumbai', 'Civil Engineering', 'OPEN:97.90,OBC:97.30,SC:95.20,ST:92.50,NT:93.30,VJNT:94.00,EWS:96.80', 'OPEN:97.80,OBC:97.20,SC:95.10,ST:92.30,NT:93.20,VJNT:93.90,EWS:96.70'),
# ('Veermata Jijabai Technological Institute (VJTI), Matunga, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous', 'Mumbai', 'Production Engineering', 'OPEN:97.70,OBC:97.00,SC:94.90,ST:92.10,NT:93.00,VJNT:93.70,EWS:96.50', 'OPEN:97.60,OBC:96.90,SC:94.80,ST:91.90,NT:92.90,VJNT:93.60,EWS:96.40');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Sardar Patel College of Engineering (SPCE), Andheri, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous', 'Mumbai', 'Computer Engineering', 'OPEN:99.10,OBC:98.40,SC:96.70,ST:94.00,NT:95.00,VJNT:95.60,EWS:98.10', 'OPEN:99.00,OBC:98.30,SC:96.60,ST:93.80,NT:94.90,VJNT:95.50,EWS:98.00'),
# ('Sardar Patel College of Engineering (SPCE), Andheri, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous', 'Mumbai', 'Electrical Engineering', 'OPEN:98.70,OBC:98.00,SC:96.20,ST:93.50,NT:94.40,VJNT:95.10,EWS:97.70', 'OPEN:98.60,OBC:97.90,SC:96.10,ST:93.30,NT:94.30,VJNT:95.00,EWS:97.60'),
# ('Sardar Patel College of Engineering (SPCE), Andheri, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous', 'Mumbai', 'Civil Engineering', 'OPEN:98.20,OBC:97.50,SC:95.60,ST:92.80,NT:93.70,VJNT:94.40,EWS:97.10', 'OPEN:98.10,OBC:97.40,SC:95.50,ST:92.60,NT:93.60,VJNT:94.30,EWS:97.00'),
# ('Sardar Patel College of Engineering (SPCE), Andheri, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous', 'Mumbai', 'Mechanical Engineering', 'OPEN:98.40,OBC:97.70,SC:95.80,ST:93.10,NT:93.90,VJNT:94.60,EWS:97.30', 'OPEN:98.30,OBC:97.60,SC:95.70,ST:92.90,NT:93.80,VJNT:94.50,EWS:97.20');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('SVKMs Shri Bhagubhai Mafatlal Polytechnic & College of Engineering, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous, Linguistic Minority - Gujarathi', 'Mumbai', 'Computer Engineering', 'OPEN:98.90,OBC:98.10,SC:96.30,ST:93.70,NT:94.60,VJNT:95.10,EWS:97.80', 'OPEN:98.80,OBC:98.00,SC:96.20,ST:93.50,NT:94.40,VJNT:95.00,EWS:97.70'),
# ('SVKMs Shri Bhagubhai Mafatlal Polytechnic & College of Engineering, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous, Linguistic Minority - Gujarathi', 'Mumbai', 'Information Technology', 'OPEN:98.70,OBC:97.90,SC:96.00,ST:93.30,NT:94.20,VJNT:94.80,EWS:97.60', 'OPEN:98.60,OBC:97.80,SC:95.90,ST:93.10,NT:94.10,VJNT:94.70,EWS:97.50'),
# ('SVKMs Shri Bhagubhai Mafatlal Polytechnic & College of Engineering, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous, Linguistic Minority - Gujarathi', 'Mumbai', 'Electronics and Telecommunication Engineering', 'OPEN:98.40,OBC:97.60,SC:95.70,ST:92.90,NT:93.90,VJNT:94.50,EWS:97.30', 'OPEN:98.30,OBC:97.50,SC:95.60,ST:92.70,NT:93.80,VJNT:94.40,EWS:97.20'),
# ('SVKMs Shri Bhagubhai Mafatlal Polytechnic & College of Engineering, Mumbai', 'CET,JEE', 'University of Mumbai, Government-Aided, Autonomous, Linguistic Minority - Gujarathi', 'Mumbai', 'Mechanical Engineering', 'OPEN:98.10,OBC:97.40,SC:95.40,ST:92.60,NT:93.60,VJNT:94.20,EWS:97.00', 'OPEN:98.00,OBC:97.30,SC:95.30,ST:92.40,NT:93.50,VJNT:94.10,EWS:96.90');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Dr. Babasaheb Ambedkar Technological University (DBATU), Lonere', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, University', 'Raigad', 'Computer Engineering', 'OPEN:96,OBC:94,SC:88,ST:82,NT:85,VJNT:86,EWS:92', 'OPEN:95,OBC:93,SC:87,ST:81,NT:84,VJNT:85,EWS:91'),
# ('Dr. Babasaheb Ambedkar Technological University (DBATU), Lonere', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, University', 'Raigad', 'Information Technology', 'OPEN:95,OBC:93,SC:87,ST:81,NT:84,VJNT:85,EWS:91', 'OPEN:94,OBC:92,SC:86,ST:80,NT:83,VJNT:84,EWS:90'),
# ('Dr. Babasaheb Ambedkar Technological University (DBATU), Lonere', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, University', 'Raigad', 'Electronics and Telecommunication Engineering', 'OPEN:94,OBC:92,SC:86,ST:80,NT:83,VJNT:84,EWS:90', 'OPEN:93,OBC:91,SC:85,ST:79,NT:82,VJNT:83,EWS:89'),
# ('Dr. Babasaheb Ambedkar Technological University (DBATU), Lonere', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, University', 'Raigad', 'Electrical Engineering', 'OPEN:93,OBC:91,SC:85,ST:79,NT:82,VJNT:83,EWS:89', 'OPEN:92,OBC:90,SC:84,ST:78,NT:81,VJNT:82,EWS:88'),
# ('Dr. Babasaheb Ambedkar Technological University (DBATU), Lonere', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, University', 'Raigad', 'Mechanical Engineering', 'OPEN:92,OBC:90,SC:84,ST:78,NT:81,VJNT:82,EWS:88', 'OPEN:91,OBC:89,SC:83,ST:77,NT:80,VJNT:81,EWS:87'),
# ('Dr. Babasaheb Ambedkar Technological University (DBATU), Lonere', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, University', 'Raigad', 'Civil Engineering', 'OPEN:91,OBC:89,SC:83,ST:77,NT:80,VJNT:81,EWS:87', 'OPEN:90,OBC:88,SC:82,ST:76,NT:79,VJNT:80,EWS:86'),
# ('Dr. Babasaheb Ambedkar Technological University (DBATU), Lonere', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, University', 'Raigad', 'Artificial Intelligence and Machine Learning', 'OPEN:97,OBC:95,SC:89,ST:83,NT:86,VJNT:87,EWS:93', 'OPEN:96,OBC:94,SC:88,ST:82,NT:85,VJNT:86,EWS:92'),
# ('Dr. Babasaheb Ambedkar Technological University (DBATU), Lonere', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, University', 'Raigad', 'Artificial Intelligence and Data Science', 'OPEN:97,OBC:95,SC:89,ST:83,NT:86,VJNT:87,EWS:93', 'OPEN:96,OBC:94,SC:88,ST:82,NT:85,VJNT:86,EWS:92'),
# ('Dr. Babasaheb Ambedkar Technological University (DBATU), Lonere', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government, University', 'Raigad', 'Robotics and Automation', 'OPEN:96,OBC:94,SC:88,ST:82,NT:85,VJNT:86,EWS:92', 'OPEN:95,OBC:93,SC:87,ST:81,NT:84,VJNT:85,EWS:91');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Usha Mittal Institute of Technology, SNDT Womens University, Mumbai', 'CET,JEE', 'SNDT Womens University, University Managed (Un-Aided)', 'Mumbai', 'Computer Engineering', 'OPEN:89,OBC:85,SC:80,ST:74,NT:76,VJNT:78,EWS:83', 'OPEN:88,OBC:84,SC:79,ST:73,NT:75,VJNT:77,EWS:82'),
# ('Usha Mittal Institute of Technology, SNDT Womens University, Mumbai', 'CET,JEE', 'SNDT Womens University, University Managed (Un-Aided)', 'Mumbai', 'Information Technology', 'OPEN:88,OBC:84,SC:79,ST:73,NT:75,VJNT:77,EWS:82', 'OPEN:87,OBC:83,SC:78,ST:72,NT:74,VJNT:76,EWS:81'),
# ('Usha Mittal Institute of Technology, SNDT Womens University, Mumbai', 'CET,JEE', 'SNDT Womens University, University Managed (Un-Aided)', 'Mumbai', 'Electronics and Telecommunication Engineering', 'OPEN:86,OBC:82,SC:77,ST:71,NT:73,VJNT:75,EWS:80', 'OPEN:85,OBC:81,SC:76,ST:70,NT:72,VJNT:74,EWS:79'),
# ('Usha Mittal Institute of Technology, SNDT Womens University, Mumbai', 'CET,JEE', 'SNDT Womens University, University Managed (Un-Aided)', 'Mumbai', 'Electrical Engineering', 'OPEN:85,OBC:81,SC:76,ST:70,NT:72,VJNT:74,EWS:79', 'OPEN:84,OBC:80,SC:75,ST:69,NT:71,VJNT:73,EWS:78'),
# ('Usha Mittal Institute of Technology, SNDT Womens University, Mumbai', 'CET,JEE', 'SNDT Womens University, University Managed (Un-Aided)', 'Mumbai', 'Mechanical Engineering', 'OPEN:84,OBC:80,SC:75,ST:69,NT:71,VJNT:73,EWS:78', 'OPEN:83,OBC:79,SC:74,ST:68,NT:70,VJNT:72,EWS:77'),
# ('Usha Mittal Institute of Technology, SNDT Womens University, Mumbai', 'CET,JEE', 'SNDT Womens University, University Managed (Un-Aided)', 'Mumbai', 'Civil Engineering', 'OPEN:83,OBC:79,SC:74,ST:68,NT:70,VJNT:72,EWS:77', 'OPEN:82,OBC:78,SC:73,ST:67,NT:69,VJNT:71,EWS:76'),
# ('Usha Mittal Institute of Technology, SNDT Womens University, Mumbai', 'CET,JEE', 'SNDT Womens University, University Managed (Un-Aided)', 'Mumbai', 'Artificial Intelligence and Machine Learning', 'OPEN:90,OBC:86,SC:81,ST:75,NT:77,VJNT:79,EWS:84', 'OPEN:89,OBC:85,SC:80,ST:74,NT:76,VJNT:78,EWS:83'),
# ('Usha Mittal Institute of Technology, SNDT Womens University, Mumbai', 'CET,JEE', 'SNDT Womens University, University Managed (Un-Aided)', 'Mumbai', 'Artificial Intelligence and Data Science', 'OPEN:90,OBC:86,SC:81,ST:75,NT:77,VJNT:79,EWS:84', 'OPEN:89,OBC:85,SC:80,ST:74,NT:76,VJNT:78,EWS:83'),
# ('Usha Mittal Institute of Technology, SNDT Womens University, Mumbai', 'CET,JEE', 'SNDT Womens University, University Managed (Un-Aided)', 'Mumbai', 'Robotics and Automation', 'OPEN:89,OBC:85,SC:80,ST:74,NT:76,VJNT:78,EWS:83', 'OPEN:88,OBC:84,SC:79,ST:73,NT:75,VJNT:77,EWS:82');
                      

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Institute of Chemical Technology (ICT), Matunga, Mumbai', 'CET,JEE', 'Institute of Chemical Technology, Deemed University, Autonomous', 'Mumbai', 'Chemical Engineering', 'OPEN:99.20,OBC:98.50,SC:96.80,ST:94.10,NT:95.00,VJNT:95.60,EWS:98.10', 'OPEN:99.10,OBC:98.40,SC:96.70,ST:93.90,NT:94.90,VJNT:95.50,EWS:98.00'),
# ('Institute of Chemical Technology (ICT), Matunga, Mumbai', 'CET,JEE', 'Institute of Chemical Technology, Deemed University, Autonomous', 'Mumbai', 'Food Engineering and Technology', 'OPEN:98.90,OBC:98.10,SC:96.30,ST:93.70,NT:94.60,VJNT:95.10,EWS:97.80', 'OPEN:98.80,OBC:98.00,SC:96.20,ST:93.50,NT:94.40,VJNT:95.00,EWS:97.70'),
# ('Institute of Chemical Technology (ICT), Matunga, Mumbai', 'CET,JEE', 'Institute of Chemical Technology, Deemed University, Autonomous', 'Mumbai', 'Pharmaceutical Chemistry and Technology', 'OPEN:98.70,OBC:97.90,SC:96.00,ST:93.30,NT:94.20,VJNT:94.80,EWS:97.60', 'OPEN:98.60,OBC:97.80,SC:95.90,ST:93.10,NT:94.10,VJNT:94.70,EWS:97.50'),
# ('Institute of Chemical Technology (ICT), Matunga, Mumbai', 'CET,JEE', 'Institute of Chemical Technology, Deemed University, Autonomous', 'Mumbai', 'Polymer Engineering and Technology', 'OPEN:98.40,OBC:97.60,SC:95.70,ST:92.90,NT:93.90,VJNT:94.50,EWS:97.30', 'OPEN:98.30,OBC:97.50,SC:95.60,ST:92.70,NT:93.80,VJNT:94.40,EWS:97.20'),
# ('Institute of Chemical Technology (ICT), Matunga, Mumbai', 'CET,JEE', 'Institute of Chemical Technology, Deemed University, Autonomous', 'Mumbai', 'Oils, Oleochemicals and Surfactants Technology', 'OPEN:98.10,OBC:97.40,SC:95.40,ST:92.60,NT:93.60,VJNT:94.20,EWS:97.00', 'OPEN:98.00,OBC:97.30,SC:95.30,ST:92.40,NT:93.50,VJNT:94.10,EWS:96.90'),
# ('Institute of Chemical Technology (ICT), Matunga, Mumbai', 'CET,JEE', 'Institute of Chemical Technology, Deemed University, Autonomous', 'Mumbai', 'Dyestuff and Intermediate Technology', 'OPEN:97.80,OBC:97.10,SC:95.10,ST:92.30,NT:93.30,VJNT:93.90,EWS:96.70', 'OPEN:97.70,OBC:97.00,SC:95.00,ST:92.10,NT:93.20,VJNT:93.80,EWS:96.60');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Loknete Shamrao Peje Government College of Engineering, Ratnagiri', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government', 'Ratnagiri', 'Computer Science and Engineering', 'OPEN:96.40,OBC:94.80,SC:90.20,ST:84.50,NT:88.30,VJNT:89.20,EWS:95.60', 'OPEN:96.10,OBC:94.50,SC:90.00,ST:84.20,NT:88.00,VJNT:89.00,EWS:95.40'),
# ('Loknete Shamrao Peje Government College of Engineering, Ratnagiri', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government', 'Ratnagiri', 'Mechanical Engineering', 'OPEN:92.10,OBC:90.50,SC:85.30,ST:79.20,NT:82.10,VJNT:83.00,EWS:91.40', 'OPEN:91.90,OBC:90.30,SC:85.10,ST:79.00,NT:81.90,VJNT:82.90,EWS:91.20'),
# ('Loknete Shamrao Peje Government College of Engineering, Ratnagiri', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government', 'Ratnagiri', 'Civil Engineering', 'OPEN:91.40,OBC:89.20,SC:84.10,ST:78.50,NT:81.60,VJNT:82.40,EWS:90.70', 'OPEN:91.10,OBC:89.00,SC:84.00,ST:78.20,NT:81.40,VJNT:82.20,EWS:90.50'),
# ('Loknete Shamrao Peje Government College of Engineering, Ratnagiri', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government', 'Ratnagiri', 'Electrical Engineering', 'OPEN:93.20,OBC:91.50,SC:86.00,ST:80.40,NT:83.10,VJNT:84.20,EWS:92.50', 'OPEN:93.00,OBC:91.20,SC:85.80,ST:80.10,NT:82.90,VJNT:84.00,EWS:92.30'),
# ('Loknete Shamrao Peje Government College of Engineering, Ratnagiri', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Government', 'Ratnagiri', 'Artificial Intelligence and Data Science', 'OPEN:96.00,OBC:94.20,SC:89.80,ST:84.00,NT:87.80,VJNT:88.90,EWS:95.20', 'OPEN:95.80,OBC:94.00,SC:89.60,ST:83.80,NT:87.60,VJNT:88.70,EWS:95.00');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Bhartiya Vidya Bhavans Sardar Patel Institute of Technology, Andheri, Mumbai', 'CET,JEE', 'University of Mumbai, Un-Aided, Autonomous', 'Mumbai', 'Computer Engineering', 'OPEN:90,OBC:86,SC:80,ST:75,NT:78,VJNT:79,EWS:87', 'OPEN:88,OBC:84,SC:78,ST:73,NT:76,VJNT:77,EWS:85'),
# ('Bhartiya Vidya Bhavans Sardar Patel Institute of Technology, Andheri, Mumbai', 'CET,JEE', 'University of Mumbai, Un-Aided, Autonomous', 'Mumbai', 'Information Technology', 'OPEN:89,OBC:85,SC:79,ST:74,NT:77,VJNT:78,EWS:86', 'OPEN:87,OBC:83,SC:77,ST:72,NT:75,VJNT:76,EWS:84'),
# ('Bhartiya Vidya Bhavans Sardar Patel Institute of Technology, Andheri, Mumbai', 'CET,JEE', 'University of Mumbai, Un-Aided, Autonomous', 'Mumbai', 'Electronics & Telecommunication', 'OPEN:88,OBC:84,SC:78,ST:73,NT:76,VJNT:77,EWS:85', 'OPEN:86,OBC:82,SC:76,ST:71,NT:74,VJNT:75,EWS:83');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Gharda Foundations Gharda Institute of Technology, Khed, Ratnagiri', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Ratnagiri', 'Computer Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Gharda Foundations Gharda Institute of Technology, Khed, Ratnagiri', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Ratnagiri', 'Mechanical Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70'),
# ('Gharda Foundations Gharda Institute of Technology, Khed, Ratnagiri', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Ratnagiri', 'Civil Engineering', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71', 'OPEN:72,OBC:68,SC:62,ST:57,NT:60,VJNT:61,EWS:69');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Vighnaharata Trust Shivajirao S. Jondhale College of Engineering & Technology, Shahapur, Asangaon, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Computer Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Vighnaharata Trust Shivajirao S. Jondhale College of Engineering & Technology, Shahapur, Asangaon, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Information Technology', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Vighnaharata Trust Shivajirao S. Jondhale College of Engineering & Technology, Shahapur, Asangaon, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73');

                      

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Aldel Education Trust St. John College of Engineering & Management, Vevoor, Palghar', 'CET,JEE', 'University of Mumbai, Un-Aided, Autonomous, Religious Minority - Christian', 'Palghar', 'Computer Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Aldel Education Trust St. John College of Engineering & Management, Vevoor, Palghar', 'CET,JEE', 'University of Mumbai, Un-Aided, Autonomous, Religious Minority - Christian', 'Palghar', 'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Aldel Education Trust St. John College of Engineering & Management, Vevoor, Palghar', 'CET,JEE', 'University of Mumbai, Un-Aided, Autonomous, Religious Minority - Christian', 'Palghar', 'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Koti Vidya Charitable Trust Smt. Alamuri Ratnamala Institute of Engineering and Technology, Sapgaon, Tal. Shahapur', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Shahapur', 'Computer Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Koti Vidya Charitable Trust Smt. Alamuri Ratnamala Institute of Engineering and Technology, Sapgaon, Tal. Shahapur', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Shahapur', 'Information Technology', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Koti Vidya Charitable Trust Smt. Alamuri Ratnamala Institute of Engineering and Technology, Sapgaon, Tal. Shahapur', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Shahapur', 'Artificial Intelligence & Data Science', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Koti Vidya Charitable Trust Smt. Alamuri Ratnamala Institute of Engineering and Technology, Sapgaon, Tal. Shahapur', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Shahapur', 'Electronics & Telecommunication', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Koti Vidya Charitable Trust Smt. Alamuri Ratnamala Institute of Engineering and Technology, Sapgaon, Tal. Shahapur', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Shahapur', 'Mechanical Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Koti Vidya Charitable Trust Smt. Alamuri Ratnamala Institute of Engineering and Technology, Sapgaon, Tal. Shahapur', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Shahapur', 'Civil Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Yadavrao Tasgaonkar College of Engineering & Management, Bhivpuri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Computer Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Yadavrao Tasgaonkar College of Engineering & Management, Bhivpuri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Information Technology', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Yadavrao Tasgaonkar College of Engineering & Management, Bhivpuri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Artificial Intelligence & Data Science', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Yadavrao Tasgaonkar College of Engineering & Management, Bhivpuri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Electronics & Telecommunication', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70'),
# ('Yadavrao Tasgaonkar College of Engineering & Management, Bhivpuri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Mechanical Engineering', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71', 'OPEN:72,OBC:68,SC:62,ST:57,NT:60,VJNT:61,EWS:69'),
# ('Yadavrao Tasgaonkar College of Engineering & Management, Bhivpuri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Civil Engineering', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70', 'OPEN:71,OBC:67,SC:61,ST:56,NT:59,VJNT:60,EWS:68');

                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Vishnu Waman Thakur Charitable Trust VIVA Institute of Technology, Virar', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Palghar', 'Computer Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Vishnu Waman Thakur Charitable Trust VIVA Institute of Technology, Virar', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Palghar', 'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Vishnu Waman Thakur Charitable Trust VIVA Institute of Technology, Virar', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Palghar', 'Artificial Intelligence & Data Science', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Vishnu Waman Thakur Charitable Trust VIVA Institute of Technology, Virar', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Palghar', 'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Vishnu Waman Thakur Charitable Trust VIVA Institute of Technology, Virar', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Palghar', 'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Vishnu Waman Thakur Charitable Trust VIVA Institute of Technology, Virar', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Palghar', 'Electronics & Telecommunication', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Vishnu Waman Thakur Charitable Trust VIVA Institute of Technology, Virar', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Palghar', 'Computer Science & Engineering (AI)', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77');





                        
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Haji Jamaluddin Thim Trusts Theem College of Engineering, Boisar', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Palghar', 'Computer Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Haji Jamaluddin Thim Trusts Theem College of Engineering, Boisar', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Palghar', 'Information Technology', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Haji Jamaluddin Thim Trusts Theem College of Engineering, Boisar', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Palghar', 'Mechanical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Haji Jamaluddin Thim Trusts Theem College of Engineering, Boisar', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Palghar', 'Civil Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Haji Jamaluddin Thim Trusts Theem College of Engineering, Boisar', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Palghar', 'Electronics & Telecommunication', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Haji Jamaluddin Thim Trusts Theem College of Engineering, Boisar', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Palghar', 'Computer Science & Engineering (AI)', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Haji Jamaluddin Thim Trusts Theem College of Engineering, Boisar', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Palghar', 'Artificial Intelligence & Data Science', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75');

                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Mahatma Education Societys Pillai HOC College of Engineering & Technology, Tal. Khalapur, Dist. Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Malayalam', 'Raigad', 'Computer Engineering', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80'),
# ('Mahatma Education Societys Pillai HOC College of Engineering & Technology, Tal. Khalapur, Dist. Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Malayalam', 'Raigad', 'Information Technology', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('Mahatma Education Societys Pillai HOC College of Engineering & Technology, Tal. Khalapur, Dist. Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Malayalam', 'Raigad', 'Artificial Intelligence & Machine Learning', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80'),
# ('Mahatma Education Societys Pillai HOC College of Engineering & Technology, Tal. Khalapur, Dist. Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Malayalam', 'Raigad', 'Computer Science & Engineering ', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('Mahatma Education Societys Pillai HOC College of Engineering & Technology, Tal. Khalapur, Dist. Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Malayalam', 'Raigad', 'Electronics & Telecommunication', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Mahatma Education Societys Pillai HOC College of Engineering & Technology, Tal. Khalapur, Dist. Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Malayalam', 'Raigad', 'Mechanical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Mahatma Education Societys Pillai HOC College of Engineering & Technology, Tal. Khalapur, Dist. Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Malayalam', 'Raigad', 'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Leela Education Society, G.V. Acharya Institute of Engineering and Technology, Shelu, Karjat', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Computer Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Leela Education Society, G.V. Acharya Institute of Engineering and Technology, Shelu, Karjat', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Information Technology', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Leela Education Society, G.V. Acharya Institute of Engineering and Technology, Shelu, Karjat', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Artificial Intelligence and Data Science', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Leela Education Society, G.V. Acharya Institute of Engineering and Technology, Shelu, Karjat', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Artificial Intelligence and Machine Learning', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Leela Education Society, G.V. Acharya Institute of Engineering and Technology, Shelu, Karjat', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Electronics & Telecommunication', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Leela Education Society, G.V. Acharya Institute of Engineering and Technology, Shelu, Karjat', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Mechanical Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Leela Education Society, G.V. Acharya Institute of Engineering and Technology, Shelu, Karjat', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad', 'Civil Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70');

                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Vidya Prasarak Mandals College of Engineering, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Computer Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('Vidya Prasarak Mandals College of Engineering, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Vidya Prasarak Mandals College of Engineering, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Artificial Intelligence and Data Science', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Vidya Prasarak Mandals College of Engineering, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Artificial Intelligence and Machine Learning', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Vidya Prasarak Mandals College of Engineering, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Electronics & Telecommunication', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Vidya Prasarak Mandals College of Engineering, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Vidya Prasarak Mandals College of Engineering, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee) VALUES
# ('Pravin Rohidas Patil College of Engineering & Technology', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Computer Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Pravin Rohidas Patil College of Engineering & Technology', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Information Technology', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Pravin Rohidas Patil College of Engineering & Technology', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Artificial Intelligence and Data Science', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Pravin Rohidas Patil College of Engineering & Technology', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Artificial Intelligence and Machine Learning', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Pravin Rohidas Patil College of Engineering & Technology', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Electronics & Telecommunication', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Pravin Rohidas Patil College of Engineering & Technology', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Mechanical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Pravin Rohidas Patil College of Engineering & Technology', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane', 'Civil Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71');


                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Bharat College of Engineering, Kanhor, Badlapur(W)', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Computer Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Bharat College of Engineering, Kanhor, Badlapur(W)', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Information Technology', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Bharat College of Engineering, Kanhor, Badlapur(W)', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Mechanical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Bharat College of Engineering, Kanhor, Badlapur(W)', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Civil Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Bharat College of Engineering, Kanhor, Badlapur(W)', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Electronics & Telecommunication', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Bharat College of Engineering, Kanhor, Badlapur(W)', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Artificial Intelligence and Data Science', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Bharat College of Engineering, Kanhor, Badlapur(W)', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Cybersecurity', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Bharat College of Engineering, Kanhor, Badlapur(W)', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Robotics and Automation', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74');


                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Dilkap Research Institute Of Engineering and Management Studies, Neral', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Computer Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Dilkap Research Institute Of Engineering and Management Studies, Neral', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Information Technology', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Dilkap Research Institute Of Engineering and Management Studies, Neral', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Mechanical Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70'),
# ('Dilkap Research Institute Of Engineering and Management Studies, Neral', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Civil Engineering', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71', 'OPEN:72,OBC:68,SC:62,ST:57,NT:60,VJNT:61,EWS:69'),
# ('Dilkap Research Institute Of Engineering and Management Studies, Neral', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Electronics & Telecommunication', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Dilkap Research Institute Of Engineering and Management Studies, Neral', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Artificial Intelligence and Data Science', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Dilkap Research Institute Of Engineering and Management Studies, Neral', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Cybersecurity', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73');

                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Shree L.R. Tiwari College of Engineering, Mira Road', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Mumbai',
#  'Computer Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Shree L.R. Tiwari College of Engineering, Mira Road', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Mumbai',
#  'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Shree L.R. Tiwari College of Engineering, Mira Road', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Mumbai',
#  'Electronics & Telecommunication', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Shree L.R. Tiwari College of Engineering, Mira Road', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Mumbai',
#  'Artificial Intelligence and Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('Shree L.R. Tiwari College of Engineering, Mira Road', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Mumbai',
#  'Robotics and Automation', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Shree L.R. Tiwari College of Engineering, Mira Road', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Mumbai',
#  'Cybersecurity', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Shree L.R. Tiwari College of Engineering, Mira Road', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Hindi', 'Mumbai',
#  'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73');

                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('B.R. Harne College of Engineering & Technology, Ambernath', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Computer Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('B.R. Harne College of Engineering & Technology, Ambernath', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Information Technology', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('B.R. Harne College of Engineering & Technology, Ambernath', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Civil Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70'),
# ('B.R. Harne College of Engineering & Technology, Ambernath', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Mechanical Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('B.R. Harne College of Engineering & Technology, Ambernath', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Electronics & Telecommunication', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('B.R. Harne College of Engineering & Technology, Ambernath', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Artificial Intelligence & Machine Learning', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76');

                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Anjuman-I-Islams Kalsekar Technical Campus, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Raigad',
#  'Computer Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Anjuman-I-Islams Kalsekar Technical Campus, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Raigad',
#  'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Anjuman-I-Islams Kalsekar Technical Campus, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Raigad',
#  'Civil Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Anjuman-I-Islams Kalsekar Technical Campus, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Raigad',
#  'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Anjuman-I-Islams Kalsekar Technical Campus, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Raigad',
#  'Electrical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Anjuman-I-Islams Kalsekar Technical Campus, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Raigad',
#  'Artificial Intelligence and Data Science', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Anjuman-I-Islams Kalsekar Technical Campus, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Muslim', 'Raigad',
#  'Cybersecurity', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77');

                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Metropolitan Institute of Technology & Management, Sukhalwad, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Computer Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Metropolitan Institute of Technology & Management, Sukhalwad, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Information Technology', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Metropolitan Institute of Technology & Management, Sukhalwad, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Mechanical Engineering', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71', 'OPEN:72,OBC:68,SC:62,ST:57,NT:60,VJNT:61,EWS:69'),
# ('Metropolitan Institute of Technology & Management, Sukhalwad, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Civil Engineering', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70', 'OPEN:71,OBC:67,SC:61,ST:56,NT:59,VJNT:60,EWS:68'),
# ('Metropolitan Institute of Technology & Management, Sukhalwad, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Electrical Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70'),
# ('Metropolitan Institute of Technology & Management, Sukhalwad, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Artificial Intelligence and Data Science', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Metropolitan Institute of Technology & Management, Sukhalwad, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Cybersecurity', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72');

# ''')




                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Vishwatmak Jangli Maharaj Ashram Trust (Kokamthan), Atma Malik Institute Of Technology & Research', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'Kokamthan',
#  'Computer Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Vishwatmak Jangli Maharaj Ashram Trust (Kokamthan), Atma Malik Institute Of Technology & Research', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'Kokamthan',
#  'Information Technology', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Vishwatmak Jangli Maharaj Ashram Trust (Kokamthan), Atma Malik Institute Of Technology & Research', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'Kokamthan',
#  'Civil Engineering', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71', 'OPEN:72,OBC:68,SC:62,ST:57,NT:60,VJNT:61,EWS:69'),
# ('Vishwatmak Jangli Maharaj Ashram Trust (Kokamthan), Atma Malik Institute Of Technology & Research', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'Kokamthan',
#  'Mechanical Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70'),
# ('Vishwatmak Jangli Maharaj Ashram Trust (Kokamthan), Atma Malik Institute Of Technology & Research', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'Kokamthan',
#  'Electrical Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Vishwatmak Jangli Maharaj Ashram Trust (Kokamthan), Atma Malik Institute Of Technology & Research', 'CET,JEE', 'Savitribai Phule Pune University, Un-Aided', 'Kokamthan',
#  'Artificial Intelligence & Machine Learning', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74');

                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('G.M. Vedak Institute of Technology, Tala, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Computer Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('G.M. Vedak Institute of Technology, Tala, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Information Technology', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70'),
# ('G.M. Vedak Institute of Technology, Tala, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Mechanical Engineering', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70', 'OPEN:71,OBC:67,SC:61,ST:56,NT:59,VJNT:60,EWS:68'),
# ('G.M. Vedak Institute of Technology, Tala, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Civil Engineering', 'OPEN:72,OBC:68,SC:62,ST:57,NT:60,VJNT:61,EWS:69', 'OPEN:70,OBC:66,SC:60,ST:55,NT:58,VJNT:59,EWS:67'),
# ('G.M. Vedak Institute of Technology, Tala, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Electronics & Telecommunication', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71', 'OPEN:72,OBC:68,SC:62,ST:57,NT:60,VJNT:61,EWS:69'),
# ('G.M. Vedak Institute of Technology, Tala, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Artificial Intelligence and Data Science', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Universal College of Engineering, Kaman, Palghar', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Gujarathi', 'Palghar',
#  'Computer Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('Universal College of Engineering, Kaman, Palghar', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Gujarathi', 'Palghar',
#  'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Universal College of Engineering, Kaman, Palghar', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Gujarathi', 'Palghar',
#  'Electronics & Telecommunication', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Universal College of Engineering, Kaman, Palghar', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Gujarathi', 'Palghar',
#  'Mechanical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Universal College of Engineering, Kaman, Palghar', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Gujarathi', 'Palghar',
#  'Artificial Intelligence and Data Science', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80'),
# ('Universal College of Engineering, Kaman, Palghar', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Gujarathi', 'Palghar',
#  'Cybersecurity', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('Universal College of Engineering, Kaman, Palghar', 'CET,JEE', 'University of Mumbai, Un-Aided, Linguistic Minority - Gujarathi', 'Palghar',
#  'Robotics and Automation', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('VPMs Maharshi Parshuram College of Engineering, Velneshwar, Ratnagiri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Ratnagiri',
#  'Computer Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('VPMs Maharshi Parshuram College of Engineering, Velneshwar, Ratnagiri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Ratnagiri',
#  'Information Technology', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('VPMs Maharshi Parshuram College of Engineering, Velneshwar, Ratnagiri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Ratnagiri',
#  'Mechanical Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70'),
# ('VPMs Maharshi Parshuram College of Engineering, Velneshwar, Ratnagiri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Ratnagiri',
#  'Civil Engineering', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71', 'OPEN:72,OBC:68,SC:62,ST:57,NT:60,VJNT:61,EWS:69'),
# ('VPMs Maharshi Parshuram College of Engineering, Velneshwar, Ratnagiri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Ratnagiri',
#  'Electrical Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('VPMs Maharshi Parshuram College of Engineering, Velneshwar, Ratnagiri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Ratnagiri',
#  'Artificial Intelligence and Data Science', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('VPMs Maharshi Parshuram College of Engineering, Velneshwar, Ratnagiri', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Ratnagiri',
#  'Cybersecurity', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Ideal Institute of Technology, Wada, Dist. Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Computer Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Ideal Institute of Technology, Wada, Dist. Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Information Technology', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Ideal Institute of Technology, Wada, Dist. Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Mechanical Engineering', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71', 'OPEN:72,OBC:68,SC:62,ST:57,NT:60,VJNT:61,EWS:69'),
# ('Ideal Institute of Technology, Wada, Dist. Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Civil Engineering', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70', 'OPEN:71,OBC:67,SC:61,ST:56,NT:59,VJNT:60,EWS:68'),
# ('Ideal Institute of Technology, Wada, Dist. Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Electrical Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70'),
# ('Ideal Institute of Technology, Wada, Dist. Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Artificial Intelligence and Machine Learning', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Vishwaniketans Institute of Management Entrepreneurship and Engineering Technology (iMEET), Khalapur, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Computer Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Vishwaniketans Institute of Management Entrepreneurship and Engineering Technology (iMEET), Khalapur, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Information Technology', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Vishwaniketans Institute of Management Entrepreneurship and Engineering Technology (iMEET), Khalapur, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Mechanical Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Vishwaniketans Institute of Management Entrepreneurship and Engineering Technology (iMEET), Khalapur, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Civil Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Vishwaniketans Institute of Management Entrepreneurship and Engineering Technology (iMEET), Khalapur, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Artificial Intelligence and Data Science', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('Vishwaniketans Institute of Management Entrepreneurship and Engineering Technology (iMEET), Khalapur, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Cybersecurity', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Vishwaniketans Institute of Management Entrepreneurship and Engineering Technology (iMEET), Khalapur, Raigad', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Robotics and Automation', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77');

                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Yashwantrao Bhonsale Institute of Technology, Sawantwadi, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Computer Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Yashwantrao Bhonsale Institute of Technology, Sawantwadi, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Information Technology', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Yashwantrao Bhonsale Institute of Technology, Sawantwadi, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Mechanical Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Yashwantrao Bhonsale Institute of Technology, Sawantwadi, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Civil Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70'),
# ('Yashwantrao Bhonsale Institute of Technology, Sawantwadi, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Electrical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Yashwantrao Bhonsale Institute of Technology, Sawantwadi, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Artificial Intelligence & Machine Learning', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Yashwantrao Bhonsale Institute of Technology, Sawantwadi, Sindhudurg', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Sindhudurg',
#  'Robotics and Automation', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75');

              


                         





                             
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('New Horizon Institute of Technology & Management, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Computer Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('New Horizon Institute of Technology & Management, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Information Technology', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('New Horizon Institute of Technology & Management, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Artificial Intelligence and Data Science', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('New Horizon Institute of Technology & Management, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Mechanical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('New Horizon Institute of Technology & Management, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Civil Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('New Horizon Institute of Technology & Management, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Electronics and Telecommunication', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('New Horizon Institute of Technology & Management, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Cybersecurity', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('A. P. Shah Institute of Technology, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Jain', 'Thane',
#  'Computer Engineering', 'OPEN:89,OBC:85,SC:79,ST:74,NT:77,VJNT:78,EWS:86', 'OPEN:87,OBC:83,SC:77,ST:72,NT:75,VJNT:76,EWS:84'),
# ('A. P. Shah Institute of Technology, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Jain', 'Thane',
#  'Information Technology', 'OPEN:88,OBC:84,SC:78,ST:73,NT:76,VJNT:77,EWS:85', 'OPEN:86,OBC:82,SC:76,ST:71,NT:74,VJNT:75,EWS:83'),
# ('A. P. Shah Institute of Technology, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Jain', 'Thane',
#  'Artificial Intelligence and Machine Learning', 'OPEN:90,OBC:86,SC:80,ST:75,NT:78,VJNT:79,EWS:87', 'OPEN:88,OBC:84,SC:78,ST:73,NT:76,VJNT:77,EWS:85'),
# ('A. P. Shah Institute of Technology, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Jain', 'Thane',
#  'Electronics and Computer Engineering', 'OPEN:87,OBC:83,SC:77,ST:72,NT:75,VJNT:76,EWS:84', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82'),
# ('A. P. Shah Institute of Technology, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Jain', 'Thane',
#  'Electronics and Telecommunication', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80'),
# ('A. P. Shah Institute of Technology, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Jain', 'Thane',
#  'Mechanical Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('A. P. Shah Institute of Technology, Thane', 'CET,JEE', 'University of Mumbai, Un-Aided, Religious Minority - Jain', 'Thane',
#  'Civil Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Chhatrapati Shivaji Maharaj Institute of Technology, Shedung, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Computer Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Chhatrapati Shivaji Maharaj Institute of Technology, Shedung, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Information Technology', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Chhatrapati Shivaji Maharaj Institute of Technology, Shedung, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Mechanical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Chhatrapati Shivaji Maharaj Institute of Technology, Shedung, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Civil Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Chhatrapati Shivaji Maharaj Institute of Technology, Shedung, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Artificial Intelligence and Data Science', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Chhatrapati Shivaji Maharaj Institute of Technology, Shedung, Panvel', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Raigad',
#  'Cybersecurity', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Indala College of Engineering, Bapsai, Tal. Kalyan', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Computer Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Indala College of Engineering, Bapsai, Tal. Kalyan', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Information Technology', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Indala College of Engineering, Bapsai, Tal. Kalyan', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Mechanical Engineering', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72', 'OPEN:73,OBC:69,SC:63,ST:58,NT:61,VJNT:62,EWS:70'),
# ('Indala College of Engineering, Bapsai, Tal. Kalyan', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Civil Engineering', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71', 'OPEN:72,OBC:68,SC:62,ST:57,NT:60,VJNT:61,EWS:69'),
# ('Indala College of Engineering, Bapsai, Tal. Kalyan', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Electrical Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Indala College of Engineering, Bapsai, Tal. Kalyan', 'CET,JEE', 'University of Mumbai, Un-Aided', 'Thane',
#  'Artificial Intelligence and Data Science', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Devi Mahalaxmi College of Engineering and Technology', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Kolhapur',
#  'Computer Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Devi Mahalaxmi College of Engineering and Technology', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Kolhapur',
#  'Information Technology', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Devi Mahalaxmi College of Engineering and Technology', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Kolhapur',
#  'Mechanical Engineering', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74', 'OPEN:75,OBC:71,SC:65,ST:60,NT:63,VJNT:64,EWS:72'),
# ('Devi Mahalaxmi College of Engineering and Technology', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Kolhapur',
#  'Civil Engineering', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73', 'OPEN:74,OBC:70,SC:64,ST:59,NT:62,VJNT:63,EWS:71'),
# ('Devi Mahalaxmi College of Engineering and Technology', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Kolhapur',
#  'Electrical Engineering', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75', 'OPEN:76,OBC:72,SC:66,ST:61,NT:64,VJNT:65,EWS:73'),
# ('Devi Mahalaxmi College of Engineering and Technology', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Kolhapur',
#  'Artificial Intelligence and Data Science', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Devi Mahalaxmi College of Engineering and Technology', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Un-Aided', 'Kolhapur',
#  'Cybersecurity', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Government College of Engineering, Chandrapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Government', 'Chandrapur',
#  'Computer Engineering', 'OPEN:91,OBC:87,SC:81,ST:76,NT:79,VJNT:80,EWS:88', 'OPEN:89,OBC:85,SC:79,ST:74,NT:77,VJNT:78,EWS:86'),
# ('Government College of Engineering, Chandrapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Government', 'Chandrapur',
#  'Information Technology', 'OPEN:90,OBC:86,SC:80,ST:75,NT:78,VJNT:79,EWS:87', 'OPEN:88,OBC:84,SC:78,ST:73,NT:76,VJNT:77,EWS:85'),
# ('Government College of Engineering, Chandrapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Government', 'Chandrapur',
#  'Electrical Engineering', 'OPEN:88,OBC:84,SC:78,ST:73,NT:76,VJNT:77,EWS:85', 'OPEN:86,OBC:82,SC:76,ST:71,NT:74,VJNT:75,EWS:83'),
# ('Government College of Engineering, Chandrapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Government', 'Chandrapur',
#  'Mechanical Engineering', 'OPEN:87,OBC:83,SC:77,ST:72,NT:75,VJNT:76,EWS:84', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82'),
# ('Government College of Engineering, Chandrapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Government', 'Chandrapur',
#  'Civil Engineering', 'OPEN:86,OBC:82,SC:76,ST:71,NT:74,VJNT:75,EWS:83', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81'),
# ('Government College of Engineering, Chandrapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Government', 'Chandrapur',
#  'Mining Engineering', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80'),
# ('Government College of Engineering, Chandrapur', 'CET,JEE', 'Dr. Babasaheb Ambedkar Technological University, Lonere, Government', 'Chandrapur',
#  'Artificial Intelligence and Machine Learning', 'OPEN:92,OBC:88,SC:82,ST:77,NT:80,VJNT:81,EWS:89', 'OPEN:90,OBC:86,SC:80,ST:75,NT:78,VJNT:79,EWS:87');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Government College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Government', 'Nagpur',
#  'Computer Engineering', 'OPEN:95,OBC:91,SC:85,ST:80,NT:83,VJNT:84,EWS:92', 'OPEN:93,OBC:89,SC:83,ST:78,NT:81,VJNT:82,EWS:90'),
# ('Government College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Government', 'Nagpur',
#  'Information Technology', 'OPEN:94,OBC:90,SC:84,ST:79,NT:82,VJNT:83,EWS:91', 'OPEN:92,OBC:88,SC:82,ST:77,NT:80,VJNT:81,EWS:89'),
# ('Government College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Government', 'Nagpur',
#  'Electronics and Telecommunication', 'OPEN:93,OBC:89,SC:83,ST:78,NT:81,VJNT:82,EWS:90', 'OPEN:91,OBC:87,SC:81,ST:76,NT:79,VJNT:80,EWS:88'),
# ('Government College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Government', 'Nagpur',
#  'Mechanical Engineering', 'OPEN:91,OBC:87,SC:81,ST:76,NT:79,VJNT:80,EWS:88', 'OPEN:89,OBC:85,SC:79,ST:74,NT:77,VJNT:78,EWS:86'),
# ('Government College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Government', 'Nagpur',
#  'Civil Engineering', 'OPEN:90,OBC:86,SC:80,ST:75,NT:78,VJNT:79,EWS:87', 'OPEN:88,OBC:84,SC:78,ST:73,NT:76,VJNT:77,EWS:85'),
# ('Government College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Government', 'Nagpur',
#  'Electrical Engineering', 'OPEN:92,OBC:88,SC:82,ST:77,NT:80,VJNT:81,EWS:89', 'OPEN:90,OBC:86,SC:80,ST:75,NT:78,VJNT:79,EWS:87'),
# ('Government College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Government', 'Nagpur',
#  'Artificial Intelligence and Machine Learning', 'OPEN:95,OBC:91,SC:85,ST:80,NT:83,VJNT:84,EWS:92', 'OPEN:93,OBC:89,SC:83,ST:78,NT:81,VJNT:82,EWS:90');

# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Kavi Kulguru Institute of Technology & Science, Ramtek', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Computer Engineering', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('Kavi Kulguru Institute of Technology & Science, Ramtek', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Information Technology', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Kavi Kulguru Institute of Technology & Science, Ramtek', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Mechanical Engineering', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77', 'OPEN:78,OBC:74,SC:68,ST:63,NT:66,VJNT:67,EWS:75'),
# ('Kavi Kulguru Institute of Technology & Science, Ramtek', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Civil Engineering', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76', 'OPEN:77,OBC:73,SC:67,ST:62,NT:65,VJNT:66,EWS:74'),
# ('Kavi Kulguru Institute of Technology & Science, Ramtek', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Electrical Engineering', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78', 'OPEN:79,OBC:75,SC:69,ST:64,NT:67,VJNT:68,EWS:76'),
# ('Kavi Kulguru Institute of Technology & Science, Ramtek', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Artificial Intelligence and Data Science', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80'),
# ('Kavi Kulguru Institute of Technology & Science, Ramtek', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Cybersecurity', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Ankush Shikshan Sansthas G.H. Raisoni College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Computer Engineering', 'OPEN:94,OBC:90,SC:84,ST:79,NT:82,VJNT:83,EWS:91', 'OPEN:92,OBC:88,SC:82,ST:77,NT:80,VJNT:81,EWS:89'),
# ('Ankush Shikshan Sansthas G.H. Raisoni College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Information Technology', 'OPEN:93,OBC:89,SC:83,ST:78,NT:81,VJNT:82,EWS:90', 'OPEN:91,OBC:87,SC:81,ST:76,NT:79,VJNT:80,EWS:88'),
# ('Ankush Shikshan Sansthas G.H. Raisoni College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Electronics and Telecommunication', 'OPEN:91,OBC:87,SC:81,ST:76,NT:79,VJNT:80,EWS:88', 'OPEN:89,OBC:85,SC:79,ST:74,NT:77,VJNT:78,EWS:86'),
# ('Ankush Shikshan Sansthas G.H. Raisoni College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Mechanical Engineering', 'OPEN:89,OBC:85,SC:79,ST:74,NT:77,VJNT:78,EWS:86', 'OPEN:87,OBC:83,SC:77,ST:72,NT:75,VJNT:76,EWS:84'),
# ('Ankush Shikshan Sansthas G.H. Raisoni College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Civil Engineering', 'OPEN:88,OBC:84,SC:78,ST:73,NT:76,VJNT:77,EWS:85', 'OPEN:86,OBC:82,SC:76,ST:71,NT:74,VJNT:75,EWS:83'),
# ('Ankush Shikshan Sansthas G.H. Raisoni College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Artificial Intelligence and Data Science', 'OPEN:95,OBC:91,SC:85,ST:80,NT:83,VJNT:84,EWS:92', 'OPEN:93,OBC:89,SC:83,ST:78,NT:81,VJNT:82,EWS:90'),
# ('Ankush Shikshan Sansthas G.H. Raisoni College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Robotics and Automation', 'OPEN:92,OBC:88,SC:82,ST:77,NT:80,VJNT:81,EWS:89', 'OPEN:90,OBC:86,SC:80,ST:75,NT:78,VJNT:79,EWS:87');

#                       ''')
                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Bapurao Deshmukh College of Engineering, Sevagram', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Wardha',
#  'Computer Engineering', 'OPEN:70,OBC:68,SC:55,ST:56,NT:62,VJNT:63,EWS:71', 'OPEN:62,OBC:58,SC:42,ST:37,NT:50,VJNT:51,EWS:49'),
# ('Bapurao Deshmukh College of Engineering, Sevagram', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Wardha',
#  'Information Technology', 'OPEN:62,OBC:58,SC:42,ST:37,NT:50,VJNT:51,EWS:49', 'OPEN:56,OBC:57,SC:51,ST:46,NT:49,VJNT:40,EWS:58'),
# ('Bapurao Deshmukh College of Engineering, Sevagram', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Wardha',
#  'Mechanical Engineering', 'OPEN:51,OBC:47,SC:31,ST:33,NT:39,VJNT:40,EWS:58', 'OPEN:49,OBC:45,SC:39,ST:34,NT:47,VJNT:38,EWS:56'),
# ('Bapurao Deshmukh College of Engineering, Sevagram', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Wardha',
#  'Civil Engineering', 'OPEN:51,OBC:47,SC:31,ST:33,NT:39,VJNT:40,EWS:58', 'OPEN:49,OBC:45,SC:39,ST:34,NT:47,VJNT:38,EWS:56'),
# ('Bapurao Deshmukh College of Engineering, Sevagram', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Wardha',
#  'Electrical Engineering', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79', 'OPEN:80,OBC:76,SC:70,ST:65,NT:68,VJNT:69,EWS:77'),
# ('Bapurao Deshmukh College of Engineering, Sevagram', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Wardha',
#  'Artificial Intelligence and Data Science', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80');

                         
# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Priyadarshani College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Computer Engineering', 'OPEN:93,OBC:89,SC:83,ST:78,NT:81,VJNT:82,EWS:90', 'OPEN:91,OBC:87,SC:81,ST:76,NT:79,VJNT:80,EWS:88'),
# ('Priyadarshani College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Information Technology', 'OPEN:92,OBC:88,SC:82,ST:77,NT:80,VJNT:81,EWS:89', 'OPEN:90,OBC:86,SC:80,ST:75,NT:78,VJNT:79,EWS:87'),
# ('Priyadarshani College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Electronics and Telecommunication', 'OPEN:90,OBC:86,SC:80,ST:75,NT:78,VJNT:79,EWS:87', 'OPEN:88,OBC:84,SC:78,ST:73,NT:76,VJNT:77,EWS:85'),
# ('Priyadarshani College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Mechanical Engineering', 'OPEN:89,OBC:85,SC:79,ST:74,NT:77,VJNT:78,EWS:86', 'OPEN:87,OBC:83,SC:77,ST:72,NT:75,VJNT:76,EWS:84'),
# ('Priyadarshani College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Civil Engineering', 'OPEN:88,OBC:84,SC:78,ST:73,NT:76,VJNT:77,EWS:85', 'OPEN:86,OBC:82,SC:76,ST:71,NT:74,VJNT:75,EWS:83'),
# ('Priyadarshani College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Artificial Intelligence and Machine Learning', 'OPEN:94,OBC:90,SC:84,ST:79,NT:82,VJNT:83,EWS:91', 'OPEN:92,OBC:88,SC:82,ST:77,NT:80,VJNT:81,EWS:89'),
# ('Priyadarshani College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided, Autonomous, Linguistic Minority - Hindi', 'Nagpur',
#  'Robotics and Automation', 'OPEN:91,OBC:87,SC:81,ST:76,NT:79,VJNT:80,EWS:88', 'OPEN:89,OBC:85,SC:79,ST:74,NT:77,VJNT:78,EWS:86');


# INSERT INTO colleges (name, exam, university, city, branch, cutoff_cet, cutoff_jee)
# VALUES
# ('Smt. Radhikatai Pandav College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Computer Engineering', 'OPEN:85,OBC:81,SC:75,ST:70,NT:73,VJNT:74,EWS:82', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80'),
# ('Smt. Radhikatai Pandav College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Information Technology', 'OPEN:84,OBC:80,SC:74,ST:69,NT:72,VJNT:73,EWS:81', 'OPEN:82,OBC:78,SC:72,ST:67,NT:70,VJNT:71,EWS:79'),
# ('Smt. Radhikatai Pandav College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Electronics and Telecommunication', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:81,OBC:77,SC:71,ST:66,NT:69,VJNT:70,EWS:78'),
# ('Smt. Radhikatai Pandav College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Mechanical Engineering', 'OPEN:70,OBC:69,SC:62,ST:59,NT:60,VJNT:59,EWS:69', 'OPEN:68,OBC:66,SC:60,ST:55,NT:60,VJNT:58,EWS:77'),
# ('Smt. Radhikatai Pandav College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Civil Engineering',  'OPEN:70,OBC:69,SC:62,ST:59,NT:60,VJNT:59,EWS:69', 'OPEN:68,OBC:66,SC:60,ST:55,NT:60,VJNT:58,EWS:77'),
# ('Smt. Radhikatai Pandav College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Electrical Engineering', 'OPEN:83,OBC:79,SC:73,ST:68,NT:71,VJNT:72,EWS:80', 'OPEN:80,OBC:73,SC:70,ST:62,NT:67,VJNT:60,EWS:70'),
# ('Smt. Radhikatai Pandav College of Engineering, Nagpur', 'CET,JEE', 'Rashtrasant Tukadoji Maharaj Nagpur University, Un-Aided', 'Nagpur',
#  'Artificial Intelligence and Data Science', 'OPEN:86,OBC:82,SC:76,ST:70,NT:70,VJNT:71,EWS:83', 'OPEN:81,OBC:79,SC:71,ST:67,NT:72,VJNT:71,EWS:80');


           








#  ''')
    





    conn.commit()
    conn.close()
    print("Database initialized successfully!")





   





# ------------------ CONNECTION HELPERS ------------------
def get_user_connection():
    conn = sqlite3.connect(USER_DB, timeout=10, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def get_college_connection():
    conn = sqlite3.connect(COLLEGE_DB, timeout=10, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# ------------------ INITIALIZE ALL ------------------
def initialize_all():
    init_user_db()
    init_college_db()













 