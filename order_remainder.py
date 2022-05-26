import pandas as pd
import numpy as np 
import smtplib as s

#You Can Exclude Numpy since the program works all good without numpy also. This will decrease your program run time
# In[37]:

#Enter You excel file directory path in the data frame
df = pd.read_excel('E:\Date.xlsx', names=['Date','Address']) # names = [This are the column names]
df['Date'] = df['Date'].dt.date   # Since python data read date in timestramp format so, it is convert into datetime


# In[35]:


df.head() # Just to show the first few columns or rows 



# In[59]:


import datetime as dt
cdate = dt.date.today()
tdate = dt.timedelta(days=14)
renewal = cdate + tdate
k = renewal.strftime('%B %d %Y')    #Its is used for formatting the default datetime into string format


# In[61]:


for i in range(0,len(df['Date'])):
    if df.loc[i, 'Date'] == renewal:
        remainder()          # Calling the Function 


# In[60]:


def remainder():
    ob=s.SMTP('smtp.gmail.com',587)
    ob.starttls()
    
    ob.login('your_email','your_email_password')
    
    subject = 'Upcoming Refilling',
    body= 'Hey, another service is waiting for you', df.loc[i],k
    message= 'Subject:{}\n\n{}'.format(subject,body)
    ob.sendmail('your_email_address','destination_email_address',message)
    print('done')

    



