from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField("Название", max_length=255)
	slug = models.SlugField("URL-адрес", max_length=255, unique=True)
	edition = models.PositiveIntegerField("Издание", default=0)
	volume = models.PositiveIntegerField("Том", default=1)
	description = models.TextField("Описание", blank=True)
	publication_date = models.DateField("Дата публикации")
	print_run = models.PositiveIntegerField("Тираж", default=0)
	stock = models.PositiveIntegerField("Количество на суладе", default=8)
	available = models.BooleanField("Доступен", default=True)
	price = models.DecimalField("Цена", max_digits=8, decimal_places=2)
	discount = models.DecimalField("Скидка", max_digits=5, decimal_places=2, default=0.00)
	created_at = models.DateTimeField("Дата создания", auto_now_add=True)
	updated_at = models.DateTimeField("Дата обновления", auto_now=True)

	class Meta:
		ordering = ['-created_at']
		verbose_name = "Книга"
		verbose_name_plural = "Книги"



	def __str__(self):
		return self.title