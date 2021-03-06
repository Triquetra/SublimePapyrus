SublimePapyrus
==============

Sublime Text 2 package for the Papyrus scripting language.

Includes function/event snippets and syntax definitions for Skyrim (1.9.32.0.8), [SKSE](http://skse.silverlock.org) (1.7.1), [SkyUI SDK](https://github.com/schlangster/skyui/wiki) (4.1), [FISS](http://www.nexusmods.com/skyrim/mods/48265/) (1.21), [NetImmerse Override](http://www.nexusmods.com/skyrim/mods/37481/) (2.9.1), [DienesTools](http://www.nexusmods.com/skyrim/mods/54325/) (1.0), [JContainers](http://www.nexusmods.com/skyrim/mods/49743/) (3.0.0), [PapyrusUtil](http://www.nexusmods.com/skyrim/mods/49098/) (2.3), and [SkyUILib](https://github.com/schlangster/skyui-lib/wiki) (1).

How do I use the package?
- Install Sublime Text 2, if you do not have it yet. Launch it once in order to make sure all necessary folders are created. Check the Creation Kit wiki for instructions on how to set up the Papyrus compiler for use with external editors.
- Get a copy of SublimePapyrus from the repository (recommended) or the CK wiki, if the repository is inaccessible.
- Copy the folder labeled "Papyrus" to "%AppData%\Sublime Text 2\Packages" or "\Sublime Text 2\Data\Packages", if you are using the portable version of Sublime Text 2.
- Copy the contents of the other folders, if you intend to use those resources, and paste them into the folder labeled "Papyrus".
- If you have Skyrim installed outside of "C:\Program Files (x86)\Steam\steamapps\common\skyrim\" or "C:\Program Files\Steam\steamapps\common\skyrim\", then you need to open the Command Palette (CTRL+SHIFT+P), type in "Papyrus INI". An option called "Papyrus INI: Create default INI file" should show up. Select it and a file called "SublimePapyrus.ini" will be created in My Documents. This file contains paths to compiled scripts, script sources, and the Papyrus compiler. Edit the paths according to where you have installed Skyrim.
 

How do I use the program PapyrusToSublimeSnippets?

The program can be launched from anywhere and allows you to type in the path to the folder containing the Papyrus source files you wish to process. The first level of subfolders in the input folder will also be processed. If you do not type in a path, then the program will process the folder, which the program is in. The generated snippets will be placed in subfolders called "snippets".

The program creates two logs: FunctionLog.txt and ClassLog.txt. The log files will be placed in the input folder and the log files contain keywords, which are formatted for use in the Papyrus syntax definition (Papyrus.tmLanguage), based on the processed source files. The syntax definition can be found in the Papyrus package.



Based on the work done by Bethesda Game Studios and Mark Hanna. Used according to the license included in the original package and said license is included in this package.

Program, for automated creation of snippets, created by Quad2Core.

Team: Quad2Core, MrJack

This version of the Sublime compiler command supports compiling scripts opened through Mod Organizer or through Creation Kit through Mod Organizer.

The INI now contains path variables.  Each path variabe in the INI will be passed to the papyrus compiler as an import directory so that script dependencies are available to scripts, even if located in Mod Organizer mods.
