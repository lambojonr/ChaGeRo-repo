from imagebattle import app
from imagebattle.model import Image
from imagebattle import db 

db.create_all()
#db.session.add(Image("http://theilovedogssite.com/wp-content/uploads/2015/01/4577137586_5f4cf7fbd3_z.jpg"))
#db.session.add(Image(("https://i.ytimg.com/vi/UIrEM_9qvZU/maxresdefault.jpg")))

db.session.commit()

app.run(debug=True)


