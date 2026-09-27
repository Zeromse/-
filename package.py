import zipfile
from pathlib import Path
p=Path('.')
files=['index.html','styles.css','app.js','server.cjs','README.md','启动预览.cmd']
assets=['reactor.jpg','reference.mp4','frame-01.jpg','frame-03.jpg','frame-07.jpg','frame-10.jpg','frame-11.jpg']
with zipfile.ZipFile('../次生预案-完整网站.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in files: z.write(p/f,'secondary-plan-ui/'+f)
 for f in assets: z.write(p/'assets'/f,'secondary-plan-ui/assets/'+f)
print('Packaged complete source and local assets')
