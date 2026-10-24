---
type: "prototype"
title: "Final prototype Travel Buddy"
stage: "Deliver"
status: "draft"
summary: "The final interactive prototype of Travel Buddy, a single HTML file that runs right in the browser. Open it right on the page or in a new tab."
takeaways:
  - "A single HTML file (about 2.6 MB after the images were compressed), nothing to install and no separate network needed for data; it uses React and fonts loaded from a CDN, so it needs the internet to open."
  - "It is a reference for developers and for the test round, not production code."
supports:
  - "[[D1]]"
  - "[[D2]]"
  - "[[D3]]"
  - "[[D4]]"
  - "[[D5]]"
  - "[[D6]]"
  - "[[D7]]"
embed: true
---
# Final prototype: Travel Buddy

The final interactive prototype of the project, replacing the wireframes in the Develop stage. The build plan and the list of screens are in [`10_Prototype_Plan.md`](../original-docs/10_Prototype_Plan.md); the lo-fi wireframes and the wireframes of the main screens are in the [Wireframe](../wireframes/index.md) document.

| File | What it is |
|---|---|
| `travel-buddy-final-prototype.html` | The interactive prototype, opened in a browser (double-click or view right on the page) |

**Note:** this is the version with compressed images (images at most 480 px wide, JPEG quality 50) so it is more than half lighter than the 6.8 MB original; the original stays in your project folder. The report loads this file when you open the page, not ahead of time. When you send the report to someone, use `python3 ../toolkit/skills/export-hub.py --bundle <folder>` so the file goes along.

**Limits:** this is a prototype, not a test result. Any conclusion about whether users understand or can use these screens needs evidence (see E1 and E2).
