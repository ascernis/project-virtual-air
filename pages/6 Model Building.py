import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Model Building")

# Selectbox
modelOption = st.selectbox("Select Machine Learning Model:",
                           ["Random Forest", "Linear Regression", "Neural Network", "Support Vector Machine"])

if modelOption == "Random Forest":
    st.write("Now Displaying: ", modelOption)

    st.code(''' 
            from sklearn.model_selection import train_test_split
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.metrics import roc_curve, auc
            from sklearn.metrics import classification_report
            from sklearn.metrics import accuracy_score

            from matplotlib.legend_handler import HandlerLine2D
            ''',
            language = "python",
            line_numbers = True)
    
    st.write("These are the imported libraries that are used to deploy the ", modelOption, " model.")

    st.code('''
            for col in data.dtypes[data.dtypes == "objects"].index:
                for_dummy = data.pop(col)
                data = pd.concat([data, pd.get_dummies(for_dummy, prefix = col)], axis = 1)
            data.head()
            ''',
            language =  "python",
            line_numbers = True)
    
    st.write('''
            The code seen in above automates the process of encoding categorical columns within a dataframe. 
            As the Random Forest model requires numerical input, 
            using the dummy function seen above is a convenient way to handle categorical variables when preparing the data for the Random Forest machine learning technique.
             ''')
    
    st.code('''
            bottom_threshold = data['CO'].quantile(0.5)
            top_threshold = data['CO'].quantile(0.5)

            data['Pollution'] = np.where(data['CO'] <= bottom_threshold, 0, 1)

            x = data.drop(['CO', 'Pollution'], axis=1)
            y = data['Pollution']

            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

            rf = RandomForestClassifier(random_state=42)
            rf.fit(x_train, y_train)
            ''',
            language = "python",
            line_numbers = True)
    
    st.write('''
            The first two lines seen above are calculated the bottom 50% of the data and the top 50% of the dataset. The next line will create a new binary column that labels the bottom threshold as ‘0’ and the top threshold as ‘1’ 
            The variable that will be used will then be dropped alongside the new Pollution column and the dataset will split using the Train-Test split function. Where 80% of the data is used for testing and the remaining 20% of the data is used for training with a random state parameter to ensure reproducibility.
            Following this, a random forest classifier will initialise the technique to be in a random state and will be fit with the newly formed train-test split.
            ''')

    st.code('''
            y_pred = rf.predict(x_test)
            ''',
            language = "python",
            line_numbers = True)
    
    st.write('''
            The code seen above will implement the predict method of the Random Forest classifier that was implemented earlier. 
            The purpose of this code is to generate predictions based on the input data made from the train-test split. 
            Using the NumPy array, ‘y_pred’ these predicted values can be compared with the actual target values to evaluate the performance of the machine learning model.
            ''')
    
    st.code('''
            false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
            roc_auc = auc(false_positive_rate, true_positive_rate)

            accuracy = accuracy_score(y_test, y_pred)
            print(f"Accuracy: {accuracy:.2%}")

            print("\n")

            report = classification_report(y_test, y_pred)
            print("Classification Report:\n", report)

            print("\n")

            print("ROC Area:\n", roc_auc)
            ''',
            language = "python",
            line_numbers = True)
    
