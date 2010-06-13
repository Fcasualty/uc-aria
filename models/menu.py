# -*- coding: utf-8 -*- 

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
response.subtitle = T('customize me!')

##########################################
## this is the main application menu
## add/remove items as required
##########################################



response.menu_aria = [
   [T('Home'), False, URL(request.application,'default','index'), []],
   [T('About Us'), False, URL(request.application,'nous','index'), []],
   [T('Our Managment Team'), False, URL(request.application,T('dirigeants'),'index'), []],
   [T('Our Expertise'), False, URL(request.application,T('expertise'),'index'), []],
   [T('Our Work'), False, URL(request.application,'realisations','index'), []],
   [T('Careers'), False, URL(request.application,'carrieres','index'), []],
   [T('Request an Estimate'), False, URL(request.application,'soumission','index'), []],
   [T('Contact Us'), False, URL(request.application,'contact','index'), []],
]

response.menu = [
    [T('Index'), False, 
     URL(request.application,'default','index'), []],
    ]

response.menu_language = [
   [T('Language'), False, URL(request.application,T('language'),'index'), []],
   [T('Language'), False, URL(request.application,T('language'),'index'), []],
   [T('Language'), False, URL(request.application,T('language'),'index'), []],
]

##########################################
## this is here to provide shortcuts
## during development. remove in production 
##########################################

response.menu_edit=[
  [T('Edit'), False, URL('admin', 'default', 'design/%s' % request.application),
   [
            [T('Controller'), False, 
             URL('admin', 'default', 'edit/%s/controllers/default.py' \
                     % request.application)],
            [T('View'), False, 
             URL('admin', 'default', 'edit/%s/views/%s' \
                     % (request.application,response.view))],
            [T('Layout'), False, 
             URL('admin', 'default', 'edit/%s/views/layout.html' \
                     % request.application)],
            [T('Stylesheet'), False, 
             URL('admin', 'default', 'edit/%s/static/base.css' \
                     % request.application)],
            [T('DB Model'), False, 
             URL('admin', 'default', 'edit/%s/models/db.py' \
                     % request.application)],
            [T('Menu Model'), False, 
             URL('admin', 'default', 'edit/%s/models/menu.py' \
                     % request.application)],
            [T('Database'), False, 
             URL(request.application, 'appadmin', 'index')],
            ]
   ],
  ]
