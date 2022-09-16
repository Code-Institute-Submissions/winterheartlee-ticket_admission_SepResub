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


## Features 

This site currently fullfils the criteria of the above user stories; events can be created and tickets purchased for said event. At this stage, the Event model currently has 'Event Name', 'Description', 'Start Date & Time', 'End Date & Time', 'Venue Name', 'Location Postcode', 'Ticket Price' and 'Ticket Allocation'.

### Features Left to Implement:

- Tickets sold need to be deducted from the 'Ticket Allocation' so no more tickets can be purchased beyond the allocated amount.
- Currently using a custom form to overide the Allauth signup page to include a 'type' choice of 'creator' or 'buyer', however I could not figure out how to add new fields to the aullauth models and therefore I used the currently existing 'first_name' field that isn't being used; this does the job for now but is not intended to be a final fix.
- Being able to filter and sort the 'all_events' and 'my event' pages would help the user around a potential large quantity of events.
- Mobile responsiveness has been considered for most of the site however there are still a few issues with large font sizes overlappying graphical elements on the creator homepage tabs.
- Ticket confirmation emails display the order number but do not show an itemised list of separate purchased tickets.

### Further Advanced Development:

- Advanced ticket analytics would need to be implemented into the creator features to make this site compete with other ticketing services.


## Testing 

Chrome was used to create this website and it is only FULLY currently functioning as should on Chrome; no other browsers have been tested so far. No Django 'tests' have been written to test the functions in the project.

A test account was created for a 'buyer' and another for a 'creator'. All aspects of the site functionality was tested on each account; no broken links were discovered and test stripe payments were successful.

Test stripe payments can be made using the test card information:
- Number: 4242 4242 4242 4242 
- MM/YY: 4242
- CVC: 424

### Validator Testing 

- HTML - [W3C Validator](https://validator.w3.org/nu)
  - The site currently has no errors from the W3C Validator; each custom html page was tested separately through the validator.
- CSS - [Jigsaw Validator](https://jigsaw.w3.org/css-validator/)
  - No errors were found with custom CSS; each CSS file was tested separatly through the validator.
- Javascript - [Jshint](https://jshint.com/) 
  - No serious issues were detected when passed through the Jshint validator; all js script files and any code between 'script' tags were tested separately through the validator.


### Unfixed Bugs

- After registering, logging in, logging out etc, the page gets redirected to the main index page, not the homepage of the user role.
- Styling for the 'tabs' on the creator homepage is not currently displaying in a satisfactory manner on mobile devices; tablet devices with larger screens work ok.


## Deployment

This site has been deployed using Heroku, the live link can be found here - https://ticketspark.herokuapp.com
The Static files and Media files have been collected and stored with Amazon Web Services.


## Credits 

- The programming languages used were HTML5, CSS3, Python and Javascript.
- The Code Institute 'Boutique Ado' walkthrough was followed through carefully and applied to my needs for this project for many of the features; particularly the Stripe payment code.
- Recommended fix for HTML5 'datetime-local' failing validation when creating/editing events was found on Stack Overflow by user 'CoffeeBasedLifeform' here: https://stackoverflow.com/questions/53180600/django-datetime-not-validating-right/53194594#53194594
- The blog app and model was created using the walkthrough at DjangoCentral: https://djangocentral.com/building-a-blog-application-with-django/

### Frameworks, Libraries and Programs:

1. [Django Framework:](https://www.djangoproject.com/)
    - Django was used as the overall framework for this dynamically built website.
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
1. [Heroku:](https://dashboard.heroku.com/)
    - Heroku was used to deply the website and the free POSTGRES database feature was used for the CRUD functionality.
1. [Amazon Web Services:](https://aws.amazon.com/)
    - AWS was used to store and link the 'static' and 'media' files for the site.



### Media:

- Creator homepage image was downloaded from [Pexels](https://www.pexels.com/photo/man-performing-on-stage-1916821/)
- Ticker purchaser homepage image was downloaded from [Pexels](https://www.pexels.com/photo/crown-raising-hands-during-performance-1652353/)
- Index buy tickets image was downloaded from [Pexels](https://www.pexels.com/photo/back-of-man-raising-hands-inside-room-full-of-people-with-purple-lights-1267350/)
- Index sell tickets image was downloaded from [Pexels](https://www.pexels.com/photo/photo-of-concert-band-during-night-time-167605/)