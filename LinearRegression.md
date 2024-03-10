## Linear Regression Mathematics

Linear regression is a method used to model the relationship between a dependent variable$y$and one or more independent variables $X$. In its simplest form, linear regression assumes a linear relationship between the independent and dependent variables. The mathematical representation of a simple linear regression model with one independent variable is:

$y = \beta_0 + \beta_1 x + \epsilon$

Where:
-$y$is the dependent variable (the variable we are trying to predict).
-$x$is the independent variable (the variable used to make predictions).
-$\beta_0$ is the intercept (the value of $y$ when $x = 0$).
-$\beta_1$ is the slope (the change in $y$ for a one-unit change in $x$).
-$\epsilon$ represents the error term (the difference between the observed and predicted values).

### Objective of Linear Regression

The objective of linear regression is to find the best-fitting line that minimizes the difference between the observed values and the values predicted by the model. This is typically done by minimizing the sum of squared errors (also known as the residual sum of squares or RSS), which is defined as:

$\text{RSS} = \sum_{i=1}^{n} (y_i - (\beta_0 + \beta_1 x_i))^2$

Where: \
-$n$ is the number of data points. \
-$y_i$ is the observed value of the dependent variable for the $i^{th}$ data point. \
-$x_i$ is the observed value of the independent variable for the $i^{th}$ data point. \
-$\beta_0$ and $\beta_1$ are the coefficients of the linear regression model. 

### Estimating Coefficients: Ordinary Least Squares (OLS)

The most common method for estimating the coefficients $\beta_0$ and $\beta_1$ in linear regression is the method of Ordinary Least Squares (OLS). OLS aims to minimize the sum of squared differences between the observed and predicted values. The formulas for calculating the coefficients are:

$\beta_1 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}$

$\beta_0 = \bar{y} - \beta_1 \bar{x}$

Where:
-$\bar{x}$ and $\bar{y}$ are the mean values of the independent and dependent variables, respectively.

### Making Predictions

Once the coefficients $\beta_0$ and $\beta_1$ are estimated, predictions can be made for new data points using the linear regression equation:

$\hat{y} = \beta_0 + \beta_1 x$

Where: \
-$\hat{y}$ is the predicted value of the dependent variable. \
-$x$ is the value of the independent variable for which we want to make a prediction. \
-$\beta_0$ and $\beta_1$ are the estimated coefficients. 

### Evaluation Metrics

Common evaluation metrics for assessing the performance of a linear regression model include Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and $R^2$ (coefficient of determination).

Linear regression is a powerful and widely used technique in statistics and machine learning for modeling the relationship between variables and making predictions based on that relationship.
