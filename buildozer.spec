[app]
# (str) Title of your application
title = Faisal's Bird

# (str) Package name
package.name = faisalsbird

# (str) Package domain (needed for android/ios packaging)
package.domain = org.faisal

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (letting it know to grab your sounds)
source.include_exts = py,png,jpg,kv,atlas,wav,txt

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2