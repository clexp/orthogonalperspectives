# Building log for post

The purpose of this build log is to provide some material from which I can create a blog post about how this was built.

This was originally constructed in 2003 in Obsidian using markdown. Directly into the same directory I began using the pelican static site generator, and spent some time trying to develop the Gumby theme.

There have been significant side projects both technical and personal since then and it has taken a side line.

I have picked it up more recently since I have found LLM coding agents have been very helpful at improving my learning rate and productivity.

I realised that obsidian wanted to use templates, I could use Obsidian templates to create front matter that was in keeping with the pelican style. I did not necessarily need to do this as it was only a small boost. I also found that as the pelican project got bigger, there were lots of files that obsidian began to index but which slowed it down. You can mark some folders and files to be ignored by Obsidian, but this is work. I do not have to do if I keep pelican and obsidian separate.

Eventually, I moved Obsidian work to a different vault and kept the pelican work going.

It was clear I have covered a great deal of material and have a large number of posts many of which are not complete.

It was also clear that there were several functions not present in a blog which some might consider to be 'table stakes'.

## Recent Development Phase

With the help of an LLM coding assistant, I've been able to accelerate development significantly. The assistant has been particularly helpful with understanding Pelican's template system and debugging configuration issues that would have taken me much longer to resolve alone.

### Major Cleanup and Restructuring

The first major task was cleaning up the project structure. The directory had accumulated redundant virtual environments, Obsidian files, and various utility scripts scattered throughout. We consolidated to a single virtual environment (`the_journey`) and organized Python scripts into a dedicated `scripts/` directory. This cleanup removed notebooks that weren't appropriate for web development work and eliminated the Obsidian integration that was slowing down the build process.

The sidebar template had a logic error that was preventing categories from displaying properly. The issue was in the conditional statements - the template was checking `{% if DISPLAY_CATEGORIES_ON_MENU %}` when it should have been `{% if not DISPLAY_CATEGORIES_ON_MENU %}`. This kind of debugging would have taken me hours to figure out manually.

### Default Image System

One of the most useful improvements was implementing a default image system. Instead of having broken image links throughout the site, we created category-specific default images that automatically appear when posts don't have custom cover images. This was implemented through a Python script that generates default images for each category, and the template logic was updated to use these defaults intelligently.

### Branding and Identity

We spent considerable time working on the site's branding, particularly the title and strapline. The original "Journey to ML" felt too generic, and we explored various options that better reflected my unique position as someone with experience in mechanical engineering and medicine now navigating the AI landscape. The current strapline "Three professional journeys, one consistent approach: viewing complex systems from the outside" captures this well while connecting to Simon Sinek's "Start with Why" framework.

### Technical Infrastructure

The site now has proper development and production configurations, with draft posts working correctly in development but hidden in production. The sidebar has been cleaned up to show only categories and social links, removing the cluttered tags section. MathJax is already configured for LaTeX rendering, which is essential for the mathematical content I plan to include.

### Outstanding Work

Despite these improvements, the site still needs significant work. The content itself needs images and text completion - this is my responsibility. The contact form needs to be implemented using Netlify Forms, and Disqus comments need to be configured. The domain needs to be updated from the old Netlify subdomain to my custom domain clexp.net.

The favicon is currently hand-made pixel art that needs to be replaced with something more professional. Social media thumbnails need to be created, and the site needs proper testing to ensure the production deployment works correctly.

This development process has highlighted how LLM assistants can significantly accelerate technical work, particularly in areas like template debugging and configuration management that would otherwise require extensive trial and error.

## Domain and Deployment Strategy

### Site Renaming and Branding Update

In a recent development session, we successfully updated the site's branding from "Journey to ML" to "Orthogonal Questions" with the strapline "Lessons from orthogonal professions, bringing an informed Why". This involved:

- **Configuration Update**: The `pelicanconf.py` file was already correctly configured with `SITENAME = 'Orthogonal Questions'`
- **Content Updates**: Updated `content/pages/Home.md` to reflect the new branding and purpose
- **Site Rebuild**: Regenerated all HTML files to ensure consistent branding throughout
- **Cleanup**: Removed old output directories containing the previous site name

### Domain Configuration Strategy

After analyzing the domain setup requirements, we determined the optimal approach for deploying to Netlify while preserving existing services:

**Current Infrastructure:**

- `clexp.net` and subdomains currently point to OpenBSD VPS
- Multiple services planned for future subdomains
- Need to maintain flexibility for additional projects

**Recommended Solution:**
Use a subdomain approach rather than pointing the apex domain to Netlify:

- **Primary Domain**: `clexp.net` → OpenBSD VPS (main services)
- **Blog Subdomain**: `blog.clexp.net` → Netlify (this Pelican blog)
- **Future Projects**: `project1.clexp.net`, `project2.clexp.net` → Various services

**Benefits of This Approach:**

- ✅ Preserves existing VPS infrastructure
- ✅ Maintains flexibility for future projects
- ✅ Clear separation of services
- ✅ No disruption to current setup
- ✅ SEO-friendly with descriptive subdomain

**Implementation Steps:**

1. Configure CNAME record in Namecheap: `blog.clexp.net` → `your-netlify-site.netlify.app`
2. Add custom domain in Netlify dashboard: `blog.clexp.net`
3. Netlify will automatically provision SSL certificate
4. Future projects can use additional subdomains without conflicts

This strategy ensures the blog can be deployed without affecting existing services while maintaining the flexibility to add more projects under the `clexp.net` domain in the future.

## Content Migration and Portfolio Strategy

### Site Evolution and Content Separation

