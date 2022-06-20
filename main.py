from flask import render_template
from flask import Flask
import ldclient
from ldclient.config import Config



app = Flask(__name__, template_folder='templates')
app._static_folder = ''

user = {
    "key": "aa0ceb", 
    "firstName": "Dennis",
    "lastName": "Pong", 
    "email": "dennis.pong@gmail.com",
    "custom": {
     "groups": ["Jedi"]   
    }
    

}

@app.route("/")
def get_feature():
    ldclient.set_config(Config("sdk-50f8b453-0734-410d-bb4d-ce0efe4bb850"))
    
    flag_value = ldclient.get().variation("launchTheme", user, False)
    
    if flag_value == True: 
        
        show_input = ldclient.get().variation("launchInput", user, "warnings.png")
        print(show_input)
        ldclient.get().close()
    
        return render_template("home.html", input = show_input)
   
    else:
        ldclient.get().close()
        return """ <h1> Welcome to LaunchDarkly</h1> """
    
    
if __name__ == '__main__':
    app.run(debug = True)
    
    