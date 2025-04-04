"""Scan contains Crawlect directories tree scan utils"""

def listFilesIn(paths = ".", recur = False, depth = 10, excl_ext_li = [], excl_dir_li = [], excl_fil_li = [], incl_ext_li = [], incl_dir_li = [], incl_fil_li = [], files = []):
    """Append all paths from specified path as Path object in a list and return it."""
    for path in paths.iterdir():
        # Inclusions parameters overrule exclusion parameters, so if a file is in the exclusion list and in the inclusion list, it will be listed.
        # If a file is in inclusion and its extension is in exclusion, the file will still be listed.
        if path.is_file() and (
                # FIle name and extension include/exclude rules.
                # No rules let all files pass.
                (excl_fil_li == [] and excl_ext_li == [] and incl_fil_li == [] and incl_ext_li == [])
                or
                # File inclusion overrules all other rules.
                (path.name in incl_fil_li)
                or
                # Extension inclusion overrules all excepted file exclusion.
                (path.suffix in incl_ext_li and path.name not in excl_fil_li)
                or
                (
                    (excl_fil_li != [] or excl_ext_li != [])
                    and
                    path.name not in excl_fil_li and path.suffix not in excl_ext_li
                )
            ):
            files.append(path)
        # Inclusions parameters overrule exclusion parameters, so if a file is in the exclusion list and in the inclusion list, it will be listed.
        elif path.is_dir() and recur is True and depth >= 1 and (
            (path.name not in excl_dir_li and incl_dir_li == [])
            or
            path.name in incl_dir_li
            ):
            depth -= 1
            listFilesIn(paths = path, recur = recur, depth = depth, excl_ext_li = excl_ext_li, excl_dir_li = excl_dir_li, excl_fil_li = excl_fil_li, incl_ext_li = incl_ext_li, incl_dir_li = incl_dir_li, incl_fil_li = incl_fil_li, files = files)
    return files