elif modelOption == "Linear Regression":
    st.write("Now Displaying: ", modelOption)

    st.code('''
            from sklearn.model_selection import train_test_split
            from sklearn.linear_model import LinearRegression
            from sklearn.metrics import mean_squared_error, r2_score
            import statsmodels.api as sm
            ''',
            language = "python",
            line_numbers = True)

    st.write("These are the imported libraries that are used to deploy the ", modelOption, " model.")
    
    st.code('''
            bottom_threshold = data['CO'].quantile(0.5)
            top_threshold = data['CO'].quantile(0.5)
            x = data.drop('CO', axis=1)
            y = data['Pollution'] = np.where(data['CO'] <= bottom_threshold, 0, 1)
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
            lr = LinearRegression()
            lr.fit(x_train, y_train)
            ''',
            language = "python",
            line_numbers = True)

    st.write('''
             Following the same logic, the first two lines seen within this table calculated the bottom 50% of the data and the top 50% of the dataset. 
             The next line will create a new binary column that labels the bottom threshold as ‘0’ and the top threshold as ‘1’
             The variable that will be used will then be dropped alongside the new Pollution column and the dataset will split using the Train-Test split function. Where 80% of the data is used for testing and the remaining 20% of the data is used for training with a random state parameter to ensure reproducibility.
             Following this, a linear regression model will initialise the technique and will be fit with the newly formed train-test split.
            ''')
    
    st.code('''
            y_pred = lr.predict(x_test)
            ''',
            language = "python",
            line_numbers = True)

    st.write('''
             The code seen above will implement the predict method of the Linear Regression that was implemented earlier. 
             The purpose of this code is to generate predictions based on the input data made from the train-test split. 
             Using the NumPy array, ‘y_pred’ these predicted values can be compared with the actual target values to evaluate the performance of the machine learning model.
            ''')
    
    st.code('''
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            print(f'Mean Squared Error: {mse}')
            print(f'R-squared Value: {r2}')
            ''',
            language = "python",
            line_numbers = True)

    st.write('''
             Evaluation Code
            ''')
    
elif modelOption ==  "Neural Network":
    st.code('''
            from sklearn.model_selection import train_test_split
            from tensorflow.keras.models import Sequential, load_model
            from tensorflow.keras.layers import Dense, Dropout
            from sklearn.metrics import accuracy_score
            from keras.optimizers import Adam
            ''',
            language = "python",
            line_numbers = True)

    st.write("These are the imported libraries that are used to deploy the ", modelOption, " model.")
    
    st.code('''
            threshold = data['O3'].quantile(0.5)
            data['Pollution'] = np.where(data['O3'] <= threshold, 0, 1)

            x = pd.get_dummies(data.drop(['Pollution', 'O3'], axis=1))
            y = data['Pollution']

            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.6, random_state=42)
            
            y_train_series = pd.Series(y_train)
            y_test_series = pd.Series(y_test)

            print(y_train_series.head())
            print(y_test_series.head())
            ''',
            language = "python",
            line_numbers = True)

    st.write('''
             The code for Neural Network follows the same logic but has a different execution. 
             The first line of code will calculate the 50th percentile of data and assign it to the ‘threshold’ variable. Similarly, the Pollution column is binary and the same parameters are set as discussed earlier.
             The ‘get_dummies’ function will create dummy variables for the categorical features within the dataframe but will drop the Pollution and variable columns.
             The code will then split 80% of the data for training and 20% for testing with a random state paramenter to ensure reproducibility. 
            ''')
    
    st.code('''
            model = Sequential()
            model.add(Dense(units=32, activation='relu', input_dim=len(x_train.columns), kernel_regularizer='l2'))

            model.add(Dropout(0.5)) 
            model.add(Dense(units=64, activation='relu', kernel_regularizer='l2'))
            
            model.add(Dropout(0.5))  
            model.add(Dense(units=128, activation='relu', kernel_regularizer='l2'))

            model.add(Dropout(0.5)) 
            model.add(Dense(units=1, activation='sigmoid'))
            ''',
            language = "python",
            line_numbers = True)

    st.write('''
             The code seen above defines a neural network with three hidden layers, dropout layers for regularisation and a final output layer for binary classification. 
             The sequential model initialises a sequential neural network model with layers added onto a linear stack. The first model adds a Dense layer with 32 units, a ReLU activation, L2 regularisaion and an input dimension equal to the number of features.
             The second layer adds another Dense layer with 64 units and an L2 regularisation. With the third Dense layer having 128 units and the same L2 regularisation.
             The Dropout layers have a dropout rate of 0.5 after each Dense layer, this is a regularisation technique that prevents overfitting the model by randomly setting a fraction of input units to zero during the training.
             The final Output layer is a Dense layer with 1 unit that has a sigmoid activation. This activation is selected as the model outputs probabilities between 0 and 1.
            ''')
    
    st.code('''optimizer = Adam(learning_rate=0.001)
            model.compile(loss = 'binary_crossentropy',
            optimizer = optimizer,
            metrics = 'accuracy')
            ''',
            language = "python",
            line_numbers = True)

    st.write('''
             The Optimiser will initialise an Adam optimiser that has a learning rate of 0.001, 
             this optimiser is a popular algorithm that is used for training neural networks. 
             The code above will use a binary crossentropy as the loss function as the target variable selected is binary. 
             The code will then measure the accuracy metric of the model.
            ''')
    
    st.code('''
            model.fit(x_train, y_train, epochs = 128, batch_size = 32)
            ''',
            language = "python",
            line_numbers = True)

    st.write('''
             The model fit code seen above will train the compiled model based on the training data. 
             It specifies the number of training epochs and the number of samples per gradient update. 
             The output seen showcases the epoch count, the loss of data, and the accuracy of that iteration. 
            ''')
    
    st.code('''
             y_hat = model.predict(x_test)
             y_hat = [0 if val < 0.5 else 1 for val in y_hat]
             
             y_hat
            ''',
            language = "python",
            line_numbers = True)

    st.write('''
             The code above transforms the continously valued predictions from the neural network model into binary predictions with a threshold of 0.5. 
             This is implemented as model uses binary classification where the outputs represents the probability of belonging to either Pollution or Not Pollution.
            ''')
    
    st.code('''
            accuracy_score(y_test, y_hat)
            ''',
            language = "python",
            line_numbers = True)

    st.write('''
             Evaluation
            ''')
    