The site has evolved from a single "learning journey" blog to a **professional portfolio ecosystem** with specialized sites for different content types:

**Current Portfolio Sites:**

- `100DOP.clexp.net` → Python course content (100 Days of Python)
- `blog.clexp.net` → Technical posts (sysadmin, C++, Rust, Arduino)
- `books.clexp.net` → Book reviews (Django backend)
- `orthogonalquestions.clexp.net` → Professional thought leadership

**Future Sites:**

- `hsma.clexp.net` → Data science & operational research
- `portmathlio.clexp.net` → Mathematical journey & ML skills

### Content Migration Process

**Programming Posts Migration:**

- Created export script to convert Pelican posts to Zola format
- Exported 6 programming posts to `export_programming_posts/`
- Removed Programming category from Pelican site
- Posts ready for import to Zola-based tech blog

**Book Reviews Migration:**

- Created export script to convert Pelican posts to Django-compatible JSON
- Exported 9 book reviews to `export_book_reviews/`
- Generated individual JSON files and combined `all_books.json`
- Ready for bulk import to Django book site

**Math Content Strategy:**

- Mathematical posts will migrate to `portmathlio.clexp.net`
- Keep only math-related commentary/opinions on this site
- Cross-link between sites for context

### New Site Focus

This site now serves as the **"professional thought leadership platform"**:

- ✅ **Commentary on current affairs**
- ✅ **Literature reviews and insights**
- ✅ **Podcast reviews and reflections**
- ✅ **Cross-disciplinary perspectives**
- ✅ **Professional development insights**
- ✅ **Links to specialized portfolio sites**

### Technical Improvements

**Footer Positioning Fix:**

- Added CSS flexbox layout to pin footer to bottom for short posts
- Footer now stays at bottom regardless of content length
- Maintains proper scrolling behavior for long posts

**Branding Updates:**

- Updated site title to "Chris M Lewis"
- Changed strapline to "From Engineering and Medicine: professional perspectives"
- Removed "alternative" to avoid political connotations
- Positioned as professional thought leadership platform

This portfolio approach provides clear separation of concerns while building a cohesive personal brand across multiple specialized sites.

## The Great Migration: When One Blog Became Many

### The Problem with Monolithic Content

The original site had become a digital equivalent of that drawer everyone has - the one where you throw everything from receipts to spare keys to that mysterious cable that might be important someday. We had programming tutorials next to book reviews next to mathematical proofs, all competing for attention like guests at a particularly awkward dinner party.

The solution was elegant in its simplicity: **specialization**. Each content type would get its own dedicated space, like a well-organized kitchen where the knives have their own block and the spices are alphabetized (in theory, at least).

### The Export Script Chronicles

Creating the export scripts was a lesson in the difference between "working" and "working well." The first attempt at converting Pelican's frontmatter to Zola's TOML format resembled a particularly enthusiastic game of digital telephone - information got lost, dates became confused, and tags went rogue.

After several iterations that would have made a coder weep, we finally achieved something that actually worked. The programming posts emerged from their Pelican cocoons as fully-formed Zola butterflies, ready to flutter off to their new home at the tech blog.

The book reviews proved more challenging. Converting to Django-compatible JSON required a delicate dance between preserving the original content's soul while making it palatable to Django's rather particular database schema. The result was a collection of JSON files that looked suspiciously like a digital library catalog, complete with metadata that would make a librarian proud.

### The Branding Identity Crisis

The site's identity had been through more iterations than a startup's pitch deck. "Journey to ML" was too generic, "Orthogonal Questions" was too academic, and "Alternative Professional Takes" sounded like a political manifesto. We finally settled on "Chris M Lewis" with "professional perspectives" - a name that was at least honest about who was writing it.

The strapline evolved from "alternative professional takes" (which sounded vaguely rebellious) to "professional perspectives" (which sounded vaguely corporate). Progress, of sorts.

### Technical Challenges: The Footer That Wouldn't Stay Put

The footer positioning issue was a classic case of CSS behaving like a particularly stubborn cat - it would sit where you wanted it to, but only when it felt like it. Short posts left the footer floating in the middle of the page like a lost balloon, while long posts made it disappear entirely.

The solution involved flexbox, which is CSS's way of saying "let's make this complicated but actually work." The footer now behaves like a proper footer should - it stays at the bottom when there's little content and gracefully disappears when there's lots of content to scroll through.

### The Wide Post Problem

Some posts were so wide they made the sidebar look like it was trying to escape down the side of the page. The responsive design was responding, all right - it was responding by having a nervous breakdown. This remains an ongoing challenge, like trying to fit a square peg into a round hole while the hole keeps changing shape.

### The Missing Images Saga

The site was littered with references to images that didn't exist, like a digital version of Schrödinger's cat - the images both existed and didn't exist simultaneously, depending on whether you were looking for them. The default image system helped, but some posts still referenced images with names like "left_one.png" which sounded like they were named by someone who had given up on descriptive naming entirely.

### Current Status: A Work in Progress

The site now serves as a professional thought leadership platform, which is a fancy way of saying "the place where I put my opinions about things." The content migration has created a cleaner, more focused site, though the technical challenges of responsive design and proper layout remain ongoing.

The portfolio approach has transformed a single, overwhelmed blog into a network of specialized sites, each with its own purpose and personality. It's like going from a general store to a shopping mall - more organized, but you have to remember which store has what you're looking for.

The journey continues, as all good journeys do, with new challenges to solve and new content to create. The site may not be perfect, but it's honest about what it is - a professional platform for sharing insights from multiple professional backgrounds, one post at a time.
