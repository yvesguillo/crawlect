"""Scan contains Crawlect directories tree scan utils"""

def listFilesIn(paths = ".", files = [], recur = False, excl_ext_li = [], excl_dir_li = [], excl_fil_li = [], incl_ext_li = [], incl_dir_li = [], incl_fil_li = []):
    """Append all paths from specified path as Path object in a list and return it."""
    for path in paths.iterdir():
        # Inclusions parameters overrule exclusion parameters, so if a file is in the exclusion list and in the inclusion list, it will be listed.
        # If a file is in inclusion and its extension is in exclusion, the file will still be listed.
        if path.is_file() and (
                # FIle and extension include/exclude combinations.
                (
                    (path.name not in excl_fil_li and incl_fil_li == [] and incl_ext_li == [])
                    or
                    (path.suffix not in excl_ext_li and incl_ext_li == [])
                    or
                    (path.suffix in excl_ext_li and path.name in incl_fil_li)
                    or
                    path.name in incl_fil_li
                    or
                    path.suffix in incl_ext_li
                )
                # Future include/exclude rules such as the creator, Git or time related ones to be added here.
            ):
            files.append(path)
        # Inclusions parameters overrule exclusion parameters, so if a file is in the exclusion list and in the inclusion list, it will be listed.
        elif path.is_dir() and recur is True and (
            (path.name not in excl_dir_li and incl_dir_li == [])
            or
            path.name in incl_dir_li
            ):
            listFilesIn(paths = path, files = files, recur = recur, excl_ext_li = excl_ext_li, excl_dir_li = excl_dir_li, excl_fil_li = excl_fil_li, incl_ext_li = incl_ext_li, incl_dir_li = incl_dir_li, incl_fil_li = incl_fil_li)
    return files