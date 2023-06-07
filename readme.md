# sidcode.github.io / cyber-physical.space (2021-) / siddhantsci.org (2012-2016)

## Wait, but why wasteful website!
Because I'm too cool for Instagram and TikTok and too lazy for long-form content. And also because I can. Like most martial arts, "self-help guides", and Thanos- I enjoy when it's _perfectly balanced, as all things should be_

It's hard to stop typing the above amidst the flow of insipid ideas. But _the hardest choices require the strongest wills_, so I'll stop with the Thanos references and get back to the point of the site. Note, there is none (like most things dualist and monist - see [Taijitu](https://en.wikipedia.org/wiki/Taijitu))

I, like many of my prolific peers born in 1994, am a younger brother of the Internet (or _internet_ for pesky pedants). This site is my jab at using the internet like it was meant- like experiencing an elder sibling with all their (in)finite wisdom and quirks. I am impacted by the connected consciousness galaxy brain of the internet everyday. The current domain name comes from my existence in cyber and physical spaces in equal measure (and probably my research on Cyber-Physical Systems). I also chose it because I got it for fairly cheap at ...wait for it... _Namecheap_.

Everyone is welcome here - friends, foes, family, stalkers, secret service spies, employers, bots, bosses...

The immutable TODO list (not for accountability, just for ego-massaging the natural notetaking narcissist in me) -

## Content- the creative craft that actually adds value

- Add a podcasts and audiobooks page / article / category where i review, reflect, rationalize, rant, regret, and ramble about them.
- Add a page for Cyber-Physical Spaces and how it relates to my life's lovely lore
- Merge _About me_ and _Stuff I've done_ pages. It's a feature of fundamental first-principles systems - **what it is, is what it does**.  
- Add backdated, present, and future dated posts - think _Tenet's_ time turnstiles (drafts underway behind the scenes). My name means _tenet_, by the way.
- Add a Design section for the site. Jeet Kune Do the site design from the best sites on the web - gwern, danluu, ssc, (derek)sivers, debarghyadas, peternorvig... (this list will continue to grow)

## Design- TODO 
- Load images and heavy stuff from a git submodule (Github Pages have a 1GB limit). Jeet Kune Do professes that having _no limitation_ is a limitation. So, we live with that.
- Fix home page UX. It should be a balance of narcissism and value
- Make description/summary appear for each article. Everyone loves TL;DRs.
- Add tools for popups, jupyter-plugin, video linker and citations/references. Basically, be a cheap [ripoff of gwern.net](https://www.gwern.net/About).
- Somehow balance the feature bloat with minimalism. Never forget _Perfectly Balanced_ and _DFTBA_.
- Prototype Python Pelican plugins properly - profit while at it!

## Reproducing the site

This is it. Everything you need to clone [this site](https://sidcode.github.io) is here.

The _master_ branch was [renamed](https://stackoverflow.com/questions/53377423/removing-github-profile-repos-from-google-search) to _main_ so Google and friends won't crawl its contents.
## How to build this website
You need pip, the Python package manager:

1. `pip install Markdown`
2. `pip install typogrify`
3. `pip install "pelican[markdown]"` and a few other plugins (liquid_tags, etc.)
4. That's it! You can now run `make devserver` from the root directory and navigate to localhost:8000.
5. `make ghp` is a nifty command which will generate updated content and push it to Github 

## About the website - by original author Lawler

When computer-programming/engineering types have a website, it's traditional to <del>brag about</del> explain the technology used to create and serve the site. I have no idea who actually reads these summaries, but for posterity's sake&hellip;

The website is a [static site](https://en.wikipedia.org/wiki/Static_web_page) created by [Pelican](https://github.com/getpelican/pelican), a Python static site generator. I added a few custom Python extensions to bend the Jinja2 templating engine to my will.

Lawler created the theme himself&mdash;both the desktop and mobile variants. The basis for the theme is Dave Liepmann's [Edward Tufte CSS](https://edwardtufte.github.io/tufte-css/), which powers the lovely serifed font and gorgeous margin notes you see throughout Lawler.io.

The code highlighting theme is Solarized Dark, my preferred color theme for... everything.

Major thanks to Jody Frankowski's [Blue Penguin theme](https://github.com/jody-frankowski/blue-penguin) (which, itself, was based on pelican-mockingbird) and Claudio Walser's [FH5CO marble theme](https://github.com/claudio-walser/pelican-fh5co-marble-example) as guides to figure out how to use some of Pelican's less-documented areas for advanced themes.
