# LaunchDarklyDemo

## Table of contents
* [Select an environment and SDK](#LaunchDarkly-Basics)
* [Select or create a flag](#Feature-Flag)
* [Application](#application)
* [Demo](#demo)

## Select an environment and SDK

First, install the LaunchDarkly SDK as a dependency in your application
```
# shell
>pip install launchdarkly-server-sdk

```


Then you want to start off by clicking on the magnifying glass icon on the top right of your screen to look for "Install SDK". 

<img width="671" alt="image" src="https://user-images.githubusercontent.com/30054892/174505770-f08e4eb7-d5fc-411b-b806-f0ad45d377e8.png">

Then Connect an SDK screen will pop up. 

<img width="1030" alt="image" src="https://user-images.githubusercontent.com/30054892/174505828-f3f24df4-3419-4339-a39e-4f17559ddaa4.png">

You can then select the proper environment and SDK. 
	
## Select or create a flag

Now that you have a proper environment with a SDK selected. You would like to create (or select) a feature flag. 

Follow the steps 

1) Navigate to the Feature Falgs tab. 

2) Click on Create Flag button to start building your flag. 

![image](https://user-images.githubusercontent.com/30054892/174506432-b873ed76-36f3-425a-a558-e625c7f7fdf2.png)

Note: See the Demo video in the final section to understand on how to successfully configure a flag.

After you create a feature flag, you can just simply select it at the Connect an SDK screen, and you can click "save and continue"

<img width="1043" alt="image" src="https://user-images.githubusercontent.com/30054892/174506971-004d3be8-f30c-425a-a62b-e029018e0f59.png">


## Application

Now that you have completed the first 2 steps in the "Connect an SDK" screen, you can now find your SDK key in section 3. See the purple box below.

![image](https://user-images.githubusercontent.com/30054892/174507121-cdd6e170-6c44-4463-9c25-20d9db7adea6.png)


Here is a code snippet where you can use to test out your feature flag implementations. 

```
# main.py 

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

```

The end goal of this step is to test out the feature flags that you have implemented. If you need a step-by-step demo, please go straight to the demo section to visualize the sequence of steps in the video provided.


Some important building blocks that I'd like to shed a light on: 

To initialize the LD client with SDK key, you can do the following: 

```
# plug in SDK-key below
ldclient.set_config(Config("[SDK-key]"))
```

Let's say if you have a feature flag with a string "launchTheme", you can call LaunchDarkly ( _ldclient.get().variation()_ )  with it to evaluate its value. 

```
ldclient.get().variation("launchTheme", user, False)
```

and you want to make sure SDK shuts down cleanly and has a chance to deliver analytics vents to LaunchDarkly before the program exits. Otherwise, the SDK would continue running and events would be delivered automatically in the background.

To do that, you can insert the following code to close the LD client. 
```
ldclient.get().close()
```




## Demo
