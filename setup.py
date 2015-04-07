from distutils.core import setup
import py2exe

setup(options = {
		"py2exe": {
	# 		# "compressed": 2, 
	# 		# "optimize": 2,
			# "includes": ['cmd', 'platform', 'colorama', 'pyreadline'],
	# 		# "excludes": excludes,
			# "packages": ['colorama', 'pyreadline'],
	# 		# "dll_excludes": dll_excludes,
			"bundle_files": 0,
	# 		# "dist_dir": "dist",
	# 		# "xref": False,
			"skip_archive": 1,
	# 		# "ascii": False,
	# 		# "custom_boot_script": '',
		},
	},
	console=['criteria.py']
)

# http://www.py2exe.org/index.cgi/FAQ
# download pywin32 from http://sourceforge.net/projects/pywin32/?source=typ_redirect
# python setup.py py2exe --bundle-files 0
# http://www.py2exe.org/index.cgi/ListOfOptions
# http://www.py2exe.org/index.cgi/GeneralTipsAndTricks

# http://www.tutorialspoint.com/python/python_command_line_arguments.htm
# http://www.pythoncentral.io/py2exe-python-to-exe-introduction/