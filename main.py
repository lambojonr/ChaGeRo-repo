from imagebattle import app
from imagebattle.model import Image
from imagebattle import db 

db.create_all()
'''db.session.add(Image("http://4.bp.blogspot.com/-U9ZFy_7CeHg/T9eoYKdgvcI/AAAAAAAAAFs/ZHRjuhD8_eQ/s1600/Vanessa-Hudgens-007.jpg"))
db.session.add(Image(("http://www.muskurahat.us/wallpapers/images/chloe-moretz-13.jpg")))
db.session.add(Image("http://www.laughspark.info/thumbfiles/705X705/jennifer-aniston-one-of-the-to-1820.jpg"))
db.session.add(Image(("http://hdlatestwallpapers.com/wp-content/uploads/2013/10/Hollywood-Celebrities-Hd-Wallpapers-.jpg")))
db.session.add(Image("http://cdn26.us1.fansshare.com/photo/camerondiaz/cameron-diaz-hollywood-celebrities-wallpaper-848807472.jpg"))
db.session.add(Image(("http://cdn.justluxe.com/articles/images/news/celebritybeautyla_1890007-thumb.jpg")))
db.session.add(Image(("https://kamalsun.files.wordpress.com/2013/01/selena_gomez_106-wide.jpg")))
db.session.commit()'''

app.run(debug=True)


