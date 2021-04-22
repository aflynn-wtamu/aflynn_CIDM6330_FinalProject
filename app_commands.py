from flask import redirect
from app_db import SupportTicket, db, LoginCredentials
from datetime import datetime

db.create_all()

def create_ticket(ticket_title,ticket_description):
    
    new_ticket = SupportTicket(ticket_title=ticket_title,ticket_description=ticket_description)
    try:
        db.session.add(new_ticket)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error adding the ticket'


def list_records_by(listorder):
    
    if SupportTicket.query.count() != 0:
        if listorder == "open":
            listFilter = 'New'
        elif listorder == "closed":
            listFilter = 'Closed'
        else:
            return
        return SupportTicket.query.filter_by(ticket_status=listFilter).order_by(SupportTicket.date_created).all()
    else:
        return 0


def delete_record(id):
    ticket_to_delete = SupportTicket.query.get_or_404(id)
    try:
        db.session.delete(ticket_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error deleting the ticket'



def create_login(cred_user,cred_password,firstName,lastName,positionTitle,positionSpeciality):
    
    new_cred = LoginCredentials(cred_user=cred_user,cred_password=cred_password,firstName=firstName,lastName=lastName,positionTitle=positionTitle,positionSpeciality=positionSpeciality)
    try:
        db.session.add(new_cred)
        db.session.commit()
        return redirect('/adminindex')
    except:
        return 'There was an error adding the ticket'


def app_login(cred_user,cred_password):
    
    try:
        user = LoginCredentials.query.filter_by(cred_user=cred_user).first().cred_user
    except:
        return 'Invalid Username'
    
    try:
        password = LoginCredentials.query.filter_by(cred_password=cred_password).first().cred_password
    except:
        return 'Invalid Password'
    
    #return redirect('/adminindex')
    return True


def update_record(id,ticket_status,update_note):
    ticket = SupportTicket.query.get_or_404(id)
    ticket.ticket_status = ticket_status
    ticket.update_note = update_note
    ticket.date_updated = datetime.utcnow()

    try:
        db.session.commit()
        return redirect('/adminindex')
    except:
        return 'There was an error adding the ticket'
