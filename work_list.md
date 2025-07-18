# This is the project planning file for the work list of the project.

## Done ✅

- [x] **Remove redundant venvs** - Kept `the_journey` virtual environment, removed unused `venv/`
- [x] **Fix template error** - Moved `header.md` template out of content directory
- [x] **Update .gitignore** - Added proper Python project ignores
- [x] **Clean project structure** - Removed redundant virtual environment files
- [x] **Verify Pelican build** - Site builds cleanly with no errors (46 articles, 54 drafts, 4 pages)

## High Priority Next Steps 🚀

- [ ] Remove summaries
- [x] **add back categories in a sidebar on the right** - Fixed sidebar template logic to show categories
- [x] **add tags in a sidebar on the right** - Removed tags section (too cluttered)
- [ ] **add a search bar** - Options: Google Custom Search (easiest), Algolia DocSearch (free for open source), Tipue Search (JavaScript-based)
- [ ] **add comments** - Disqus integration already available in theme, just need to add DISQUS_SITENAME to publishconf.py
- [ ] **Fix missing images** - Address `mech_two_cover.jpg` and other missing image references
- [ ] **Complete draft articles** - 54 drafts ready for publishing (huge content opportunity!)
- [ ] **Test Netlify deployment** - Ensure cloud deployment still works after venv cleanup
- [x] **Review and clean up utility scripts** - Removed notebooks, cleaned up redundant files
- [x] **set all posts to draft** - Status field workflow is working correctly!
  - ✅ Development: Shows published + draft posts
  - ✅ Production: Shows only published posts
  - ✅ Netlify will only show published posts (uses publishconf.py)
- [ ] **Review and promote draft posts** - Select which of the 54 drafts to publish

## Content Enhancement 📝

- [x] **Get images for posts** - Created default image system with category-specific defaults
- [ ] **Get some maths in the posts** - Add LaTeX/MathJax rendering for mathematical content
- [ ] **Complete additional posts for courses and books** - Expand literature reviews and course notes

## Technical Features 🛠️

- [ ] **Get a search function** - Add search capability to the blog
- [ ] SKIP: **Get a word cloud** - Visualize content themes
- [ ] **Get comments** - Add comment system (Disqus integration available in theme)
- [ ] **Add dark mode support** - Enhance user experience
- [ ] **Improve mobile responsiveness** - Better mobile layout

## Code Quality 🧹

- [ ] **Remove redundant files** - Clean up unused files in templates/, etc.
- [ ] **Remove redundant code** - Optimize utility scripts
- [ ] **Ensure comments are up to date** - Document the codebase
- [ ] **Remove redundant variables/functions/classes** - Code cleanup
- [ ] **Set up auto documentation** - Document the build process

## Under consideration 🤔

- [ ] **Add interactive visualizations** - For ML/math content
- [ ] **Implement RSS feeds** - Better content syndication
- [ ] **Add reading time estimates** - User experience enhancement
- [ ] **Create content series navigation** - Link related posts

## Current Status 📊

- **Articles**: 46 published, 54 drafts
- **Pages**: 4 (About, Contact, Home, Site Notes)
- **Hosting**: Netlify (cloud deployment ready)
- **Framework**: Pelican 4.8.0 with Gum theme
- **Development**: Local server running at http://127.0.0.1:8000
