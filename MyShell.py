import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
import django
django.setup()

#from learning_logs.models import MyModel

from django.contrib.auth.models import User




import django
django.setup()

from learning_logs.models import Topic
topics = Topic.objects.all()

for topic in topics:
    print(topic.id,topic)

# if you know the id of a particular object, you can use the topics.models.get()
# method to retrieve the object and examine its attributes

t = Topic.objects.get(id=2)
print(t.text)
print(t.date_added)


#to get data through a foreign key relationship, you use the lowercase name of the 
# related model followed by an underscore and the word set.

entries = t.entry_set.all()

for entry in entries:
    print(entry)

for user in User.objects.all():
    print(user.username, user.id)
