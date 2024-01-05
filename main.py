
from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import psycopg2.extras

# create application route
app = Flask(__name__)

# create database connection
conn = psycopg2.connect(
    host="localhost",
    database="olympics_db",
    user="postgres",
    password="admin")
cur = conn.cursor()

@app.route('/')
def Homepage():
   return render_template('Homepage.html')

# create a route

@app.route('/insert_sports')
def forms():
    return render_template('insert_sports.html')

# add post method
@app.route('/insert_sports', methods=['POST'])
def show_sports_post():
    player_id = request.form['player_id']
    sports_name =  request.form['sports_name']
    location = request.form['location']
    year =  request.form['year']
    print(player_id, sports_name, location, year)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("INSERT INTO olympics_db.sports (player_id, sports_name, location, year) VALUES (%s, %s, %s, %s)", (player_id, sports_name, location, year))
    conn.commit()
    
    return(redirect(url_for('display')))

# display data from database
@app.route('/show_sports')
def display():
    cur = conn.cursor()
    cur.execute("SELECT * FROM olympics_db.sports")
    rows = cur.fetchall()
    return (render_template('show_sports.html', rows=rows))


# add post method

   

@app.route('/delete_sports', methods=['POST','GET'])

def delete_sports_post():
    if request.method == 'GET':
        return(render_template('delete_sports.html'))
    else:
        player_id = request.form['player_id']
        sports_name =  request.form['sports_name']
        location = request.form['location']
        year =  request.form['year']
        print(player_id, sports_name, location, year)
        cur = conn.cursor()
        cur.execute("delete from  olympics_db.sports  where player_id=%s and sports_name=%s and location=%s and year = %s ", (player_id, sports_name, location, year))
    # database specific query
    conn.commit()
    return redirect(url_for('display'))





@app.route('/insert_player')
def forms_fun():
    return render_template('insert_player.html')

# add post method
@app.route('/insert_player', methods=['POST'])
def show_player_post():
    player_id =  request.form['player_id']
    first_name =  request.form['first_name']
    last_name =  request.form['last_name']
    gender =  request.form['gender']
    height =  request.form['height']
    weight =  request.form['weight']
    dob =  request.form['dob']
    print(player_id, first_name,last_name,gender,height,weight,dob)
    cur = conn.cursor()
    cur.execute("INSERT INTO olympics_db.player (player_id, first_name,last_name,gender,height,weight,dob) VALUES (%s, %s, %s , %s, %s, %s, %s)", (player_id, first_name,last_name,gender,height,weight,dob ))
    # database specific query
    conn.commit()
    return redirect(url_for('displayplayer'))

# display data from database
@app.route('/show_player')
def displayplayer():
    cur = conn.cursor()
    cur.execute("SELECT * FROM olympics_db.player")
    rows = cur.fetchall()
    return (render_template('show_player.html', rows=rows))

# add post method
@app.route('/edit_player', methods=['POST','GET'])

def edit_player_post():
    if request.method == 'GET':
        return(render_template('edit_player.html'))
    else:
        player_id =  request.form['player_id']
        first_name =  request.form['first_name']
        last_name =  request.form['last_name']
        gender =  request.form['gender']
        height =  request.form['height']
        weight =  request.form['weight']
        dob =  request.form['dob']
        print(player_id, first_name,last_name,gender,height,weight,dob)
        cur = conn.cursor()
        cur.execute("update olympics_db.player set first_name = %s ,last_name = %s, gender=%s, height=%s, weight=%s, dob=%s where player_id = %s ", (first_name,last_name,gender,height,weight,dob,player_id))
        # database specific query
        conn.commit()
        return redirect(url_for('displayplayer'))

@app.route('/edit_sports', methods=['POST','GET'])

def edit_sports_post():
    if request.method == 'GET':
        return(render_template('edit_sports.html'))
    else:
        player_id =  request.form['player_id']
        sports_name =  request.form['sports_name']
        location =  request.form['location']
        year =  request.form['year']
        print(player_id, sports_name,location,year)
        cur = conn.cursor()
        cur.execute("update olympics_db.sports set player_id = %s, sports_name = %s ,location = %s, year=%s where player_id = %s ", (player_id, sports_name,location,year))
        # database specific query
        conn.commit()
        return redirect(url_for('displayplayer'))

@app.route('/delete_player', methods=['POST','GET'])
def delete_player_post():
    if request.method == 'GET':
        return(render_template('delete_player.html'))
    else:
            player_id =  request.form['player_id']
            first_name =  request.form['first_name']
            last_name =  request.form['last_name']
            gender =  request.form['gender']
            height =  request.form['height']
            weight =  request.form['weight']
            dob =  request.form['dob']
            print(player_id, first_name,last_name,gender,height,weight,dob)
            cur = conn.cursor()
            cur.execute("delete from  player  where player_id=%s and first_name = %s and last_name = %s and gender=%s and height=%s and weight=%s and dob=%s", (player_id, first_name,last_name,gender,height,weight,dob))
    # database specific query
            conn.commit()
            return redirect(url_for('displayplayer'))


@app.route('/runquerysports')
def runquerysports_post():
     
            
            cur = conn.cursor()
            cur.execute("select sports_name ,player_id ,year ,location  from olympics_db.sports where year > 2000 ")
    # database specific query
            rows = cur.fetchall()
            return (render_template('runquerysports.html', rows=rows))

@app.route('/runqueryplayer')       
def runqueryplayer_post():
    
    cur = conn.cursor()
    cur.execute("SELECT player_id , first_name, last_name, gender, height, weight  from olympics_db.player order by height")
    # database specific query
    rows = cur.fetchall()
    return (render_template('runqueryplayer.html', rows=rows))

# run the application
if __name__ == '__main__':
    app.run(debug=True)