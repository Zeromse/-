import cv2
from PIL import Image,ImageDraw
v=cv2.VideoCapture(r'C:\Users\Zerom\Desktop\ui参考\ui归档 ark\「次生预案」活动.mp4')
s=Image.new('RGB',(1200,700))
for i,t in enumerate([0,1,2,3,4,5]):
 v.set(cv2.CAP_PROP_POS_MSEC,t*1000); ok,f=v.read()
 if ok:
  im=Image.fromarray(cv2.cvtColor(f,cv2.COLOR_BGR2RGB)); im.thumbnail((400,330)); s.paste(im,(i%3*400,i//3*350)); ImageDraw.Draw(s).text((i%3*400,i//3*350+300),str(t),fill='white')
s.save('secondary-plan-ui/early.jpg')
