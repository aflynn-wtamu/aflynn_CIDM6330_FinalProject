import unittest
from app_db import SupportTicket, db, LoginCredentials
from datetime import datetime


class TicketDatabaseTestCase(unittest.TestCase):
    
    def testA_addticket_db(self):
        ticket_status = 'New'
        ticket_title = 'Unit Test Title'
        ticket_description = 'Test Description'
        new_ticket = SupportTicket(ticket_status=ticket_status,ticket_title=ticket_title,ticket_description=ticket_description)
        try:
            db.session.add(new_ticket)
            db.session.commit()
            pass
        except:
            self.fail('There was an error adding the ticket')
    

    def testB_updateticket_db(self):
        ticket_to_update = SupportTicket.query.filter_by(ticket_title='Unit Test Title').one()
        ticket_to_update.ticket_status = 'Closed'
        ticket_to_update.update_note = 'Update Note Added'
        ticket_to_update.date_updated = datetime.utcnow()

        try:
            db.session.commit()
            pass
        except:
            self.fail('There was an error updating the ticket')
    

    def testC_deleteticket_db(self):
        ticket_to_delete = SupportTicket.query.filter_by(ticket_title='Unit Test Title').one()

        try:
            db.session.delete(ticket_to_delete)
            db.session.commit()
            pass
        except:
            self.fail('There was an error deleting the ticket')


class UserDatabaseTestCase(unittest.TestCase):
    
    def testA_adduser_db(self):
        cred_user = 'usernametest'
        cred_password = 'password'
        firstName = 'Test Firstname'
        lastName = 'Test Lastname'
        positionTitle = 'Test Tier One Support Specialist'
        positionSpeciality = 'Test Desktop Support'
        new_user = LoginCredentials(cred_user=cred_user,cred_password=cred_password,firstName=firstName,lastName=lastName,positionTitle=positionTitle,positionSpeciality=positionSpeciality)
        try:
            db.session.add(new_user)
            db.session.commit()
            pass
        except:
            self.fail('There was an error adding the user')
    

    def testB_updateuser_db(self):
        ticket_to_update = LoginCredentials.query.filter_by(cred_user='usernametest').one()
        cred_user = 'usernametestupdate'
        cred_password = 'passwordupdate'
        firstName = 'Test Firstname update'
        lastName = 'Test Lastname update'
        positionTitle = 'Test Tier Two Support Specialist'
        positionSpeciality = 'Test Enterprise Support'

        try:
            db.session.commit()
            pass
        except:
            self.fail('There was an error updating the user')
    

    def testC_deleteuser_db(self):
        ticket_to_delete = LoginCredentials.query.filter_by(cred_user='usernametest').one()

        try:
            db.session.delete(ticket_to_delete)
            db.session.commit()
            pass
        except:
            self.fail('There was an error deleting the user')