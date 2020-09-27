# ISAT Slides Collection

General principles:

- each slides deck is described in a YAML manifest;
- the YAML manifest lists a number of Markdown files
  that compose the slides deck;
- a Python script "compiles" the YAML manifest into
  a HTML file;
- that HTML file can be displayed in your browser
  (you don't need to host it), or you can publish it
  (along with a few static assets) if you want.

## Getting started

Look at the YAML file corresponding to the deck that
you want to edit. The format should be self-explanatory.

Make changes in the YAML file, and/or in the referenced
Markdown files. If you have never used Remark before:

- use `---` to separate slides,
- use `.foo[bla]` if you want `bla` to have CSS class `foo`,
- define (or edit) CSS classes in [workshop.css](workshop.css).

After making changes, run `./build.sh once`; it will
compile each `foo.yml` file into `foo.yml.html`.

If you have problems running `./build.sh` (because of
Python dependencies or whatever),
you can also run `./start.sh` to start a web server exposing the slides,
it will start a docker container of `nginx:alpine` image
in the backgrund with its `/` root attached to current directory.  

To stop the container run `./stop.sh`.

(but the slides should also work if you load them from your
local filesystem).
