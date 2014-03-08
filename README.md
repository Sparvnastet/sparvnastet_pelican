# Sparvnastet Pelican
## Project serving static pages for sparvnastet.org

### Getting up and running

Start off with creating a virtualenvironment.
If you haven't already, install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

    mkvirtualenv sparv_pelican

    pip install Markdown
    pip install pelican-vimeo
    pip install pelican-youtube
    pip install fabric

    git clone git@github.com:Sparvnastet/sparvnastet_pelican.git


### Development server
Activate your virtualenvironment and start the development server

    workon sparv_pelican
    ./develop_server.sh start



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

