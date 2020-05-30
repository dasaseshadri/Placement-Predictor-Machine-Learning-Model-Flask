# Placement-Predictor-Machine-Learning-Model-Flask

An ML Model deployed using Flask which helps College students by predicitng the Tier of the Company they would likely get into in their Campus Placements based on their Mock Test Scores at College

# Project Directory Structure
### Tree
| README.md
| model.py
| model.pkl
| app.py
|
|___templates
|   | index.html
|
|___static
|   |___css
|       | style.css
|
| request.py
| placements.csv
|
|___Output
|   | app0.png
|   | app1.png
|   | app2.png
|   | app3.png
|   | app4.png
|   | app5.png

# Project Details

This Application is built in Python and deployed in localhost with Flask. The main code lies in app.py which launches the app. The code working of the Machine Learning Model is written in model.py which is written in python using ML Libraries.
Here, I have built a simple Linear Regression ML Model to predict the tier of Campus Placement Company the student is expected to get. In the web UI, four fields are to be filled, which are the student's scores in 4 different rounds that are usually conducted by any company and these are the scores obtained by students in the Mock Test conducted by their college. They are: Aptitude Round, Coding Round, Technical Interview, HR Interview. Scores are to be filled on a scale of 1-10. 

The data for training the ML model is provided in "placements.csv" file. It has four columns containing the four scores respectively.

Front end Web UI is written in index.html file present in "templates" folder and styling part is written in style.css file present in "static -> css" folder.

# How to Run

First, Clone/Download the project into your local system. Then open terminal and cd into the project folder.
Then, enter the command "python model.py" as shown in "app0.png" screenshot in "Outputs" folder. Then after few seconds, if the terminal ends by printing "2" on screen then the app is working fine. This is just a test print written inside the model file to ensure the prediction is happening well by passing static values as a list [2,9,7,7] to the model which should predict it as "Tier 2" and that is what is printed as "2" on screen.

Next, check your folder if "model.pkl" got created. That is the pickle file for our model which is basically created when the model.py runs well.

Then type "python app.py" in terminal. If it runs well, then the output as shown in screenshot "app1.png" in "Outputs" folder should appear on the terminal on screen.

Next, open up your web browser and type "localhost:5000" to run the web app. This is because Flask apps usually by default run on the "5000" port. A screen similar to the screenshot "app2.png" in "Outputs" folder appears containing the homepage with 4 textboxes to enter the 4 scores.

Enter the 4 scores and click on the "Predict Placement Company Tier" button to view your predicted company.

I have trained the model as follows: Sum of 4 scores >30 --> Tier #1
                                     Sum of 4 scores <30 & >25 ---> Tier #2
                                     Sum of 4 scores <=25 ---> Tier 1

The sample output for Tier#1 is shown in "app3.png", that for Tier#2 is shown in "app4.png" and for Tier#3 in "app5.png" of "Outputs" folder respectively.

NOTE: Since the dataset used here is of very less size, so there may be few Mispredictions as well as our ML Model would not have learnt sufficiently from the data.

# Future Work

Next, I would like to improve this model by increasing the dataset size and by trying with better ML Prediction models.
