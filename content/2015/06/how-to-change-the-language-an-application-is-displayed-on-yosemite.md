Title: How to Change the Language an Application is Displayed on Yosemite
Date: 2015-06-15 11:00
Category: Old
Tags: mac, tips and tricks,environment
Slug: how-to-change-the-language-an-application-is-displayed-on-yosemite
Authors: easydevmixin
Summary: Change the language an application is displayed on Yosemite
Status: published

This is something I’ve learned today. I’m from Barcelona, Catalonia, so I have my main Mac OSX interface localized in Catalan. Not every application is translated to that language. By proximity, if an application is not Catalan-translated it uses Spanish and, if there is no Spanish translation it falls back to English.

Today I wanted to give a try to SourceTree. I regularly use Git on the command line, but I wanted to have a taste on how it feels to use Git with a GUI. There also are things that I find will be easier to do using a GUI rather than a command line CLI (e.g. staging separate parts of a file for different commits).

The thing is that the commands used on Git are in English and I’m also used to use English regularly for technical reading and writing (I always try to improve it either!). When I have started up SourceTree I’ve found that the interface was all in Spanish. Not a bad thing! But as I’m used to English I wanted it in English. So this is how I’ve achieved my goal.

Mac OSX stores some propertied for apps on keys (they call them plists files). One way to find out what are the keys for a given application is using the `defaults` command. So, opening a Terminal I have written this command:

    easydevmixin@bimbolane $ defaults find sourcetree | grep -i SourceTree

And the output has been:

            "SourceTree_0x1.25c8426p+28" =         {
    Found 1 keys in domain 'com.torusknot.SourceTreeNotMAS.LSSharedFileList': {
    Found 52 keys in domain 'com.torusknot.SourceTreeNotMAS': {
                    NSBundleIdentifier = "com.torusknot.SourceTreeNotMAS";
                    NSBundlePath = "/Applications/SourceTree.app";
                        default = "Open in SourceTree";
                    NSMessage = openInSourceTree;

The one key we are interested in is `com.torusknot.SourceTreeNotMAS `. If we want to read its content:

    easydevmixin@bimbolane $ defaults read com.torusknot.SourceTreeNotMAS
    {
        NSNavLastRootDirectory = "~";
        NSNavPanelExpandedSizeForOpenMode = "{712, 448}";
        "NSOutlineView Items Sidebar_magento_git" =     (
            4092625529179514928,
    ...
    lots of things here
    ...
        mergeArgs = "";
        mergeCmd = "";
        mergeTool = 0;
        showFileStatusViewOptionsTip = 0;
        trialLastReminderDate = "2015-06-08 14:38:40 +0000";
        windowRestorationMethod = 2;
    }

So, if `read` will give us the contents of a specific key, `write` will allow us to write a new content within it:

    easydevmixin@bimbolane $ defaults write com.torusknot.SourceTreeNotMAS AppleLanguages '("en-US")'
    easydevmixin@bimbolane $ defaults read com.torusknot.SourceTreeNotMAS
    {
        AppleLanguages =     (
            "en-US"
        );
        NSNavLastRootDirectory = "~";
        NSNavPanelExpandedSizeForOpenMode = "{712, 448}";
        "NSOutlineView Items Sidebar_magento_git" =     (
    ...

Now whenever I run SourceTree, a perfect English GUI show up to me :)

## Extra bonus

What if I wanted to show the SourceTrees’ GUI in English just once? In this case I could’ve launched the app from the Terminal with this command:

    easydevmixin@bimbolane $ /Applications/SourceTree.app/Contents/MacOS/SourceTree -AppleLanguages '(en-US)'

That would have launched SourceTree in English just for that time.

## Resources

If you are interested in this particular subject about deeply tweaking your system, I’ve found those references interesting:

- [Tons of defaults write commands](https://github.com/mathiasbynens/dotfiles/blob/master/.osx)
- [Man page for defaults command](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/defaults.1.html)
- [SECRETS: a database of hidden settings for Mac OS X](http://secrets.blacktree.com/)

Have fun!
