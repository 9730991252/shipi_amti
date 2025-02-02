    from django.test import TestCase

# Create your tests here.
    def save(self, *args,**kwargs):
       super().save(*args,**kwargs)
 
       image1 = Image.open(self.image1.path)
       output_size = (350,350)
       image1.thumbnail(output_size)
       image1.save(self.image1.path)
 
       if self.image2:
           image2 = Image.open(self.image2.path)
           image2.thumbnail(output_size)
           image2.save(self.image2.path)
 
       if self.image3:
           image3 = Image.open(self.image3.path)
           image3.thumbnail(output_size)
           image3.save(self.image3.path)
 
       if self.image4:
           image4 = Image.open(self.image4.path)
           image4.thumbnail(output_size)
           image4.save(self.image4.path)
 
       if self.image5:
           image5 = Image.open(self.image5.path)
           image5.thumbnail(output_size)
           image5.save(self.image5.path)