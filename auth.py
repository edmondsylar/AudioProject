import streamlit as st
from tinydb import TinyDB, Query
import os
import streamlit_extras as ste

# we are going to create simple authentication class for the application.


class Auth:
    def __init__(self, username, password):
        self.user = username
        self.password = password

        self.logedIn = False
        
        # create the database
        if not os.path.exists('auth_db.json'):
            db = TinyDB('auth_db.json')

        self.auth_table = db.table('authentication')

    def login(self):
        User = Query()
        result = self.auth_table.search((
                User.user == self.user) & (User.password == self.password
            ))
        if result:
            st.session_state['AuthUser'] = self.user

            self.logedIn = True
            return self.logedIn
        else:
            return self.logedIn

    def logout(self):
        st.session_state['AuthUser'] = None
        self.logedIn = False
        # clean up the session.
        if st.session_state['replicate_key']:
            st.session_state['replicate_key'] = None
