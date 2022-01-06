1. Configure:
    
    - `Run | Edit Configurations`
    
    - `View | Appearance | Toolbar`

2. Run/debug configurations can be created as:

    - _Temporary_ — created every time you run or debug functions or tests.
        1. The maximum number of temporary configurations is 5. The older ones are automatically deleted when new ones are added. 
        2. If necessary, you can increase this limit in `Settings/Preferences | Advanced Settings | IDE | Temporary Run/Debug configurations limit`.
    - _Permanent_ — created explicitly from a template or by saving a temporary configuration.
        1. Permanent configurations remain as part of your project until you remove them.

3. Create permanent run/debug configurations

    - Save a temporary configuration as permanent
      1. Select a temporary configuration in the `run/debug configuration` switcher and then click `Save Configuration`.
          - Once you save a temporary configuration, it becomes permanent and it is recorded in a separate XML file in the `<project directory>/.idea/ directory`.
      2. Alternatively, select a temporary configuration in the `Run/debug configurations` dialog and click `Save` on the toolbar.
    - Create a run/debug configuration from a template
      1.Open the `Run/Debug Configuration` dialog in one of the following ways:
         - Select `Run | Edit Configurations` from the main menu.
         - With the `Navigation bar` visible (`View | Appearance | Navigation Bar`), choose `Edit Configurations` from the run/debug configuration selector.
         - Press `Alt+Shift+F10` and then press `0`.
      2. In the `Run/Debug Configuration` dialog, click `Icons general add` on the toolbar or press `Alt+Insert`.

         The list shows the `run/debug configuration templates`.

         Select the `desired template`. If you are not sure which template to choose, refer to Run/debug configurations dialog for more information on particular templates.
      3. Specify the `run/debug configuration name` in the `Name field`. 
      
         This name will be shown in the list of the available run/debug configurations.
      4. Select `Allow parallel run` if you want to allow multiple instances of the configuration to run at the same time.

         If this option is disabled, attempting to re-run the configuration will terminate the active session.
      5. Set the `run/debug configuration parameters`.
      6. In the `Before launch` section, define whether you want to perform any specific actions before launching the application, for example, execute some tools or scripts prior to launching the run/debug configuration.
      7. Apply the changes and close the dialog.








   