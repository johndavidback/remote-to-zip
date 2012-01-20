# This script will take a tuple of URLs and place them in a zip file.
import sys

import urllib
import zipfile

def zip_from_remote(files, zip_name='out.zip'):

    # Let's create a zip file to use.
    zip_file = zipfile.ZipFile(zip_name, 'w')

    # So, take the list of files and go through it.
    for f in files:
        # Assuming they are in types like ('filename.png', 'url/to/file')
        local_file = urllib.urlretrieve(f[1])

        # This will bring back a tuple, where 0 = a local file copy, and 1 = the HTTP instance
        # So let's write that to the file with the name we provided
        zip_file.write(local_file[0], f[0], zipfile.ZIP_DEFLATED)

    # Close the zip file
    zip_file.close()

    # Clean up all the memory for our urllib.urlretrieve's
    urllib.urlcleanup()


files = (
    ('john.jpg', 'http://johndavidback.com/media/images/john.jpg'),
    ('sweet-cat.jpg', 'http://placekitten.com/g/200/300'),
)

#zip_from_remote(files, 'john.zip')

if __name__ == '__main__':
    # clean arguments
    files = []
    for arg in sys.argv:
        # __file__, you're not an argument. you're silly. get down from there.
        if arg == __file__:
            continue

        try:
            local, remote = arg.split('=')
        except ValueError:
            print 'Each argument is local=remote'
            sys.exit(1)

        files.append((local, remote))

    # well, we don't want to make an empty zip...
    if len(files) == 0:
        print 'Need at least one local=remote pair'
        sys.exit(1)

    zip_from_remote(files)
