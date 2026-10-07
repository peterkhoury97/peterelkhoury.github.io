# Peter El-Khoury portfolio design

Date: 2026-10-07
Status: proposed written specification; project-first direction approved in chat.

## Purpose
Present Peter as a software engineer who builds useful products and dependable backend systems. Recruiters should quickly understand his Java/.NET experience; potential clients should see concrete applications and a clear way to contact him.

## Approach
A single responsive page built with semantic HTML, one stylesheet and a small JavaScript file. No framework, package installation, paid hosting, backend, or build step. All important copy and project content appear in HTML so the site remains usable without JavaScript.

The selected approach leads with projects. A CV-first alternative would give employment history more prominence but make the product work harder to discover. A minimal gallery would be quicker to scan but provide less evidence of Peter's contribution.

## Visual direction
Use a warm off-white background, dark navy typography, and a restrained orange accent. Large, confident typography and generous spacing establish a professional product-engineering identity. Put screenshots inside consistent browser-style frames, preserving the original interfaces rather than recoloring them. Use a system font stack to avoid external font dependencies.

Desktop: a concise header, spacious hero, featured project followed by a two-column project grid, then experience and contact. Mobile: single-column layout, readable screenshot previews, wrapping skill tags and a compact accessible menu. Avoid decorative animations that obscure project content.

## Page content
1. Header: name/initials, Work, Experience, About, and contact action.
2. Hero: Peter El-Khoury, software engineer, Riyadh/remote-friendly. Positioning emphasizes Java and .NET backends, automation and complete business applications. Actions: View my work and Get in touch; secondary Download CV.
3. Selected work: five project stories, each with an actual interface image, purpose, Peter's ownership, verified capabilities and technology tags. Do not invent customers, traffic, revenue, adoption or performance numbers.
4. Experience: Emcrey, Clover Broker, Onsite Snagging and earlier roles, with dates and concise responsibilities from the CV. Label this as CV-based experience; verify any current-employment wording before publication.
5. About and skills: short practical introduction, backend/API strengths, databases, cloud/deployment and automation. Education: Computer Science, Lebanese Canadian University, 2018.
6. Contact/footer: email, verified GitHub profile, CV download, and LinkedIn from the existing portfolio source after checking the link. No contact form requiring a server.

## Five project stories
### Pektrix chatbot
Use the ChatApp source and real widget/dashboard evidence. Describe an embeddable chatbot and messaging experience; verify AI/integration features against source before adding specific claims. Feature it first if its screenshots best support the hero story.

### FreshOps cleaning application
Show the operations overview or dispatch board. Explain how booking, customers, teams, dispatch and payments fit into one multi-company operations platform. Verified stack: ASP.NET Core and PostgreSQL.

### Trading scanners
One story with two clearly named parts: TradingView premarket/strategy scanning and P2P crypto price monitoring. Use separate screenshots in its detail view so readers do not assume a single application UI. Describe scanning, filtering and alerts without trading-return claims.

### LeadBot lead generation
Show the actual dashboard with safe demo or empty data. Explain business research, contact collection and export/Sheets integration. Verified stack: Python, Flask, async search, SocketIO and Redis.

### Sports Booking / OneGame
Use the older OneGame/Sports Booking application, not the unrelated generic BookingApp. Explain clubs, pitches, reservations and real-time communication. Verify web stack from its source; the CV separately supports Flutter/Google Maps work in the broader Sports Booking project.

## Screenshot sourcing and acceptance
- Inspect existing screenshots before use. Capture applications using local demo environments where feasible.
- Use actual application interfaces. Do not generate fictional screenshots or substitute a generic illustration.
- Capture no secrets, private customer information, leads, personal messages, tokens or account balances. Prefer empty or demo screens.
- Do not initiate scraping, send alerts/messages, place trades or change production data just to obtain images.
- If an older application cannot run because services are unavailable, inspect and render its existing frontend for an explicitly labeled interface preview if faithful rendering is possible. Record that provenance. If no faithful capture is possible, report the missing screenshot instead of claiming it is complete.
- Include at least one meaningful screenshot for each of the five project cards. The trading detail view can contain a screenshot for each scanner family.
- Save optimized, legible local images with useful alt text and declared dimensions. Show uncropped images in a keyboard-accessible enlargement dialog.

## Files and responsibilities
- index.html: complete readable content, project cards, metadata, navigation, contact and screenshot dialog markup.
- styles.css: design tokens, layout, browser frames, focus states, responsive behavior and reduced-motion support.
- script.js: menu behavior, screenshot enlargement and optional section navigation enhancement. Use native dialog behavior and restore focus when closing.
- assets/images/: local project screenshots.
- assets/Peter-El-Khoury-CV.pdf: supplied CV for download, inspected before publishing.
- .nojekyll: serve plain static assets without Jekyll processing.
- README.md: local preview and GitHub Pages deployment steps.
- docs/: specification and screenshot provenance.

Asset references use relative paths. No live project APIs are called by the portfolio. Project links appear only when their destinations and ownership are verified; do not link every card to a generic profile as if it were its repository.

## Behavior and error handling
HTML content remains visible with JavaScript disabled. The menu exposes expanded state and responds to keyboard activation. Screenshot enlargement supports Escape, a visible close button and focus restoration. Respect prefers-reduced-motion. A missing image must not collapse the card or conceal its description; fix missing assets before delivery.

Use email links for contacting Peter and a normal download link for the CV. No simulated form submissions or misleading live-demo buttons.

## Hosting
Prepare for GitHub Pages from a public repository on GitHub Free. Keep the site compatible with either peterkhoury97.github.io or a project repository URL. Default to branch-based root publishing to avoid unnecessary tooling. Verify the existing portfolio repository before selecting or modifying a remote. Build and preview locally first; do not claim deployment until a live URL is verified.

Official reference: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages.

## Validation
- Check all five project identities and all career details against source material.
- Inspect every screenshot at full size and in its card for sensitive content, legibility and correct attribution.
- Review desktop and mobile layouts, including 360px width; require no horizontal overflow or clipped controls.
- Exercise navigation, menu, CV download, email links, screenshot opening/closing, keyboard access and reduced motion.
- Check missing assets, broken relative paths and JavaScript console errors.
- Preview under both root and a repository-style subpath.
- Report any unavailable screenshot or unverified deployment explicitly.

## Self-review
Scope is one static page. Project identity, screenshot provenance, graceful behavior, asset paths and hosting are consistent. No placeholder project, fabricated metric, paid dependency or backend requirement is included. Implementation should begin only after the written-spec review required by the invoked brainstorming skill.
