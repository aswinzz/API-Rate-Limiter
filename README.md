## API RATE LIMITER

### How to setup
- Clone this repo and open the directory in your terminal
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`
- visit `localhost:8000` in your browser

### How to test the rate limiting feature
- go to `http://localhost:8000/rest-auth/registration/` and create an account for a user
- go to `http://localhost:8000/rest-auth/login/` and login using the created account to generate a token key.
- in this codebase there are two endpoints for testing `/api/1` & `api/2`
- if you do a `POST` request to any of these url's using the Authorization Token that was generated, in the output you can see whether the request was successful or failed due to the exceeding of request rates.

### How it works?
- Each User trying to access the same endpoint in a day will be restricted to hit the endpoint only a pre defined number of times, which can vary accross endpoints.
- If a user tries to access an endpoint the access count is incremented and in a day if the count reaches the maximum limit, the user will not be able to access the endpoint in that day.
- The access count is resetted after one day.

### Screenshots
<p align="center"> 
<img src="https://github.com/aswinzz/API-Rate-Limiter/blob/master/ss.png" />
</p>

### Future Plans
This can be converted into a package and can be used by everyone with single installation and very simple setup steps.


### Contributing
Your contributions are always welcome! Feel free to open up issues and create Pull Request if you feel like adding more features to this project. 🎉
