# kiranalogy

#Installation

# Full analysis url- http://localhost:8000/gross-analysis/

# Landing page url- http://localhost:8000

#Linux Based Setup For Registration_Module development
Note: Ubuntu 14.04 or Ubuntu 16.04 LTS is recommended to be used.

1. Refresh your apt package index
    
   sudo apt-get update

2. Now, install pip using Python Version 2
   
   sudo apt-get install python-pip
   
3. Upgrade the pip for latest version
   
   pip install -U pip

4. After installing pip , install the dependencies

   pip install -r requirements.txt

5. Now, clone the repository

   https://github.com/aakarshgoel96/kiranalogy.git

5. Move to the project directory.

   cd kiranalogy
   
6. Place the file https://drive.google.com/open?id=0B1nE0jfVT8AbOV9jX29DQjdrMzg into muse Folder and rename it with musedb.csv

7. You are all set to run the development server

   python manage.py runserver

8. Visit [http://localhost:8000][localhost] in your browser & you are all set.
   [localhost]: http://localhost:8000/


We have added the database file(db.sqlite3), So there is not need to setup the database
