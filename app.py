#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def index(): 
    if request.method == "POST":
        DPS = request.form.get("DPS")
        NetIncomeGrowth = request.form.get("NetIncomeGrowth")
        ShareholdersEquityGrowth = request.form.get("ShareholdersEquityGrowth")

      
        model = joblib.load("EquityREG")
        pred = model.predict([[float(DPS),float(NetIncomeGrowth),float(ShareholdersEquityGrowth)]])
        s1 = "The equity class based on Linear Regression model is : " + str(pred)
        
        model = joblib.load("EquityDT")
        pred = model.predict([[float(DPS),float(NetIncomeGrowth),float(ShareholdersEquityGrowth)]])
        s2 = "The equity class based on Decision Tree model is : " + str(pred)
        
        
        model = joblib.load("EquityNN")
        pred = model.predict([[float(DPS),float(NetIncomeGrowth),float(ShareholdersEquityGrowth)]])
        s3 = "The equity class based on Neural Network model is : " + str(pred)
        
        return(render_template("index.html", result1=s1, result2=s2, result3=s3))
    else: 
          return(render_template("index.html", result1="2", result2="2", result3="2"))
        


# In[ ]:


if __name__=="__main__":
    
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




