# CityXP API

![CityXP]()<br>


## Table of Contents
* [CityXP API](#CityXP-api)
  * [Objective](#Objective)
    * [React Frontend](#React-Frontend)
  * [Live page](#Live-Page)
* [Planning & Agile](#Planning-and-Agile)
  * [Design](#Design)
  * [Wireframes](#Wireframes)
  * [Agile](#Agile)
  * [Labels used](#Labels-used)
  * [User stories](#User-stories)
  * [Relationship Diagram](#Relationship-Diagram)
  * [Methodology CRUD](#Methodology-CRUD)
  * [Features and Functionality for Superusers](#Features-and-Functionality-for-Superusers)
* [Manual Testing](#Manual-testing)
  * [Deployed Admin Screens](#deployed-admin-screens)
  * [Validation](#validation)
  * [Future Improvements](#Future-Improvements)
  * [Installed Python Packages](#Installed-Python-Packages)
  * [Package Dependencies](#Package-Dependencies)
* [Development and Deployment](#Development-and-Deployment)
  * [Heroku](#Heroku)
  * [Forking](#Forking)
  * [Languages and Technologies](#Languages-and-Technologies)
  * [Other forms of development](#Other-forms-of-development)
* [Credits](#Credits)
  * [Media](#Media)
* [Acknowledgements](#Acknowledgements)

## Objective
This is the API for the SourdoughCircle FrontEnd application.
Here the backend information such as users, profiles, posts, comments, likes, categories etc are stored.

### React Frontend
The repository for the frontend of the application can be found here:<br>[CityXP FrontEnd]()

## Live Page
[CityXP API]()

In development:
![API Preview]()
Deployed version:
![API Preview]()

# Planning and Agile

## Design:

## Wireframes:
### Homescreen/Feed
![Home]()
### Liked posts page
![Liked]()
### Login page
![Login]()
### Profile page
![Profile]()
### Saved posts page (was later removed during planning)
![Saved]()
### Signup page
![Sign up]()

## Agile:
The API and Frontend of this project was planned using Agile methodology and MoSCoW prioritization on github projects.<br>

The user stories project can be found [here]() 

## Labels used:
`must have`
`should have`
`could have`
`wont have`


![Project planning]()

## User Stories
### `Must-Have`:<br>


### `Should-Have`:<br>


### `Could-Have`:<br>


### `Wont-Have` & `Future implementation`:<br>



<b>The issues were closed and the milestones subsequently too.</b>

## Relationship Diagram
The relationship diagram between models from an individual perspective can be best defined as follows:

- The [Profile]() flaunts the owner(OneToOne),<br>
 created_at(DateTimeField),<br>
 updated_at(DateTimeField),<br>
 name(CharField),<br>
 email(EmailField),<br>
 content(TextField),<br>
 image(ImageField),<br>
 facebook_link(URLField),<br>
 twitter_link(URLField) and<br>
 instagram_field(URLField)<br>


***
<br>


<img src="" alt="Models Diagram">

## Methodology CRUD
When performing CRUD (Create, Retrieve, Update, Delete) function based views, the following methods were used to manipulate the table in the database.

For such, to the subsequent endpoints:
/profiles/, /posts/, /comments/, /likes/, /followers/, /contact/, /category/

- POST - Used to create an object to a list of (endpoint)
- GET - Used to retrieve series of objects from a list of (endpoint)

Singularly, for the same endpoints past the primary keys:
/profiles/int:pk/, /posts/int:pk/int:pk/, /comments/int:pk/, /likes/int:pk/, /followers/int:pk/, /contact/int:pk/, category/

- GET - Used to view a single object in a list or (endpoint)
- PUT - Used to update a single object in a list of (endpoint)
- DELETE - Used to delete an existant single object from a list of (endpoint)

Users can then:
- CRUD Profiles
- CRUD Posts
- CRUD Comments
- CRUD Likes
- CRUD Followers
- CR Contacts


## Features and Functionality for Superusers

As a Superuser one has the ability to perform the following via the admin panel:
- CRUD Posts
- CRUD Comments
- CRUD Profiles
- CRUD Contacts
- Change Passwords
- Change emails
- Promote users to Superuser

<img src="" alt="Admin Panel (local)"><br>


# Manual Testing

Manual Testing for the overall functionality of the API was performed by entering dummy data in the backend both via Backend-and Front-end.
All data is CRUDed accordingly.<br>
<b>[Detailed manual testing is located here](/Testing.md)</b>




## Deployed admin Screens

<details>
<summary><b>Django admin panel</b></summary>
<summary>
<br>

  An overview of the django admin panel to display the different pathways and to inform what the admin can do.

  - <b>Profiles</b><br>
    The admin overview of all the profiles where admin can pick a profile and delete it (GET, POST and DELETE)
  ![Profiles]()
  - <b>Profiles details</b><br>
    Profile details, here the admin can change all the details in the profile as displayed in the image. The admin can also delete users. (GET, PUT, PATCH, DELETE)
  ![Profiles details]()
  - <b>Posts</b><br>
    Postlist for admin to view and handle all the posts on the website (GET, POST and DELETE)
  ![Posts]()
  - <b>Posts details</b><br>
    Post details admin view to make it easy for admin to handle the posts details. The admin can change all the details of the post and delete it if needed. (GET, PUT, PATCH and DELETE)
  ![Posts details]()
  - <b>Likes</b><br>
    Likes view that displays a list of the likes and what post that is liked (GET, POST, DELETE)
  ![Likes]()
  - <b>Likes details</b><br>
    Details view for likes where admin can edit what posts the like should be connected to, the admin can also change user that liked and delete likes. (GET, PUT, PATCH and DELETE)
  ![Likes details]()
  - <b>Contact</b><br>
    Contact list view of all the incoming messages from the contact form on the website. Admin can create new contact and delete existing ones. (GET, POST, DELETE)
  ![Contact]()
  - <b>Contact details</b><br>
    Admin contact details where admin can read the message and it's details, edit, add new information, and delete. An admin response field is also implemented but non working at the moment, this will be a [future improvement](#future-improvements) where admin is supposed to be able to respond directly on the admin panel and the email will be sent to the email the user added to the form. (GET, PUT, PATCH and DELETE)
  ![Contact details]()
  - <b>Comments</b><br>
    Comments list admin overview for the admin to see all the comments, add new ones and delete existing ones. (GET, POST and DELETE)
  ![Comments]()
  - <b>Comments details</b><br>
    Details view for comments where admin can update all the fields needed for the comment, the admin can also delete the comment. (GET, PUT, PATCH and DELETE)
  ![Comments details]()
  - <b>Category</b><br>
    Category list view for admin to display all existing categories with id number and name. Admin can add new categories or delete existing ones. (GET, POST and DELETE)
  ![Category]()
  - <b>Category details</b><br>
    Details view for categories. The admin can update existing fields and delete if needed. (GET, PUT, PATCH and DELETE)
  ![Category details]()


</summary>
</details>
<details>
<summary><b>Deployed API overview</b></summary>
<summary>
<br>

  Below are screenshots of the deployed API that displays the main overview and that the paths are working correctly and not displaying any sensitive information, the main testing was done in the local API to get more details and information when testing and can be found [here](#manual-testing) and the live API can be found [here]()

  - [Start]()<br>
    The main page of the deployed API
  ![Start]()
  - [/profiles]()<br>
    The profile list on the deployed API
  ![Profiles]()
  - [/profiles/id]()<br>
    The profile id view on the deployed API
  ![Profiles id]()
  - [/posts]()<br>
    The posts list on the deployed API
  ![Posts]()
  - [/posts/id]()<br>
    The posts id view on the deployed API
  ![Posts id]()
  - [/likes]()<br>
    The likes list on the deployed API
  ![Likes]()
  - [/likes/id]()<br>
    The likes id view on the deployed API
  ![Likes id]()
  - [/contact (authentication required to display)]()<br>
    The contact list on the deployed API. This page should respond with non authenticated information to not give everyone access to users information and messages sent through with the contact form.
  ![Contact]()
  - [/contact/id (authentication required to display)]()<br>
    The contact id view on the deployed API. This page should respond with non authenticated information to not give everyone access to users information and messages sent through with the contact form.
  ![Contact id]()
  - [/comments]()<br>
    The comments list on the deployed API.
  ![Comments]()
  - [/comments/id]()<br>
    The comments id view on the deployed API.
  ![Comments id]()

</summary>
</details>

## Validation
CI Python Linter was also used in parallel with the development of the API, to keep the code free of errors.

The Code has not exhibited apparent errors after consecutive tests and corrections throughout the development.
Minor errors was appearing in the validation but was simple to resolve:


 ![Python validation]()

## Future Improvements



## Installed Python Packages
The following packages were installed when developing this project:
To install, the following command ran: ```pip install``` ...


## Package Dependencies
-

# Development and Deployment
The project was developed using GitHub and GitPod platforms...
- Navigate to: "Repositories" and create "New".
- Mark the following field: ✓ Public
- Select template: "Code-Institute-Org/react-ci-template".
- Add a Repository name: "cityexplorer-api".
- ...and create Repository.


For Commits on this project, the following commands ran:
- ```git add .``` <- Stages before commiting.
- ```git commit -m "written imperative declaration"``` <- Declares changes and updates.
- ```git push``` <- Push all updates to the GitHub Repository.

To run the server locally (Debug = True), the following command ran:
- ```python manage.py runserver``` <- Loads the website on the in-built Terminal.

During development migrations to the database were made.
To make migrations the following commands ran:
- ```python manage.py makemigrations``` <- Creates a new database migration
- ```python manage.py migrate``` <- Applies pending migrations

To create or update Requirements.txt file the following commands ran:
- ```pip3 freeze --local > requirements.txt```  <-Runs the req.
- ```pip install -r requirements.txt``` <- Install req.

To create a Superuser the following command ran (from Heroku terminal): 
- ```python manage.py createsuperuser``` (username->email->password1->password2) <- Creates a Superuser

To create a new Django project, in the currenct directory, the followig command ran:
- ```django-admin startproject NAMEOFTHEPROJECT .``` <- Starts the project

To create the app the following command ran:
- ```python3 manage.py startapp NAMOFTHEAPP``` <- Creates a folder for the app withing the project
- 

## Heroku
The website is being hosted and deployed on Heroku:
- Navigate to: "Create new app" add a unique name "djangorestframework-api" and select your region. Click "Create App"
- Head over to "Settings" tab and apply the respective config VARs
- Move to "Deploy" section and select "Github" method"
- From here search for the repository name "connect", from the GitHub account.
- Hit "Connect" and "Enable Automatic Deploys" to keep the the repository in parallel to Heroku.
- Manually "Deploy Main Branch".
- Upon successful deployment, retrieve the link for the mock terminal.
- The live app can be found [here]().

## Forking
Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to 
  fork.

- On the top right of the page under the header, 
  click the fork button.

- This will create a duplicate of the full 
  project in your GitHub Repository.

## Languages and Technologies
- Django REST Framework (Python Framework - API)

## Other forms of development
- [Diagrams](https://app.diagrams.net/) - Diagram set up
- [Github](https://github.com/) - Host for the repository
- [Gitpod](https://gitpod.io/) - Code editor
- [ElephantSQL](https://www.elephantsql.com/) - Database
- [Cloudinary](https://cloudinary.com/) - Static & Media host
- [Heroku](https://id.heroku.com/) - Cloud platform/Host the live project

# Credits

## Media:


# Acknowledgements