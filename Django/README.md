## Django

- Create Dynamic WebPages/WebApps : Update the HTML and CSS automatically
- A project has several webapps together. Eg Google Maps, Photos, Search...

### HTTP
- Client and Server
- Django WebApp runs at server
- client sends a GET request, server sends a response

### Creating a project

'''python
django-admin startproject <projectname>
'''

- create some default useful files
  - `urls.py`: table of contents for the website

```bash
python manage.py runserver
```
- runs the server locally

```bash
python manage.py startapp <appname>
```
- start a new webapp on the server
- make sure to add the name to `INSTALLED_APPS` in `settings.py`

### Working
- A client opens a HTTP connection, and lands on homepage of Django server
- From here, they can type an accesible URL, and go the that app. This is controlled by `urls.py`
- The app opens the URL linked to empty path. We can go to any other pages by typing names

- Parametrising Path: We dont want to have _hello_ _xyz_ for all possible names repeated. 

- HttpRequests are messy. We can use `render` to return HTML pages (called templates) in response to requests.

#### Templating Language (eg. isitchristmas.com)
  - The parametrised paths can be used to pass variable to HTML pages, as context (dictionary).

  - Good First project: "isitnewyear"

  - Django manipulates the HTML before rendering, verified using View Page Source 

#### Static Files
- Statics like CSS can be handled efficiently, HTML is NOT a static
- create a `static` directory

- Second Project: "To Do List"
  - Views contains all the logic of the code
  - Template Inheritance: No need to copy HTML of index for other pages like add
    - create `layout.html` in templates
  - (feeling sleepy) In href, add link to the path instead of page, as it help to change the code less if path file changed
  - Namespace collision: multiple "index.html" confused it for apps, use app_name in `urls.py`
  - ```html
      <form action="{% url 'tasks:add' %}" method="post">
    ```
    action means on-click, go to that page. post method means we will sent form data to the add page
  - Forbidden error: make the form safe using CSRF token for every session. Here, django middleware takes care of these tokens.

#### Forms in Django
- A class infrastructure to make things easy.
- Auto client side vaildation
- Basic HTML changes not required, makes the form control pythonic
- Server side validation: we access _add_ page in two ways, initially via GET request, then via post request of submit. They should behave differently, as POST request should add the task to the main list. Recall, all this validation happens in _views.py_. Helps when client side page is not updated to server.
- After submitting, we redirect the form (here) using `reverse` function to get to the desired label.

- security issue with global variables, every user has same variables
  - **sessions in django**
  - In index views, if on first visit no tasks list is found, create an empty one for the current session
  - `request.session` has all the data about that session/user
  - This data is stored in a table, we need to create using _migration_ to database (next lecture)
  - cookies are involved