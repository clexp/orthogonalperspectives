# Site Construction Journey: Building a Professional Portfolio with Pelican

_This document chronicles the development journey of building a professional portfolio site using Pelican static site generator, from initial setup through feature implementation and ongoing improvements._

## Project Overview

**Site**: Chris M Lewis - Professional Perspectives  
**Framework**: Pelican 4.8.0 with Gum theme  
**Purpose**: Professional portfolio showcasing thought leadership in AI Ethics, Engineering, and Medical perspectives  
**Architecture**: Static site with multi-platform content strategy

## Phase 1: Foundation & Setup

### Initial Environment Setup

The project began with establishing a proper Python development environment. We created a virtual environment named `the_journey` to isolate dependencies and ensure reproducible builds.

**Key Decision**: Using `the_journey` as the virtual environment name rather than the generic `venv` - this reflects the personal nature of the project and makes it memorable.

**Dependencies**:

- Pelican 4.8.0 (static site generator)
- Markdown 3.4.3 (content formatting)
- Jinja2 3.1.2 (template engine)
- Feedgenerator 2.1.0 (RSS feeds)
- Docutils 0.20.1 (documentation)

### Content Architecture

The site follows a multi-category approach to organize diverse professional content:

- **AI Ethics**: Ethical analysis and commentary
- **Commentary**: Professional insights and perspectives
- **Literature**: Book reviews and technical documentation
- **Machine Learning**: ML concepts and applications
- **Maths**: Mathematical foundations and concepts
- **Podcasts**: Notes from AI/ML podcasts
- **Project**: Technical implementations
- **Python**: Python-specific learning

**Design Principle**: Each category serves a specific professional audience while maintaining cohesive branding.

## Phase 2: Theme Customization & Branding

### Gum Theme Adaptation

The project uses the Gum theme as a foundation, but heavily customized for professional presentation.

**Key Customizations**:

- Updated site branding to "Chris M Lewis" with subtitle "From Engineering and Medicine: contrasting professional viewpoints"
- Implemented category-based navigation
- Added professional color scheme (#3498DB primary)
- Enhanced typography for readability

### Navigation Structure

The navigation follows a logical hierarchy:

- Home: Landing page
- Portfolio: Multi-platform strategy explanation
- About: Professional background
- Contact: Professional contact information
- Site Notes: Development documentation

**UX Decision**: Keeping navigation minimal and focused on professional needs rather than blog-style navigation.

## Phase 3: Content Management System

### Draft/Published Workflow

Implemented a sophisticated content management system using Pelican's built-in draft functionality:

**Development Environment**: Shows both published and draft content for easy review
**Production Environment**: Shows only published content
**Netlify Deployment**: Uses `publishconf.py` to ensure only published content goes live

**Current Status**: 36 published articles, 49 drafts ready for review and promotion

### Image Management System

Created a comprehensive image management system with category-specific defaults:

**Default Images**: Each category has a professional default image
**Thumbnail System**: Automatic thumbnail generation for performance
**Fallback Strategy**: Generic defaults for missing images

**Technical Implementation**: Images stored in `/content/images/` with category-specific subdirectories

## Phase 4: Technical Challenges & Solutions

### Virtual Environment Cleanup

**Problem**: Multiple virtual environments causing confusion
**Solution**: Standardized on `the_journey` environment, removed redundant `venv/`
**Result**: Cleaner project structure and easier onboarding

### Template Error Resolution

**Problem**: Template files in content directory causing build errors
**Solution**: Moved `header.md` template to proper template directory
**Learning**: Pelican has strict separation between content and templates

### Search Implementation Challenges

**Problem**: Need for internal search functionality without external dependencies
**Initial Approach**: Google Custom Search (rejected - not internal)
**Current Implementation**: Basic search UI with placeholder functionality
**Next Steps**: Implement proper search index generation during build

**Technical Details**:

- Search bar added to navigation with emoji icon (🔍) to avoid font issues
- Search results page template created
- JavaScript routing implemented
- TODO: Actual search index generation

### Greek Character Issue

**Problem**: Search icon displaying as Greek characters due to font issues
**Solution**: Replaced icon font with emoji (🔍)
**Learning**: Icon fonts can be problematic across different systems

## Phase 5: Content Migration Strategy

### Multi-Platform Architecture

The site is part of a larger portfolio strategy:

- **Main Site** (current): Thought leadership and professional commentary
- **books.clexp.net**: Django-based book reviews
- **Specialized Tech Sites**: Tutorial and technical content
- **Personal Blog**: Personal reflections and insights

**Migration Progress**:

- ✅ Programming posts exported to Zola format
- ✅ Book reviews exported to Django JSON format
- ⏳ Mathematical posts (pending portmathlio.clexp.net)
- ⏳ Technical tutorials (pending specialized sites)

### Content Categorization

**Strategy**: Focus on thought leadership while moving tutorial content to specialized sites
**Result**: Cleaner main site focused on professional insights and commentary

## Phase 6: Development Workflow

### Build Process

**Command**: `make html` for static generation
**Development Server**: `make devserver PORT=8001` (port 8000 was occupied)
**Live Reload**: Enabled for automatic browser updates during development

### Version Control

**Strategy**: Git-based workflow with clear commit messages
**Branching**: Feature-based development for major changes
**Deployment**: Netlify integration for automatic deployment

## Phase 7: Current Status & Next Steps

### Completed Features

- ✅ Basic search UI implementation
- ✅ Professional branding and navigation
- ✅ Content management system
- ✅ Image management system
- ✅ Multi-category organization
- ✅ Draft/published workflow
- ✅ Netlify deployment ready

### Immediate Next Steps

1. **Complete Search Functionality**: Implement actual search index
2. **Add Comments**: Disqus integration
3. **Contact Form**: Netlify Forms implementation
4. **Social Media Integration**: Professional networking links

### Technical Debt

- Search functionality needs backend implementation
- Mobile responsiveness could be improved
- Theme could be modernized
- Some missing images need addressing

## Lessons Learned

### Design Principles

1. **Professional Focus**: Every feature serves professional presentation
2. **Content First**: Architecture supports content strategy
3. **Progressive Enhancement**: Start simple, enhance gradually
4. **Multi-Platform Strategy**: Don't try to do everything on one site

### Technical Insights

1. **Static Site Benefits**: Fast, secure, easy to deploy
2. **Template Limitations**: Jinja2 can conflict with JavaScript
3. **Virtual Environment Best Practices**: Clear naming and documentation
4. **Content Management**: Draft/published workflow is powerful

### Development Workflow

1. **Incremental Development**: Small, testable changes
2. **Documentation**: Keep work lists and site notes updated
3. **Testing**: Regular builds and deployment testing
4. **Version Control**: Clear commit messages and feature branches

## Future Vision

### Short Term (Next 3 months)

- Complete search functionality
- Add comments and contact forms
- Review and promote draft content
- Improve mobile experience

### Medium Term (6 months)

- Modernize theme design
- Add interactive visualizations
- Implement dark mode
- Complete content migration

### Long Term (1 year)

- Establish thought leadership presence
- Cross-link with specialized sites
- Professional networking integration
- Analytics and performance optimization

---

_This document serves as both a technical record and a narrative of the development journey, capturing not just what was built, but why decisions were made and how challenges were overcome._
