# TinyFunds User Guide

## General Information
Tinyfunds is a gamified microdonation and microvolunteering platform designed with smaller causes and individuals in mind. 
Users can create worthy causes that they think need additional funding as well as contribute their time or  
their money to someone else's cause, which increases their user level!

You can navigate to our site in a browser of your choice at tinyfunds.herokuapp.com.
The site will perform optimally with browsers that support google log-ins.

---
### <ins>User Account Management</ins>
#### How to Login
Tinyfunds will automatically search for a connected google account that is signed in on your browser, and log you in if it exists.  
Otherwise:
1. Use the Navbar to travel to the "Account" page, or directly travel to tinyfunds.herokuapp.com/account/.
2. A Google log in button will be displayed if you not logged in.
> Note: Even if you are logged in, your user account will not be added to the roster of registered users until you change your account profile name.

#### How to Logout
To Log out from tinyfunds, you will have to edit your account page and manually log out.  
Follow these steps:
1. Use the Navbar to travel to the "Account" page, or directly travel to tinyfunds.herokuapp.com/account/.
2. On the left-hand side, click on the grey "Edit Account" button 
3. Click on the red "Logout" button to complete the log out.

#### How to Change User Information
On your account profile page, personal information can be modified while donation and level statistics are automatically generated. 
To Edit your personal information:
1. Use the Navbar to travel to the "Account" page, or directly travel to tinyfunds.herokuapp.com/account/.
2. On the left-hand side, click on the grey "Edit Account" button 
3. You may update your account name in the top box, change your image in the middle box, and edit your bio in the third box.
4. Once your are satisfied with the changes (if any), press the blue "Update" button.
---

### <ins>Event Management</ins>
#### Posting Events
Posting an event is a process that will create a new donation/volunteering event page managed by one user (the creator).  
To create a new event posting:
1. Make sure that you are logged in, anonymous users are unable to create new events. 
2. Travel to the "Post" section of the Navbar, or directly travel to tinyfunds.herokuapp.com/explore/new. 
3. Fill out all of the fields with valid information. If you have an invalid input, you will recieve a warning. 
4. Press the blue "Post" button to create the event page and to be redirected to the new page. 

#### Updating or Removing events
To edit an event, travel to that specific Event's page while logged in with the account that manages that event.  
- To update an event:  
    Find the blue "Edit Event" button at the bottom of the event page to bring up the editing UI form. When you are satisfied with your changes, press the blue "Update" button to commit those changes.

- To delete an event:  
    Find the red "Delete Event" button at the bottom of your event page. Press this button, and confirm your intent to delete your event. If you decide to remove your event, it will be wiped from the database and removed from the event list.
---

### <ins>Site Exploration</ins> ###
#### Browsing Events
To browse events, travel using the Navbar to the "Events" tab. You will see a list of all active events, and can scroll up/down through them to browse through. If you see an event with a title and description that interested you, simply click on that event to be brought to that page. You can return to the events list by simply pressing the "event" navbar selection again, or using your browser's back button.


#### Browsing Users
To browse users, travel using the Navbar to the "Users" tab. You will see a list of all registered users, and can scroll up/down through them to browse through. To see more information about a user, simply click on that entry to be brought to their page. You can return to the users list by simply pressing the "user" navbar selection again, or using your browser's back button.

---
### <ins>Donation Mechanics Guide</ins>
>***Important Note:***
>
>Please use our testing paypal log-in information to prevent the transfer of real funds!
- Username:
    - acmrpersonal@gmail.com
- Password:
    - personalacmr123

  
   
#### How to Donate Funds
To Directly Donate Funds:
1. Travel to an Event page to which you wish to contribute.
2. On the right hand side, locate the donation goal widget.
3. Press the "Donate button" to be redicted to the checkout page.
4. Decide on a donation ammount, and select a payment option and complete the paypal donation process in the popup window.
5. For testing purposes, please use the paypal account above to perform transfer of real funds.
6. Funds will be added to the updated Event page after you are redirected back, as well as a donation feed entry. 

#### How to Pledge Hours or Funds
To Pledge Volunteer Hours or Funds:
1. Travel to an Event page to which you wish to contribute.
2. On the right hand side, locate the donation goal widget.
3. Press either of the "Pledge a donation!" or "Pledge hours!" buttons.
4. Decide on the amount of the relevant contribution metric.
5. (optional) Include a note with more specifc information about your donation.
6. After submtiting your pledge by pressing the "Pledge!" button, a new donation entry will appear in the event's feed.
7. Reach out to the event organization to figure out a way to fullfill your pledge, be it hours or alternative funding.
8. Fund Goals are totals are <ins>**NOT**</ins> updated until the pledge is confirmed recieved by the event organizer.

#### How Organizations Recieve Pledged Hours or Funds.
To Confirm Pledged Hours or Funds:
1. Travel to the Event page that you are managing.
2. On the right hand side, locate the donation goal widget.
3. Find a pledge of either type that is unconfirmed. 
4. Reach out/ coordinate with the user that pledged those funds to recieve those pledged resources.
5. After you have recieved the donation, press the "Confirm!" button at the bottom of the donation entry to verify the pledge.
6. The donation entry will gain green colored text, and your donation totals will be updated to reflect the confirmation.

---
### <ins>Code Sources and Works Cited</ins>


*  Title: Google Maps Platform Overview
*  Author: Google
*  Date: 2020-11-20
*  URL: https://developers.google.com/maps/documentation/javascript/overview
*  Software License: Creative Commons Attribution 4.0 License  
___

*  Title: Django AllAuth SocialAccount Test Cases
*  Author: Raymond Penners (Github Username: pennersr)
*  Date: 2020-10-05
*  URL: https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/tests.py
*  Software License: MIT License
*  Additional Notes: 
    - We only used some of the helper functions as a guide to implement our own version of similar test cases in early versions. 
    - In the final release, we created our own test functions based on these concepts since we extended the base Allauth User Model in Sprint 4.  
___

*  Title: Django : Custom User Model & Allauth for OAuth
*  Author: Sarthak Kumar
*  Date: 2019 April 1
*  Code version: None provided
*  URL: https://medium.com/@ksarthak4ever/django-custom-user-model-allauth-for-oauth-20c84888c318
*  Software License: None provided
___

*  Title: Smart Payment Buttons Integration - Developer Paypal
*  Author: Paypal
*  Date: n.d. Last accessed November 24 2020
*  Code version: None provided
*  URL: https://developer.paypal.com/demo/checkout/#/pattern/client
*  Software License: Paypal Developer Agreement (https://www.paypal.com/us/webapps/mpp/ua/xdeveloper-full)
___

*  Title: Customize the PayPal Checkout Button
*  Author: Paypal
*  Date: 2020
*  Code version: None provided
*  URL: https://developer.paypal.com/docs/archive/checkout/how-to/customize-button/
*  Software License: Paypal Developer Agreement (https://www.paypal.com/us/webapps/mpp/ua/xdeveloper-full)
