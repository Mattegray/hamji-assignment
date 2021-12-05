# Hamji

Welcome to Tridge sandbox project!

We'd love to collaborate with amazing developers as we drive the development of "Global Sourcing Hub of Food & Agriculture" into the future.

## Guidelines
- Setup project on your local computer
- Achieve TODO items one by one
- Mark an item as done in the TODO list
    - [x] Like this
- After completion, please send it in a zip file


## Setup
- Install PIP packages
```
pip install -r requirements.txt
```
- Run server
```
python manage.py runserver
```
- Now that the server’s running, visit http://127.0.0.1:8000/polls/ with your Web browser


## TODO
1. [x] Raise 404 if no matching question
   * Added dummy question to raise 404
   * Changes in:
     * `polls/templates/polls/index.html`
2. [x] Show only questions that are published and not yet closed
   * Added `closed` and `closed_at` attributes in the `Question` model
   * Changed to fetch only questions `not closed` in views
   * Changes in:
     * `polls/models.py`
     * `polls/serializers.py`
     * `polls/views.py`
3. [x] Enable to comment on question
   * Added `Comment` model and created `CommentForm`
   * Added `comment()` function in views and added url
   * Modified template to add and show comments
   * Changes in:
     * `polls/models.py`
     * `polls/admin.py`
     * `polls/forms.py`
     * `polls/urls.py`
     * `polls/views.py`
     * `polls/templates/polls/detail.html`
4. [x] Enable to comment on comment
   * Added `parent` attribute to `Comment`
   * Modified `comment()` function in views
   * Modified template to add and show comments on comments
   * Changes in:
     * `polls/models.py`
     * `polls/views.py`
     * `polls/templates/polls/detail.html`
5. [x] Enable to suggest new choice for question
   * Added `ChoiceForm` to forms
   * Added `choice()` function in views and added url
   * Modified template to add choices
   * Changes in:
     * `polls/forms.py`
     * `polls/urls.py`
     * `polls/views.py`
     * `polls/templates/polls/detail.html`
6. [x] Limit the number of choices that can be suggested on one question
   * Added `signals.py` to use the `pre_save` signal to check and limit number of choices before save
   * Connected signals with apps and init
   * Modified `choice()` function to render error message if limit is reached
   * Changes in:
     * `polls/apps.py`
     * `polls/__init__.py`
     * `polls/signals.py`
     * `polls/views.py`
7. [x] Extends `Question.closed_at` by one day, when new choice is suggested for that question
     - Requirements:
         - Use Django signal/receiver system
           * Added `post_save` signal in signals to extend the date by one day
           * Changes in:
             * `polls/signals.py`
8. [x] In `/polls/`, fetch only 5 questions through REST API
   * Modified `get_queryset()` in views to get 5 last published questions
   * Changes in:
     * `polls/views.py`
9. [x] Handle race condition on handling "vote" action
   * Modified to increment `vote` as `F()` object to avoid race condition
   * Modified signal receiver to raise error only when inserting choice, not when updating it
   * Changes in:
     * `polls/views.py`
     * `polls/signals.py`
10. [x] Implement login system
    * Used the `auth` app to implement login
    * Added templates for the login system and added url and link in settings
    * Changes in:
      * `hamji/settings.py`
      * `hamji/urls.py`
    * New files:
      * `templates/registration/login.html`
      * `templates/base.html`
      * `templates/home.html`
    * Created new 'accounts' app to implement the signup system
    * Modified templates and paths to allow signup
      * Changes in:
        * `hamji/settings.py`
        * `hamji/urls.py`
        * `templates/home.html`
      * New files:
        * `accounts/`
        * `templates/registration/signup.html`
11. [ ] Implement system that a question creator can approve suggested choices
12. [ ] Implement global search for questions and choices

