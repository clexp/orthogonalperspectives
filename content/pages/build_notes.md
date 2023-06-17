title: Site Notes
date: 2010-12-03 10:20
Modified: 2010-12-03 10:20
Tags: documents
Slug: how this was made
Authors: clexp
Summary: <img align="left" width="100" height="100" src=/images/#.jpg>A story about how I put this together




### Static or dynamic
It took a while before I knew what this meant, but reading around, I could see a static site would be more than adequate for a block site. The number of frameworks was endless, but I reduced to the size by considering python only frameworks. Distil left a reasonable number of competitors, and it was hard to strike a balance between a marketing site and documentation blog. I did not really want the documentation site as I am demonstrating a learning journey which is a human and visual thing for the journeyman as it also is for the listener to the story.

Many of the static sites did not seem to have much in terms of image control. It seems they're mainly for text and documentation. Nick docs, and Sphinx seem to be quite competent documentation building sites. I was paralysed with decision so I just had to choose something. Pelican seemed pretty well supported an active so I started using it.

### Write a theme or pick one?
I took some time to work my way through the themes list and there was some close contenders. I wondered about writing my own theme on a journey to learn machine learning not web development, so I picked a theme.

### Write in html? ugh!
I wanted to write in Mark down, because this is much easier to see when editing it than HTML. I was using the Obsidian markdown editor. This is very powerful tool and I'm probably only using 10% of it. This tool is learning journey in its self. At some point, you've got to come back out of the rabbit hole and go back to the one you meant to go down. I found a pelican Ken format marked down to HTML. I wrote a series of posts in a new Obsidian vaults and copied them over to the Pelican content folder. This may have been an unnecessary, unnecessary step, but I did not want to include the markdown files in the pelican content folder. Having done it for awhile, there may be a workaround

### Ship it!  Ship it!  Ship it! 
Having listened to a lot of podcasts about software development. I found an interesting take that I found a personal challenge. Being a bit of a perfectionist engineer I want things to be just right before I put them out into the world. This is meant that I have some projects which, after much investment I have abandoned because there's not felt ready. Some commentators indicate ship a minimum viable project product as early as possible that will guide the remaining work. I felt once I had markdown and formatted the thing into a static site on my home machine, I would need to get something on a server out there.   Having a chain to get up to a server that would force me to focus on what was important

### Which hosting service?
There are endless hosting services that can provide free or cheap hosting a static and small sites. For awhile, I was trying to Roku, but they begin to charge a fee. Then, after a while, I found a few other sites, such as slide, audio, render and nullify. I then went onto also fine history microblog and mixer. I found mixer through some obsidian blocks. History seems to be focused on the station customers. Micro block seems to be doing a lot for me. That would be very quick but essentially that makes it almost another Wickes or WordPress. I'm trying to learn as much as I can, this means I do have to go down some rabbit holes. I might use a few different services to get a feel for how these providers work. I settled on Netlify

### picture thumbnails
I really wanting a picture in each article summary and this was half done.  I found this [https://stackoverflow.com/questions/43991473/pelican-add-image-to-summary] which told me what to modify.  