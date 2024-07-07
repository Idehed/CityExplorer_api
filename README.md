# CityXP API

![CityXP](images/family.webp)<br>
CityXP is a social media platform designed for people that like to discover new cities. Users can share their experiences, stories, and images about different cities, creating a community of city explorers. Whether you're posting about hidden gems, local cuisine, or cultural landmarks, CityXP is the perfect place to document and discover city life around the world.

Additionally, CityXP offers a feature where users can become certified city guides. As a guide, you can showcase your knowledge and passion for your city, providing personalized tour that visitors can enjoy.

## Table of Contents
* [CityXP API](#CityXP-api)
  * [Development Goals](#Development-Goals)
    * [React Frontend](#React-Frontend)
  * [Live page](#Live-Page)
* [Planning & Agile](#Planning-and-Agile)
  * [Wireframes](#Wireframes)
  * [Agile](#Agile)
  * [Labels used](#Labels-used)
  * [Database design](#Database-Design)
  * [Methodology CRUD](#Methodology-CRUD)
  * [Features and Functionality for Superusers](#Features-and-Functionality-for-Superusers)
* [Manual Testing](#Manual-testing)
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

## Development Goals
The goal of this API is to store backend data for the CityEP FrontEnd application.
Here the backend information such as users, profiles, posts, comments, likes, guide, reviews are stored. And all is CRUD functioned.

### React Frontend
The repository for the frontend of the application can be found here:<br>[CityXP FrontEnd](https://github.com/Idehed/cityexplorer-frontend)

## Live Page
[CityXP API](https://cityexplorer-api-1e4f09c72732.herokuapp.com/)


# Planning and Agile

## Wireframes:
Wireframes can be seen here in the Frontend: <br>[CityXP FrontEnd](https://github.com/Idehed/cityexplorer-frontend) 

## Agile:
The API and Frontend of this project was planned using Agile methodology and MoSCoW prioritization on github projects.<br>

The user stories project can be found [here](https://github.com/users/Idehed/projects/6) 

## Labels used:

    - Must Have 
    - Should have  
    - Could have
    - Future implementation
    - Won't have
This projects user stories was divied into 9 milestones , "Authentication", "Navigation", "Posts", "Profile", "Comments", "Likes", "Contact", "Guides" and "Followers". All the user stories has been labeled and assinged to the developer and some labels has been put later such as "won't fix" and "Future implementation".
![Project planning](https://github.com/Idehed/CityExplorer_api/assets/146822758/42430643-e6d2-4d85-8b12-5ad6c91945db)

<b>All the issues were closed and the milestones subsequently too.</b>

## Database Design

<br>


![Database design](https://github.com/Idehed/CityExplorer_api/assets/146822758/91e83df7-de8a-4ffd-9852-4f06dcece426)

## Methodology CRUD
When performing CRUD (Create, Retrieve, Update, Delete) function based views, the following methods were used to manipulate the table in the database.

For such, to the subsequent endpoints:
/profiles/, /posts/, /comments/, /likes/, /followers/, /guides/, /reviews/

- POST - Used to create an object to a list of (endpoint)
- GET - Used to retrieve series of objects from a list of (endpoint)

Singularly, for the same endpoints past the primary keys:
/profiles/int:pk/, /posts/int:pk/int:pk/, /comments/int:pk/, /likes/int:pk/, /followers/int:pk/, /guides/int:pk/, /reviews/int:pk/

- GET - Used to view a single object in a list or (endpoint)
- PUT - Used to update a single object in a list of (endpoint)
- DELETE - Used to delete an existant single object from a list of (endpoint)

Users can then:
- CRUD Profiles
- CRUD Posts
- CRUD Comments
- CRUD Likes
- CRUD Followers
- CRUD Guides
- CRUD Reviews

![Admin panel](https://github.com/Idehed/CityExplorer_api/assets/146822758/f57e6712-d1cb-41e8-bebd-25918f636bf0)

## Features and Functionality for Superusers

As a Superuser one has the ability to perform the following via the admin panel:
- CRUD Posts
- CRUD Guides
- CRUD Profiles
- CRUD Contacts
- Change Passwords
- Change emails
- Promote users to Superuser




# Manual Testing

Manual Testing for the overall functionality of the API was performed by entering dummy data in the backend via Backend-end.
All data is CRUD functioned.
Create, Read, Update and Delete.
Screenshots have been taken to display that everything is working as expected.<br>
<b>[Detailed manual testing is located here](/Testing.md)</b>


## Validation
CI Python Linter was also used with the development of the API, to keep the code free of errors.

Minor errors was appearing in the validation but was simple to resolve:

    - E501 line to long (85 > 79 characters)
    - E225 missing whitespace around operator   
    - E128 continuation line under-indented for visual indent
    - E122 continuation line missing indentation or outdented
    - E111 indentation is not a mutiplie of 4
    - E117 over-indented
    - E302 expencted 2 blac lines,found 1
    - W292 no newline at end of file

I had one that i could not fix and it was this one, i tried with everything but all outcome was line to long.
 ![Python validation](https://github.com/Idehed/CityExplorer_api/assets/146822758/ca439639-8afe-4538-96b4-a3ace0892a0a)

## Future Improvements
<b>Contact page</b><br>
I did not have enought time to implement the contact page so that is one thing to improve the website.
<b>Notification</b><br>
Notification for the user if someone has likes, commented or followed you would be nice to have.
<b>Django-resized</b>
Would add the django-rezsized for both profile model and post model for impreved performace.
<b>Edit guide</b>
Would be nice to have the function to be able to edit your guide information.
<b>Delete reviews</b>
The option to delete your review if you for some reason have changed your mind or a guide.


## Installed Python Packages
The following packages were installed when developing this project:
To install, the following command ran: ```pip install``` ...


## Package Dependencies

    - asgiref==3.8.1
    - cloudinary==1.40.0  
    - dj-database-url==0.5.0
    - dj-rest-auth==2.1.9
    - Django==4.2
    - django-allauth==0.44.0
    - django-cloudinary-storage==0.3.0
    - django-cors-headers==4.4.0
    - django-filter==24.2
    - djangorestframework==3.15.2
    - djangorestframework-simplejwt==5.3.1
    - gunicorn==22.0.0
    - oauthlib==3.2.2
    - pillow==10.3.0
    - psycopg2==2.9.9
    - PyJWT==2.8.0
    - python3-openid==3.2.0
    - pytz==2024.1
    - requests-oauthlib==2.0.0
    - setuptools==68.0.0
    - sqlparse==0.5.0


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
- The live app can be found [here](https://cityexplorer-api-1e4f09c72732.herokuapp.com/).

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
- [Github](https://github.com/) - Host for the repository
- [Gitpod-Enterprise](https://codeinstitute-ide.net/) - Code editor
- [PostgreSQL](https://dbs.ci-dbs.net/) - Database
- [Cloudinary](https://cloudinary.com/) - Static & Media host
- [Heroku](https://id.heroku.com/) - Cloud platform/Host the live project

# Credits

- The lessons and tutorials provided by Code Institute, on the final module entitled "Django REST Framework" for the 'Advanced Front-End' endtitled "moments".

- I have been getting insperation from following users:<br>
[Gareth McGirr](https://github.com/Gareth-McGirr),<br>
[Hujanen91](https://github.com/Hujanen91),<br>

- I got help with creating the star rating using this website [React-simple-star-rating](https://react-simple-star-rating.vercel.app/?path=/story/introduction--page)

## Media:

- Many of my icons has been collected from this website 
[Flaticon](https://www.flaticon.com/)

- Some others here [Flaticon](https://fontawesome.com/)

- My font is from [Google Fonts](https://fonts.google.com/)

- The signup and signin images are from [Unsplash](https://unsplash.com/)


# Acknowledgements
- My mentor [Gareth McGirr](https://github.com/Gareth-McGirr) for his continuing support and great advice throughout this project.
- The slack community that helped me with many error problems throughout this project!