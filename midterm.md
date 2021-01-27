# Traffic Predictions with Uber Ride Data - Midterm Report
Swapnil Lad, Minrui Liang, Dean Long, Sayuj Shajith, Arnold Wang
----------------------------------------------------------------

## Introduction
Many problems of urban transportation begin and end with traffic. Traffic is responsible for increased pollution and increased wait times, and unpredictable traffic can cause complications in personal matters. The ability to accurately predict when traffic will flare up can increase the reliability of trip time estimates, reducing some of the societal friction incurred in-transit by urban and suburban road travelers. 
	Nowadays, a not insignificant percentage of vehicles on the road are vehicles for hire. Companies like Uber pay ordinary vehicle-owners to act as taxis for users of the Uber phone app. Uber and its competitors have an additional incentive to accurately predict trip times: they need to fairly compensate their drivers for their time and fuel. 
 
## Problem Definition
Uber has released data representing a significant portion of the billions of trips booked on their platform from the past few years. Averaged data for all Uber trips departing from a particular origin and arriving at a certain destination over a given time frame can be downloaded in hourly, daily, monthly, and quarterly resolutions. Among the provided statistics is the mean trip time for the origin and destination pair. How can we use past trip data to make consistent and accurate predictions of trip times booked today or tomorrow?
Isolating a single edge (average speed) between two vertices (postal code-resolution locations) simplifies our regression problem into a time-series problem; given historical data, can we predict the average speed for the next time segment?

It’s not guaranteed that historical trip data is enough for us to make a good prediction. However, we can synthesize the Uber dataset with other sources of environmental data to increase our accuracy. Data from Uber is in the form of records of Uber trips within a city during a given time period. An average speed is given for each trip from destination A to B; multiple trips from A to B can be included in the dataset with the same or different average speeds. Apart from date, time, and location data, each average speed is associated with no other features. But because the data provides a date, time, and location, we can add feature data for each trip from other robust data sets; one such data set we have identified and used the “Weather Underground” dataset to provide historical weather data at an equal or greater time resolution than that of the Uber data. Weather data is just an example solution to a more interesting problem; what data can we involve from outside data sources as appended features to each trip datapoint in order to improve our regression?

 
## Methods
### Data Collection
We decided to restrict the uber trip data to the month of February since this was a month that occurred before lockdown ordinances were imposed in the United States. In order to account for weather as a factor in our predictive model, we collected weather data from Weather Underground in the month of February. We collected data for temperature, humidity, and wind speed. From the web pages, the weather data’s daily averages needed to be collected from the page of each date for the month of February, and Python’s Beautiful Soup library was used to parse and extract the appropriate data and put them into a single Python list. The data was then separated and put into columns of the Pandas data frame. The apply function was used to split units from the data so that only the numerical data remained and was ultimately joined with the uber trip data. In order to clean the data we dropped entries with missing values and used the apply function in Pandas to keep formatting consistent between the two data sources.

### Regresssion
Using the data that we had for all of the uber trips and the associated weather (temperature, humidity, and wind speed), we decided to use the FB Prophet forecasting and regression library as the backbone for our initial analysis. In order to build the basis for our study, we decided to first understand the metrics of a single node (an approach that we hope to expand to include all nodes through a graph in order to represent all departure and arrival locations in the dataset). We first began by using the pandas library to determine the location that had the most arrivals throughout our sample month of February. We found that location 42778520 had roughly 3191 arrivals within just one month. We were excited to see this as it showed that our data was rich with information and we had enough filtered data samples to build a strong model and draw conclusions. 

In order to increase our understanding of the regressors that we were working with, we decided to use the matplotlib library to display the spread of our regression data. Our intention in choosing to go with a specific month was to create a microcosm for general data trends. In analyzing the visuals from the data, we noticed that there was a good spread of data across the viable range for all three of the chosen datasets (temperature, humidity, and wind speed). This was exciting as if we had data without much variation, it would be hard to utilize these datasets as regressors on our model. We initially began this process through the use of daily data for weather, but in our final approach we are hoping to get more granular with the data and apply hourly weather information (along with the other regressors) in order to build a stronger model. Seeing the good spread of data here on the day basis gives hope that the hourly data will also be abundantly spread and representative of the entire time span.

