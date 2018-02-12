import setuptools

def configure():
# Initialize the setup kwargs
    kwargs = {"name": "coords",
              "version": "0.0",
              "author": "Malcolm White",
              "author_email": "malcolcw@usc.edu",
              "maintainer": "Malcolm White",
              "maintainer_email": "malcolcw@usc.edu",
              "url": "http://malcolmw.github.io/coords",
              "description": "Coordinate system transformations",
              "download_url": "https://github.com/malcolmw/coords.git",
              "platforms": ["linux", "osx"],
              "py_modules": ["coords"]}
    return(kwargs)

if __name__ == "__main__":
    kwargs = configure()
    setuptools.setup(**kwargs)
