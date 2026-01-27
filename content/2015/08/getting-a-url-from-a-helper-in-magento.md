Title: Getting a URL From a Helper in Magento
Date: 2015-08-06 11:30
Category: Old
Tags: magento,development,
Slug: getting-a-url-from-a-helper-in-magento
Authors: easydevmixin
Summary: How to get a URL from a Magento Helper object
Status: published

> Disclaimer: [please read my first post on Magento]({filename}./about-magento-posts.md)

TL;DR; use `$url = Mage::helper('module_name')->_getUrl('controller/action');`

I’m new to Magento and currently I’m doing some work on it. Today I needed to get a URL from my module in order to call the login functionality. As I’ve no previous experience on it I have had to dig deep on the Internet until I’ve met the Magento helpers.

It happens that helpers on Magento are methods you can define in your module and, as their name implies, help you do something. I like to keep controllers at their minimum so I take most of the ‘business logic’ to the helpers.

For this particular case I needed to check if a user was already logged in when heading to a specific URL or not. If not, I wanted to redirect him to the login page and then take him to the requested page. I make those checks on the helper for that module, and the login action I had created for the user to be able to log into my app was in a controller named LoginController (quite an original name, uh?) inside my controllers/ directory. So my question was, if I detect the user is not logged in or his session has expired, how can I redirect him to the login page and then take him to the page he had requested? I’ve found the answer on the helper.

You can invoke any helper in Magento as long as you have declared it on the module’s config.xml file. If you have done that, you invoke the helper this way: `Mage::helper('module_name');` and Magento *magically* instantiates the required helper for you to use it. Usually the file containing the methods is called `Data.php` and resides under the directory helpers/ inside your module. In there you can create the methods you find necessary to do your work. So, lets say we have a method named `myMethod()`. In order to call it you’d use `Mage::helper('module_name')->myMethod();` and the method would be executed.

How does this help us? Not too much, aside from knowing how to call our own methods. But it happens that a helper inherits from  the Magento class `Mage_Core_Helper_Abstract` and this class has a method named `_getUrl()` which we can use in order to get the url of a known controller action.

So, long story short, if I want to get my `login` action which resides in my `account` module I would do the following:

    :::php
    $loginUrl = Mage::helper('account')->_getUrl('account/login');

And that would return me the URL for the login page. A simple pseudocode for this could be something like this:

    :::php
    // this is app/code/local/Account/Helper/Data.php
    ...
    public function getUserData()
    {
       ...
       if ($his->userIsNotLogged())
       {
            // Get the login URL and then redirect there
            $loginUrl = Mage::helper('account')->_getUrl('account/login');
            header("Location: " . $loginUrl);
            die();
       }
       else
       {
            // do whatever to get the user info
       }
    }
    ...

The pattern is always the same:

    :::php
    Mage::helper('module_name_as_specified_on_config.xml') ->_getUrl('controller/action);