elif modelOption == "Support Vector Machine":    
     st.code('''
             from sklearn.model_selection import train_test_split
             from sklearn.svm import SVC
             from sklearn.linear_model import LinearRegression
             from sklearn.metrics import accuracy_score, mean_squared_error
             from sklearn.preprocessing import StandardScaler
             from sklearn.metrics import classification_report, confusion_matrix
            ''',
            language = "python",
            line_numbers = True)
     
     st.write("These are the imported libraries that are used to deploy the ", modelOption, " model.")

     st.code('''
             bottom_threshold = data['CO'].quantile(0.5)
             top_threshold = data['CO'].quantile(0.5)
             
             x = data.drop('CO', axis=1)
             y = data['Pollution'] = np.where(data['CO'] <= bottom_threshold, 0, 1)

             x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
             ''',
             language = "python",
             line_numbers = True)
     
     st.write('''
              Following the same logic as the previous models. 
              The code above seperates the variable into the bottom and top thresholds into a binary column where the state is either Polluted or Not Polluted. 
              The data is then split using the Train-Test Split where 20% of the data is used for testing and the remaining 80% is used for training.
              ''')
     
     st.code('''
             svm_model = SVC(probability=True)
             svm_model.fit(x_train, y_train)
             svm_predictions = svm_model.predict(x_test)
             ''',
             language = "python",
             line_numbers = True)
     
     st.write('''
              The code above sets up and trains the Support Vector Machine for the classification task. 
              The model will then predict the classes of the test data using the predict method called svm_predictions.
              ''')
     
     st.code('''
             svm_accuracy = accuracy_score(y_test, svm_predictions)p
             print(f"SVM Accuracy: {svm_accuracy}"

             svm_classification_report = classification_report(y_test, svm_predictions)svm_confusion_matrix = confusion_matrix(y_test, svm_predictions)
             print(f"SVM Classification Report:\n{svm_classification_report}")
             
             print(f"SVM Confusion Matrix:\n{svm_confusion_matrix}")
             ''',
             language = "python",
             line_numbers = True)
     
     st.write("Evaluation")

else:
    st.write("Select a Model")