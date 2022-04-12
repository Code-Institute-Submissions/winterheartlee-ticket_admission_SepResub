# TicketSpark - Event Creation & Ticketing System

TicketSpark is a Django-built website that is focused on providing event organisers with a simple e-ticketing system for users to buy tickets with a credit/debit card using the Stripe platform. Event creators can create, modify and delete event information and a clear separation has been implemented into the design so that the 'ticket purchasers' and 'event creators' have different registration information that allows them access appropriate navigation and database information. The focus on this site currently is for the Event creators as it is intended that event links will be directed to a buy now page for each event from the creators own website.
<br>
This project was built using Django and Python for the backend control and HTML, CSS & Javascript for the front end.
<br>
<br>
### <b>IMPORTANT NOTE: The events currently setup on the deployed heroku site are not real events and have simply been used to fill out the website content and demonstate its features.</b>
<br>

![Screenshot of creator homepage](media/readme_images/homepage_example.png)

## User Stories:
### Event Creators:
- Register as an event creator
- Create, modify and delete events
- Search for events
- Populate a 'My Events' page for each creator for easy access to management.
- Make sure 'creators' can't buy tickets; keep these two identities separated.
### Ticket Purchasers:
- Register to buy tickets
- See list of all events
- Search for events
- Have user profile with order history
- Able to buy tickets online with debit or credit card
- Make sure buyers can't create events.

## Wireframe:
- Wireframe was created using Balsamiq.
- [View full wireframe here](static/images/fungi-finders-wireframe.png)

![Wireframe Preview](static/images/wireframe-example.png)

## Features 

This site currently fullfils the criteria of the above user stories; events can be created and tickets purchased for said event. At this stage, the Event model currently has 'Event Name', 'Description', 'Start Date & Time', 'End Date & Time', 'Venue Name', 'Location Postcode', 'Ticket Price' and 'Ticket Allocation'.

### Features Left to Implement:

- Tickets sold need to be deducted from the 'Ticket Allocation' so no more tickets can be purchased beyond the allocated amount.
- Currently using a custom form to overide the Allauth signup page to include a 'type' choice of 'creator' or 'buyer', however I could not figure out how to add new fields to the aullauth models and therefore I used the currently existing 'first_name' field that isn't being used; this does the job for now but is not intended to be a final fix.
- Being able to filter and sort the 'all_events' and 'my event' pages would help the user around a potential large quantity of events.
- Mobile responsiveness has been considered for most of the site however there are still a few issues with large font sizes overlappying graphical elements.


## Testing 

Chrome was used to create this website and it is only FULLY currently functioning as should on Chrome; no other browsers have been tested so far. No Django 'tests' have been written to test the functions in the project.


### Validator Testing 

- HTML - [W3C Validator](https://validator.w3.org/nu/?doc=http%3A%2F%2Fflask-mushroom-forager-project.herokuapp.com%2F)
  - The site currently has no errors from the W3C Validator.
- CSS - [Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fflask-mushroom-forager-project.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
  - No errors were found with custom CSS however there is an error inside the Materialize Library CSS.
- Javascript - [Jshint](https://jshint.com/) 
  - No serious issues were detected when passed through the Jshint validator.
- Python PEP8 Compliant - [PEP8 Online](http://pep8online.com/) 
  - No errors detected and is PEP8 compliant.

### Unfixed Bugs

- after registering, logging in, logging out etc, the page gets redirected to the main index page, not the homepage of the user role.
- When the edit_event page is called, the 'Start Date and Time' and "End Date and Time' database entries are not being populated and have to be selected again.


## Deployment

This site has been deployed using Heroku, the live link can be found here - https://ticketspark.herokuapp.com/com/
The Static files and Media files have been collected and stored with Amazon Web Services.


## Credits 

- The programming languages used were HTML5, CSS3, Python and Javascript.
- The Code Institute 'Boutique Ado' walkthrough was followed through carefully and applied to my needs for this project for many of the features; particularly the Stripe payment code.

### Frameworks, Libraries and Programs:

1. [Bootstrap 4:](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    - Bootstrap 4 was used for its grid system and easy to use style classes.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Raleway' font that was used through the site.
1. [Font Awesome:](https://fontawesome.com/)
    - icons loaded from Font Awesome.
1. [GitPod](https://www.gitpod.io/)
    - GitPod was the IDE used to create the code.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from GitPod.



### Media:

- Creator homepage image was downloaded from [Pexels](https://www.pexels.com/photo/man-performing-on-stage-1916821/)
- Ticker purchaser homepage image was downloaded from [Pexels](https://www.pexels.com/photo/crown-raising-hands-during-performance-1652353/)
- Index buy tickets image was downloaded from [Pexels](https://www.pexels.com/photo/back-of-man-raising-hands-inside-room-full-of-people-with-purple-lights-1267350/)
- Index sell tickets image was downloaded from [Pexels](https://www.pexels.com/photo/photo-of-concert-band-during-night-time-167605/)