from django.db import models
from django.utils.translation import gettext_lazy as _

class UpdateCreateDate(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Fecha de actualización'))

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Nombre de la categoría'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('categoría')
        verbose_name_plural = _('categorías')

    @property
    def quiz_count(self):
        return self.quizzes.count()

class Quiz(UpdateCreateDate):
    title = models.CharField(max_length=50, verbose_name=_('Título del cuestionario'))
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='quizzes',
        verbose_name=_('Categoría')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('cuestionario')
        verbose_name_plural = _('cuestionarios')

    @property
    def question_count(self):
        return self.question_set.count()

class Question(UpdateCreateDate):
    SCALE = (
        ('B', _('Principiante')),
        ('I', _('Intermedio')),
        ('A', _('Avanzado')),
    )

    title = models.TextField(verbose_name=_('Texto de la pregunta'))
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_('Cuestionario'))
    difficulty = models.CharField(max_length=1, choices=SCALE, verbose_name=_('Dificultad'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('pregunta')
        verbose_name_plural = _('preguntas')

class Option(UpdateCreateDate):
    option_text = models.CharField(max_length=200, verbose_name=_('Texto de la opción'))
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='options',
        verbose_name=_('Pregunta')
    )
    is_right = models.BooleanField(default=False, verbose_name=_('¿Es correcta?'))

    def __str__(self):
        return self.option_text

    class Meta:
        verbose_name = _('opción')
        verbose_name_plural = _('opciones')
