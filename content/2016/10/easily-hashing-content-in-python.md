Title: Easily Hashing Content of Any Size in Python
Date: 2016-10-13 11:00
Category: Old
Tags: python, development
Slug: easily-hashing-content-in-python
Authors: easydevmixin
Summary: Calculating MD5, SHA1, SHA256, etc... for any size in Python
Status: published

Sometimes need arises in order to check if some data has been tampered or not by chance or because a bilious user. Imagine downloading a file from the internet where the owner of the file has placed another file with the hash signature of the former. You want to check if the file you downloaded has the same signature as the one the author claims to have. If so, then you can be pretty sure it hasn’t been tampered.

Here is an implementation in Python 3.x to hash files and strings of any given size. The first implementation is probably more understandable by anyone having some programming experience. The latter is more idiomatic and makes use of the built-in function `iter(callable, sentinel)` (documentation [here](https://docs.python.org/3/library/functions.html#iter)). By default the algorithm used in order to do the hash is SHA1, but another one can be easily used just passing a new instance of it to the `hasher_alg` parameter.

## Basic hash utils file

    #!python
    # hashutils.py
    import hashlib
    from io import BytesIO

    BLOCKSIZE = 65536


    def digest_file(filename, hasher_alg=hashlib.sha1()):
        hasher = hasher_alg
        with open(filename, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        return hasher.hexdigest()


    def digest_string(content, encoding='utf8', hasher_alg=hashlib.sha1()):
        hasher = hasher_alg
        content_io = BytesIO(content.encode(encoding))
        buf = content_io.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = content_io.read(BLOCKSIZE)
        return hasher.hexdigest()
## Idiomatic hash utils file

    #!python
    # hashutils_idiomatic.py
    import hashlib
    from io import BytesIO

    BLOCKSIZE = 65536


    def digest_file_pythonic(filename, hasher_alg=hashlib.sha1()):
        hasher = hasher_alg
        with open(filename, 'rb') as afile:
            for chunk in iter(lambda: afile.read(BLOCKSIZE), b''):
                hasher.update(chunk)
        return hasher.hexdigest()


    def digest_string_pythonic(content, encoding='utf8', hasher_alg=hashlib.sha1()):
        hasher = hasher_alg
        content_io = BytesIO(content.encode(encoding))
        for chunk in iter(lambda: content_io.read(BLOCKSIZE), b''):
            hasher.update(chunk)
        return hasher.hexdigest()

I’ve based this post mainly from these answers given on StackOverflow:

- [Get MD5 hash of big files in Python](https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python)
- [Hashing a file in Python](https://stackoverflow.com/questions/22058048/hashing-a-file-in-python)

And that’s it! Happy hashing!
