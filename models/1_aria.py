# coding: utf8
#########################################################################
# Aria Default Setting
#########################################################################
# Location                    : models/1_aria.py
# Corresponding controller    : controllers/aria.py
#
# Organization                : TBD
# Author                      : Christopher Steel
# Copyright                   : 2010
# Contributors                :
# Last Changes                : 2010-02-11
#
# Description : 1_aria.py contains our default aria settings and the code
# for changing the value of our session variable. Disabling aria has no
# effect as only aria enabled menus have been created for this
# applicationas of 2010-02-11.
# 
if not session._aria: session._aria = 'True'
# If I set request.vars._aria via the controller to 'True' or 'False'
# my new setting gets save to session._aria here.
if request.vars._aria:
    session._aria = request.vars._aria
