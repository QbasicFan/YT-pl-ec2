from django.db import models


'''
name | link | type | rating
'''
class bookMark(models.Model):
    diff = (
	    ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
         )

    title = models.CharField(max_length=100)
    link = models.CharField(max_length=400) #trim the vlink generate id
    cate = models.ForeignKey('catego', on_delete=models.CASCADE )
    rate = models.CharField(max_length=20 , choices=diff)
    vid = models.CharField(max_length=100, blank=True, null=True)


    def save(self, *args, **kwargs):


        getLink = self.link

        linkType = "shorts"
        delimLength = 7
        if "=" in getLink:
            linkType = "="
            delimLength = 1

        delim = getLink.find(linkType)
        self.vid = getLink[delim+delimLength:len(getLink)]


        super(bookMark, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

#########################
#sub catego
#########################
class catego(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

