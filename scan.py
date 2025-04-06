#! /usr/bin/env python3

from pathlib import Path

class Scan:
    """Scan class contains Crawlect directories tree scan utilities."""
    def __init__(self, crawler):
        self.crawler = crawler

    def listFilesIn(self, path = None, depth = None, files = None):
        """Append all eligible paths from `crawler.path` as Path object in a list and return it."""
        if files is None:
            files = []

        if depth is None:
            depth = self.crawler.depth

        if path is None:
            path = Path(self.crawler.path)

        for pathCandidate in path.iterdir():
            if pathCandidate.is_file() and self.isFileToInclude(pathCandidate):
                files.append(pathCandidate)
            elif pathCandidate.is_dir() and self.crawler.recur and depth >= 1 and self.isDirToInclude(pathCandidate):
                files.append(pathCandidate)
                self.listFilesIn(path = pathCandidate, depth = depth-1, files = files)
        return files

    def isFileToInclude(self, path):
        """
        Filter file `path` according to filtering rules.
        All files pass if there are no rules.
        Inclusion overrules exclusion.
        File-name rules takes precedence against extension rules.
        """
        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_ext_li == () and self.crawler.excl_fil_li == () and self.crawler.incl_ext_li == () and self.crawler.incl_fil_li == ():
            return True

        # Forcibly included by file-name always wins:
        if path.name in self.crawler.incl_fil_li:
            return True

        # Forcibly included by extension and not excluded by file-name wins:
        if path.suffix in self.crawler.incl_ext_li and path.name not in self.crawler.excl_fil_li:
            return True

        # Forcibly excluded by extension looses if not saved by file-name inclusion:
        if path.suffix in self.crawler.excl_ext_li and path.name not in self.crawler.incl_fil_li:
            return False

        # Forcibly excluded by file-name always looses:
        if path.name in self.crawler.excl_fil_li:
            return False

        # Is neither forcibly included or excluded but an extension or file inclusion is overruling:
        if self.crawler.incl_ext_li != () or self.crawler.incl_fil_li != ():
            return False

        # If I forgot some case scenario, you may pass Mr Tuttle:
        return True

    def isDirToInclude(self, path):
        """
        Filter directory `path` according to filtering rules.
        All directories pass if there are no rules.
        Inclusion overrules exclusion.
        """
        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_dir_li == () and self.crawler.incl_dir_li == ():
            return True

        # Is forcibly included:
        if path.name in self.crawler.incl_dir_li:
            return True
        
        # Is forcibly excluded:
        if path.name in self.crawler.excl_dir_li:
            return False
        
        # Is neither forcibly included or excluded but a directory inclusion is overruling:
        if self.crawler.incl_dir_li != ():
            return False
        
        # If I forgot some case scenario, you may pass Mr Tuttle:
        return True


