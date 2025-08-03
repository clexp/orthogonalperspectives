# This is the project planning file for the work list of the project.

## Done ✅

- [x] **Remove redundant venvs** - Kept `the_journey` virtual environment, removed unused `venv/`
- [x] **Fix template error** - Moved `header.md` template out of content directory
- [x] **Update .gitignore** - Added proper Python project ignores
- [x] **Clean project structure** - Removed redundant virtual environment files
- [x] **Verify Pelican build** - Site builds cleanly with no errors (46 articles, 54 drafts, 4 pages)
- [x] **Remove summaries**
- [x] **add back categories in a sidebar on the right** - Fixed sidebar template logic to show categories
- [x] **add tags in a sidebar on the right** - Removed tags section (too cluttered)
- [x] **Export programming posts** - Converted 6 programming posts to Zola format, removed Programming category
- [x] **Export book reviews** - Converted 9 book reviews to Django JSON format for books.clexp.net
- [x] **Update site branding** - Changed to "Chris M Lewis" with "professional perspectives" strapline
- [x] **Fix footer positioning** - Footer still floats up on short posts, needs CSS flexbox fix
- [x] **Fix wide posts layout** - Wide posts cause sidebar to spill to bottom, need responsive design fix
- [x] **Create AI Ethics category** - Added AI_Ethics directory for ethical analysis content
- [x] **Create portfolio navigation page** - Added portfolio page explaining multi-platform strategy
- [x] **Finalize site name** - Current "Chris M Lewis" branding not quite right, needs refinement
- [x] **Review and clean up utility scripts** - Removed notebooks, cleaned up redundant files
- [x] **set all posts to draft** - Status field workflow is working correctly!
  - ✅ Development: Shows published + draft posts
  - ✅ Production: Shows only published posts
  - ✅ Netlify will only show published posts (uses publishconf.py)
- [x] **Get images for posts** - Created default image system with category-specific defaults
- [x] **Get some maths in the posts** - MathJax already configured in theme, LaTeX rendering available
- [x] **Implement basic search bar** - Added search input to navigation with placeholder functionality
  - ✅ Fixed Greek character issue in search icon (replaced with emoji)
  - ✅ Created search results page template
  - ✅ Added search routing and JavaScript functionality
  - ⚠️ **TODO**: Implement actual search index (currently placeholder)

## High Priority Next Steps 🚀

- [ ] **Complete search functionality** - Current search is placeholder, needs proper implementation
  - [ ] **Option A**: Generate search index during build process
  - [ ] **Option B**: Implement client-side search library (Tipue Search, Fuse.js)
  - [ ] **Option C**: Use Algolia DocSearch (free for open source)
- [ ] **add comments** - Disqus integration already available in theme, just need to add DISQUS_SITENAME to publishconf.py
- [ ] **add contact form** - Use Netlify Forms for professional contact handling
- [ ] **connect social media** - Link LinkedIn, GitHub, Twitter, and Mastodon (mastodon.social)
- [ ] **Fix missing images** - Address `mech_two_cover.jpg` and other missing image references
- [ ] **Complete draft articles** - 54 drafts ready for publishing (huge content opportunity!)
- [ ] **Test Netlify deployment** - Ensure cloud deployment still works after venv cleanup
- [ ] **Update Netlify domain** - Change from clexp-ml-pathway.netlify.app to clexp.net
- [ ] **Configure custom domain** - Set up clexp.net with Namecheap DNS
- [ ] **Review and promote draft posts** - Select which of the 54 drafts to publish

## Content Enhancement 📝

- [ ] **Complete additional posts for courses and books** - Expand literature reviews and course notes

## Technical Features 🛠️

- [ ] **Get comments** - Add comment system (Disqus integration available in theme)
- [ ] **Add dark mode support** - Enhance user experience
- [ ] **Improve mobile responsiveness** - Better mobile layout
- [ ] **Create professional favicon** - Replace hand-made pixel art with consistent favicon across all blogs
  - Tools: Favicon.io, RealFaviconGenerator.net, Figma, Sketch/Adobe
  - Consider social media thumbnails (1200x630px) vs favicon (16x16px) - different design needs