![alt text](https://github.gatech.edu/raw/awang348/4641-Traffic-Prediction/master/4641-midterm-1.PNG?token=AAAGZCATLJK2Q6BGQGLYD427VR5JC)

After finding that our regressors were worthy of further analysis, we then decided to split the month of February (the chosen subset of time that we picked for this initial research) into two parts, one to train the model and the other to test the model. The split was made by cutting the data in half, roughly giving 14 days worth of data in each group. By taking this approach we were able to provide substantial amounts of data on both ends of the regression. We fed the first half of our data into the Prophet model, with the date and mean travel time being the values used for the linear time series analysis. Temperature, humidity, and wind speed were then added to the model as additional regressors to add complexity to the system. We decided to begin our approach with just these three regressors, but we are hoping to take the results from this experiment and further build on our model by introducing additional regressors as we expand to all graph edges. 

![alt text](https://github.gatech.edu/raw/awang348/4641-Traffic-Prediction/master/4641-midterm-2.PNG?token=AAAGZCAN5HPREM3YKORJY627VR5K2)

We then moved on to fit the testing data through the FB Prophet library and forecasted to see the results of our model. In order to better understand the results of our model, we decided to study some of the validation metrics such as mse and rmse which would help us better understand the validity of our approach.

### Clustering and Feature Selection

We sought to apply clustering as a way of evaluating features for inclusing within our regression model. We started the clustering by choosing the most common destination, and created a new dataframe that only contains rows that had that place as it’s destination. We originally tried to apply a KMeans clustering algorithm to our data, and we got wildly inaccurate results. We tried some hyperparameter fitting, but we still did not get the results that we wanted. We plotted the clustering and used the visual representation to analyze whether it was a good fit. In the results, it is clear to see that this method was not a good fit for our data.
We then used a more modern algorithm on our data. We used the DBSCAN algorithm and these results ended up making more sense for our data. We could tell that it did a better job of clearly creating clusters in our data than KMeans did. 


## Results
### Regression
Using the first 15 days as a basis we predicted the second half average speed on this road. The following graph represents our prediction:

![alt text](https://github.gatech.edu/raw/awang348/4641-Traffic-Prediction/master/4641-midterm-3.PNG?token=AAAGZCE3FQZZJ2SIHWWIWMS7VR5MA)

The dots on the graph denote the training data points, the line is the actual prediction, and the light blue section color of the graph denotes the confidence interval of our prediction.
From the graph we can see that the confidence interval of our prediction is quite large with a value of roughly 6. This could be attributed to both our training data not having the specific time of day, and the small sample size we are using. In order to narrow the confidence interval, we will need to do more granular analysis on speed based on the specific time of day and increase the training data size. We plan on doing this going forward for our final presentation as we now have a good grasp on the methods and success metrics to keep in mind.
The error statistics as compared with the actual mean speeds are as follows:

![alt text](https://github.gatech.edu/raw/awang348/4641-Traffic-Prediction/master/4641-midterm-6.PNG?token=AAAGZCG7Q7GKT42JNXMRTNS7VR5M4)

The horizon column means the number of days since the cutoff. For this analysis our cutoff date is 2/15/20 (Horizon 1 days -> 2/16/20). As we can see from the general error trends, the accuracy of our prediction follows that of a time series regression. The closest days to the cutoff point has the most accurate predictions and the furthest has the most deviations. We should take note that although the predictions are yielding decent results for the short term, if we want longer term predictions we will have to look into alternatives. This also makes sense as most general time series models tend to be more accurate as you attempt to predict values closer to the training range (as seen here for the first couple of days which produces some of the lowest values for the the mse, rmse, and other metrics across our sampled timespan in this analysis). We hope to take the conclusions that we have drawn from this sample study and apply this knowledge towards the development of our final model and analysis.

### Clustering and Feature Selection

Here are the results from our KMeans clustering (Average Miles Per Hour vs Humidity):

![alt text](https://github.gatech.edu/raw/awang348/4641-Traffic-Prediction/master/4641-midterm-5.PNG?token=AAAGZCD5GE2WM6QRMRGNGCC7VR5N2)

Here are the results from our DBScan Clustering (Average Miles Per Hour vs Humidity):

![alt text](https://github.gatech.edu/raw/awang348/4641-Traffic-Prediction/master/4641-midterm-5.PNG?token=AAAGZCFD7SBRCT5ETIS2IMS7VR5O6)

Clustering proved itself as a tool we could use to determine whether an added feature was meaningful for our regression; we could tell that while along some axes the clusters are evident, along others there was no meaningful grouping of attributes. Observing a meaningful split (as we did in this case with normalized average speed along the y-axis) can be interpreted as indicating a meaningful parameter to include for regression. In this case, we can use values from edges leading into and out of a destination vertex. Conversely, there is no split along the humidity axis; this indicates that humidity is a relative non-factor in our regression.


## Discussion
This iteration of our project saw us making regressions on data points bearing similar start and end locations. Incorporating more edges and vertices to form a small network graph from regressions performed with well-fit regressors using Prophet (or another library) can allow us to “fill in the gap” for missing edges of graph. Improving the predictions on individual edges will improve our results as a whole; however, it is yet to be seen whether a “piecemeal” construction of a graph will produce better results than a convolutional neural network approach. 
Our results for initial regressions on specific edges seemed poor. Time-series analysis using the Prophet library allowed us to make predictions on a daily basis, with the added weather data of temperature, humidity, and wind speed; forecasts within one-day had a non-normalized RMSE of within 0.518. The units on this RMSE value are based on predictions of average miles per hour. We are eager to make future investigations on conducting hourly predictions, while also including precipitation data rather than proven non-factors like humidity. We expect hourly predictions to be more accurate than daily predictions, given that features that we included (weather data) is usually more impactful on traffic conditions on an hourly scale. 
