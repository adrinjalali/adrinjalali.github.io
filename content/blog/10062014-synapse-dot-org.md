Title: synapse.org
Date: 2014-6-10
Category: Blog
Tags: dream-challenge

I decided to actually write on this blog (decision was made this morning and is final :D ).

On June 2nd I received an email from my adviser telling me about the [DREAM Challenges](https://www.synapse.org/Portal.html#!Challenges:DREAM). I kind of liked it as some sub-challenges fit exactly what I've been doing for that past few months, and that project is already in a phase that we've submitted a manuscript about it. So why not?

Going through their pages, I realized they've got a python client to interact with their databases; that's cool, but it didn't support python 3. As a result I made [this pull request](https://github.com/Sage-Bionetworks/synapsePythonClient/pull/150) and at the moment of writing this post, they seem to be interested in accepting the commits (although the changes are not perfect and/or complete and more work is required).

Later I was reading challenge descriptions which made me interact with the website for a while, and that made me a bit frustrated. I have to say, I'm not a web-developer and I'm talking as a simple end user.

If I was the web-site's development manager, I'd add these to the first possible [sprint](http://www.scrumalliance.org/community/articles/2007/march/glossary-of-scrum-terms#1118):

- Add a proper navigation system to the website; currently you can only easily navigate within a challenge/project. You need to go to the home page first to go anywhere else.
- Try to go to DREAM challenges, you need to go to the home page, wait for that timer based frame to come which has the link to the challenge, click on it. In my browser (chromium), I have to refresh the whole page if I miss it once, or wait for it to come again. So: add proper links, menus, or whatever you think suits the framework for a nice navigation to projects.
- Within a challenge description page, click on a link and the whole page will be reloaded, slowly and painfully. For some reason the layout of the page changes through time after each part of the page is loaded. A simple markdown based static website works much faster and better, if you want it to be fancy, add proper AJAX components/codes to make it smooth and fast. The website has serious performance issues and seems unnecessarily heavy.

I'm pretty sure developers have their reason for having the website the way it is, but those reasons must be justified/changed.

