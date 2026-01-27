Title: Connecting to HTTPS Using Openssl
Date: 2016-08-02 11:00
Category: Old
Tags: openssl, tips and tricks, development,
Slug: connecting-to-https-using-openssl
Authors: easydevmixin
Summary: How to use openssl as if it was telnet with https connections
Status: published

Sometimes I’ve found myself in the need of checking a website that works under HTTPS but didn’t want to use a browser for whatever reason. In those cases tools like **telnet** or **[httpie](https://github.com/jkbrzt/httpie)** do not work, as they are unable to handle the underlying SSL protocol. We can use **openssl** in those cases in order to establish a connection *à la* telnet.

Say we have a Django project running on a Ubuntu Server. The server is using Nginx in order to reverse proxy requests to GUnicorn which is passing those requests to Django. Adding to that, Nginx is also the SSL terminating point, meaning it holds the certificate in order to establish a secure connection between the client and the server, and it redirects all `http` requests to their `https` equivalents.

We’re good to go! Let’s see what happens if we use httpie to get an static asset from the server:

    vagrant@trust-prod-ubuntu-1404-lts:~$ http http://localhost/static/css/test.txt
    HTTP/1.1 301 Moved Permanently
    Connection: keep-alive
    Content-Length: 184
    Content-Type: text/html
    Date: Tue, 02 Aug 2016 10:51:50 GMT
    Location: https://localhost/static/css/test.txt
    Server: nginx/1.6.3

    <html>
    <head><title>301 Moved Permanently</title></head>
    <body bgcolor="white">
    <center><h1>301 Moved Permanently</h1></center>
    <hr><center>nginx/1.6.3</center>
    </body>
    </html>

As we can see Django response is a `301 Moved Permanently`. So let’s try to get this resource with httpie:

    vagrant@trust-prod-ubuntu-1404-lts:~$ http https://localhost/static/css/test.txt

    http: error: SSLError: [Errno 1] _ssl.c:510: error:14090086:SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed


Oops! Doesn’t look like it worked!

And here it is when openssl comes to the rescue. Establishing a secure connection using openssl works a lot like using telnet. Let’s have a look at how to do it:

    :::bash
    vagrant@trust-prod-ubuntu-1404-lts:~$ openssl s_client -connect localhost:443
    ...
    Lots of stuff about the https certificate
    ...
    ---
    GET /static/css/test.txt HTTP/1.1
    Host: localhost

    HTTP/1.1 200 OK
    Server: nginx/1.6.3
    Date: Tue, 02 Aug 2016 10:57:17 GMT
    Content-Type: text/plain; charset=utf-8
    Content-Length: 29
    Last-Modified: Tue, 02 Aug 2016 10:51:15 GMT
    Connection: keep-alive
    ETag: "57a07b23-1d"
    Expires: Wed, 03 Aug 2016 10:57:17 GMT
    Cache-Control: max-age=86400
    Pragma: public
    Cache-Control: public
    Accept-Ranges: bytes

    Hello! I am an static asset!

And here it is! We have been able to establish a secure communication channel with the server and get a resource.

I find that kind of things useful in order to test/debug certain aspects of web applications where I need to watch out for headers and more low-level stuff than the one you usually get from a web browser.

There are other reasons to do so. For example, wanna know if your server is vulnerable to [POODLE](https://www.us-cert.gov/ncas/alerts/TA14-290A)? Long story short, POODLE leverages a flaw in the SSLv3 implementation so a malicious attacker could see in ‘plain text’ things that should be encrypted. Let’s check it out!

    vagrant@trust-prod-ubuntu-1404-lts:~$ openssl s_client -connect localhost:443 -ssl3
    CONNECTED(00000003)
    140659731752608:error:14094410:SSL routines:SSL3_READ_BYTES:sslv3 alert handshake failure:s3_pkt.c:1262:SSL alert number 40
    140659731752608:error:1409E0E5:SSL routines:SSL3_WRITE_BYTES:ssl handshake failure:s3_pkt.c:598:

If the server was vulnerable the connection would’ve been successful and we should have had to take measures.

Ok! Enough for today. Now we have another tool for use in our tool belt!

Cheers!
