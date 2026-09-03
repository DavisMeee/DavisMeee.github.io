# Tong (Davis) Chen — Academic Homepage

Source for [davismeee.github.io](https://davismeee.github.io), an academic homepage focused on generative medical AI, surgical intelligence, multimodal learning, and vision-language-action models.

## Update the site

- Homepage content: `_pages/about.md`
- Profile and site metadata: `_config.yml`
- Navigation: `_data/navigation.yml`
- Visual styles: `assets/css/main.scss` and `_sass/`
- Profile image and favicons: `images/`

## Run locally

Install Ruby and Bundler, then run:

```bash
bundle install
bundle exec jekyll serve --livereload
```

The site will be available at `http://127.0.0.1:4000`.

## Citation data

The `Get Citation Data` GitHub Action updates the `google-scholar-stats` branch on a daily schedule. Set the repository secret `GOOGLE_SCHOLAR_ID` to the public ID from the Google Scholar profile URL.

## Theme

Built from [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io), which incorporates components from Minimal Mistakes and Academic Pages. See [LICENSE](LICENSE).
