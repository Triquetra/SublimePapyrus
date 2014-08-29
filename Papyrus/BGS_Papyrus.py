import sublime, sublime_plugin
import os
import ConfigParser
from StringIO import StringIO

INI_LOCATION      = os.path.expanduser("~/Documents/SublimePapyrus.ini")
# Default values for a standardized Steam installation (for end-users and modders)
if (os.path.exists("C:\\Program Files (x86)")):
    END_USER_ROOT = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\skyrim"
else:
    END_USER_ROOT = "C:\\Program Files\\Steam\\steamapps\\common\\skyrim"

DEFAULT_INI_TEXT = """[DEFAULT]
skyrimroot={0}
moroot={1}
[Skyrim]
scripts=%(skyrimroot)s\\Data\\Scripts\\Source
compiler=%(skyrimroot)s\\Papyrus Compiler\\PapyrusCompiler.exe
flags=TESV_Papyrus_Flags.flg
# The output folder is dynamically set to the parent of the script location
# If you'd rather have a consistent output directory, set it here
;output=%(moroot)s\\overwrite
[Import Paths]
# List import paths to be searched (in order) for script dependencies
;path1=%(moroot)s\\PapyrusUtil\\Scripts\\Source
;path2=%(moroot)s\\FISS\\Scripts\\Source
;path3=%(moroot)s\\JContainers\\Scripts\\Source
;path4=%(moroot)s\\DienesTools\\Scripts\\Source
;path5=%(moroot)s\\NetImmerse Override\\Scripts\\Source
;path6=%(moroot)s\\SkyUILib\\Scripts\\Source
;path7=%(moroot)s\\SkyUI\\Scripts\\Source
;path8=%(moroot)s\\SKSE\\Scripts\\Source
""".format(END_USER_ROOT, "C:\\Program Files (x86)\\ModOrganizer\\mods")

def getPrefs(pathandfile):
    currentDir, filename = os.path.split(pathandfile)
    parser = ConfigParser.SafeConfigParser()
    parser.readfp(StringIO(DEFAULT_INI_TEXT))
    parser.read([INI_LOCATION])
    ret = {}
    ret["compiler"] = parser.get("Skyrim", "compiler")
    if parser.has_option("Skyrim", "output"):
        ret["output"] = parser.get("Skyrim", "output")
    else:
        ret["output"] = os.path.dirname(currentDir)
    ret["flags"] = parser.get("Skyrim", "flags")
    ret["filename"] = filename
    ret["import"] = [currentDir]
    for key, val in parser.items("Import Paths"):
        if key.startswith("path"):
            ret["import"].append(val)
    ret["import"].append(parser.get("Skyrim", "scripts"))
    ret["import"] = ";".join(filter(None, ret["import"]))
    return ret

class CreateDefaultSettingsFileCommand(sublime_plugin.WindowCommand):
    def run(self, **args):
        if not os.path.exists(INI_LOCATION) or \
            sublime.ok_cancel_dialog("WARNING: INI file already exists.\n Overwrite?"):
            with open(INI_LOCATION, 'w') as inifile:
                inifile.write(DEFAULT_INI_TEXT)
            self.window.open_file(INI_LOCATION)

class CompilePapyrusCommand(sublime_plugin.WindowCommand):
    def run(self, **args):
        config = getPrefs(args["cmd"])
        args["cmd"] = [config["compiler"], config["filename"]]
        args["cmd"].append("-f=%s" % config["flags"])
        args["cmd"].append("-i=%s" % config["import"])
        args["cmd"].append("-o=%s" % config["output"])
        args["working_dir"] = os.path.dirname(config["compiler"])
        self.window.run_command("exec", args)
