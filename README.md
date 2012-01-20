Remote to Zip
=============

This is meant to be a goofy little script that will allow you to come up with a tuple of file names and urls
and then add those to a local zip file and save it.

Usage:
------
Download the file.

Type this:

    $ python remote_to_zip.py local=remote local=remote

`local` is the filename you want in your ZIP
`remote` is the location of the remote file, including protocol

Whatever your zip file name is you passed it, unzip that

    $ unzip john.zip

Done.

Why:
----
I had a need for it in a project and that was that.  I wanted to share it around so I just grabbed the key parts and
put them here.  For whatever reason I had a hard time figuring out how to grab a remote file easily and put the contents
into a local file.


jdb
