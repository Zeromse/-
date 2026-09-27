import cv2
from PIL import Image,ImageDraw
p=r'C:\Users\Zerom\Desktop\ui参考\ui归档 ark\「次生预案」活动.mp4'
v=cv2.VideoCapture(p)
fps=v.get(cv2.CAP_PROP_FPS); count=v.get(cv2.CAP_PROP_FRAME_COUNT); duration=count/fps
print(f'Duration {duration}, fps {fps}')
sheet=Image.new('RGB',(1200,4*250),(25,25,25)); d=ImageDraw.Draw(sheet)
for i in range(12):
 t=duration*(i+.3)/12; v.set(0 if False else cv2.CAP_PROP_POS_MSEC,t*1000); ok,frame=v.read()
 if ok:
  cv2.imwrite(f'secondary-plan-ui/assets/frame-{i:02}.jpg',frame)
  im=Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)); im.thumbnail((400,220)); x=i%3*400; y=i//3*250; sheet.paste(im,(x,y)); d.text((x+8,y+223),f'{i:02} / {t:.1f}s',fill='white')
sheet.save('secondary-plan-ui/contact.jpg')
