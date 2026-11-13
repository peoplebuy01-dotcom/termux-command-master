# Sanjay — Portfolio

A responsive, dark editorial-style personal portfolio built with plain HTML, CSS and JavaScript.

## Preview locally

From the repository root:

```bash
cd portfolio
python -m http.server 8000
```

Open `http://127.0.0.1:8000` in a browser.

## Deploy with GitHub Pages

The workflow at `.github/workflows/deploy-portfolio.yml` publishes this folder. In the repository, open **Settings → Pages** and select **GitHub Actions** as the build and deployment source if it is not already enabled. Then push a change to `main` or run the workflow manually.

## Personalization

Update `index.html` with verified project links and contact details. The current copy intentionally describes active learning areas rather than claiming professional certifications or expertise.

## Stack

- Semantic HTML
- Responsive CSS and reduced-motion support
- Small vanilla JavaScript navigation
- GitHub Actions + GitHub Pages

No build tools or paid services required.
