# CLAUDE.md

## REQUIREMENTS

* We use UV for package management. Only use UV!
* Do not compliment, butter up, be overly agreeable with the user. Doint that is considered a failure

## Project Overview

This is a static website for the Boston Robot Hackers community - a robotics makerspace and meetup group. The site is built with vanilla HTML, CSS, and JavaScript, focusing on modern design principles and responsive layout.

## Architecture

The project uses a simple static website structure:

- `index.html` - Main page with sections for news, meetings, and projects
- `styles.css` - Modern CSS with CSS custom properties (variables) and responsive design
- `script.js` - Basic JavaScript for navigation and placeholder functionality
- `images/` - Static assets including the robot logo

## Key Design Patterns

### CSS Architecture
- Uses CSS custom properties defined in `:root` for consistent theming
- Modern flexbox and grid layouts for responsive design
- Component-based class naming (`.card`, `.section`, `.hero`, etc.)
- Mobile-first responsive design with breakpoints at 768px and 480px

### JavaScript
- Event delegation for smooth scrolling navigation
- Placeholder functions for dynamic content loading (`loadMoreNews()`, `loadMoreProjects()`)
- DOM manipulation follows modern JavaScript practices

## Development

Since this is a static website with no build process:

- **Local Development**: Open `index.html` directly in a browser or use a simple HTTP server
- **Testing**: Manual testing across different screen sizes and browsers
- **Deployment**: Static file hosting (no compilation needed)

## Content Structure

The site features three main content sections:

1. **What's New**: News updates with image, title, content, and date
2. **Meetings**: Regular community events (Weekly Hack Night, Monthly Showcase, Workshop Series)
3. **Projects**: Current community initiatives with status indicators

Each content card follows a consistent structure with emoji icons, titles, descriptions, and metadata.

## Styling Notes

- Uses a professional color scheme with blue primary, red secondary, and amber accent colors
- Typography uses system fonts for optimal performance
- Hover effects and animations enhance user experience
- Box shadows and border radius create modern card-based layout