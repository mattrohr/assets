## About

This repository contains assets such as images and PDFs used in my other GitHub project READMEs.

### Why alternative hosting methods are insufficient:

Often developers place these assets in the `main` repository branch, but this increases clone size. Additionally, because the images are part of the git history, the clone size is permanently inflated. In particular, animated project demonstration gifs can increase the repository size by orders of magnitude.

Another popular option is to host assets on platforms like [imgur.com](www.imgur.com). However if an image needs to be updated, some problems arise: 1) since Imgur URLs are unique (e.g. [https://i.imgur.com/leTGjlH.jpg](https://i.imgur.com/leTGjlH.jpg)) you need to change the README.md URL every image update, and 2) overtime your Imgur account will grow into an unorganizable mess. Additionally [imgur.com](www.imgur.com) only hosts images, not other file types like excel for bill of materials. Generic file hosting services like [dropbox.com](www.dropbox.com) are an option, but they still have unique links, are time-consuming to upload and link to, and are not a traditional content distribution network (CDN) so they may not load quickly or at all when multiple people try and access an asset.

You could host files on your own server, but you would be using a free service like [GitHub Pages](https://pages.github.com) which uses GitHub for distribution anyway, or you pay, or you may not realize in time it doesn't have a robust CDN in the event one of your projects experiences dramatic virality.

A few developers keep assets in a separate `assets` branch, so at least the large binary assets are not a part of the history of the `main` branch, but a `git clone` still downloads all branches, so this is not ideal.

### Why this way?

Now, all of my personal projects keep their assets in this separate repository. This allows the benefits of git like change tracking without downsides like bloated clones, to be applied to images. Additionally, images can be statically linked to without needing to update the README.md hyperlink. For example:
```
<p align="center">
<img src="https://raw.githubusercontent.com/mattrohr/assets/main/dotfiles/demo.gif" width="636" alt="dotfiles demo">
</p>
```

### Drawbacks:
Downsides of this approach are size limits. 

1) GitHub blocks pushes that exceed 100 MB. To track files beyond this limit, you must use Git Large File Storage which is a paid service. So far the only files that approach that size are my project's demo data like [brainfreeze](https://github.com/mattrohr/brainfreeze) for which I can use a service like [dropbox.com](www.dropbox.com).

2) GitHub recommends keeping repo sizes under 5 GB, after which you may receive disapproving finger wags from no-reply@github.com. It's unknown if repo size will need to be shrunk if/when that limit is breached. If this becomes an issue, I'll host assets on my own server and domain.

## Acknowledgements
- [Anish Athalye](https://github.com/anishathalye) for the [idea](https://github.com/anishathalye/assets)