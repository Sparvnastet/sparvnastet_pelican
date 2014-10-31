# Sparvnastet Pelican
## Project serving static pages for sparvnastet.org

### Getting up and running

Start off with creating a virtualenvironment.
If you haven't already, install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

    mkvirtualenv sparv_pelican

    pip install Markdown
    pip install pelican
    pip install pelican-vimeo
    pip install pelican-youtube
    pip install fabric
    pip install ghp-import

    git clone git@github.com:Sparvnastet/sparvnastet_pelican.git


### Development server
Activate your virtualenvironment and start the development server on localhost:8000

    workon sparv_pelican
    ./develop_server.sh start


### Installing Foundation
We use [foundation.zurb.com](foundation.zurb.com) as framework for the CSS stuff.

    sudo npm install -g bower grunt-cli

    gem install foundation

You need Ruby installed for this since Foundation uses SASS which is built with Ruby.

More information on foundation and the installation process here
[http://foundation.zurb.com/docs/sass.html](http://foundation.zurb.com/docs/sass.html)

### Adding content
Pages to be published are saved in the ``content`` directory.
Running either ``make html`` or ``fab build`` will process the content data
and store the resulting output it in the ``output`` directory.

#### Naming pages
Prepend every page with the current date like
``2014-03-04-this-is-the-filename.rst``. This will help us keep the files in
 order. This doesn't affect anything visible. The actual publish date is set
  in the meta tag in the file like:

    :title: The Page title
    :date: 2012-07-26 00:00
    :modified: 2012-07-26 00:00
    :category: Blog
    :tags: a-tag-for-this-page
    :slug: the-slug
    :authors: Sparven
    :summary: a short content summary

``slug`` will be the title of the page and also the name of the file when
processed and placed in the ``output`` directory. A file with ``:slug:
sparvnastet`` will end up as ``output/sparvnastet.html``


### Compiling ``markdown`` and ``rst`` files to ``html``

Run ``make publish`` to generate HTML-files from your sources.
NOTE that this will first delete everything in the ``/output`` directory.


### Adding files for publishing

Add files that you want to be uploaded the ``/content/files`` directory.
The contents of the following directories will be copied from ``/content``
to ``/output``

    STATIC_PATHS = [
        'images',
        'files'
    ]

To define more directories, change the values in ``pelicanconf.py``


### Publishing to sparvnastet.org

The page is served on [sparvnastet.github.io](sparvnastet.github.io).

Run ``make github``. This will first run the ``publish`` command, then run the ``ghp-import`` script
and add all changes to the ``gh-pages`` branch before pushing it to github.
It will then push the contents of the ``gh-pages`` branch to the ``sparvnastet.github.io`` repo.

NOTE: Never push anything directly to ``sparvnastet.github.io``


### Changing the layout

``Foundation`` is used for the presentation. Theme used is``themes/sparrowtheme``.
The current theme is defined in ``pelicanconf.py`` as::

    THEME = 'themes/sparrowtheme'


#### Compile CSS
Use Grunt to compile the SCSS into CSS

    cd themes/sparrowtheme/foundation/
    grunt

This will output the SCSS into the directory specified in ``themes/sparrowtheme/foundation/Gruntfile.js``


Structure of the theme directory

    themes/
        sparrowtheme/
            static/
                css/
            foundation/
                [foundation specific stuff]
                css/
                scss/
            templates/

The ``sparrowtheme/static/css`` directory contains the output from ``sparrowtheme/foundation/scss/`` after grunt (or any other)
build process has compiled the ``*.scss`` files into ``css``.


# Calendar

## Adding events to the calendar
The calendar resides in ``content/calendar/calendar.json``. To add an event simply add an object to the list in the JSON file.
NOTE: The calendar widget doesn't sort the events by date at the moment. It simply picks the first object as the latest event.



#### FAQ
+ Makefile:107: *** missing separator.  Stop.
- Ensure you're using real tabs and not spaces when editing the Makefile.