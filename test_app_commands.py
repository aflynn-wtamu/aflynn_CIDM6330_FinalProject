import unittest
from app_db import SupportTicket, db, LoginCredentials
from app_commands import list_records_by, delete_record, create_ticket, create_login, app_login, update_record

class TicketCommandsTestCase(unittest.TestCase):
    
    def testA_addticket(self):
        ticket_title = 'Unit Test Title'
        ticket_description = 'Test Description'

        try:
            create_ticket(ticket_title,ticket_description)
            SupportTicket.query.filter_by(ticket_title='Unit Test Title').one()
            pass
        except:
            self.fail('There was an error adding the ticket')
    

    def testB_listticket(self):
        ticketcount = len(SupportTicket.query.filter_by(ticket_status='New').all())
        
        listorder = "open"
        testticketcount = len(list_records_by(listorder))

        self.assertEqual(ticketcount,testticketcount)
    

    def testC_updateticket(self):
        ticket_to_update = SupportTicket.query.filter_by(ticket_title='Unit Test Title').one()

        try:
            update_record(ticket_to_update.id,'Closed','Update Note Added')
            SupportTicket.query.filter_by(ticket_title='Unit Test Title',ticket_status='Closed').one()
            pass
        except:
            self.fail('There was an error updating the ticket')
    

    def testD_listticket(self):
        ticketcount = len(SupportTicket.query.filter_by(ticket_status='Closed').all())
        
        listorder = "closed"
        testticketcount = len(list_records_by(listorder))

        self.assertEqual(ticketcount,testticketcount)
    

    def testE_deleteticket(self):
        ticket_to_delete = SupportTicket.query.filter_by(ticket_title='Unit Test Title').one()
        expected_count = len(SupportTicket.query.all())-1

        try:
            delete_record(ticket_to_delete.id)
            self.assertEqual(len(SupportTicket.query.all()),expected_count)
        except:
            self.fail('There was an error deleting the ticket')
            
            

class UserCommandsTestCase(unittest.TestCase):
    
    def testA_adduser_db(self):
        cred_user = 'usernametest'
        cred_password = 'password'
        firstName = 'Test Firstname'
        lastName = 'Test Lastname'
        positionTitle = 'Test Tier One Support Specialist'
        positionSpeciality = 'Test Desktop Support'
        
        try:
            create_login(cred_user,cred_password,firstName,lastName,positionTitle,positionSpeciality)
            login_to_delete = LoginCredentials.query.filter_by(cred_user='usernametest').one()
            db.session.delete(login_to_delete)
            db.session.commit()
            pass
        except:
            self.fail('There was an error adding the user')

    
    def testB_login(self):
        cred_user = 'usernametest'
        cred_password = 'password'
        firstName = 'Test Firstname'
        lastName = 'Test Lastname'
        positionTitle = 'Test Tier One Support Specialist'
        positionSpeciality = 'Test Desktop Support'
        create_login(cred_user,cred_password,firstName,lastName,positionTitle,positionSpeciality)

        if app_login(cred_user,cred_password):
            login_to_delete = LoginCredentials.query.filter_by(cred_user='usernametest').one()
            db.session.delete(login_to_delete)
            db.session.commit()
            pass
        else:
            self.fail('There was an error validating the user')