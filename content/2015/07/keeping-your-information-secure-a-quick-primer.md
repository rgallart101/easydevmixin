Title: Keeping Your Information Secure (a quick primer)
Date: 2015-07-03 11:00
Category: Old
Tags: cryptography, gpg,security
Slug: keeping-your-information-secure-a-quick-primer
Authors: easydevmixin
Summary: A primer on using cryptographic tools on a Mac
Status: published

![GnuPG Logo]({static}../../img/keeping-your-information-secure-a-quick-primer-1.png)

Kings, emperors, politicians, diplomatics, small, medium and big companies, common people… one thing they all share is that probably, at a certain point in time, they all wanted to keep some kind of information secure. Here secure means “accessible only for those who have permission to do it so if anyone else tries to read that info it would be no different than a mess for him”.

The art of keeping information secure has evolved through time from plain substitution cyphers to complex mathematic computations. Luckily for us, there’s no need for us to be expert mathematicians.

In today’s post we will take a look at [GnuPG](https://www.gnupg.org/index.html) (GNU Privacy Guard), which is the free and open source port for [PGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) (Pretty Good Privacy) and acquired by Symantec on 2010.

You can use GnuPG on any of the currently major OSes:

- For Mac: [GPGTools](https://gpgtools.org/) or install `gpg` using [Homebrew](http://brew.sh/)
- For Windows: [GPG4Win](http://www.gpg4win.org/)
- For Linux: just install the GnuPG package on your preferred distribution

For this post I will be using GPGTools for Mac (unless otherwise stated).

## Symmetric and Asymmetric encryption ciphers (a bit of background)
In order to know what we are talking about we must know there are two types of encryption systems.
The classical system (symmetric system from now on) in which a secret is shared among the ones having access to the encrypted data. There are certain issues with the symmetric system. The first one comes with the key distribution. Suppose we want to write a message to a friend living on the other side of the world. How do we send the key in a secure fashion? That’s a big problem. Adding to that, if the message is intercepted by a third and this third is able to decipher its contents, he or she will also be able to craft a new message using the same key, and the final recipient will never know this has happened.

That doesn’t happen with the asymmetric system. In that system, a public and private key are generated for the user. The private key is used to sign messages we send to others and to decipher messages which have been sent to us. We must keep this private key and not share it with anyone. The public key is used by others to cypher messages addressed to us, and it can be shared with everyone. That makes very hard for an attacker to decipher a message addressed to us, not to say to craft a new message. And doing things in that fashion we can be sure that the message has been sent by the person who said has sent it (non-repudiability), it is authenticated (authenticability), has not been read while in transit (confidentiality) and has not been altered (integrity).

## Using symmetric encryption
With that knowledge let’s see how to encrypt some data.

Let’s say we have a file whose content is confidential and we want to share it with one of our colleagues. Previously we have met in person and we have stated that we will share the secret ‘oursecret’ to cypher and decypher data.

    ~/easydevmixin
    easydevmixin@bimbolane $ touch secret-doc.txt
    ~/easydevmixin
    easydevmixin@bimbolane $ echo "This is a very secret content" > secret-doc.txt
    ~/easydevmixin
    easydevmixin@bimbolane $ cat secret-doc.txt
    This is a very secret content
    ~/easydevmixin
    easydevmixin@bimbolane $ gpg --output secret-doc.txt.secret --symmetric secret-doc.txt

![Entering the passphrase: oursecret]({static}../../img/keeping-your-information-secure-a-quick-primer-2.png)

    ~/easydevmixin
    easydevmixin@bimbolane $ ll
    total 16
    -rw-r--r--  1 easydevmixin  staff    30B  1 jul 12:16 secret-doc.txt
    -rw-r--r--  1 easydevmixin  staff    78B  1 jul 12:18 secret-doc.txt.secret
    ~/easydevmixin
    easydevmixin@bimbolane $ cat secret-doc.txt.secret
    �Q
      %����=�(^�6=�jH����|�(���n�9=�������Ԫ��U�ŞJ�Մ6$�����èk��%~/

As you can see, when cyphering the file a dialog has opened asking us for the key. On different systems that can be different (e.g. asking for the password on the console). Once the encrypted file has been created you can see that it is just a bunch of apparently nonsense bytes put together and, hopefully, no one will be able to decipher it except the one with the correct key.

Lets now see how to decipher the message. Suppose we have sent the file via email to our colleague.

    ~/docs
    colleague@colleaguemachine $ ll
    total 8
    -rw-r--r--  1 colleague  staff    78B Jul  1 12:28 secret-doc.txt.secret
    ~/docs
    colleague@colleaguemachine $ gpg --output secret-doc.txt --decrypt secret-doc.txt.secret

It will ask for the password here, just like before.

    gpg: CAST5 encrypted data
    gpg: encrypted with 1 passphrase
    gpg: WARNING: message was not integrity protected
    ~/docs
    colleague@colleaguemachine $ ll
    total 16
    -rw-r--r--  1 colleague  staff    30B Jul  1 12:29 secret-doc.txt
    -rw-r--r--  1 colleague  staff    78B Jul  1 12:28 secret-doc.txt.secret
    ~/docs
    colleague@colleaguemachine $ cat secret-doc.txt
    This is a very secret content

Just like before, when deciphering GnuPG asks for the shared secret and now we can read the contents of the file.

As you can see by the line `gpg: CAST5 encrypted data` if you use symmetric cypher with no options by default GnuPG uses CAST5. If you want to use any other algorithm you can use the `--cipher-algo <algo>` where `<algo>` can be: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH, CAMELLIA128, CAMELLIA192 or CAMELLIA256. So, if we want to cypher the file using IDEA, we’d do the following:

    ~/easydevmixin
    easydevmixin@bimbolane $ ll
    total 8
    -rw-r--r--  1 easydevmixin  staff    30B  1 jul 12:26 secret-doc.txt
    ~/easydevmixin
    easydevmixin@bimbolane $ gpg --output secret-doc.txt.secret --symmetric --cipher-algo IDEA secret-doc.txt
    ~/easydevmixin
    easydevmixin@bimbolane $ ll
    total 16
    -rw-r--r--  1 easydevmixin  staff    30B  1 jul 12:26 secret-doc.txt
    -rw-r--r--  1 easydevmixin  staff    78B  1 jul 12:39 secret-doc.txt.secret

## Using assymmetric encryption
If we prefer to use asymmetric encryption for all the advantages that it has, first of all we need to have the public key for the recipient and to be included in our keyring. This is the keyring as showed by GPGTools for Mac.

![Image showing the GnuPG Keychain]({static}../../img/keeping-your-information-secure-a-quick-primer-3.png)

For other OSes the way you see your keyring could be different. So lets say I want to send the super secret file to Ramon Maria (with the email rgallart101).

    ~/easydevmixin
    easydevmixin@bimbolane $ ll
    total 8
    -rw-r--r--  1 easydevmixin  staff    30B  1 jul 12:26 secret-doc.txt
    ~/easydevmixin
    easydevmixin@bimbolane $ gpg --sign --encrypt --armor --recipient rgallart101@aaaaaaaa.aaa secret-doc.txt

    You need a passphrase to unlock the secret key for
    user: "Ramon Maria Gallart Escolà <rgallart@xxxxxxxxxxxxx.xxx>"
    4096-bit RSA key, ID 29BA241F, created 2015-01-13

![Entering the password to decypher the content]({static}../../img/keeping-your-information-secure-a-quick-primer-4.png)


    gpg: 1955B998: There is no assurance this key belongs to the named user

    pub  4096R/1955B998 2015-01-13 Ramon Maria Gallart Escolà <rgallart101@aaaaaaaa.aaa>
     Primary key fingerprint: 22F8 AAB2 8DD0 D760 BB46  871E 6C7F 0BEA 5D49 C0E1
          Subkey fingerprint: DBB9 B33D AB22 1419 437E  52BD 2116 D103 1955 B998

    It is NOT certain that the key belongs to the person named
    in the user ID.  If you *really* know what you are doing,
    you may answer the next question with yes.

    Use this key anyway? (y/N) y
    ~/easydevmixin
    easydevmixin@bimbolane $ ll
    total 16
    -rw-r--r--  1 easydevmixin  staff    30B  1 jul 12:26 secret-doc.txt
    -rw-r--r--  1 easydevmixin  staff   1,7K  1 jul 12:56 secret-doc.txt.asc

You can see there is a warning stating that the key could not belong to the person you are sending the file to. This is because the way GnuPG and PGP keyring work. As long as you know this public key belongs to the person you want to send the file to, it is OK to use it. Just use your common sense and take the appropriate precautions. For example, if you know the person, you can talk to him and compare the key ID.

Lets see how the encrypted file looks like.

    ~/easydevmixin
    easydevmixin@bimbolane $ cat secret-doc.txt.asc
    -----BEGIN PGP MESSAGE-----
    Comment: GPGTools - https://gpgtools.org

    hQIMAyEW0QMZVbmYAQ/+OLyP9nAq9Bnf2ludnWPIjyi8IMxhuPxiR2ybkCuAqqqp
    +HLAf8IeJoRIeboN7nLDnacOEP48I07/6WHxCFGP1kBOEzP7KtBCHz75+COUPX0C
    5Z9P1rhDkZldtFx/m2p0kgIaxomGH0ne4xryjVpOR2n6JUl2rUtrFpiHp7n8zndi
    hRsxe7cyOaT9yP1SUfJDH3Fc7jvZTRa+BPoIBW0O0f/xRVKEtzujs5do2QgFLBO4
    KTYiUSr7aV3gvVcF1zRd1JN79JQfPeO8HrYoCLCNvmpsS5c2Nk14ojVwpbl+AUZL
    pnKwdtu+Uo45E5J5x310k7uisCOCj1rO05X3o67qegspo+TUsnyYIrunRFg1CIdX
    sO3RIkw9UzY+goE3aA14TF+RZ16ITP2cw+nWoKeNK3KTcmbwfB9opz5qRIwuJaCv
    RnQq/KOE9WAZ2bnQfbSEatUCCwjM4zFN/p3MXg1FyJuLrle4Wc8gZzUTiwNMB/bB
    WFq1bIzPVxigEf3x9Uqs/m1CviG7I0VRs9Wd5tsn/91vPwFm+Ck4POn4LPuWd2gV
    lDjBOkQMqumATcG8hF6PBINcCHPmZaubSAPCe5B0E19wZfCLrRoj9lxIBMiSMnVm
    SjH9nj9oYqTkQVoN1dJiIGSdGjvxUJp+mUwuvJVkpKhL8cOTiyWDCxGkoiAUF1TS
    6QFhE5h13iuGy21PC3lVwFMmFG+Pt7kZ0giVf4kd/o0sKdodnUBoIBgM7JfrXxo0
    H/r86XK27YGxOykqciKsc5OZe2VUR9wp72OzdPlLclqdproNAUGd4z1fkGUshpP7
    vy2QMtLIKdAXboLv94kOmobhuybdzhyMvVL9zr4HKD7PMOBf2l6z3P7MiqNXFk4O
    9rK1ahNxJnV5oiD8xpsW1e1XHTjM/jnYNIl7UNcXY72P2vTsYMbv4DXDUnqK6b2n
    sVkDyq0MYo/oc83bVzgTobXGwUawb8fge9zor2Xr3YQK0eZOM2zJYfZmpcJST61T
    0eX6W0HyClCEYMhtxO2L5wxaXuSc71Nd+TmH6hw6xShXhr+AXAZwtrPd5NtO2KUi
    ECYJyKhKmz041mu91x+PExGATaSbyEU2ONOcnCb6uxc3UBFxmqD0ttccqf2qx67N
    KPl91wZGYA70l/+I6LoFWEG1mJ+GPYp6RGhfRX01DVZqmQLGfuxKyFzlc81dazdV
    RKBP+1OOtCSgO/Cxv1MqzqQ1R8yZ6LT4yelecrxnU0CPQpYgbOMtiC/05uhX0hcw
    Lw3txZdmhmaKCt/YykALqOcA+qZUi/9w7QmOG9HEBWdMNCxoZyqTm4BKAriCE78b
    58ywU5YQdDXwNNaOE4qq4okTIY2LMMwur8GvJOwHWOfZmNi5q3+0Gqd83zDxWDvL
    wYRM6genw8k0uJHJfeDlbXdzPn2KphG2gAQ48eLQHe81PghPkThIaQy2UU/omXyO
    nJC6yBG2c1JamAUteo0Id/Zq2ZZoVpy8gIqYIyp5I1umNIdXCSuI3nvWAq9iTBrL
    86njOpRucCbnTtv6eqj2Jbg0RCyyMLiU8UosTIjXXCkPuB2/zPbNG56R
    =mdx9
    -----END PGP MESSAGE-----
    ~/easydevmixin
    easydevmixin@bimbolane $

Now you can send the file secret-doc.txt.asc to its recipient and he will be able to decrypt it just in the same fashion we’ve done it with the symmetric file:

    ~/easydevmixin
    easydevmixin@bimbolane $ gpg --output secret-doc-1.txt --decrypt secret-doc.txt.asc

    You need a passphrase to unlock the secret key for
    user: "Ramon Maria Gallart Escolà <rgallart101@aaaaaaaaaaa.aaa>"
    4096-bit RSA key, ID 1955B998, created 2015-01-13 (main key ID 5D49C0E1)

    gpg: encrypted with 4096-bit RSA key, ID 1955B998, created 2015-01-13
          "Ramon Maria Gallart Escolà <rgallart101@aaaaaaaaaaa.aaa>"
    gpg: Signature made dc  1 jul 12:56:11 2015 CEST using RSA key ID 29BA241F
    gpg: Good signature from "Ramon Maria Gallart Escolà <rgallart@xxxxxxxx.xxx>" [unknown]
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    Primary key fingerprint: 943A 7E8A AED1 22DE 6E86  F959 75A3 F585 29BA 241F
    ~/easydevmixin
    easydevmixin@bimbolane $ ll
    total 24
    -rw-r--r--  1 easydevmixin  staff    30B  1 jul 14:47 secret-doc-1.txt
    -rw-r--r--  1 easydevmixin  staff    30B  1 jul 12:26 secret-doc.txt
    -rw-r--r--  1 easydevmixin  staff   1,7K  1 jul 12:56 secret-doc.txt.asc
    ~/easydevmixin
    easydevmixin@bimbolane $ cat secret-doc-1.txt
    This is a very secret content

And that’s all for this post. In future post we will see how we can manage our Keychain, how to integrate GnuPG with our mail client and more things.

Happy cyphering!
