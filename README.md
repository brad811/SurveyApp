# SurveyApp
A simple survey app

### Requirements
- python 3
- Docker
- docker-compose

### How to run
- `cd` to the project directory
- Set up the environment variables by running `. ./env.sh`
- `docker-compose build`
- `docker-compose up`
- Visit `http://localhost:8000/survey/`
- To add, edit, or delete questions, or view results, go to the Django admin panel: `http://localhost:8000/admin/surveyapp/question/`

### Details
This is a simple Django survey app using MySQL, than can be run within docker containers.

An admin can enter survey questions with multiple choice answers using the Django admin interface, which has been extended to allow easier creation of questions along with their choices at the same time. You can also see the number of votes each choice has so far on the same screen.

Visitors to the site are shown a random question that they have not already answered (based on their session, so this can be easily tested using an incognito/private window or different browser), and that has at least one choice. If the user does not select an answer and clicks the submit button, they will be shown an error message. The layout easily adjusts to different screen sizes.
