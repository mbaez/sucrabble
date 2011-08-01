#!/usr/bin/env python
try:
    from sugar.activity import bundlebuilder
    bundlebuilder.start()
except ImportError:
    import os
    os.system("find ./ | sed 's,^./,SucrabbleActivity.activity/,g' > MANIFEST")
    os.system('rm SucrabbleActivity.xo')
    os.chdir('..')
    os.system('zip -r SucrabbleActivity.xo SucrabbleActivity.activity')
    os.system('mv SucrabbleActivity.xo ./SucrabbleActivity.activity')
    os.chdir('SucrabbleActivity.activity')
