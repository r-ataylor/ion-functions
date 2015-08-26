def version(version_number):
    """Wrapper to add version to ion function
    Version matches that of the last update in the
    doc string for function with '-' replaced with '.'
    e.g 2015-05-12 becomes 2015.05.12
        """
    def decorate(f):
        f.version = version_number
        return f
    return decorate