
# coding: utf-8

# In[1]:

#Import Graph Lab Creat


# In[2]:

import graphlab


# In[3]:

sales=graphlab.SFrame('home_data.csv')


# In[4]:

sales


# In[5]:

#Exlporing data for housing prices


# In[6]:

#set the graph lab canvas to ipynb to show the data in the pyhton nootbook screen if you are wrinting code on nootbook
graphlab.canvas.set_target('ipynb')
sales.show(view="Scatter Plot",x="sqft_living",y="price")


# In[9]:

#we can use the scatter plot to predict sales price from square feet of living
#split the data set into training data and testing data
#seed value to be any value to be used in random generator
#.8 -> split the data  into 80 % trainign data and 20 % testing data
training_data,testing_data=sales.random_split(.8,seed= 0)


# In[10]:

#building regression model
#@param
#training_data
#target=the value you want to predict
#feateur list =features
sqft_model=graphlab.linear_regression.create(training_data,target='price',features=['sqft_living'])


# In[11]:

#evaluation the model erro
#TGet the average price of test data ,,, (mean)

print testing_data['price'].mean()


# In[13]:

#evaluate() return some statistics about the model
print sqft_model.evaluate(testing_data)
#our model has a big RMSE Value 'rmse': 255202.36355439396 ,, which mean that the model will predict some way bad

