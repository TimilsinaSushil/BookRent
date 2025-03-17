from django.db import models
from publishers.models import Publisher
from authors.models import Author
from django.utils.text import slugify
import uuid

# imports for qrcode generation
import qrcode
from io import BytesIO;
from django.core.files import File
from PIL import Image

# Create your models here.

class BookTitle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_books(self):
        return self.books.all()

    def __str__(self):
        return f"Book Position: {self.title}"
    
    def save(self, *args, **kwargs):    #overriding save methode to save slug
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Book(models.Model):
    title = models.ForeignKey(BookTitle, on_delete=models.CASCADE, related_name="books")
    isbn = models.CharField(max_length=24, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    def save( self, *args, **kwargs):
        if not self.isbn:
            self.isbn = str(uuid.uuid4()).replace("-","")[:24].lower()

            # Generate QR Code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.isbn)
            qr.make(fit=True)
            qrcode_image = qr.make_image(fill="black", back_color="white").convert("RGB")  # Ensure correct mode

            canvas = Image.new('RGB', qrcode_image.size, 'white')

            canvas.paste(qrcode_image, (0, 0))

            fname = f'qr_code={self.isbn}.png'

            buffer = BytesIO()

            canvas.save(buffer, 'PNG')

            self.qr_code.save(fname, File(buffer), save=False)

            canvas.close()

        super().save(*args, **kwargs)
