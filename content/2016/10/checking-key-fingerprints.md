Title: Checking Key Fingerprints
Date: 2016-10-22 11:00
Category: Old
Tags: ssh, security
Slug: checking-key-fingerprints
Authors: easydevmixin
Summary: How to check the fingerprints of public keys
Status: published

# TL;DR;

- Checking a public-key fingerprint on Linux/Mac OSX:

```
ssh-keygen -lf <public key file>
```

- Checking a public-key fingerprint on macOS:

```
ssh-keygen -E md5 -lf <public key file>
```

# The problem

Sometimes I’ve found myself in the need of checking out if a public key I gave to some site (usually Github, Bitbucket and the likes) is the same one I already have in my machine.

**Turns out that usually only the public-key fingerprint is given**, not its whole content, and so it get complicated to verify if I still have that key or if I should delete it from the service.

# The solution

Usually the fingerprints are given using a MD5 hash of the file. We can check public-key fingerprints by using `ssh-keygen`:

```
ssh-keygen -lf <public key file>
```

This will work on Linux and Mac OSX. Nevertheless, If you happen to be using the new macOS Sierra, then you need to issue this command instead:

```
ssh-keygen -E md5 -lf <public key file>
```

Both commands will give you an output like this:

```
easydevmixin@easydevmixin.local $ ssh-keygen -lf id_rsa_example.pub
2048 MD5:c3:b0:8f:60:70:b4:dc:6c:28:61:12:b9:fb:e8:49:f3 easydevmixin@easydevmixin.local (RSA)
```

With that output it is straightforward knowing if the key you used in a service still is in your machine.

And for those of you who have arrived here, this is a goodie script that will print all your public-key fingerprints on screen:

    :::bash
    # fingerprints.sh
    for file in *.pub
    do
        echo $file
        ssh-keygen -lf $file
        echo
    done

Happy fingerprinting!
