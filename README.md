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
6. [ ] Limit the number of choices that can be suggested on one question
7. [ ] Extends `Question.closed_at` by one day, when new choice is suggested for that question
     - Requirements:
         - Use Django signal/receiver system
8. [x] In `/polls/`, fetch only 5 questions through REST API
   * Modified `get_queryset()` in views to get 5 last published questions
   * Changes in:
     * `polls/views.py`
9. [ ] Handle race condition on handling "vote" action
10. [ ] Implement login system
11. [ ] Implement system that a question creator can approve suggested choices
12. [ ] Implement global search for questions and choices

