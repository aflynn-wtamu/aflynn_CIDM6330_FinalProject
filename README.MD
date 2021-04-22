# Support Ticket App 

# Application Setup

Please use the following steps to setup the application:

* **Setup the Virtual Environment**
    * Open a command terminal using **bash**
    * Create the virtual environment and **install flask**
        ``` bash
        # create venv folder and virtual environment
        py -m venv venv

        # activate virtual environment
        . venv/Scripts/activate

        # install Flask
        pip install Flask

        # install python and activate .env file
        pip install python-dotenv
        ```


# Run Application

Please use the following steps to run the application:

* **Open Terminal and Run app.py**
    * Open a command terminal using **bash**
    * Run app.py using python
        ``` bash
        py app.py
        ```

# Run Tests

Please use the following steps to test the application:

* **Open Terminal and Run Test Commands**
    * Open a command terminal using **bash**
    * Activate the **virtual environment**
        ``` bash
        . venv/Scripts/activate
        ```
    * Run unittest commands using python
        ``` bash
        # Database Tests
        py -m unittest -v test_app_db.TicketDatabaseTestCase
        py -m unittest -v test_app_db.UserDatabaseTestCase

        # Commands Test
        py -m unittest -v test_app_commands.TicketCommandsTestCase
        py -m unittest -v test_app_commands.UserCommandsTestCase

        # Interface Test
        py -m unittest -v test_app.TicketInterfaceTestCase
        ```