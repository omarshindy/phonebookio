# Phonebookio


It's a simple app to create a phonebook you can register to the app and then login to create contact info with contact type




# Run app

- simply clone this repo and cd to phonebookio then creare .env file to store our environment variables to start the app 
Note: we only share environment variables when run the app localy but on production environments we save our env variables on the server

```
SECRET_KEY='django-insecure-ukl!5$utj^g@ysm%5ke!#fq-$k6*qgi#r)81k^1o%-z#@ma14!'
POSTGRES_DB='contactiodb'
POSTGRES_USER='admin'
POSTGRES_PASSWORD='123'
```


- Start docker using this command 

```
docker-compose up --build
```

# Basic ERD Diagram
![erd](https://user-images.githubusercontent.com/23037901/212565764-c6a46798-2bd8-4245-963b-5046865ea05d.jpg)
