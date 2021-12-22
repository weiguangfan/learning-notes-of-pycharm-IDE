- `View | Tool Windows | Python Packages`;
    1. The `Python Packages` tool window shows installed packages and the packages available in the `PyPI repository`.
    2. Use the `Search` field to filter out the list of the available packages.
    3. You can preview package documentation in the documentation area, or you can click the `Documentation` link and open the corresponding resource in a browser.
    4. To delete an installed package, click `...` in the upper-right corner of the Python Package tool window.
    5. Install packages from repositories
        - Start typing the package name in the `Search` field of the `Python Package` tool window. You should be able to see the number of the matching packages.
        - Expand the list of the available versions in the upper-right corner of the tool window. Select the required version or keep it the latest.
        - Click the `Install` button next to the version list. Once PyCharm notifies you about successful installation, you should see the package in the list of the installed packages.
        - If needed, click `*` and provide a path to any custom repository you want to install from.
    6. Install packages from Version Control System
        - Click the `Add Package` link on the Python Packages toolbar and select `From Version Control`.
        - Specify a path to the target git repository. Refer to `pip documentation for more information about supported path formats`.
        - Select `Install as editable (-e)` if you want to install a project in editable mode (for example, setuptools develop mode).
    7. Install packages from a local machine
        - Click the `Add Package` link on the `Python Packages` toolbar and select `From Disk`.
        - Specify a path to the package directory or an archive (zip or whl).
    
- `File/Settings/Python Interpreter`;
    1. Install a package;
        - Click the `+` button on the package toolbar.
        - In the `Available Packages` dialog that opens, preview the list of the available packages.
        - To specify a custom repository, including devpi or PyPi, click `Manage Repositories`.In the `Manage Repositories` dialog that opens, click `+` add a URL of a local repository, for example, http://localhost:3141/root/pypi/+simple/, then click `OK`.
        - In the Available Packages dialog, click `O` reload the list of the packages.
        - Type the `name` of the package to install in the `Search` field. The list shrinks to show the matching packages only.
        - `Specify version`: if this checkbox is selected, you can select the desired version from the list of available versions. By default, the latest version is taken.
        - `Options`: If this checkbox is selected, you can type the `pip install command-line options` in the text field.
        - Select the target package and click `Install Package`.
    2. Uninstall a package
        - In the list of the packages, select the packages to be removed.
        - Click `-` . The selected packages are removed from disk.
    3. Upgrade a package
        - In the list of the packages, select the package to be upgraded.
        - Click `^`.
        - Click `OK` to complete upgrading.
    

