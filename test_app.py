import unittest
from app import app
from app_db import SupportTicket
from app_commands import create_ticket, delete_record

LOCALHOST = 'http://127.0.0.1:5000/'

#Tester Add
#tester = app.test_client(self)
#response = tester.get("/add")
#statuscode = response.status_code
#self.assertEqual(statuscode, 200)

#Tester Delete
#tester = app.test_client(self)
#response = tester.get(f'/delete/{record_id}')
#statuscode = response.status_code
#self.assertEqual(statuscode, 302)

class TicketInterfaceTestCase(unittest.TestCase):
    
    def testA_responsepage(self):
        #Tester Add
        pagelist = ["/add","/listopen","/listclosed","/signup","/login","/adminindex","/listopenadmin","/listclosedadmin"]

        tester = app.test_client(self)
        for page in pagelist:
            response = tester.get(page)
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)
    

    def testB_responseid(self):
        
        ticket_title = 'Unit Test Title'
        ticket_description = 'Test Description'
        create_ticket(ticket_title,ticket_description)
        SupportTicket.query.filter_by(ticket_title='Unit Test Title').one()
        ticketid = SupportTicket.query.filter_by(ticket_title='Unit Test Title').one().id
        page = "/update/" + str(ticketid)

        tester = app.test_client(self)
        response = tester.get(page)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        delete_record(ticketid)