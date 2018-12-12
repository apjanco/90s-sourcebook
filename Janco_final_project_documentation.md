## Final Project Documentation 

This project was a website to facilitate the work of a Digital Humanities workshop at the Association for Slavic, East European and Eurasian Studies (ASEEES) meeting in Boston.  The event took place on the morning of December 6th at the Marriot Copley Place.  The event was a collaboration between members of the ASEEES Digital Humanities affiliate organization (SlavicDH) and a group of scholars planning a 1990s Multimedia Sourcebook.  The ongoing discussions and points of difference between these two groups was a very productive and helpful  experience.  For example, the Sourcebook group originally requested a meeting space for a small group of investigators listed on their NEH grant applications.  SlavicDH imagined more of a hackathon where participants could engage with the Sourcebook, test new ideas and help in community engagement and development.  Given that the Sourcebook already had a "core" group of investigators, the contributions of SlavicDH shifted.  Instead of a hackathon, we planned an event where participants discussed the design and research questions facing the Sourcebook group.  The discussions would be instructive for both participants and the Sourcebook, but we were focued much more on planning than on implimentation or making.  The focus of my web design shifted from building the Sourcebook to creating a website to facilitate the work of the workshop and to showcase possible tools and methods that could help to re-imagine the Sourcebook project as both a resource for teaching and DH research. 

To that end, the site includes:
  - 3,136 scans from a Soviet book journal.  Text was extracted from all the images using Google Vision. [See here](http://104.236.220.106/all-kos/)
  - [Bestsellers Lists](http://104.236.220.106/bestsellers/) were added from a spreadsheet provided by Bradley Gorski.  A simple network visualization was created using D3. 
  - Metadata was generated using the Distant Viewing Toolkit for a 20 minute compilation of television commercials from post-Soviet Russia. [See here](http://104.236.220.106/distant_viewing/)
  - Pages were created for each workshop session to allow instructors to post materials in advance for their session.  Here are links for the [Image session](http://104.236.220.106/image/) and [Text analysis](http://104.236.220.106/text/) sessions. 
<hr>
1) Assess how well the redesigned web site met the goals of the client and how well it demonstrates (or fails to demonstrate) principles of good web page design.  

One of the main unintended takeaways from this project was the opportunity to test ideas and impliment features that I have seen elsewhere, but have not applied in my own work.  All of the tables, for example, use server-side processing using [jQuery dataTables](https://datatables.net/).  This is extremely fast and adds significantly to the user experience.  It is not clear to me that the tables were used extensively during the workshop.  The document images were available to all participants, but we did not have time to really delve into the image collection or to discuss them.  The last-minute addition of a collaborative Google Doc for notes was probably the most utilized page during the event.  I added a [secret page](http://104.236.220.106/secret/) to experiment with a CSS Nintendo theme.  I was successful in adding a Prodigy image annotation application to the page [see here](http://104.236.220.106:8080/). While the code is there, I was not able to create a web-app for a text summarization tool that I created in an earlier class. The application is very memory hungry and the server times out.  The workshop leaders mostly prepared slides and did not make much use of the content spaces that I provided to them.  In future events, I could add areas for presenters to upload their slides at the beginning of the workshop.    

2)  document/describe the files that have been changed (or will need to be changed) 

This version of the project is entirely unlike the draft.  This is largely due to the ongoing discussions with the project partners mentioned above.  I also dropped the "Russian like" font in favor of a highly readable and clean font.  The menus were originally a light blue, which my partner called "boring."  Feeling spurned, I recalled a beloved Trapper Keeper from middle school and worked to replicate its design.  The gradients were inspired by the wonderful design sense of [Ines Montani](https://ines.io/).  

3) give instructions for modifying/changing the site in general terms of design

The current site was designed to serve a single event.  I will save a disk image so that the code can be re-used when needed for similar SlavicDH events.  If funded, the project partners would like to work with a development firm in Chicago.  I have been in touch with them and will transfer any data as requested.  

4) mention any details that will be important to the client in understanding the design/redesign and ongoing maintenance of the site - Not teaching them HTML5 or JavaScript or CSS*.

The site uses Django's flat pages app, which allows users to update and author content through the admin interface.  I also added a CKEditor WYSIWYG editor for formatting.    

What was the most successful part of the redesign and why?   

I had a lot of fun making this site and I learned a great deal in the process.  It was a great opportunity to test new ideas and to impliment features that I've wanted to try, but did not have occasion to experiment with. 

What was the least successful part of the redesign?     

I would have liked to work more closely with the other organizers on the site and to have included more of their feedback.  We held weekly meetings as the event got closer.  We had so many philosophical and logistical issues to address that I never had time to get more concrete design feedback from them.  We had a particularly hard time working with the OCR, which consumed most of our attention as the event neared. We also lost a presenter, which shifted our focus to finding a replacement. 

If you had a second chance to redesign the web site, what changes would you incorporate?    

While I was able to add some fun visualizations and items to the Sourcebook, I would also like to add simple and practical applications that participants could use.  Rather than just creating a network visualization, for example, I could create an interactive application that allows users to change node and edge attributes or to use other data.  

What was the best/worst part of the redesign process? What would you do differently?   

It's over!  Now I have to do other things.  This was very fun. 


What challenges did you encounter in working with a client to carry out their vision?  

The partners were primarily interested in content, while the DH group was more interested in applications and digital methods.  I think that we struck a good bargain, but that we should spend more time getting clarity on expectations and common definitions of terms before moving forward.  We had a pattern of disagreeing and trying to agree, only to fall back into the same disagreements each meeting.   
