Name: Shawnia Noel
ID: 101207361


This application is written in python and make use of library psycopg2 which is a python wrapper for libpq which is the official library in C to connect to postgresql server.
In order to be able to use library psycopg2, it has to be pip installed prior to runnning the application.
The newest version of psycopg2 only support python version newer than 3.6 so please make sure you have a python version no older than 3.7
More details can be found here: https://www.psycopg.org/docs/news.html#news


So prior to running the application, check the following:
    1. psycopg2 was pip installed
    2. python version is no older than python 3.7
    3. launch and log into pgAdmin4
    4. Create an empty database "Students", or you can choose any name, you would simply need to change the dbname variable in the code
    5. open the source code, q1.py and replace the following arguments with the ones that correcpond to you:
        on line 11 of program code.
        connection = psycopg2.connect(dbname= "Students", user="postgres", password = "PASSWORD", host="localhost",port="5432")
        replace arguments :dbname with the name of your database created in step 4
                          :user with the username that owns the database, by default it should be postgres
                          :password with the password of the user mentioned prior
                          :port with whichever port your localhost is running, by default it should be 5432


To run the application just run it like you normally would for any python program.
I personnally just run it in vscode like in the video demonstration though you are welcome to run anyway you are used to.

Additional documentation for library psycopg2 can be found here : https://www.psycopg.org/docs/index.html


Youtube video link: https://youtu.be/pdl46OzE0kM