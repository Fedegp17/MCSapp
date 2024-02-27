
"""To begin, we can check the scripts 'views' and 'urls' of this folder. The 'urls.py' script contains all the
   information of the paths or urls that the application will be using. All the posible urls that the users can access
   will be listed in that script

   Moving forward, the script 'views.py' will be the responsible for rendering the view (the front end response) that
   the user will be seing on his side.

   Regarding the STATIC FOLDER:
     - The images can be found in the Google Drive, it is not a good practice to include images in a GitHub
       repository
     - The CSS folder contains the cascade style sheets used for the fronend of the server
     - The js folder contains all the JavaScript scripts, although currently it is empty

   Regarding the TEMPLATES FOLDER:
     - Currently there are 2 main views, the login view where the user needs to enter the user and password, and the
       view once the user has entered. The 'Main_script.html' contains the main organization and elements that all
       the views will share, such as the SIDEBAR. Since all the views will have the sidebar because it is the main
       menu, we can heredate this document and its content to the rest of the html scripts, so we don´t need to copy and
       paste that on every html script. Also, in case we need to update or modify the sidebar, we only need to modify
       the mainscript, and all the views will be modified.
   """