## Code Quality 🧹

- [ ] **Remove redundant files** - Clean up unused files in templates/, etc.
- [ ] **Remove redundant code** - Optimize utility scripts
- [ ] **Ensure comments are up to date** - Document the codebase
- [ ] **Remove redundant variables/functions/classes** - Code cleanup
- [ ] **Set up auto documentation** - Document the build process

## Content Migration Plan 📦

### **Phase 1: Content Audit & Categorization**

- [ ] **Audit all existing posts** - Categorize each post by target site
- [ ] **Identify thought leadership content** - Keep only professional commentary/insights
- [ ] **Identify tutorial content** - Move to specialized tech sites
- [ ] **Identify personal content** - Decide if to keep or move to separate personal blog

### **Phase 2: Content Migration**

- [ ] **Move mathematical posts** - Export to portmathlio.clexp.net (when ready)
- [ ] **Move technical tutorials** - Export to appropriate tech sites
- [ ] **Move personal reflections** - Decide on destination (personal blog or keep)
- [ ] **Update internal links** - Point to specialized sites where appropriate
- [ ] **Create redirects** - Ensure old links still work after migration

### **Phase 3: Content Focus**

- [ ] **Keep only thought leadership** - AI Ethics, papers reviews, industry commentary
- [ ] **Remove tutorial content** - All how-to posts moved to tech sites
- [ ] **Focus on professional insights** - Commentary, analysis, perspectives
- [ ] **Cross-link strategy** - Link to specialized sites for detailed content

## Design & Style Updates 🎨

### **Theme Replacement**

- [ ] **Replace Gumby theme** - Current theme is "acceptable for now" but needs upgrade
- [ ] **Choose modern theme** - Clean, professional design suitable for thought leadership
- [ ] **Implement responsive design** - Fix wide posts and mobile layout issues
- [ ] **Update color scheme** - Professional palette for business audience

### **Visual Assets**

- [ ] **Replace stock art** - Current images are "horrible", need professional alternatives
- [ ] **Create custom favicon** - Professional favicon across all portfolio sites
- [ ] **Design social media thumbnails** - Consistent branding for social sharing
- [ ] **Add professional imagery** - High-quality images for posts and pages

### **Layout Fixes**

- [ ] **Fix footer positioning** - CSS flexbox solution for proper footer placement
- [ ] **Fix responsive design** - Wide posts breaking sidebar layout
- [ ] **Improve mobile experience** - Better mobile navigation and readability
- [ ] **Optimize typography** - Professional font choices and spacing

## Contact Form Implementation 📧

### **Netlify Forms Setup**

- [ ] **Design contact form** - Professional form with appropriate fields
- [ ] **Add Netlify form attributes** - `data-netlify="true"` and form name
- [ ] **Configure form handling** - Set up form submission and notifications
- [ ] **Add form validation** - Client-side and server-side validation
- [ ] **Test form functionality** - Ensure submissions work correctly

### **Contact Page Enhancement**

- [ ] **Update contact page content** - Professional contact information
- [ ] **Add form styling** - Match site design and branding
- [ ] **Add success/error messages** - User feedback for form submissions
- [ ] **Add spam protection** - Honeypot fields or reCAPTCHA if needed
- [ ] **Configure email notifications** - Set up form submission notifications

### **Professional Contact Information**

- [ ] **Add LinkedIn profile** - Professional networking link
- [ ] **Add GitHub profile** - Technical portfolio link
- [ ] **Add professional email** - Business contact method
- [ ] **Add portfolio links** - Links to other portfolio sites

## Under consideration 🤔

- [ ] **Add interactive visualizations** - For ML/math content
- [ ] **Implement RSS feeds** - Better content syndication
- [ ] **Add reading time estimates** - User experience enhancement
- [ ] **Create content series navigation** - Link related posts

## Current Status 📊

- **Articles**: 36 published, 49 drafts
- **Pages**: 6 (including new search page)
- **Hosting**: Netlify (cloud deployment ready)
- **Framework**: Pelican 4.8.0 with Gum theme
- **Development**: Local server running at http://127.0.0.1:8001
- **Search**: Basic UI implemented, needs backend functionality
