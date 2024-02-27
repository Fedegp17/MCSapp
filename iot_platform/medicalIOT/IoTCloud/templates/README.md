The folder 'templates' of the application 'IoTCloud' will contain
all the html files. The HTML files can be found in the folder 'iot_temp' which means 
'iot templates'.

In oder to avoid having excesive or duplicated information in the HMLT
documents, the style (CSS) document will be in the folder 'static/css'
and a 'father' HTML will be created (base_script) which will inherit
the main structure to other documents.

Please refer to additional comments in the HTML scripts.

Regarding the TEMPLATES FOLDER:
 - Currently, there are 2 main views, the login view where the user needs to enter the user and password, and the 
   view once the user has entered. The 'Main_script.html' contains the main organization and elements that all
   the views will share, such as the SIDEBAR. Since all the views will have the sidebar because it is the main 
   menu, we can heredate this document and its content to the rest of the html scripts, so we don´t need to copy and
   paste that on every html script. Also, in case we need to update or modify the sidebar, we only need to modify 
   the mainscript, and all the views will be modified.