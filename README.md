# Happy Dussehra — Rama's arrow and Ravana Dahan

A free, mobile-friendly, interactive Vijayadashami greeting. Click **Release the arrow** to see Rama's correctly oriented bow, an arrow flying toward ten-headed Ravana, the Ravana Dahan effect and an English/Hindi greeting. Replay and WhatsApp sharing are included.

## Publish as a free GitHub Pages site

1. Visit **[Settings → Pages](https://github.com/shwetadinkar/dussehra-greeting/settings/pages)** for this repository.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Set **Branch** to `main` and **Folder** to `/(root)`. Click **Save**.
4. When GitHub finishes publishing, visit **https://shwetadinkar.github.io/dussehra-greeting/**.
5. Test the arrow, fire, English/Hindi and replay. Then share the same link in WhatsApp.

**Do not share until the website opens**. The website is public and costs nothing on the GitHub Pages free tier for this static site.

## Files

- `index.html`: complete standalone interactive greeting
- `scripts/generate_preview.py`: renders the corrected stage into an OG/WhatsApp thumbnail
- `.github/workflows/preview.yml`: commits `preview.png` automatically whenever the page changes (or from Actions → Run workflow)
- `preview.png`: automatically generated WhatsApp preview image, after the workflow succeeds

The frontend is plain HTML, CSS, SVG and JavaScript. No Python server or API is required to serve it; Python is used only to create the preview image. No names or personal details are collected.

To test locally:

```bash
python -m http.server 8000
```

Then open http://localhost:8000 in your web browser.
