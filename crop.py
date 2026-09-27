from PIL import Image
im=Image.open('secondary-plan-ui/assets/frame-00.jpg')
im.crop((720,100,1280,950)).save('secondary-plan-ui/assets/reactor.jpg',quality=95)
