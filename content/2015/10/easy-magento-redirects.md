Title: Easy Magento Redirects
Date: 2015-10-14 11:00
Category: Old
Tags: magento,development
Slug: easy-magento-redirects
Authors: easydevmixin
Summary: Easily redirecting in Magento
Status: published

In Magento it’s pretty easy to set a redirection. Say you want to redirect from `/products/abc` to `https://anothersite.com/whatever.html`. You can do that in a couple of ways.

## Using the Magento Admin
Go to `Catalog > URL Rewrite Management`. Once there click on the `Add URL Rewrite Button`. You can choose from the select to create a custom redirection, for categories or for products.

Lets choose the `Custom` option. There are 5 mandatory fields and a couple optionals.

**Type**: this is already filled up for us (it’s `Custom`)
**Store**: you must tell Magento for which store do you want to set up the redirection.
**ID Path**: this is just an identifier for the redirection. I use to place here the whole path I want to be redirected.
**Request Path**: a word of attention here! This is NOT the whole URL, but just the request part of the URL. So, for instance, if you have the URL `https://mymagentostore.com/a/url/to/be/redirected` on this field you must place `/a/url/to/be/redirected`.
**Target Path**: This is the whole URL you want your Request Path to be redirected to. E.g., `http://anothersite.com/whatever.html`.
**Redirect**: this is optional. Depending on your needs you will select here `Permanent (301)` or `Temporary (302)`.
**Description**: this is optional. Just write down a description for the redirection here if you like.

![Magento settings screen configuring a redirection]({static}../../img/easy-magento-redirects.png)

Once this is done, flush your cache and point your browser to the URL you wanted to be redirected. Now you should see the redirection taking place and the browser pointing to the redirected URL.

This is a very easy method in order to set up one redirection really quickly. Its main disadvantage is when you want to redirect a bunch of similar URLs to the same destination URL. Lets say “*I want to redirect everything under /images to https://myotherdomain.com/myimages/*“. I that case this method would be inefficient and you should take another approach to the problem.

## Redirections through .htaccess file
This is the way to go if you want to solve the problem of redirecting a bunch of URLs to the same destination URL.

Following the previous case, lets say we want to redirect everything under `https://mymagento.com/images` to `https://myotherdomain.com/images`.

Open your `.htaccess` file on your Magento root and look for the line stating `RewriteEngine on` (should be on line 117 or so). Write just beneath it the following:

    RewriteRule ^images/(.*) https://myotherdomain.com/images [L,R=301]

This will make Apache to care for the URLs having its request paths starting with `images/` and then permanently redirect them  to `https://myotherdomain.com/images`.

This is just one example. I’ve found more information regarding `mod_rewrite` (which is the Apache module where the rewrite conditions exist) on:

- [How To Set Up Mod\_Rewrite](https://www.digitalocean.com/community/tutorials/how-to-set-up-mod_rewrite)
- [Apache Module mod\_rewrite](http://httpd.apache.org/docs/current/mod/mod_rewrite.html#rewriterule)

Happy Magento redirects!
