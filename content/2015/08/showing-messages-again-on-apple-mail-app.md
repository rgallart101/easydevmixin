Title: Showing Messages (again) on Apple Mail App
Date: 2015-08-31 11:00
Category: Old
Tags: macos,apple,environment,
Slug: showing-messages-again-on-apple-mail-app
Authors: easydevmixin
Summary: Solving an unusual problem with Apple Mail by which messages were not showing up
Status: published

Today I’ve faced a problem. After quite a long time not using Apple’s desktop Mail app, I’ve found messages were not showing. I could see there were unread emails, but the app didn’t show them to me.

I found the solution to that problem on [Apple’s forum](https://discussions.apple.com/thread/2599231). Long story short if you ever have this problem:

1. Shut Mail down
2. Copy the file `\~/Library/Preferences/com.apple.mail.plist` (or `\~/Library/Preferences/com.apple.mail-shared.plist` if you have more than one account) to your Desktop. This is just for having a current backup copy of that file.
3. Get into Time Machine and restore a copy of the same file you know it was working (in my particular case I’ve chosen a copy two-and-a-half older). It will ask you to substitute the current file (you want to).
4. Open Mail. Your email messages should be showing again!

Cheers!
