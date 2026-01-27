Title: Easy Magento Session Storage
Date: 2015-08-07 11:00
Category: Old
Tags: magento,development,
Slug: easy-magento-session-storage
Authors: easydevmixin
Summary: Using Magento's storage system
Status: published

Today I needed to delete a session for a test customer on my Magento environment. I had no idea where sessions were stored, so I headed down to the database and looked for some `sesson-something` table. I found 4 tables with that name, but non had the content I was looking for (in fact they were empty).
So I’ve made a quick Googling and found that you can use mainly three session-storage types.
They are all setup on `app/etc/local.xml` with the tag `<session_save>`.

## File storage
In order to use a file storage for your sessions you just have to setup the following:

```
<session_save><![CDATA[files]]></session_save>
```

Et voilà! The sessions will be stored under `/var/session`.

## Database storage
Just use the following:

```
<session_save><![CDATA[db]]></session_save>
```

I got the sessions saved on the `core_session` table when using this one. Its main advantage over file storage is when one uses a clustered environment.

## Memcache storage
First of all, you need a Memcache server running and have access to it. For the rest it is quite simple to use, just a little bit more verbose than the previous two:

```
  <session_save><![CDATA[memcache]]></session_save>
  <session_save_path><![CDATA[tcp://localhost:12345?persistent=1&weight=2&timeout=10&retry_interval=10]]></session_save_path>
```

> You must adjust `localhost:port` to your own configuration.

With Memcache you can manage 1000’s of sessions at one time, but  its setup can be trickier, especially for peoplo who have never configured any.

So now you know how you can setup the most used session storage mechanisms in Magento.

Hope you find it useful and happy sessioning!

### Resources
I’ve found this great article by [Ashley Schroder](http://magebase.com/author/ashley/) which I just have summarized here: [Magento Session Storage: Which to Choose and Why?](http://magebase.com/magento-tutorials/magento-session-storage-which-to-choose-and-why/)
