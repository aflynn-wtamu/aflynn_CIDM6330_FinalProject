from flask import render_template, request, redirect
from app_db import app, SupportTicket
from app_commands import list_records_by, delete_record, create_ticket, create_login, app_login, update_record

@app.route('/')
def index():
    return render_template('index.html')


# Add Action
@app.route('/add', methods=['GET','POST'])
def create():
    if request.method=='POST':
        return create_ticket(request.form['title'],request.form['description'])
    else:
        return render_template('methods/add.html')


# List by date action
@app.route('/listopen')
def listopen():
    tickets = list_records_by('open')
    if tickets is None:
        return 'There was an error displaying the tickets'
    elif tickets == 0:
        return 'There are no tickets to display'
    else:
        return render_template('methods/listopen.html', tickets=tickets)


# List by title action
@app.route('/listclosed')
def listclosed():
    tickets = list_records_by('closed')
    if tickets is None:
        return 'There was an error displaying the tickets'
    elif tickets == 0:
        return 'There are no tickets to display'
    else:
        return render_template('methods/listclosed.html', tickets=tickets)


# Delete action
@app.route('/delete/<int:id>')
def delete(id):
    return delete_record(id)


# ----- Admin Tools -----

# Create Login
@app.route('/signup', methods=['GET','POST'])
def loginindex():
    if request.method=='POST':
        return create_login(request.form['user'],request.form['password'],request.form['firstName'],request.form['lastName'],request.form['positionTitle'],request.form['positionSpeciality'])
    else:
        return render_template('methods/signup.html')


# Log Into App
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        if app_login(request.form['user'],request.form['password']):
            redirect('/adminindex')
    else:
        return render_template('methods/login.html')


# Open Admin View
@app.route('/adminindex')
def adminindex():
    return render_template('methods/adminindex.html')


# List by date action
@app.route('/listopenadmin')
def listopenadmin():
    tickets = list_records_by('open')
    if tickets is None:
        return 'There was an error displaying the tickets'
    elif tickets == 0:
        return 'There are no tickets to display'
    else:
        return render_template('methods/listopenadmin.html', tickets=tickets)


# List by title action
@app.route('/listclosedadmin')
def listclosedadmin():
    tickets = list_records_by('closed')
    if tickets is None:
        return 'There was an error displaying the tickets'
    elif tickets == 0:
        return 'There are no tickets to display'
    else:
        return render_template('methods/listclosedadmin.html', tickets=tickets)


# Update action
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    ticket = SupportTicket.query.get_or_404(id)
    
    if request.method=='POST':
        return update_record(id,request.form['status'],request.form['note'])
    else:
        return render_template('methods/update.html', ticket=ticket)

if __name__ == "__main__":
    app.run(debug=True)
