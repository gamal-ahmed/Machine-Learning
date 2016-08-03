# House price predcitor 


predicting house prices, by creating models that predict a continuous value (price) from input features (square footage).
This is just one of the many places where regression can be applied.Other applications range from predicting health outcomes in medicine, stock prices in finance, and power usage in high-performance computing, to analyzing which regulators are important for gene expression.

how to analyze the performance of your predictive model and implement regression in practice using an iPython notebook.


# Install
- Install [python](https://www.python.org/downloads/) 
- Download and install iPython notebook. follow instructions [here](https://ipython.org/ipython-doc/2/install/install.html)
- install GraphLab Create from [here](https://turi.com/download/install-graphlab-create-command-line.html).

# Code

Import Graph Lab Creat

    import graphlab
Load houses data set to be used in building our model

    sales=graphlab.SFrame('home_data.csv')

Print out the sales variable you have to see something like that :

    sales
   ![Houses data set](https://s31.postimg.org/4abgml2uj/Capture.png)

the data set includes alot of features but here we will predict in our model using sqft_living feature only.

Visualising data for housing prices

    #set the graph lab canvas to ipynb to show the data in the pyhton nootbook screen if you are writing code on Ipython nootbook
    graphlab.canvas.set_target('ipynb')sales.show(view="Scatter Plot",x="sqft_living",y="price")

![enter image description here](https://s32.postimg.org/osbzk9p5x/scatter_sqft_living_price.png)

  Split the data set into training data and testing data

    #we can use the scatter plot to predict sales price from square feet of living
    #seed value to be any value to be used in random generator
    #.8 -> split the data  into 80 % trainign data and 20 % testing data
    
    training_data,testing_data=sales.random_split(.8,seed= 0)


 Building the  regression model
 
   

     #@param
        #training_data
        #target=the value you want to predict
        #feateur list =features
        sqft_model=graphlab.linear_regression.create(training_data,target='price',features=['sqft_living'])

Evaluation the model

    #Get the average price of test data ,,, (mean)
    
    print testing_data['price'].mean()
    543054.042563

`evaluate()` return some statistics about the model

    print sqft_model.evaluate(testing_data)
    {'max_error': 4140864.0864752606, 'rmse': 255202.36355439396}
Our model has a big RMSE Value 'rmse': 255202.36355439396 ,, which mean that the model will predict some way bad
