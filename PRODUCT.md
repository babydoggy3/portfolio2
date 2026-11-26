# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS with vanilla JS, no framework, no build step, no site generator (pinned by the user's brief). CSS is authored in `styles.css` and inlined into `index.html` by `tools/inline-css.py`. Hosted on GitHub Pages as a project repo under the custom domain path `https://claudedaigan.com/portfolio2/`, so every URL in the page is relative.

## Users

- Recruiters and hiring managers screening Claude Daigan for an operations, automation or AI-workflow role. They arrive from LinkedIn, a job application or a shared link, skim on desktop between other candidates, and want to know fast what he has built, whether it is real, and how to reach him.
- Business owners evaluating him as an operations & automation / AI workflow builder. They mostly open the link on a phone, look for proof he can take repetitive work off their plate, and decide whether to email.
- ASSUMPTION (subagent run, no interview possible): roughly half of visits are on phones; desktop is the recruiter's default.

## Product Purpose

A one-page, project-based portfolio for Claude Lester Daigan (Central Visayas, Philippines), Operations & Automation Specialist. It is a sibling of his general portfolio at `/portfolio/` but shows only the engineering work: 11 projects (AI agents, RAG, n8n and Apps Script automations, Sheets systems), with the work history, skills and certificates as secondary support. Success = a qualified visitor opens a demo, then emails or connects on LinkedIn.

## Positioning

He came to automation from the operations seat itself (bank teller, HR assistant and aide, procurement officer, digital-marketing VA) and now automates that repetitive work (data entry, applicant screening, reporting, outreach) with Python, n8n and AI agents (LangChain, LangGraph, Deep Agents). Four projects are live, self-hosted demos a visitor can use; the rest are shared Google Sheets systems.

## Operating Context

- Visitors compare several candidates in one sitting; projects must be reachable and scannable from the first screen.
- Proof is external: live demos on `*.lackey43.duckdns.org`, Google Sheets and a Google Form, LangChain Academy and Coursera certificate pages, Google Drive files.
- This page must not link to the marketing site (claudedaigan.com root) or the other portfolio, and must not show a phone number, WhatsApp or Messenger.

## Capabilities and Constraints

- Content source of truth: `/opt/data/profiles/work/sites/portfolio/index.html` (name, title, description, availability, about, 10 skills, 11 projects with every link, 5 jobs, education, 9 certificates). Copy is used verbatim.
- Marketing design samples (Canva posts, reels, lead magnet, gym landing page, testimonial design, carousel) are excluded entirely.
- Contact channels: email `claude_daigan@protonmail.com` and LinkedIn `https://linkedin.com/in/claude-lester-d-a84558288/`. No others.
- Performance target: Lighthouse mobile performance >= 90, accessibility and best practices 100.

## Brand Commitments

- Name shown as "Claude Daigan"; title "Operations & Automation Specialist"; availability "Available".
- Voice: plain, first-person, specific, no hype ("I care about the unglamorous details, because that is where automation either holds up or quietly breaks.").
- Programmer / technology themed with strong animation and visuals (user's words). Must not resemble the `/portfolio/` "Moviehouse at Night" world or the marketing site's Messenger-thread world.

## Evidence on Hand

- 11 projects with live links; real screenshots of the four live demos (captured 2026-11-26) in `assets/img/shot-*.webp`.
- 5 roles 2019-2026, 1 degree, 9 certificates (local images in `assets/img/cert-*.webp`).
- Headshot `assets/img/profile-*.webp`.
- Absent and never to be fabricated: metrics, user counts, client names, testimonials, GitHub stars, uptime figures, years-of-experience totals, pricing.
- ASSUMPTION: the Google Sheets projects are shown with code-drawn visuals, not screenshots, because the shared sheets display trainees' names and emails.

## Product Principles

1. The working thing first: every project leads with what it does and a link to open it.
2. Specific over impressive: real tool names and plain verbs, no invented numbers.
3. One way to act: email first, LinkedIn second.
4. Respect the skim: name, role, contact and the first project inside one screen.

## Accessibility & Inclusion

WCAG 2.2 AA contrast, keyboard-reachable links, visible focus, reduced-motion respected (all decorative motion off), no blinking loops longer than 5 s. ASSUMPTION: no product-specific needs beyond AA were stated.
