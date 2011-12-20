# This script will take a tuple of URLs and place them in a zip file.

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
    ('dialog.png', 'http://s3.amazonaws.com/scrippsmedia/bundles/dialog.png'),
)

zip_from_remote(files, 'john.zip')