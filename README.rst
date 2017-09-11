gblinks
===============================

Broken links!

Oh man, Gitbook is such a nice tool to handle your documentation, but it's so easy to mess it up and add broken links here and there, right?

Gblinks is a easy to use tool to detect those links on time so you can fix them before publishing your documentation. The process can even be integrated in your CI workflow!

Cool, where do I get it?
------------------------

Make it easy and get it from pip:

::

    $ pip install gblinks

If the version there is a bit outdated or you need a patch that is not in master yet, you can get it directly from GitHub:

::

    $ git clone https://github.com/davidmogar/gblinks.git
    $ cd gblinks
    $ python setup.py install

And now what?
-------------

Now you use it ;)

This is the easier part. You only have to run the next command:

::

    $ gblinks -v PATH_TO_YOUR_GITBOOK

The output will be something similar to this:

.. code:: json
		[
        {
    		    "file": "my_gitbook/README.md",
    		    "link_path": "my_gitbook/chapter2/README.md",
        		"link_text": "chapter 2",
		        "link_url": "#chapter2"
    		},
    		{
        		"file": "my_gitbook/README.md",
    		    "link_path": "my_gitbook/chapter10/contributors.md",
        		"link_text": "Contributors for this chapter",
		        "link_url": "#contributors"
    		}
    ]

You can also remove the verbose flag to get only a warning with the number of broken links.

If your want to check what options you can use with gblinks, just run the next command:

::

		$ gblinks --help

I have a fix/new feature
------------------------

That's great. Contributors are always welcomed. Just send a pull request and be part of gblinks!
