Title: About
Date: 2015-06-19 11:00
Status: published

## So, what is this blog about?

As I say on ‘[Why a blog?]({filename}../2015/06/why-a-blog.md)’ I’ve always wanted to write one, but I had never had the time, the theme (as in subject) to talk about or whatever reason (as in excuse) imaginable not to do it.

I’ve been working in Barcelona, Catalonia, for almost 13 years as a developer, software analyst, project manager and teacher (not the 15 years doing all of that, but a bit of them from time to time). I’ve also been a year remotely working for a San Francisco located company as a software architect, regularly travelling there. You can check [my LinkedIn profile](https://www.linkedin.com/in/ramagaes/) if you wish. You are also welcome to connect with me!

In this blog I will try to put part of my experience and the things I’m still learning (which are a lot). My main focus is on Python and Django, but I have experience on Java and C# and I also like information security and sysops fields.

Some posts will be written as a way to show something that I know to you, so you can quickly start working on that particular thing. Others will be written as notes to myself, but that I think they could be useful for you. A few of them will be projects that I’d like to share with you while I’m being developing them. And maybe some of them will be about opinions I have about things happening related to development, security and privacy, etc…

Whatever it is, I’m sure you will find something appealing to you!

Cheers!

## 2026 update: from building things to breaking (and fixing) them

Ten years ago, **EasyDevMixin** (easydevmixin.com) was my corner of the internet to talk about building software: Python, Django, and the kind of engineering problems where the worst thing that happens is a failing unit test and a bruised ego.

Then something subtle happened.

I started caring *a lot* about what happens **after** the code ships.

At first it was the usual “sysops and security are interesting” curiosity. Then it turned into:

- “Why is this endpoint reachable from places it absolutely shouldn’t be?”
- “Who thought *this* was a reasonable permission model?”
- “Why is the ‘harmless’ feature on fire at 3am?”

Somewhere along the line, my job shifted from **writing features** to **preventing features from becoming crime scenes**.

### A very reasonable career progression (with absolutely no chaos involved)

Over the last decade, I gradually moved through a few worlds:

- **Developer → software architect / manager-ish roles**
  I spent years building systems, leading work, and generally trying to keep complexity from evolving into folklore.

- **Developer → product security / AppSec**
  I kept getting pulled toward the parts of the stack where “interesting” meant “someone will eventually exploit this.” Threat modeling, secure coding guidance, bug bounty workflows, fixing design issues that no lint tool will ever catch… that kind of fun.

- **Product security → incident response**
  Eventually, I wanted to be closer to the moment where theory meets reality. Incident response is where your assumptions get tested—politely, with a chair, and sometimes at 2am.

- **Incident response → digital forensics**
  These days I spend a lot more time asking questions like:
    - “What actually happened?”
    - “What evidence do we have?”
    - “What’s the timeline?”
    - “Why is that process named like that?”

  I enjoy the detective work, the method, the rigor—and the satisfaction of turning a messy situation into something understandable and actionable.

### So what will this blog be about now?
If/when I write here again, expect a mix of:

- **Security engineering and product security** (practical, not performative)
- **Incident response lessons learned** (the kind you don’t get from diagrams)
- **Digital forensics & investigation thinking** (how to reason, validate, and document)
- Occasional **developer nostalgia**, because I still love building things—I just like them better when they don’t accidentally become a free public API for everyone on the internet.

I’ll also be writing about **setting up local AIs for Product Security and exploit research**—how to run models locally, wire them into workflows, and use them to move faster *without* moving into questionable territory. The focus will always be **controlled, ethical, and legal** research… because my goal is to break software responsibly, not break laws creatively.

If you’re into that mix—welcome. If you’re not—also welcome, but I may gently point you toward the nearest “Hello World” for your own safety.

Cheers (still),

Ramon
