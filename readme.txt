This Url Shortening Project is done on Django framework with the Programming language of 
Python with html,css & Bootstrap for the View.

The Project is hosted on http://ayush1995.pythonanywhere.com/ and is live right now.
The webserver for the same is Nginx and hosted on pythonanywhere.com.
The database is SqLite DB which uses to store the Long and Short Urls and Riderections for same.

The Basic approach was to GET the Long Url in DB, Generate the Random  short Url in lowercase and 0-9 digits and then assign the same for that 
particular long URL and POST the short Url on the Home (VIEW) with the link available of shortened URL which on click can be redirected to the Original website.
The Shortened Url along with Long URL remains save in DB and you can Use it by anytime Visiting the site.

I think this is the best approach because it is so simple and not complicated in the Django framework to develop such a thing.
I could have done the same with PHP but i find this one more simple and interested.

My future Plan would be to create a login session so that personalised shortened url can be used 
frequently by person to person.

-----------------------------------FOR SETUP AND INSTALLATION----------------------------

1. Download the zip file to your system.
2. Create mkdir Project_name && cd Project_name in command prompt in the folder you want to create the project.
3. Once you are in that directory install virtualenvironment by command "virtualenv ." (without the quotes)
4. Install nginx for this project 
5. Run the commands MakeMigration and migrate for this project (if done any changes in model)
6. Run the server for this project by "python manage.py runserver" command 
7. Goto 127.0.0.1 (localhost) and Enjoy!!
