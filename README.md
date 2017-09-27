## Testcase for the MockAir website

## Running the code:

*The test was written on Ubuntu 16.04

The test uses two modules that you may not have installed:
* [Requests](https://http://docs.python-requests.org/en/master/) - HTTP library for Python.
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - Provides Pythonic idioms for navigating, searching, and modifying a parse tree.


You can use the requirements file to install these, preferably within a virtualenv.
```
pip install -r requirements.txt
```

Then simply run on the command line
```
nosetests
```

You should see the following:
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.905s

OK
```

## Assumptions

*A successful GET / POST request to an endpoint would return a 200 status code and a HTML page with the required information (a referral to the next page). I could not find access to raw XML or JSON response. For this reason, the assertions within the tests are as simple as asserting that the access code is 200 and that the HTML response contains/does not contain a certain string.


## Difficulties encountered

The test code itself is quite simple and didn’t take long to write, one issue I did encounter was getting a 500 status code when trying to send a POST request to any of the endpoints.

This was happening because I was not starting a session at the beginning of the test, meaning that the cookies and token required to complete the booking were not set.

I eventually figured this out by using a tool called Postman and keeping an eye on Chrome’s developer tools while clearing my browser cookies mid booking (a cookie got deleted, resulted in a 500 error). This reassured me that the problem wasn’t with individual POST requests in my code and the data I was sending to the endpoints.

Figuring out the above issue took significantly longer than finding the endpoints, what data to send to them or to write the actual test.
